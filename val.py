'''
   VAL board microcode engine
'''

# Page number only references are to:
# https://datamuseum.dk/bits/30000960 R1000_SCHEMATIC_VAL.PDF

import uengine
import diag_chains
import typval

# Ref: p2
def c_bus(src, mux):
    ''' explain c-bus source '''
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
    ''' explain a/b bus source '''
    return {
        0: "Bits 0…15",
        1: "Bits 16…31",
        2: "Bits 32…47",
        3: "Bits 48…63",
    }[x]

# Ref: p2
def rand(x):
    ''' explain random bits '''
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
        yield "alu_func = " + typval.ALU_FUNC[uins.alu_func]
        yield "a_adr = " + typval.a_adr(uins.a_adr)
        yield "b_adr = " + typval.b_adr(uins.b_adr)
        yield "c_adr = " + typval.c_adr(uins.c_adr)
        yield "c_bus ← " + c_bus(uins.c_source, uins.c_mux_sel)
        yield "mult_a ← " + ab_src(uins.m_a_src)
        yield "mult_b ← " + ab_src(uins.m_b_src)
        yield "rand = " + rand(uins.rand)
        yield "frame = 0x%x" % uins.frame
