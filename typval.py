'''
   VAL board microcode engine
'''

# Page number only references are to:
# "VAL" https://datamuseum.dk/bits/30000960 R1000_SCHEMATIC_VAL.PDF
# "TYP" https://datamuseum.dk/bits/30000959 R1000_SCHEMATIC_TYP.PDF

# Ref: VAL:p2
# Ref: TYP:p5
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

# Ref: VAL:p2
# Ref: TYP:p5
def a_adr(x):
    ''' explain a_adr field '''
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
        return "ZERO_COUNTER"  # TYP: SPARE
    if x == 0x16:
        return "PRODUCT"  # TYP: SPARE
    if x == 0x17:
        return "LOOP_COUNTER"
    if x < 0x20:
        return "TOP - %d" % (0x20 - x)
    return "FRAME:REG0x%x" % (x - 0x20)

# Ref: p2
def b_adr(x):
    ''' explain b_adr field '''
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
    ''' explain c_adr field '''
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
