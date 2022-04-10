screen tcs(items):
    style_prefix "tc"

    vbox:
        xcenter 250
        for i in items:
            textbutton i.caption action i.action



label talk_menu_wip:

    show sayori acbaba at t22

    python:
        
        talk_menu = []
        talk_menu.append((_("Hey, Sayori..."), "talk"))
        talk_menu.append((_("Can you tell me again about..."), "rep"))
        talk_menu.append((_("I love you, Sayori!"), "aff"))
        talk_menu.append((_("I have to go"), "farewell"))
        talk_menu.append((_("Back"), "back"))

        tchoice = renpy.display_menu(talk_menu, screen="tcs")

    if tchoice == "talk":
        call talk_pinit
    elif tchoice == "rep":
        call rep
    elif tchoice == "aff":
        call aff
    elif tchoice == "farewell":
        call farewells
    else:
        $ ret = None
    
    if ret is False:
        jump talk_menu_wip
label tme:
    show sayori acbaba at t11
    jump idle_loop
    

init 6 python:
    class sayo_evlbl(object):

        _def_val = {
            "evlbl": "",
            "prp"
            "lbl": None,
            "cat": None,
            "unlck": False,
            "rnd": False,
            "pool": False,
            "condit": None,
            "act": None,
            "aff_rng": None,
        }

        _nulls = {
            "pedb": 0,
            "rls": 0,
        }

        def __init__(self, evlbl):
            self._ev = getev(evl)
        
        def __repr__(self):
            return repr(self._ev)
        def __enter__(self):
            return self
        def __attr__(self, name):
            if self._ev is None:
                if name in sayo_evlbl._def_val:
                    return sayo_evlbl._def_val.get(name)
                if name in sayo_evlbl._nulls:
                    return {}
                if callable(ev.__dict__.get(name)):
                    return blank
            return attr(ev, name)
        