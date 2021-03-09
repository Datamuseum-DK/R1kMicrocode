
'''
   Simulate R1000.Emulator tracefile output for ucode load
   =======================================================
'''

import r1k_m200_ucode_file

def buncher(prefix, first_suffix, iterable):
    ''' Make bunch of 16 entries '''
    t = ""
    for n, i in enumerate(iterable):
        t += "".join(" %02x" % j for j in i)
        if n % 16 == 15:
            yield prefix + t + first_suffix
            first_suffix = ""
            t = ""

class SimulateUloadTrace():

    '''
       Simulate the emulator trace output when .M200_UCODE file is loaded

       python3 -u sim_download.py > _sim
       sed -e '/i8052/!d' -e 's/^............//' /critter/_r1000 > _dnl
       diff -u _dnl _sim

       This should produce only approx 100 lines of diff
    '''

    def __init__(self, iterable):
        self.ucode = r1k_m200_ucode_file.R1kM200UcodeFile(iterable)

        for disp, regf in zip(
            self.dispatch_ram_load(),
            self.regfile_load()
        ):
            print(regf)
            print(disp)

        for i in zip(
            self.typ_ucode_load(),
            self.val_ucode_load(),
            self.fiu_ucode_load(),
            self.ioc_ucode_load(),
            self.seq_ucode_load()
        ):
            for j in i:
                print(j)

    def dispatch_ram_load(self):
        ''' LOAD_DISPATCH_RAMS_200.SEQ '''
        prefix = " i8052.SEQ.2 DL 9b 02 18 18 00 00 00 00"
        first_suffix = " 00 70 1a 8f 10 9a 8c 18 be 18 59 be 19 58 bc 63 08 bf 42 74"
        first_suffix += " 16 bc 4d 38 bd 95 ff c0 18 be 18 59 be 19 58 54 9a a8 5c 00"
        t = ""
        for n, i in enumerate(self.ucode.dispatch_ram_low()):
            t += "".join(" %02x" % j for j in i)
            if n % 16 == 15:
                j = n >> 4
                s = " %02x" % (j >> 4)
                s += " %02x" % ((j << 4) & 0xff)
                yield prefix + s + t + first_suffix
                first_suffix = ""
                t = ""
        prefix = " i8052.SEQ.2 DL 9b 00 18 18 00 00 00 00"
        for n, i in enumerate(self.ucode.dispatch_ram_high()):
            t += "".join(" %02x" % j for j in i)
            if n % 16 == 15:
                j = n >> 4
                s = " %02x 00" % (j << 2)
                yield prefix + s + t + first_suffix
                first_suffix = ""
                t = ""

    def typ_regfile_load(self):
        ''' LOAD_REGISTER_FILE_200.TYP '''
        prefix = " i8052.TYP.6 DL d9 00 18 18 00 00 00 00"
        first_suffix = " 00 70 18 8f 10 d8 0c c1 38 74 16 bc 5a bc 34 54 d8 de 5c 00"
        yield from buncher(prefix, first_suffix, self.ucode.typ_regfile())

    def val_regfile_load(self):
        ''' LOAD_REGISTER_FILE_200.VAL '''
        prefix = " i8052.VAL.7 DL d9 00 18 18 00 00 00 00"
        first_suffix = " 00 70 18 8f 10 d8 0c c1 38 74 16 bc 5a bc 34 54 d8 de 5c 00"
        yield from buncher(prefix, first_suffix, self.ucode.val_regfile())

    def regfile_load(self):
        ''' alternate TYP and VAL '''
        for typ, val in zip(self.typ_regfile_load(), self.val_regfile_load()):
            yield typ
            yield val

    def ioc_ucode_load(self):
        ''' LOAD_CONTROL_STORE_200.IOC '''
        prefix = " i8052.IOC.4 DL 38 00 18 18 00 00 00 00"
        first_suffix = " 8f 18 40 8f 19 43 10 d0 18 10 d0 19 11 bc 61 93 02 40 93 02 43 16 5c 00"
        yield from buncher(prefix, first_suffix, self.ucode.ioc_ucode())

    def seq_ucode_load(self):
        ''' LOAD_CONTROL_STORE_200.SEQ '''
        prefix = " i8052.SEQ.2 DL 99 00 18 18 00 00 00 00"
        first_suffix = " 00 8f 10 98 70 18 08 bf 41 74 16 bc 4a 54 98 9e 5c 00"
        yield from buncher(prefix, first_suffix, self.ucode.seq_ucode())

    def fiu_ucode_load(self):
        ''' LOAD_CONTROL_STORE_200.FIU '''
        prefix = " i8052.FIU.3 DL 99 00 18 18 00 00 00 00"
        first_suffix = " 00 8f 10 98 70 18 08 bf 13 74 16 bc 39 54 98 9e 5c 00"
        yield from buncher(prefix, first_suffix, self.ucode.fiu_ucode_raw())

    def val_ucode_load(self):
        ''' LOAD_CONTROL_STORE_200.VAL '''
        prefix = " i8052.VAL.7 DL 99 00 18 18 00 00 00 00"
        first_suffix = " 00 8f 10 98 70 18 08 c1 3b 74 16 bc 4c 54 98 9e 5c 00"
        yield from buncher(prefix, first_suffix, self.ucode.val_ucode())

    def typ_ucode_load(self):
        ''' LOAD_CONTROL_STORE_200.TYP '''
        prefix = " i8052.TYP.6 DL 99 00 18 18 00 00 00 00"
        first_suffix = " 00 8f 10 98 70 18 08 c1 3b 74 16 bc 4c 54 98 9e 5c 00"
        yield from buncher(prefix, first_suffix, self.ucode.typ_ucode())


if __name__ == "__main__":
    SimulateUloadTrace(open("M207_54.M200_UCODE", "rb").read())
