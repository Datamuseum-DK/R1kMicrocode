
import r1k_m200_ucode_file
import diag_chains

class UIns():
    def __init__(self, attrs):
        self._attrs = list(sorted(attrs))
        for i in attrs:
            setattr(self, i, 0)
        self._cstr = None

    def __str__(self):
        if self._cstr:
            return self._cstr
        k = ["%s=%x" % (i, getattr(self, i)) for i in self._attrs]
        return "<U " + " ".join(k) + ">"

    def orval(self, attr, val, invert):
        i = getattr(self, attr)
        setattr(self, attr, i | (1<<val))


def hack():
    for n, i in enumerate(zip(
        ucode.seq_ucode(),
        ucode.fiu_ucode(),
        ucode.typ_ucode(),
        ucode.val_ucode(),
        ucode.ioc_ucode(),
    )):
        print("%04x" % n, " ".join(j.hex() for j in i))


def chew(name, chain, ucodes):

    print("#" * len(name))
    print(name)
    print("#" * len(name))

    # Corner-turn for convenience
    ct = [list() for _i in range(8)]
    attrs = set()
    for i in chain:
        for n, j in enumerate(reversed(i)):
            ct[n].append(j)
            if j[1][0] != 'x':
                attrs.add(j[1])

    vals = {}
    for i in attrs:
        vals[i] = set()

    pval = set()
    aval = (1<<64) - 1
    oval = 0
    for adr, i in enumerate(ucodes):
        u = UIns(attrs)
        for j, k in zip(i, ct):
            for n, y in enumerate(k):
                if y[3]:
                    m = (0xff^j) & (0x80 >> n)
                else:
                    m = j & (0x80 >> n)
                if m:
                    if y[1][0] == 'x':
                        print("%02x" % j, "%02x" % m, y)
                    else:
                        u.orval(y[1], y[2], y[3])
        j = int.from_bytes(i, 'big')
        aval &= j
        oval |= j
        p = len(bin(j)[2:].replace('0', '')) & 1
        pval.add(p)
        #print("----", p, "%04x" % adr, i.hex(), u)
        for j in attrs:
            vals[j].add(getattr(u, j))
    print("    AND %016x" % aval)
    print("    OR  %016x" % oval)
    print("    PARITIES", pval)
    for i, j in sorted(vals.items()):  
        print("   ", i, len(j), "[%d…%d]" % (min(j), max(j)))

ucode = r1k_m200_ucode_file.R1kM200UcodeFile()

chew("SEQ", diag_chains.SEQ_UIR_SCAN_CHAIN, ucode.seq_ucode())
chew("FIU", diag_chains.FIU_MICRO_INSTRUCTION_REGISTER, ucode.fiu_ucode())
chew("TYP", diag_chains.TYP_WRITE_DATA_REGISTER, ucode.typ_ucode())
chew("VAL", diag_chains.VAL_WRITE_DATA_REGISTER, ucode.val_ucode())
chew("IOC", diag_chains.IOC_DIAG_CHAIN, ucode.ioc_ucode())
