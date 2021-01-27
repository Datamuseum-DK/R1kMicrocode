'''
   This file contains the definitions of the DIAG chains used to
   load the microcode onto the various boards
'''

#######################################################################
# Microcode is loaded by the 8051 on each board, by feeding a byte
# at time to several serial-to-parallel registers.
# The structures below have 8 lists, one for each bit in the byte
# each listing the 8 signals appearing on the parallel outputs.

#######################################################################
# The chain for the Decode RAMs is documented at:
#     [30000958] R1000_SCHEMATIC_SEQ.PDF p56

SEQ_DECODER_SCAN = [
    [
        # DIAG.D0
        ("UADR.DEC11", "uadr", 2, 0),
        ("UADR.DEC10", "uadr", 3, 0),
        ("UADR.DEC8", "uadr", 5, 0),
        ("UADR.DEC7", "uadr", 6, 0),
        ("UADR.DEC5", "uadr", 8, 0),
        ("UADR.DEC4", "uadr", 9, 0),
        ("UADR.DEC1", "uadr", 12, 0),
        ("UADR.DEC0", "uadr", 13, 0),
    ], [
        # DIAG.D1
        ("IBUFF_FILL~.DEC", "ibuff_fill", 0, 1),
        ("USES_TOS.DEC", "uses_tos", 0, 0),
        ("DECODER.PARITY", "parity", 0, 0),
        ("UADR.DEC12", "uadr", 1, 0),
        ("UADR.DEC9", "uadr", 4, 0),
        ("UADR.DEC6", "uadr", 7, 0),
        ("UADR.DEC3", "uadr", 10, 0),
        ("UADR.DEC2", "uadr", 11, 0),
    ], [
        # DIAG.D2
        ("CSA_FREE.DEC1", "csa_free", 0, 0),
        ("CSA_FREE.DEC0", "csa_free", 1, 0),
        ("CSA_VALID.DEC2", "csa_valid", 0, 0),
        ("CSA_VALID.DEC1", "csa_valid", 1, 0),
        ("CSA_VALID.DEC0", "csa_valid", 2, 0),
        ("", "x25", 0, 0),
        ("", "x26", 0, 0),
        ("", "x27", 0, 0),
    ], [
        # DIAG.D3
        ("CUR_CLASS3", "cur_class", 0, 0),
        ("CUR_CLASS2", "cur_class", 1, 0),
        ("CUR_CLASS1", "cur_class", 2, 0),
        ("CUR_CLASS0", "cur_class", 3, 0),
        ("MEM_STRT.DEC2", "mem_strt", 0, 0),
        ("MEM_STRT.DEC1", "mem_strt", 1, 0),
        ("MEM_STRT.DEC0", "mem_strt", 2, 0),
        ("ZERO.D3.0", "zero_d3", 0, 0),
    ],[
        ("", "zero_d4", 0, 0),
        ("", "zero_d4", 1, 0),
        ("", "zero_d4", 2, 0),
        ("", "zero_d4", 3, 0),
        ("", "zero_d4", 4, 0),
        ("", "zero_d4", 5, 0),
        ("", "zero_d4", 6, 0),
        ("", "zero_d4", 7, 0),
    ],[
        ("", "zero_d5", 0, 0),
        ("", "zero_d5", 1, 0),
        ("", "zero_d5", 2, 0),
        ("", "zero_d5", 3, 0),
        ("", "zero_d5", 4, 0),
        ("", "zero_d5", 5, 0),
        ("", "zero_d5", 6, 0),
        ("", "zero_d5", 7, 0),
    ],[
        ("", "zero_d6", 0, 0),
        ("", "zero_d6", 1, 0),
        ("", "zero_d6", 2, 0),
        ("", "zero_d6", 3, 0),
        ("", "zero_d6", 4, 0),
        ("", "zero_d6", 5, 0),
        ("", "zero_d6", 6, 0),
        ("", "zero_d6", 7, 0),
    ],[
        ("", "zero_d7", 0, 0),
        ("", "zero_d7", 1, 0),
        ("", "zero_d7", 2, 0),
        ("", "zero_d7", 3, 0),
        ("", "zero_d7", 4, 0),
        ("", "zero_d7", 5, 0),
        ("", "zero_d7", 6, 0),
        ("", "zero_d7", 7, 0),
    ]
]

