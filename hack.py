'''
   The sandbox
'''

import os

import uload
import html_style
import decode
import seq
import val
import typ
import fiu

class UCode():
    def __init__(self, filename):
        self.filename = filename
        self.basedir = os.path.join(html_style.HTML_DIR, filename)
        os.makedirs(self.basedir, exist_ok=True)

        u = uload.UCodeFile(filename)
        self.dec = decode.DecodeRam(self, u.decode_low, u.decode_high)
        self.seq = seq.Seq(self, u.seq)
        self.val = val.Val(self, u.val)
        self.typ = typ.Typ(self, u.typ)
        self.fiu = fiu.Fiu(self, u.fiu)
        self.afmt = self.seq.afmt

    def html_head(self, fo):
        fo.write(html_style.HTML_HEAD)
        fo.write('<a href="%s">DECODE</a><br>\n' % os.path.join(self.basedir, "dec.html"))

    def filename_for_uins(self, uadr):
        return os.path.join(self.basedir, self.afmt % uadr + ".html")

    def link_to_uadr(self, uadr):
        t = '<a href="'
        t += self.afmt % uadr + ".html"
        t += '">UADR ' + self.afmt % uadr + '</a>'
        return t

    def make_html_pages(self):
        fo = open(os.path.join(self.basedir, "dec.html"), "w")
        self.html_head(fo)
        self.dec.html_page(fo)
        fo.write(html_style.HTML_TAIL)
        for n, i in enumerate(self.seq.uins):
            if not i:
                continue
            self.make_one_uins_page(n)

    def make_one_uins_page(self, uadr):
        fo = open(self.filename_for_uins(uadr), "w")
        self.html_head(fo)

        for i in (
            self.seq,
            self.val,
            self.typ,
            self.fiu,
        ):
            fo.write("<h4>" + i.name + "</h4>\n")
            i.html_table(fo, lo=uadr, hi=uadr+1)
            for j in i.explain(uadr):
                fo.write(j + '<br>\n')

        fo.write(html_style.HTML_TAIL)
        
def main():
    foi = open(os.path.join(html_style.HTML_DIR, "index.html"), "w")
    foi.write(html_style.HTML_HEAD)
    for filename in uload.UCODE_FILES:
        foi.write('<a href="%s/dec.html">%s</a><br/>\n' % (filename, filename))
        print(filename)
        uc = UCode(filename)
        uc.make_html_pages()
    foi.write(html_style.HTML_TAIL)

if __name__ == "__main__":
    main()
