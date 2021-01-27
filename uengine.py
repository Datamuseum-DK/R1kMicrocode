'''
   The base class of a microcode engine
'''

class Uinstruction():
    ''' A single micro-instruction '''

    def __init__(self, name, uword, scan_chain):
        bits = len(uword) * 8
        self.uword = int.from_bytes(uword, 'big')
        i = set()
        down_shift = bits
        for n in range(bits):
            down_shift -= 1
            _schematic_name, attr, shift, invert = scan_chain[n & 7][n >> 3]
            bit = (self.uword >> down_shift) & 1
            val = getattr(self, attr, 0)
            val |= (bit ^ invert) << shift
            setattr(self, attr, val)
            i.add(attr)
            if attr[:5] == "zero_" and val:
                raise ValueError("Field %s.%s has 0x%x value at index 0x%x" % (name, attr, val, n))
        self.str = "<" + name
        for i in sorted(i):
            if i[:5] != "zero_":
                self.str += " " + i + " 0x%x" % getattr(self, i)
        self.str += ">"

    def __str__(self):
        return self.str

class UcodeEngine():
    ''' Basic Stuff '''

    def __init__(self, up, name, address_width, scan_chain):
        self.up = up
        self.name = name
        self.address_width = address_width
        self.scan_chain = scan_chain
        self.uins = [None] * (1 << address_width)
        self.attrs = None
        self.fmt = None
        self.afmt = None

    def finish(self):
        ''' Summarize the uins in various ways '''
        a = set()
        for i in self.scan_chain:
            for _schematic_name, attr, _shift, _invert in i:
                if attr[:5] != "zero_":
                    a.add(attr)
        self.attrs = list(sorted(a))
        self.fmt = []
        for a in self.attrs:
            lo = 1
            hi = 0
            for i in self.uins:
                if i:
                    lo = min(lo, getattr(i, a))
                    hi = max(hi, getattr(i, a))
            if not hi:
                print(self.name, "Field", a, "is always zero")
            if lo:
                print(self.name, "Field", a, "is never zero")
            self.fmt.append("%%0%dx" % len("%x" % hi))
        self.afmt = "%%0%dx" % len("%x" % (len(self.uins) - 1))

    def __iter__(self):
        yield from self.uins

    def __getitem__(self, idx):
        return self.uins.__getitem__(idx)

    def __setitem__(self, idx, val):
        return self.uins.__setitem__(idx, val)

    def define_instruction(self, address, uword):
        ''' Define a microinstruction '''
        retval = Uinstruction(self.name, uword, self.scan_chain)
        self.uins[address] = retval
        return retval

    def html_page(self, fo):
        ''' Produce a HTML page '''
        for i in range(0, len(self.uins), 0x100):
            self.html_table(fo, i, i + 0x100)
            fo.write("<br/>\n")

    def html_table_heads(self, fo):
        ''' Table header cells '''
        for i in self.attrs:
            fo.write('<th>%s</th>\n' % i)

    def html_table_fields(self, fo, uins):
        ''' Table data cells '''
        for attr, fmt in zip(self.attrs, self.fmt):
            fo.write('<td>' + fmt % getattr(uins, attr) + '</td>\n')

    def html_table(self, fo, lo=0, hi=None):
        ''' Produce a HTML (sub-)table '''
        if hi is None:
            hi = len(self.uins)
        s = set(self.uins[lo:hi])
        if len(s) == 1 and None in s:
            return
        fo.write('<table class="border">\n')
        fo.write('<tr>\n')
        fo.write('<th>Index</th>\n')
        self.html_table_heads(fo)
        fo.write('</tr>\n')
        for n, i in enumerate(self.uins[lo:hi]):
            if not i:
                continue
            if not n:
                fo.write('<tr class="top">\n')
            elif (n+lo) % 16:
                fo.write('<tr>\n')
            else:
                fo.write('<tr class="top">\n')
            fo.write('<td>' + self.afmt % (n+lo) + '</td>\n')
            self.html_table_fields(fo, i)
            fo.write('</tr>\n')
        fo.write('</table>\n')

    def explain(self, _uadr):
        ''' Humanize uins '''
        return
        yield None
