'''
   Python-friendly microcode program classes
'''

import r1k_m200_ucode_file
import diag_chains

LOAD_ADR = 0x100

class DiagChain():
    ''' Convenienized version of diag_chains.*  '''

    def __init__(self, source):
        # Corner-turn for convenience
        self.chain = [list() for _i in range(8)]
        self.attrs = dict()
        self.fmt = dict()
        for bit, i in enumerate(source):
            for n, j in enumerate(reversed(i)):
                j = list(j)
                j[2] = 1 << j[2]
                if j[3]:
                    j[3] = j[2]
                j.append(0x80 >> bit)
                self.chain[n].append(j)
                if j[1][0] != 'x':
                    self.attrs[j[1]] = self.attrs.get(j[1], 0) | j[2]

        for i, j in self.attrs.items():
            x = len("%x" % j)
            x = "%0" + "%d" %x + "x"
            self.fmt[i] = x

class Uins():
    ''' A full R1k Microinstruction word '''

    def __init__(self, adr):
        self.adr = adr
        self.str = "%04x:" % adr

    def __str__(self):
        return self.str

class Uprog():
    ''' A Complete Microcode '''
    def __init__(self, iterable=None):
        ucode = r1k_m200_ucode_file.R1kM200UcodeFile(iterable)
        self.wcs = [Uins(i + LOAD_ADR) for i in range(len(ucode))]
        self.chains = {}
        self.attrs = {}
        self.dispatch_attrs = {}

        for name, parity, chainspec, ucodes in (
            ("seq", 0, diag_chains.SEQ_UIR_SCAN_CHAIN, ucode.seq_ucode()),
            ("fiu", 1, diag_chains.FIU_MICRO_INSTRUCTION_REGISTER, ucode.fiu_ucode()),
            ("typ", 0, diag_chains.TYP_WRITE_DATA_REGISTER, ucode.typ_ucode()),
            ("val", 1, diag_chains.VAL_WRITE_DATA_REGISTER, ucode.val_ucode()),
            ("ioc", 0, diag_chains.IOC_DIAG_CHAIN, ucode.ioc_ucode()),
        ):
            chain = DiagChain(chainspec)
            self.chains[name] = chain
            for i in sorted(chain.attrs):
                self.attrs[name + "_" + i] = chain.fmt[i]
            for i, j in zip(self.wcs, self.chew(parity, chain, ucodes)):
                i.str += " " + name + "_"
                for a, b in j.items():
                    setattr(i, name + "_" + a, b)
                    i.str += " " + a + "=" + chain.fmt[a] % b

        self.dispatch_chain = DiagChain(diag_chains.SEQ_DECODER_SCAN)
        for i in sorted(self.dispatch_chain.attrs):
            self.dispatch_attrs["dispatch_" + i] = self.dispatch_chain.fmt[i]
        self.dispatch_ram = {}
        for shift, ucodes in (
             (6, ucode.dispatch_ram_high()),
             (0, ucode.dispatch_ram_low()),
        ):
            for n, j in enumerate(self.chew(1, self.dispatch_chain, ucodes)):
                i = Uins(n << shift)
                i.str += " dispatch_"
                for a, b in j.items():
                    setattr(i, "dispatch_" + a, b)
                    i.str += " " + a + "=" + self.dispatch_chain.fmt[a] % b
                self.dispatch_ram[i.adr] = i

    def dispatch(self, x):
        ''' Look instruction up in dispatch RAM '''
        t = self.dispatch_ram.get(x)
        if t is None:
            t = self.dispatch_ram.get(x & ~0x3f)
        return t

    def __iter__(self):
        yield from self.wcs

    def __getitem__(self, idx):
        return self.wcs.__getitem__(idx)

    def chew(self, parity, chain, uwords):
        ''' Apologies for the opaqueness here... '''
        for uword in uwords:
            a = dict((i, 0) for i in chain.attrs)
            par = 0
            for octet, bitspecs in zip(uword, chain.chain):
                for spec in bitspecs:
                    if spec[1] == 'ignore':
                        continue
                    if octet & spec[4]:
                        par ^= 1
                    if (spec[3] ^ octet) & spec[4]:
                        assert spec[1][0] != 'x', (octet, spec)
                        a[spec[1]] |= spec[2]
            assert par == parity
            yield a

def main():
    ''' ... '''
    uprog = Uprog()
    for i, j in sorted(uprog.dispatch_ram.items()):
        print(i, j)
    print("%x" % uprog[0x27].seq_branch_adr)
    for i in uprog:
        print(i)

if __name__ == "__main__":
    main()
