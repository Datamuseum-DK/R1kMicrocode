'''
   Python-friendly microcode program classes
'''

import r1k_m200_ucode_file
import diag_chains

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
        self.str = "%04x:" % adr

    def __str__(self):
        return self.str

class Uprog():
    ''' A Complete Microcode '''
    def __init__(self, iterable=None):
        ucode = r1k_m200_ucode_file.R1kM200UcodeFile(iterable)
        self.wcs = [Uins(i) for i in range(len(ucode))]
        self.chains = {}
        self.attrs = []

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
                self.attrs.append(name + "_" + i)
            for i, j in zip(self.wcs, self.chew(parity, chain, ucodes)):
                i.str += " " + name + "_"
                for a, b in j.items():
                    setattr(i, name + "_" + a, b)
                    i.str += " " + a + "=" + chain.fmt[a] % b

    def __iter__(self):
        yield from self.wcs

    def __getitem__(self, idx):
        return self.wcs.__getitem__(idx)

    def chew(self, parity, chain, uwords):
        ''' Apologies for the opaqueness here... '''
        for uword in uwords:
            i = int.from_bytes(uword, 'big')
            par = len(bin(i)[2:].replace('0', '')) & 1
            assert par == parity
            a = dict((i, 0) for i in chain.attrs)
            for octet, bitspecs in zip(uword, chain.chain):
                for spec in bitspecs:
                    if (spec[3] ^ octet) & spec[4]:
                        assert spec[1][0] != 'x'
                        a[spec[1]] |= spec[2]
            yield a

def main():
    ''' ... '''
    uprog = Uprog()
    print(uprog.attrs)
    print("%x" % uprog[0x27].seq_branch_adr)
    for i in uprog:
        print(i)

if __name__ == "__main__":
    main()
