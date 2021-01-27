'''
   FIU board microcode engine
'''

import uengine
import diag_chains

def tivi_src(x):
    ''' explain tivi_src '''
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
    }[x]

def mem_start(x):
    ''' explain mem_start '''
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
    }[x]

class Fiu(uengine.UcodeEngine):
    ''' Uengine for FIU '''
    def __init__(self, up, uload):
        super().__init__(
            up,
            "FIU",
            14,
            diag_chains.FIU_MICRO_INSTRUCTION_REGISTER
        )
        for n, i in uload:
            self.define_instruction(n, i)
        self.finish()

    def explain(self, uadr):
        uins = self[uadr]
        if uins.lfl & 0x40:
            yield "lfl = zero-fill 0x%x" % (uins.lfl & 0x3f)
        else:
            yield "lfl = sign-fill 0x%x" % (uins.lfl & 0x3f)
        yield "tivi_src = " + tivi_src(uins.tivi_src)
        yield "mem_start = " + mem_start(uins.mem_start)
