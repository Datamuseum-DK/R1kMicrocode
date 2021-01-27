'''
   Things related to ".M200_UCODE" files, and reading thereof.
'''

UCODE_FILES = [
    "M207_54.M200_UCODE",
    "M207_53.M200_UCODE",
    "M207_45.M200_UCODE",
    "M207_44.M200_UCODE",
    "M207_36.M200_UCODE",
    "ABUS_TEST.M200_UCODE",
    "DIAG.M200_UCODE",
    "FPTEST.M200_UCODE",
    "P2UCODE.M200_UCODE",
    "P3UCODE.M200_UCODE",
    "PHASE2_MULT_TEST.M200_UCODE",
]

# This is currently guesswork, based on the uwords in SEQ which perform
# a "CASE" type branch:  It makes most sense if the majority of them branch
# the the subsequent instructions.  The result looks like it could make sense.
LOAD_ADR = 0x100

class UCodeSection():
    ''' One section of a microcode file = an array of encoded microinstructions '''
    def __init__(self, octets, width_in_bytes, stride=0, offset=0, load_adr = 0):
        if not stride:
            stride = width_in_bytes
        assert not len(octets) % stride
        self.uwords = []
        self.with_in_bits = width_in_bytes * 8
        self.load_adr = load_adr
        for i in range(0, len(octets), stride):
            self.uwords.append(octets[i+offset:i+offset+width_in_bytes])

    def __iter__(self):
        for n, i in enumerate(self.uwords):
            yield n + self.load_adr, i

    def __len__(self):
        return len(self.uwords)

    def __getitem__(self, idx):
        return self.uwords.__getitem__(idx)

class UCodeFile():
    ''' Read in one .M200_UCODE file '''
    def __init__(self, filename):
        self.octets = open(filename, 'rb').read()

        # Could this be the initial register-file ?
        self.xxx = UCodeSection(self.octets[0x400:0x6400], 8)

        self.decode_low = UCodeSection(self.octets[0x6400:0x8400], 8)
        self.decode_high = UCodeSection(self.octets[0x8400:0xa400], 8)

        self.typ = UCodeSection(self.octets[0xa400:], 8, stride=32, offset=0, load_adr=LOAD_ADR)

        # This makes VAL.alu_func look right in 0x027x instructions
        self.val = UCodeSection(self.octets[0xa400:], 8, stride=32, offset=8, load_adr=LOAD_ADR)

        self.fiu = UCodeSection(self.octets[0xa400:], 8, stride=32, offset=16, load_adr=LOAD_ADR)

        self.seq = UCodeSection(self.octets[0xa400:], 8, stride=32, offset=24, load_adr=LOAD_ADR)
