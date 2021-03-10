
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

# R1000_HARDWARE_FUNCTIONAL_SPECIFICATION p59
MACRO_EVENTS = {
    # MEMORY
    0x100: "Refresh Memory",

    # SYSBUS
    0x110: "Sysbus_status",
    0x118: "Sysbus_packet",
    0x128: "Slice_timer",
    0x130: "GP_timers",

    # SEQUENCER
    0x140: "CSA_Underflow",
    0x148: "CSA_overflow",
    0x150: "resolve_ref",
    0x158: "TOS_optimization_err",
    0x168: "dispatch",
    0x170: "break_class",
    0x178: "IBUF_empty",
}

class Listing():

    def __init__(self, iterable=None):
        uprog = r1k_uprog.Uprog(iterable)
        idisp = {}
        for i, j in uprog.dispatch_ram.items():
            idisp[j.dispatch_uadr] = i
        explainer = Explain(uprog)
        for uins in uprog:
            print("%04x:" % uins.adr)
            t = MACRO_EVENTS.get(uins.adr)
            if t:
                print("    ", "-" * len(t))
                print("    ", t)
                print("    ", "-" * len(t))
            t = idisp.get(uins.adr)
            if t:
                i = macro_disass.disassemble(t).rstrip().expandtabs()
                print("    ", "-" * len(i))
                print("    ", i)
                print("    ", "-" * len(i))
                for x, y, z in explainer.decode(uprog.dispatch(t), uprog.dispatch_attrs):
                    if z is None:
                        z = ""
                    print("    ", x.ljust(20), y.rjust(4), z)

            for x, y, z in explainer.decode(uins, uprog.attrs):
                if z is None:
                    z = ""
                d = r1k_explain.defaults.get(x)
                if d == getattr(uins, x):
                    y += "*"
                else:
                    y += " "
                print("    ", x.ljust(20), y.rjust(5), z)
    
Listing()
