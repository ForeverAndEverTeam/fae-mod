screen overlay():
    zorder 50
    style_prefix "choice"

    vbox:
        xpos 0.05
#        xalign 0.05
        yanchor 1.0
        ypos 715
#        yalign 0.95
    
        textbutton _("Talk"):
            action [
                Jump("talk_menu"),
            ]

        textbutton _("Music") action Function(select_music)

        textbutton _("Play") action Function(mg)



