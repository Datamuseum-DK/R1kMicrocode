'''
   SEQ board microcode engine
'''

# Page number only references are to:
# https://datamuseum.dk/bits/30000958 R1000_SCHEMATIC_SEQ.PDF

import uengine
import diag_chains

# Ref: p68
BRANCH_TYPE = {
    0x0: "Branch False",
    0x1: "Branch True",
    0x2: "Push (branch address)",
    0x3: "Unconditional Branch",
    0x4: "Call False",
    0x5: "Call True",
    0x6: "Continue",
    0x7: "Unconditional Call",
    0x8: "Return True",
    0x9: "Return False",
    0xa: "Unconditional Return",
    0xb: "Case False",
    0xc: "Dispatch True",
    0xd: "Dispatch False",
    0xe: "Unconditional Dispatch",
    0xf: "Unconditional Case Call",
}

class Seq(uengine.UcodeEngine):
    ''' Uengine for SEQ '''
    def __init__(self, up, uload):
        super().__init__(
            up,
            "SEQ",
            14,
            diag_chains.SEQ_UIR_SCAN_CHAIN
        )
        for n, i in uload:
            self.define_instruction(n, i)
        self.finish()

    def explain(self, uadr):
        uins = self[uadr]
        yield "Prev:   " + self.up.link_to_uadr(uadr - 1)
        yield "Next:   " + self.up.link_to_uadr(uadr + 1)
        if uins.branch_adr:
            yield "Branch: " + self.up.link_to_uadr(uins.branch_adr)
        else:
            yield "Branch: 0"

        yield "br_type = " + BRANCH_TYPE[uins.br_type]
