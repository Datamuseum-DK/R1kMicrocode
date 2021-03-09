
'''
    Functions explaining uins words as strings
    ==========================================
'''

def seq_br_type(val):
    return {
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
    }.get(val)

def seq_cond_sel(val):
    return {
        # Ref: R1000_SCHEMATIC_TYP.PDF p40
        0x18: "TYP.ALU_ZERO(late)",
        0x19: "TYP.ALU_NONZERO(late)",
        0x1a: "TYP.ALU_A_GT_OR_GE_B(late)",
        0x1c: "TYP.LOOP_COUNTER_ZERO(early)",
        0x1e: "TYP.ALU_ZERO(late, combo)",
        0x1f: "TYP.ALU_32_CARRY_OUT(late)",
        0x20: "TYP.ALU_CARRY(late)",
        0x21: "TYP.ALU_OVERFLOW(late)",
        0x22: "TYP.ALU_LT_ZERO(late)",
        0x23: "TYP.ALU_LE_ZERO(late)",
        0x24: "TYP.SIGN_BITS_EQUAL(med_late)",
        0x25: "TYP.FALSE (early)",
        0x26: "TYP.TRUE (early)",
        0x27: "TYP.PREVIOUS (early)",
        0x28: "TYP.OF_KIND_MATCH (med_late)",
        0x29: "TYP.CLASS_A_EQ_LIT (med_late)",
        0x2a: "TYP.CLASS_B_EQ_LIT (med_late)",
        0x2b: "TYP.CLASS_A_EQ_B (med_late)",
        0x2c: "TYP.CLASS_A_B_EQ_LIT (med_late)",
        0x2d: "TYP.PRIVACY_A_OP_PASS (med_late)",
        0x2e: "TYP.PRIVACY_B_OP_PASS (med_late)",
        0x2f: "TYP.PRIVACY_BIN_EQ_PASS (med_late)",
        0x30: "TYP.PRIVACY_BIN_OP_PASS (med_late)",
        0x31: "TYP.PRIVACY_NAMES_EQ (med_late)",
        0x32: "TYP.PRIVACY_PATHS_EQ (med_late)",
        0x33: "TYP.PRIVACY_STRUCTURE (med_late)",
        0x34: "TYP.PASS_PRIVACY_BIT (early)",
        0x35: "TYP.D_BUS_BIT_32 (med_late)",
        0x36: "TYP.D_BUS_BIT_33 (med_late)",
        0x37: "TYP.D_BUS_BIT_34 (med_late)",
        0x38: "TYP.D_BUS_BIT_35 (med_late)",
        0x39: "TYP.D_BUS_BIT_36 (med_late)",
        0x3a: "TYP.D_BUS_BIT_33_34_OR_36 (med_late)",
        0x3f: "TYP.D_BUS_BIT_21 (med_late)",
        # Ref: R1000_HARDWARE_FUNCTIONAL_SPECIFICATION.PDF p81
        0x40: "SEQ.macro_restartable",
        0x41: "SEQ.restartable_@(PC-1)",
        0x42: "SEQ.valid_lex(loop_counter)",
        0x43: "SEQ.loop_counter_zero",
        0x44: "SEQ.TOS_LATCH_valid",
        0x45: "SEQ.saved_latched_cond",
        0x46: "SEQ.previously_latched_cond",
        0x47: "SEQ.#_entries_in_stack_zero",
        0x48: "SEQ.ME_CSA_underflow",
        0x49: "SEQ.ME_CSA_overflow",
        0x4a: "SEQ.ME_resolve_ref",
        0x4b: "SEQ.ME_TOS_opt_error",
        0x4c: "SEQ.ME_dispatch",
        0x4d: "SEQ.ME_break_class",
        0x4e: "SEQ.ME_ibuff_emptry",
        0x4f: "SEQ.uE_field_number_error",
        # Ref: R1000_SCHEMATIC_FIU.PDF p60
        0x60: "FIU.MEM_EXCEPTION~",
        0x61: "FIU.PHYSICAL_LAST~",
        0x62: "FIU.WRITE_LAST",
        0x63: "CSA_HIT",
        0x64: "OFFSET_REGISTER_????",
        0x65: "CROSS_WORD_FIELD~",
        0x66: "NEAR_TOP_OF_PAGE",
        0x67: "REFRESH_MACRO_EVENT",
        0x68: "CONTROL_ADDRESS_OUT_OF_RANGE",
        0x69: "SCAVENGER_HIT~",
        0x6a: "PAGE_CROSSING~",
        0x6b: "CACHE_MISS~",
        0x6c: "INCOMPLETE_MEMORY_CYCLE",
        0x6d: "MAR_MODIFIED",
        0x6e: "INCOMPLETE_MEMORY_CYCLE_FOR_PAGE_CROSSING",
        0x6f: "MAR_WORD_EQUALIS_ZERO~",
    }.get(val)

def seq_int_reads(val):
    return {
        0: "TYP VAL BUS",
        1: "CURRENT MACRO INSTRUCTION",
        2: "DECODING MACRO INSTRUCTION",
        3: "TOP OF THE MICRO STACK",
        4: "SAVE OFFSET",
        5: "RESOLVE RAM",
        6: "CONTROL TOP",
        7: "CONTROL PRED",
    }.get(val)

def fiu_tivi_src(val):
    return {
        0x0: "tar_var",
        0x1: "tar_val",
        0x2: "tar_fiu",
        0x3: "tar_frame",
        0x4: "fiu_var",
        0x5: "fiu_val",
        0x6: "fiu_fiu",
        0x7: "fiu_frame",
        0x8: "type_var",
        0x9: "type_val",
        0xa: "type_fiu",
        0xb: "type_frame",
        0xc: "mar_0xc",
        0xd: "mar_0xd",
        0xe: "mar_0xe",
        0xf: "mar_0xf",
    }.get(val)