#######################################################################
# https://datamuseum.dk/bits/30000958 R1000_SCHEMATIC_SEQ.PDF
#
# p3:
#	brnch_adr.uir<0:13>
#	parity.uir
#	latch.uir
#	br_type.uir<0:3>
#	b_timing.uir<0:1
#	cond_sel.uir<0:6>
#	halt
#	l_late_macro
#	lex_adr.uir<0:1>
#	en_micro.uir
#	int_reads.uir<0:2>
#	random.uir<0:6>
# p97:
#	UIR scan chain
#

SEQ_UIR_SCAN_CHAIN = [
    [
        # DIAG.D0 = L21+L23 @ p80
        ("BRNCH_ADR.UIR6", "branch_adr", 7, 0),
        ("BRNCH_ADR.UIR7", "branch_adr", 6, 0),
        ("BRNCH_ADR.UIR8", "branch_adr", 5, 0),
        ("BRNCH_ADR.UIR9", "branch_adr", 4, 0),
        ("BRNCH_ADR.UIR10", "branch_adr", 3, 0),
        ("BRNCH_ADR.UIR11", "branch_adr", 2, 0),
        ("BRNCH_ADR.UIR12", "branch_adr", 1, 0),
        ("BRNCH_ADR.UIR13", "branch_adr", 0, 0),
    ],[
        # DIAG.D1 = L25+L29 @ p80
        ("COND_SEL.UIR~5", "cond_sel", 1, 1),
        ("COND_SEL.UIR~6", "cond_sel", 0, 1),
        ("BRNCH_ADR.UIR0", "branch_adr", 13, 0),
        ("BRNCH_ADR.UIR1", "branch_adr", 12, 0),
        ("BRNCH_ADR.UIR2", "branch_adr", 11, 0),
        ("BRNCH_ADR.UIR3", "branch_adr", 10, 0),
        ("BRNCH_ADR.UIR4", "branch_adr", 9, 0),
        ("BRNCH_ADR.UIR5", "branch_adr", 8, 0),
    ],[
        # DIAG.D2 = I29+I31 @ p80
        ("LATCH.UIR", "latch", 0, 0),
        ("BR_TYPE.UIR1", "br_type", 2, 0),
        ("BR_TYPE.UIR0", "br_type", 3, 0),
        ("COND_SEL.UIR~0", "cond_sel", 6, 1),
        ("COND_SEL.UIR~1", "cond_sel", 5, 1),
        ("COND_SEL.UIR~4", "cond_sel", 2, 1),
        ("COND_SEL.UIR~3", "cond_sel", 3, 1),
        ("COND_SEL.UIR~2", "cond_sel", 4, 1),
    ],[
        # DIAG.D3 = I33+I35 @ p80
        ("INT_READS.UIR2", "int_reads", 0, 0),
        ("INT_READS.UIR1", "int_reads", 1, 0),
        ("BR_TYPE.UIR3", "br_type", 0, 0),
        ("BR_TYPE.UIR2", "br_type", 1, 0),
        ("EN_MICRO.UIR", "en_micro", 0, 0),
        ("B_TIMING.UIR1", "b_timing", 0, 0),
        ("B_TIMING.UIR0", "b_timing", 1, 0),
        ("INT_READS.UIR0", "int_reads", 2, 0),
    ],[
        # DIAG.D4 - unused
        ("", "zero_4", 7, 0),
        ("", "zero_4", 6, 0),
        ("", "zero_4", 5, 0),
        ("", "zero_4", 4, 0),
        ("", "zero_4", 3, 0),
        ("", "zero_4", 2, 0),
        ("", "zero_4", 1, 0),
        ("", "zero_4", 0, 0),
    ],[
        # DIAG.D5 = I37 + I39 @ p80
        ("RANDOM.UIR3", "random", 3, 0),
        ("RANDOM.UIR2", "random", 4, 0),
        ("RANDOM.UIR5", "random", 1, 0),
        ("RANDOM.UIR4", "random", 2, 0),
        ("RANDOM.UIR6", "random", 0, 0),
        ("PARITY.UIR", "parity", 0, 0),
        ("LEX_ADR.UIR1", "lex_adr", 0, 0),
        ("LEX_ADR.UIR0", "lex_adr", 1, 0),
    ],[
        # DIAG.D6 = I41 @ p80
        ("", "zero_6", 5, 0),
        ("", "zero_6", 4, 0),
        ("", "zero_6", 3, 0),
        ("", "zero_6", 2, 0),
        ("", "zero_6", 1, 0),
        ("", "zero_6", 0, 0),
        ("RANDOM.UIR1", "random", 5, 0),
        ("RANDOM.UIR0", "random", 6, 0),
    ],[
        # DIAG.D7 - unused
        ("", "zero_7", 7, 0),
        ("", "zero_7", 6, 0),
        ("", "zero_7", 5, 0),
        ("", "zero_7", 4, 0),
        ("", "zero_7", 3, 0),
        ("", "zero_7", 2, 0),
        ("", "zero_7", 1, 0),
        ("", "zero_7", 0, 0),
    ]
]

