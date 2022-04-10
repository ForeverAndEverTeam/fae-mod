screen overlay():
    style_prefix "tc"
    zorder 50
    vbox:
        xpos 0.05
    #        xalign 0.05
        yanchor 1.0
        ypos 715
    #        yalign 0.95

        textbutton _("Talk") action Function(dlg)

        textbutton _("Music") action Function(select_music)

        textbutton _("Play") action Function(mg)

screen hidden():

    tag menu
    use overlay

    imagemap:
        auto "mod_assets/images/gui_prefs_%s.png"

        hotspot (608, 276, 48, 45) action Call("boop")
