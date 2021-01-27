'''
   The decode RAMS are not really a microcode engine as such, but we
   can use the same infrastructure.

   There are two lookup tables, each with 1024 locations.  The "low"
   table decodes instructions 0x0000 to 0x03ff, the "high" table
   decodes instructions 0x0400 to 0xffff in blocks of 64.

   See also: [30000971] r1000_haRDWARE_FUNCTIONAL_SPECIFICATION p69
'''

import uengine
import diag_chains
import macro_disass

class DecodeRam(uengine.UcodeEngine):
    ''' Uengine for decode rams '''
    def __init__(self, up, decode_low, decode_high):
        super().__init__(
            up,
            "DEC",
            16,
            diag_chains.SEQ_DECODER_SCAN
        )
        for n, i in decode_low:
            uins = self.define_instruction(n, i)
        for n, i in decode_high:
            if n < 16:
                continue
            uins = self.define_instruction(n << 6, i)
            for j in range(1, 64):
                self[(n << 6) + j] = uins
        self.finish()

    def html_page(self, fo):
        s = set()
        fo.write('<table class="border">\n')
        fo.write('<tr>\n')
        fo.write('<th>Ins</th>\n')
        fo.write('<th>Disass</th>\n')
        fo.write('<th>Ucode</th>\n')
        self.html_table_heads(fo)
        fo.write('</tr>\n')
        lines = 0
        for n, i in enumerate(self.uins):
            if i.uword in s:
                continue
            s.add(i.uword)
            if not lines % 4:
                fo.write('<tr class="top">\n')
            else:
                fo.write('<tr>\n')
            lines += 1
            fo.write('<td>' + self.afmt % n + '</td>\n')
            fo.write('<td class="left">' + macro_disass.dissassemble(n) + '</td>\n')
            fo.write('<td>' + self.up.link_to_uadr(i.uadr) + '</td>\n')
            self.html_table_fields(fo, i)
            fo.write('</tr>\n')
        fo.write('</table>\n')
