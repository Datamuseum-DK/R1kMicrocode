
'''
   Take a .M200_UCODE file apart
   =============================
'''

class R1kM200UcodeFile():

    ''' A Rational 1000 .M200_UCODE file '''

    def __init__(self, input):
        self.ucode = bytes(input)

    def dispatch_ram_low(self):
        for i in range(0x6400, 0x8400, 2):
            yield self.ucode[i:i+2]

    def dispatch_ram_high(self):
        for i in range(0x8400, 0xa400, 2):
            yield self.ucode[i:i+2]

    def typ_regfile(self):
        for a in range(0x400, 0x6400, 24):
            yield self.ucode[a:a+12]

    def val_regfile(self):
        for a in range(0x400, 0x6400, 24):
            yield self.ucode[a+16:a+24] + self.ucode[a+12:a+16]

    def ioc_ucode(self):
        for a in range(0xa400, len(self.ucode), 32):
            v = 0
            for c in self.ucode[a+16:a+16+8]:
                v <<= 2
                v |= c & 3
            yield bytes((v >> 8, v & 0xff))

    def val_ucode(self):
        for a in range(0xa400, len(self.ucode), 32):
            yield self.ucode[a+8:a+8+8]

    def seq_ucode(self):
        for a in range(0xa400, len(self.ucode), 32):
            yield self.ucode[a+24:a+24+8]

    def typ_ucode(self):
        for a in range(0xa400, len(self.ucode), 32):
            yield self.ucode[a:a+8]

    def fiu_ucode(self):
        for a in range(0xa400, len(self.ucode), 32):
            yield self.ucode[a+16:a+16+8]
