'''
   TYP board microcode engine
'''

# Page number only references are to:
# https://datamuseum.dk/bits/30000959 R1000_SCHEMATIC_TYP.PDF

import uengine
import diag_chains

# Ref: p5
ALU_FUNC = {
    0x00: "PASS_A",
    0x01: "A_PLUS_B",
    0x02: "INC_A_PLUS_B",
    0x03: "LEFT_I_A",
    0x04: "LEFT_I_A_INC",
    0x05: "DEC_A_MINUS_B",
    0x06: "A_MINUS_B",
    0x07: "INC_A",
    0x08: "PLUS_ELSE_MINUS",
    0x09: "MINUS_ELSE_PLUS",
    0x0a: "PASS_A_ELSE_PASS_B",
    0x0b: "PASS_B_ELSE_PASS_A",
    0x0c: "PASS_A_ELSE_INC_A",
    0x0d: "INC_A_ELSE_PASS_A",
    0x0e: "PASS_A_ELSE_DEC_A",
    0x0f: "DEC_A_ELSE__PASS_A",
    0x10: "NOT_A",
    0x11: "A_NAND_B",
    0x12: "NOT_A_OR_B",
    0x13: "ONES",
    0x14: "A_NOR_B",
    0x15: "NOT_B",
    0x16: "A_XNOR_B",
    0x17: "A_OR_NOT_B",
    0x18: "NOT_A_AND_B",
    0x19: "X_XOR_B",
    0x1a: "PASS_B",
    0x1b: "A_OR_B",
    0x1c: "DEC_A",
    0x1d: "A_AND_NOT_B",
    0x1e: "A_AND_B",
    0x1f: "ZEROS",
}

class Typ(uengine.UcodeEngine):
    ''' Uengine for TYP '''
    def __init__(self, up, uload):
        super().__init__(
            up,
            "FIU_OR_TYP2",
            14,
            #diag_chains.TYP_WRITE_DATA_REGISTER
            diag_chains.FIU_OR_TYP2
        )
        for n, i in uload:
            self.define_instruction(n, i)
        self.finish()

    def _explain(self, uadr):
        uins = self[uadr]
        yield "alu_func = " + ALU_FUNC[uins.alu_func]
