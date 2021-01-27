'''
   Enlist PyReveng3 to disassemble a macro instruction
'''

from pyreveng import mem
import pyreveng.cpu.r1000 as r1000

def dissassemble(ins):
    ''' Disassemble a macro instruction to a text-string '''
    ram = mem.WordMem(0, 0x10, bits=16)
    ram[0] = ins
    ram[1] = 2
    ram[2] = 0
    ram[3] = 0
    cpu = r1000.r1000()
    cpu.m = ram
    cpu.disass(0)
    for i in ram:
        return i.render()
    return "PyReveng3 could not disassemble 0x%04x" % ins