#######################################################################
# https://datamuseum.dk/bits/30000957 R1000_SCHEMATIC_FIU.PDF
# p49:
#	OFFS_LIT<0:6>
#	LFL<0:6>
#	LFREG_CNTL<0:1>
#	OFFS_SRC
#	LENGTH_SRC
#	FILL_MODE_SRC
#	OREG_SRC
#	OP_SEL<0:1>
#	VMUX_SEL<0:1>
#	MEM_START<0:4>
#	RDATA_SRC
#	UIR.P
#	TIVI_SRC<0:3>
#	LOAD_OREG~
#	LOAD_VAR~
#	LOAD_TAR~
#	LOAD_MDR~
#
FIU_MICRO_INSTRUCTION_REGISTER = [
    [
        ("", 'x00', 0, 0),
        ("", 'x01', 0, 0),
        ("", 'x02', 0, 0),
        ("", 'x03', 0, 0),
        ("", 'x04', 0, 0),
        ("", 'x05', 0, 0),
        ("", 'x06', 0, 0),
        ("", 'x07', 0, 0),
        # DIAG.D0 = J18+J19 @p48
        #("LFL0", "lfl", 6, 0),
        #("OFFS_LIT6", "offs_lit", 0, 0),
        #("OFFS_LIT5", "offs_lit", 1, 0),
        #("OFFS_LIT4", "offs_lit", 2, 0),
        #("OFFS_LIT3", "offs_lit", 3, 0),
        #("OFFS_LIT2", "offs_lit", 4, 0),
        #("OFFS_LIT1", "offs_lit", 5, 0),
        #("OFFS_LIT0", "offs_lit", 6, 0),
    ], [
        ("", 'x10', 0, 0),
        ("", 'x11', 0, 0),
        ("", 'x12', 0, 0),
        ("", 'x13', 0, 0),
        ("", 'x14', 0, 0),
        ("", 'x15', 0, 0),
        ("", 'x16', 0, 0),
        ("", 'x17', 0, 0),
        # DIAG.D1 = K12+K16 @p48
        #("LFREG_CNTL1", "lfreg_cntl", 0, 0),
        #("LFREG_CNTL0", "lfreg_cntl", 1, 0),
        #("LFL6", "lfl", 0, 0),
        #("LFL5", "lfl", 1, 0),
        #("LFL4", "lfl", 2, 0),
        #("LFL3", "lfl", 3, 0),
        #("LFL2", "lfl", 4, 0),
        #("LFL1", "lfl", 5, 0),
    ], [
        ("", 'x20', 0, 0),
        ("", 'x21', 0, 0),
        ("", 'x22', 0, 0),
        ("", 'x23', 0, 0),
        ("", 'x24', 0, 0),
        ("", 'x25', 0, 0),
        ("", 'x26', 0, 0),
        ("", 'x27', 0, 0),
        # DIAG.D2 = H20+M3 @p48
        #("CHAIN?", "chain", 0, 0),
        #("XX", "xxd2", 0, 0),
        #("OREG_SRC", "oreg_src", 0, 0),
        #("FILL_MODE_SRC", "fill_mode_src", 0, 0),
        #("VMUX_SEL1", "vmux_sel", 0, 0),
        #("VMUX_SEL0", "vmux_sel", 1, 0),
        #("OP_SEL1", "op_sel", 0, 0),
        #("OP_SEL0", "op_sel", 1, 0),
    ], [
        ("", 'x30', 0, 0),
        ("", 'x31', 0, 0),
        ("", 'x32', 0, 0),
        ("", 'x33', 0, 0),
        ("", 'x34', 0, 0),
        ("", 'x35', 0, 0),
        ("", 'x36', 0, 0),
        ("", 'x37', 0, 0),
        # DIAG.D3 = K43+K47 @p48
        #("TIVI_SRC3", "tivi_src", 0, 0),
        #("TIVI_SRC2", "tivi_src", 1, 0),
        #("TIVI_SRC1", "tivi_src", 2, 0),
        #("TIVI_SRC0", "tivi_src", 3, 0),
        #("LOAD_MDR", "load_mdr", 0, 0),
        #("LOAD_TAR~", "load_tar", 0, 1),
        #("LOAD_VAR~", "load_var", 0, 1),
        #("LOAD_OREG~", "load_oreg", 0, 1),
    ], [
        ("", 'x40', 0, 0),
        ("", 'x41', 0, 0),
        ("", 'x42', 0, 0),
        ("", 'x43', 0, 0),
        ("", 'x44', 0, 0),
        ("", 'x45', 0, 0),
        ("", 'x46', 0, 0),
        ("", 'x47', 0, 0),
        # DIAG.D4 = M35+M39 @p48
        #("UIR.P", "parity", 0, 0),
        #("XX", "xxd4", 0, 0),
        #("RDATA_SRC", "rdata_src", 0, 0),
        #("MEM_START4", "mem_start", 0, 0),
        #("MEM_START3", "mem_start", 1, 0),
        #("MEM_START2", "mem_start", 2, 0),
        #("MEM_START1", "mem_start", 3, 0),
        #("MEM_START0", "mem_start", 4, 0),
    ], [
        # DIAG.D5 - unused
	("", "x50", 0, 0),
	("", "x51", 0, 0),
	("", "x52", 0, 0),
	("", "x53", 0, 0),
	("", "x54", 0, 0),
	("", "x55", 0, 0),
	("", "x56", 0, 0),
	("", "x57", 0, 0),
    ], [
        # DIAG.D6 - unused
	("", "x60", 0, 0),
	("", "x61", 0, 0),
	("", "x62", 0, 0),
	("", "x63", 0, 0),
	("", "x64", 0, 0),
	("", "x65", 0, 0),
	("", "x66", 0, 0),
	("", "x67", 0, 0),
    ], [
        # DIAG.D7 - unused
	("", "x70", 0, 0),
	("", "x71", 0, 0),
	("", "x72", 0, 0),
	("", "x73", 0, 0),
	("", "x74_parity?", 0, 0),
	("", "x75", 0, 0),
	("", "x76", 0, 0),
	("", "x77", 0, 0),
    ]
]

