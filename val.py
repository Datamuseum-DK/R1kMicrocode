'''
   VAL board microcode engine
'''

# Page number only references are to:
# https://datamuseum.dk/bits/30000960 R1000_SCHEMATIC_VAL.PDF

import uengine
import diag_chains

# Ref: p2
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

# Ref: p2
def a_adr(x):
    if x < 0x10:
        return "GP 0x%x" % x
    if x == 0x10:
        return "TOP"
    if x == 0x11:
        return "TOP + 1"
    if x == 0x12:
        return "SPARE_0x12"
    if x == 0x13:
        return "LOOP_REG"
    if x == 0x14:
        return "ZEROS"
    if x == 0x15:
        return "ZERO_COUNTER"
    if x == 0x16:
        return "PRODUCT"
    if x == 0x17:
        return "LOOP_COUNTER"
    if x < 0x20:
        return "TOP - %d" % (0x20 - x)
    return "FRAME:REG0x%x" % (x - 0x20)

# Ref: p2
def b_adr(x):
    if x == 0x14:
        return "BOT - 1"
    if x == 0x15:
        return "BOT"
    if x == 0x16:
        return "CSA/VAL_BUS"
    if x == 0x17:
        return "SPARE_0x17"
    return a_adr(x)

# Ref: p2
def c_adr(x):
    if x < 0x20:
        return "FRAME:REG??" # XXX: "inversion of C field of uword
    if x < 0x40:
        return "GP 0x%x" % (0x3f - x)
    if x < 0x2f:
        return "TOP"
    if x < 0x2e:
        return "TOP + 1"
    if x < 0x2d:
        return "SPARE_0x2d"
    if x < 0x2c:
        return "LOOP_REG"
    if x < 0x2b:
        return "BOT - 1"
    if x < 0x2a:
        return "BOT"
    if x < 0x29:
        return "WRITE_DISABLE (default)"
    if x < 0x28:
        return "LOOP_COUNTER"
    return "TOP - %d" % (x - 0x1f)

# Ref: p2
def c_bus(src, mux):
    if not src:
        return "fiu_bus"
    return {
        0: "ALU << 1",
        1: "ALU >> 16",
        2: "ALU",
        3: "WSR",  # XXX: hard to read on p2
    }[mux]

# Ref: p2
def ab_src(x):
    return {
        0: "Bits 0…15",
        1: "Bits 16…31",
        2: "Bits 32…47",
        3: "Bits 48…63",
    }[x]

# Ref: p2
def rand(x):
    return {
        0x0: "NO_OP",
        0x1: "INC_LOOP_COUNTER",
        0x2: "DEC_LOOP_COUNTER",
        0x3: "CONDITION_TO_FIU",
        0x4: "SPLIT_C_SOURCE (C_SRC HI, NON-C_SRC LO)",
        0x5: "COUNT_ZEROS",
        0x6: "IMMEDIATE_OP",
        0x7: "SPARE_0x7",
        0x8: "SPARE_0x8",
        0x9: "PASS_A_HIGH",
        0xa: "PASS_B_HIGH",
        0xb: "DIVIDE",
        0xc: "START_MULTIPLY",
        0xd: "PRODUCT_LEFT_16",
        0xe: "PRODUCT_LEFT_32",
        0xf: "SPARE_0xf",
    }[x]

class Val(uengine.UcodeEngine):
    ''' Uengine for VAL '''
    def __init__(self, up, uload):
        super().__init__(
            up,
            "VAL",
            14,
            diag_chains.VAL_WRITE_DATA_REGISTER
        )
        for n, i in uload:
            self.define_instruction(n, i)
        self.finish()

    def explain(self, uadr):
        uins = self[uadr]
        yield "alu_func = " + ALU_FUNC[uins.alu_func]
        yield "a_adr = " + a_adr(uins.a_adr)
        yield "b_adr = " + b_adr(uins.b_adr)
        yield "c_adr = " + c_adr(uins.c_adr)
        yield "c_bus ← " + c_bus(uins.c_source, uins.c_mux_sel)
        yield "mult_a ← " + ab_src(uins.m_a_src)
        yield "mult_b ← " + ab_src(uins.m_b_src)
        yield "rand = " + rand(uins.rand)
        yield "frame = 0x%x" % uins.frame
