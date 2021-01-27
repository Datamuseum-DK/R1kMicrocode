'''
   FIU board microcode engine
'''

import uengine
import diag_chains

class Fiu(uengine.UcodeEngine):
    ''' Uengine for FIU '''
    def __init__(self, up, uload):
        super().__init__(
            up,
            "FIU_OR_TYP1",
            14,
            diag_chains.FIU_MICRO_INSTRUCTION_REGISTER
        )
        for n, i in uload:
            self.define_instruction(n, i)
        self.finish()