#######################################################################
# https://datamuseum.dk/bits/30000959 R1000_SCHEMATIC_TYP.PDF
# p3:
#	uir.a<0:5>		*L23,L24,L25,L26,L27,L28
#	uir.b<0:5>		*L29,L30,L31,L32,L33,L34
#	uir.frame<0:4>		*L35,L36,L37,L38,L39
#	c_lit~<0:1>		*I18,I19
#	uir.p			*I20
#	uir.rand_<0:3>		*K19,J20,J19,J18
#	uir.c<0:5>		*K25,K24,K23,K22,J25,J24
#	uir.prv_chk0		*J23
#	uir.prv_chk1		*J22
#	uir.prv_ch[k2]		*I25
#	c_mux.sel		*I24
#	uir.alu_func<0:4>	*I23,I22,I21,J21,K21
#	uir.c_source		*K20
#	mar_cntl_<0:3>		*I17,I16,I15,I14
#	csa_cntl_<0:2>		*L16,L15,L14
#
TYP_WRITE_DATA_REGISTER = [
    [
        # DIAG.D8 = K27+K30 @p63
        # Inverted because DIAG.D8 is non-inverted input
        # to inverting mux K27
        ("UIR.B1", "b_adr", 4, 1),
        ("UIR.B0", "b_adr", 5, 1),
        ("UIR.A5", "a_adr", 0, 1),
        ("UIR.A4", "a_adr", 1, 1),
        ("UIR.A3", "a_adr", 2, 1),
        ("UIR.A2", "a_adr", 3, 1),
        ("UIR.A1", "a_adr", 4, 1),
        ("UIR.A0", "a_adr", 5, 1),
    ], [
        # DIAG.D9 = K33+K36 @p63
        # Inverted because DIAG.D9 is non-inverted input
        # to inverting mux K30
        ("UIR.FRAME3", "frame", 1, 1),
        ("UIR.FRAME2", "frame", 2, 1),
        ("UIR.FRAME1", "frame", 3, 1),
        ("UIR.FRAME0", "frame", 4, 1),
        ("UIR.B5", "b_adr", 0, 1),
        ("UIR.B4", "b_adr", 1, 1),
        ("UIR.B3", "b_adr", 2, 1),
        ("UIR.B2", "b_adr", 3, 1),
    ], [
        # DIAG.D10 = K43 @p63 + J17+J16 @ p64
        # Note that pin 2 on J17 says C_LIT~4
        # That must be a mistake for UIR.FRAME4
        # Compare with VAL schematic.
        ("UIR.RAND3", 'rand', 0, 0),
        ("UIR.RAND2", 'rand', 1, 0),
        ("UIR.RAND1", 'rand', 2, 0),
        ("UIR.RAND0", 'rand', 3, 0),
        ("UIR.P", 'parity', 0, 0),
        ("UIR.C_LIT~1", 'c_lit', 0, 1),
        ("UIR.C_LIT~0", 'c_lit', 1, 1),
        ("UIR.FRAME4", "frame", 0, 0),
    ], [
        # DIAG.D11 = K26+J26 @p64
        ("UIR.PRIV_CHEK1", 'priv_check', 1, 0),
        ("UIR.PRIV_CHEK0", 'priv_check', 2, 0),
        ("UIR.C5", 'c_adr', 0, 0),
        ("UIR.C4", 'c_adr', 1, 0),
        ("UIR.C3", 'c_adr', 2, 0),
        ("UIR.C2", 'c_adr', 3, 0),
        ("UIR.C1", 'c_adr', 4, 0),
        ("UIR.C0", 'c_adr', 5, 0),
    ], [
        # DIAG.D12 = H23+H21 @p64
        ("UIR.C_SOURCE", 'c_source', 0, 0),
        ("UIR.ALU_FUNC4", 'alu_func', 0, 0),
        ("UIR.ALU_FUNC3", 'alu_func', 1, 0),
        ("UIR.ALU_FUNC2", 'alu_func', 2, 0),
        ("UIR.ALU_FUNC1", 'alu_func', 3, 0),
        ("UIR.ALU_FUNC0", 'alu_func', 4, 0),
        ("C_MUX.SEL", 'c_mux_sel', 0, 0),
        ("UIR.PRIV.CHEK2", 'priv_check', 0, 0),
    ], [
        # DIAG.D13 = I13+L13 @p65
        ("CSA_SCAN_OUT", 'x50', 0, 0),
        ("CSA_CNTL2", 'csa_cntl', 0, 0),
        ("CSA_CNTL1", 'csa_cntl', 1, 0),
        ("CSA_CNTL0", 'csa_cntl', 2, 0),
        ("MAR_CNTL3", 'mar_cntl', 0, 0),
        ("MAR_CNTL2", 'mar_cntl', 1, 0),
        ("MAR_CNTL1", 'mar_cntl', 2, 0),
        ("MAR_CNTL0", 'mar_cntl', 3, 0),
    ], [
        ("", 'x60', 0, 0),
        ("", 'x61', 0, 0),
        ("", 'x62', 0, 0),
        ("", 'x63', 0, 0),
        ("", 'x64', 0, 0),
        ("", 'x65', 0, 0),
        ("", 'x66', 0, 0),
        ("", 'x67', 0, 0),
    ], [
        ("", 'x70', 0, 0),
        ("", 'x71', 0, 0),
        ("", 'x72', 0, 0),
        ("", 'x73', 0, 0),
        ("", 'x74', 0, 0),
        ("", 'x75', 0, 0),
        ("", 'x76', 0, 0),
        ("", 'x77', 0, 0),
    ],
]

