
import r1k_uprog
import r1k_explain
import macro_disass

class Explain():

    def __init__(self, uprog):
        self.uprog = uprog

    def decode(self, uins, attrs):
        for fld, fmt in attrs.items():
            v = getattr(uins, fld)
            i = getattr(r1k_explain, fld, None)
            if not i:
                yield fld, fmt % v, None
            else:
                yield fld, fmt % v, i(v)

class Listing():

    def __init__(self, iterable=None):
        uprog = r1k_uprog.Uprog(iterable)
        idisp = {}
        for i, j in uprog.dispatch_ram.items():
            idisp[j.dispatch_uadr] = i
        explainer = Explain(uprog)
        for uins in uprog:
            print("%04x:" % uins.adr)
            t = idisp.get(uins.adr)
            if t:
                i = macro_disass.disassemble(t).rstrip().expandtabs()
                print("    ", i)
                print("    ", "-" * len(i))
                for x, y, z in explainer.decode(uprog.dispatch(t), uprog.dispatch_attrs):
                    if z is None:
                        z = ""
                    print("    ", x.ljust(19), y.rjust(4), z)

            for x, y, z in explainer.decode(uins, uprog.attrs):
                if z is None:
                    z = ""
                d = r1k_explain.defaults.get(x)
                if d == getattr(uins, x):
                    y += "*"
                else:
                    y += " "
                print("    ", x.ljust(19), y.rjust(5), z)
    
Listing()
