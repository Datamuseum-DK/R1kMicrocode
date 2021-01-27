'''
   TYP board microcode engine
'''

# Page number only references are to:
# https://datamuseum.dk/bits/30000959 R1000_SCHEMATIC_TYP.PDF

import uengine
import diag_chains
import typval

# Ref: p5
def a_adr(x):
    ''' Almost but not quite the same as VAL '''
    if x == 0x15:
        return "SPARE_0x15"
    if x == 0x16:
        return "SPARE_0x16"
    return typval.a_adr(x)

# Ref: p5
def mar_control(x):
    ''' explain mar control '''
    return {
        0x0: "NOP",
        0x1: "RESTORE_RDR",
        0x2: "DISABLE_DUMMY_ADR_NEXT",
        0x3: "SPARE_0x03",
        0x4: "RESTORE_MAR",
        0x5: "RESTORE_MAR_REFRESH",
        0x6: "INCREMENT_MAR",
        0x7: "INCREMENT_MAR_IF_INCOMPLETE",
        0x8: "LOAD_MAR_SYSTEM",
        0x9: "LOAD_MAR_CODE",
        0xa: "LOAD_MAR_IMPORT",
        0xb: "LOAD_MAR_DATA",
        0xc: "LOAD_MAR_QUEUE",
        0xd: "LOAD_MAR_TYPE",
        0xe: "LOAD_MAR_CONTROL",
        0xf: "LOAD_MAR_RESERVED",
    }[x]

# Ref: p5
def csa_control(x):
    ''' explain csa control '''
    return {
        0x0: "LOAD_CONTROL_TOP",
        0x1: "START_POP_DOWN",
        0x2: "PUSH_CSA",
        0x3: "POP_CSA",
        0x4: "DEC_CSA_BOTTOM",
        0x5: "INC_CSA_BOTTOM",
        0x6: "NOP",
        0x7: "FINISH_POP_DOWN",
    }[x]

# Ref: p5
def c_bus(src, mux):
    ''' explain cbus source '''
    if not src:
        return "fiu_bus"
    return {
        0: "ALU",
        1: "WSR",  # XXX: hard to read on p2
    }[mux]

# Ref: p5
def privacy_check(x):
    ''' explain privacy check '''
    return {
        0x0: "CHECK_BINARY_EQ",
        0x1: "CHECK_BINARY_OP",
        0x2: "CHECK_A_(TOP)_UNARY_OP",
        0x3: "CHECK_A_(TOP-1)_UNARY_OP",
        0x4: "CHECK_B_(TOP)_UNARY_OP",
        0x5: "CHECK_B_(TOP-1)_UNARY_OP",
        0x6: "CLEAR_PASS_PRIVACY_BIT",
        0x7: "NOP"
    }[x]

# Ref: p5
def rand(x):
    ''' explain random bits '''
    return {
        0x0: "NO_OP",
        0x1: "INC_LOOP_COUNTER",
        0x2: "DEC_LOOP_COUNTER",
        0x3: "SPLIT_C_SOURCE (C_SRC HI, NON-C_SRC LO)",
        0x4: "CHECK_CLASS_A_LIT",
        0x5: "CHECK_CLASS_B_LIT",
        0x6: "CHECK_CLASS_A_??_B",
        0x7: "CHECK_CLASS_AB_LIT",
        0x8: "SPARE_0x08",
        0x9: "PASS_A_HIGH",
        0xa: "PASS_B_HIGH",
        0xb: "ARRY IN = Q BIT FROM VAL",
        0xc: "WIRET_OUTHER_FRAME",
        0xd: "SET_PASS_PRIVACY_BIT",
        0xe: "CHECK_CLASS_SYSTEM_B",
        0xf: "INC_DEC_128",
    }[x]

class Typ(uengine.UcodeEngine):
    ''' Uengine for TYP '''
    def __init__(self, up, uload):
        super().__init__(
            up,
            "TYP",
            14,
            diag_chains.TYP_WRITE_DATA_REGISTER
        )
        for n, i in uload:
            self.define_instruction(n, i)
        self.finish()

    def explain(self, uadr):
        uins = self[uadr]
        yield "alu_func = " + typval.ALU_FUNC[uins.alu_func]
        yield "a_adr = " + a_adr(uins.a_adr)
        yield "b_adr = " + typval.b_adr(uins.b_adr)
        yield "c_adr = " + typval.c_adr(uins.c_adr)
        yield "c_bus ← " + c_bus(uins.c_source, uins.c_mux_sel)
        yield "frame = 0x%x" % uins.frame
        yield "mar_control = " + mar_control(uins.mar_cntl)
        yield "csa_control = " + csa_control(uins.csa_cntl)
        yield "privacy_check = " + privacy_check(uins.priv_check)
        yield "rand = " + rand(uins.rand)