#######################################################################
# https://datamuseum.dk/bits/30000960 R1000_SCHEMATIC_VAL.PDF
#    p3:
#	uir.a_<0:5>		*L23,L24,L25,L26,L27,L28
#	uir.b_<0:5>		*L29,L30,L31,L32,L33,L34
#	uir.c_<0:5>		*K25,K24,K23,K22,J25,J24
#	uir.frame_<0:4>		*L35,L36,L37,L38,L39
#	c_mux.sel_<0:1>		*I18,I19
#	uir.rand_<0:3>		*K19,J20,J19,J18
#	uir.m_a_src_<0:1>	*J23,J22
#	uir.m_b_src_<0:1>	*I25,I24
#	uir.alu_func<0:4>	*I23,I22,I21,J21,K21
#	uir.c_source		*K20
#	uir.p(arity)		*I20
#   p65:  parity check
#	c_mux_sel1
#	uir.rand_<0:3>
#	uir.a_<0:5>
#	uir.b_<0:5>
#	uir.c_<0:5>
#	uir.c_source
#	uir.frame_<0:4>
#	uir.alu_func_<0:4>
#	uir.a_src<0:1>
#	uir.b_src<0:1>
#	uir.p<0:1>
#	uir.c_mux_sel0
#   p66:
#	DIAG.D<11:12>
#   p67:
#	DIAG.D<8:10>

