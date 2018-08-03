style spinner_up is choice_button:
    padding (0, 0)
    xysize (100, 15)
    background Frame("gui/button/spinner_up_[prefix_]background.png", 5, 5)

style spinner_down is spinner_up:
    background Frame(im.Flip("gui/button/spinner_up_idle_background.png", vertical = True), 5, 5)
    hover_background Frame(im.Flip("gui/button/spinner_up_hover_background.png", vertical = True), 5, 5)
    insensitive_background Frame(im.Flip("gui/button/spinner_up_insensitive_background.png", vertical = True), 5, 5)

style spinner_box is choice_button:
    xpadding 0
    xsize 100
    hover_background Frame("gui/button/choice_button_idle_background.png", 5, 5)

python early:
    ui_spinner = renpy.register_sl_statement("spinner", 0, 0)
    ui_spinner.add_property("key")
    ui_spinner.add_property("maxv")
    ui_spinner.add_property("minv")
    ui_spinner.add_property("step")
    ui_spinner.add_property("dict")
    ui_spinner.add_property("xsize")
    ui_spinner.add_property("zfill")
    
    ui_lspinner = renpy.register_sl_statement("listspinner", 0, 0)
    ui_lspinner.add_property("key")
    ui_lspinner.add_property("values")
    ui_lspinner.add_property("start")
    ui_lspinner.add_property("step")
    ui_lspinner.add_property("dict")
    ui_lspinner.add_property("xsize")


screen spinner(key, maxv, minv = 0, step = 1, dict = globals(), xsize = 100, zfill = 0): #key = Variable name
    python:
        try:
            dict[key] = min(max(dict[key], minv),maxv)
        except:
            dict[key] = minv
        v = dict[key]
    vbox:
        spacing 3
        pos(0, 0)
        anchor (0, 0)
        
        button style "spinner_up" xsize xsize action [SetDict(dict, key, min(v + step, maxv)), SensitiveIf(v < maxv)]
        textbutton str(v).zfill(zfill) xsize xsize style "spinner_box" text_xalign 0.5
        button style "spinner_down" xsize xsize action [SetDict(dict, key, max(v - step, minv)), SensitiveIf(v > minv)]

screen listspinner(key, values, start = 0, dict = globals(), xsize = 100, step = 1): #key = Variable name
    default v_id = start
    
    $ dict[key] = values[v_id]
    $ v = dict[key]
    vbox:
        spacing 3
        pos(0, 0)
        anchor (0, 0)
        
        button style "spinner_up" xsize xsize action [SetScreenVariable("v_id", v_id + step), SensitiveIf(v_id < len(values) - step)]
        textbutton str(v) xsize xsize style "spinner_box" text_xalign 0.5
        button style "spinner_down" xsize xsize action [SetScreenVariable("v_id", v_id - step), SensitiveIf(v_id > 0)]
