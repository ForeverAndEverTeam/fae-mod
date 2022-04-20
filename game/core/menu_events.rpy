screen tcs(items):
    style_prefix "tcs_b"

    vbox:
        xcenter 250
        for i in items:
            textbutton i.caption action i.action



label talk_menu_wip:

    show sayori abaabaa at t22

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
    show sayori abaabaa at t11
    jump idle_loop
    


init python:
    def dlg():
        renpy.hide_screen('hidden')
        renpy.jump('talk_menu_wip')
    
    def select_music():
        renpy.hide_screen('hidden')
        renpy.show_screen('music_menu')

    def mg():
        renpy.jump('mglist')