VAL_WRITE_DATA_REGISTER = [
    [
        # DIAG.D8 = K27 + K30 @ p66
        # Inverted because DIAG.D8 is non-inverted input
        # to inverting mux K27
        ("UIR.B1", 'b_adr', 4, 1),
        ("UIR.B0", 'b_adr', 5, 1),
        ("UIR.A5", 'a_adr', 0, 1),
        ("UIR.A4", 'a_adr', 1, 1),
        ("UIR.A3", 'a_adr', 2, 1),
        ("UIR.A2", 'a_adr', 3, 1),
        ("UIR.A1", 'a_adr', 4, 1),
        ("UIR.A0", 'a_adr', 5, 1),
    ], [
        # DIAG.D9 = K33 + K36 @ p66
        # Inverted because DIAG.D9 is non-inverted input
        # to inverting mux K33
        ("FRAME.3", 'frame', 1, 1),
        ("FRAME.2", 'frame', 2, 1),
        ("FRAME.1", 'frame', 3, 1),
        ("FRAME.0", 'frame', 4, 1),
        ("UIR.B5", 'b_adr', 0, 1),
        ("UIR.B4", 'b_adr', 1, 1),
        ("UIR.B3", 'b_adr', 2, 1),
        ("UIR.B2", 'b_adr', 3, 1),
    ], [
        # DIAG.D10 = K43 @p66, J16 @p67
        ("UIR.RAND3", 'rand', 0, 0),
        ("UIR.RAND2", 'rand', 1, 0),
        ("UIR.RAND1", 'rand', 2, 0),
        ("UIR.RAND0", 'rand', 3, 0),
        ("UIR.P", 'parity', 0, 0),
        ("C_MUX.SEL1", 'c_mux_sel', 0, 0),
        ("C_MUX.SEL0", 'c_mux_sel', 1, 0),
        ("FRAME.4", 'frame', 0, 0),
    ], [
        # DIAG.D11 = K26 + J26 @ p67
        ("UIR.M_A_SRC1", 'm_a_src', 0, 0),
        ("UIR.M_A_SRC0", 'm_a_src', 1, 0),
        ("UIR.C5", 'c_adr', 0, 0),
        ("UIR.C4", 'c_adr', 1, 0),
        ("UIR.C3", 'c_adr', 2, 0),
        ("UIR.C2", 'c_adr', 3, 0),
        ("UIR.C1", 'c_adr', 4, 0),
        ("UIR.C0", 'c_adr', 5, 0),
    ], [
        # DIAG.D12 = H23+H21 @ p67
        ("UIR.C_SOURCE", 'c_source', 0, 0),
        ("UIR_ALU_FUNC4", 'alu_func', 0, 0),
        ("UIR.ALU_FUNC3", 'alu_func', 1, 0),
        ("UIR.ALU_FUNC2", 'alu_func', 2, 0),
        ("UIR.ALU_FUNC1", 'alu_func', 3, 0),
        ("UIR.ALU_FUNC0", 'alu_func', 4, 0),
        ("UIR.M_B_SRC1", 'm_b_src', 0, 0),
        ("UIR.M_B_SRC0", 'm_b_src', 1, 0),
    ], [
        ("", 'x50', 0, 0),
        ("", 'x50', 1, 0),
        ("", 'x50', 2, 0),
        ("", 'x50', 3, 0),
        ("", 'x50', 4, 0),
        ("", 'x50', 5, 0),
        ("", 'x50', 6, 0),
        ("", 'x50', 7, 0),
    ], [
        ("", 'x60', 0, 0),
        ("", 'x60', 1, 0),
        ("", 'x60', 2, 0),
        ("", 'x60', 3, 0),
        ("", 'x60', 4, 0),
        ("", 'x60', 5, 0),
        ("", 'x60', 6, 0),
        ("", 'x60', 7, 0),
    ], [
        ("", 'x70', 0, 0),
        ("", 'x70', 1, 0),
        ("", 'x70', 2, 0),
        ("", 'x70', 3, 0),
        ("", 'x70', 4, 0),
        ("", 'x70', 5, 0),
        ("", 'x70', 6, 0),
        ("", 'x70', 7, 0),
    ],
]