def fiu_mem_start(val):
    return {
    0x00: "hold0",
    0x01: "hold1",
    0x02: "start-rd",
    0x03: "start-wr",
    0x04: "continue",
    0x05: "start_rd_if_true",
    0x06: "start_rd_if_false",
    0x07: "start_wr_if_true",
    0x08: "start_wr_if_false",
    0x09: "start_continue_if_true",
    0x0a: "start_continue_if_false",
    0x0b: "start_last_cmd",
    0x0c: "start_if_incmplt",
    0x0d: "start_physical_rd",
    0x0e: "start_physical_wr",
    0x0f: "start_physical_tag_rd",
    0x10: "start_physical_tag_wr",
    0x11: "start_tag_query",
    0x12: "start_lru_query",
    0x13: "start_available_query",
    0x14: "start_name_query",
    0x15: "setup_tag_read",
    0x16: "init_mru",
    0x17: "scavenger_write",
    0x18: "acknowledge_refresh",
    0x19: "nop_0x19",
    0x1a: "force_miss",
    0x1b: "reserved_0x1b",
    0x1c: "reserved_0x1c",
    0x1d: "reserved_0x1d",
    0x1e: "reserved_0x1e",
    0x1f: "reserved_0x1f",
    }.get(val)

def fiu_lfl(val):
    if val & 0x40:
        return "zero-fill 0x%x" % (val & 0x3f)
    return "sign-fill 0x%x" % (val & 0x3f)

def typval_a_adr(val):
    if val < 0x10:
        return "GP 0x%x" % val
    if val == 0x10:
        return "TOP"
    if val == 0x11:
        return "TOP + 1"
    if val == 0x12:
        return "SPARE_0x12"
    if val == 0x13:
        return "LOOP_REG"
    if val == 0x14:
        return "ZEROS"
    if val == 0x15:
        return "ZERO_COUNTER"  # TYP: SPARE
    if val == 0x16:
        return "PRODUCT"  # TYP: SPARE
    if val == 0x17:
        return "LOOP_COUNTER"
    if val < 0x20:
        return "TOP - %d" % (0x20 - val)
    return "FRAME:REG0x%x" % (val - 0x20)

def typval_b_adr(val):
    if val == 0x14:
        return "BOT - 1"
    if val == 0x15:
        return "BOT"
    if val == 0x16:
        return "CSA/VAL_BUS"
    if val == 0x17:
        return "SPARE_0x17"
    return typval_a_adr(val)

def typval_c_adr(val):
    # XXX: Looks bogus!
    if val < 0x20:
        return "FRAME:REG??" # XXX: "inversion of C field of uword
    if val < 0x40:
        return "GP 0x%x" % (0x3f - val)
    if val < 0x2f:
        return "TOP"
    if val < 0x2e:
        return "TOP + 1"
    if val < 0x2d:
        return "SPARE_0x2d"
    if val < 0x2c:
        return "LOOP_REG"
    if val < 0x2b:
        return "BOT - 1"
    if val < 0x2a:
        return "BOT"
    if val < 0x29:
        return "WRITE_DISABLE (default)"
    if val < 0x28:
        return "LOOP_COUNTER"
    return "TOP - %d" % (val - 0x1f)

def typval_alu_func(val):
    return {
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
    }.get(val)

def typ_a_adr(val):
    if val == 0x15:
        return "SPARE_0x15"
    if val == 0x16:
        return "SPARE_0x16"
    return typval_a_adr(val)

def typ_b_adr(val):
    return typval_b_adr(val)

def typ_c_adr(val):
    return typval_c_adr(val)

def typ_mar_cntl(val):
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
    }.get(val)

def typ_csa_cntl(val):
    return {
        0x0: "LOAD_CONTROL_TOP",
        0x1: "START_POP_DOWN",
        0x2: "PUSH_CSA",
        0x3: "POP_CSA",
        0x4: "DEC_CSA_BOTTOM",
        0x5: "INC_CSA_BOTTOM",
        0x6: "NOP",
        0x7: "FINISH_POP_DOWN",
    }.get(val)

def typ_c_mux_sel(val):
    return {
        0x0: "ALU",
        0x1: "WSR",  # XXX: hard to read on p2
    }.get(val)

def typ_priv_check(val):
    return {
        0x0: "CHECK_BINARY_EQ",
        0x1: "CHECK_BINARY_OP",
        0x2: "CHECK_A_(TOP)_UNARY_OP",
        0x3: "CHECK_A_(TOP-1)_UNARY_OP",
        0x4: "CHECK_B_(TOP)_UNARY_OP",
        0x5: "CHECK_B_(TOP-1)_UNARY_OP",
        0x6: "CLEAR_PASS_PRIVACY_BIT",
        0x7: "NOP"
    }.get(val)

def typ_rand(val):
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
    }.get(val)

def typ_alu_func(val):
    return typval_alu_func(val)

def val_a_adr(val):
    return typval_a_adr(val)

def val_b_adr(val):
    return typval_b_adr(val)

def val_c_adr(val):
    return typval_c_adr(val)

def val_alu_func(val):
    return typval_alu_func(val)

def val_m_a_src(val):
    return {
        0: "Bits 0…15",
        1: "Bits 16…31",
        2: "Bits 32…47",
        3: "Bits 48…63",
    }.get(val)

def val_m_b_src(val):
    return val_m_a_src(val)

def val_rand(val):
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
    }.get(val)

def val_c_mux_sel(val):
    return {
        0: "ALU << 1",
        1: "ALU >> 16",
        2: "ALU",
        3: "WSR",  # XXX: hard to read on p2
    }.get(val)
