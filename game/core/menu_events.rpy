screen tcs(items):
    style_prefix "choice"

    vbox:
        xcenter 250
        #ypos 800
        for i in items:
            textbutton i.caption action i.action



label talk_menu_wip:

    show sayori idle at t22

    python:

        talk_menu = []
        talk_menu.append((_("Hey, Sayori..."), "talk"))
        talk_menu.append((_("Can you tell me again about..."), "rep"))
        talk_menu.append((_("I feel..."), "mood"))
        talk_menu.append((_("I want to say..."), "say"))
        talk_menu.append((_("Change Player Information"), "cpi"))
        #talk_menu.append((_("Kiss me"), "kiss"))
        #if renpy.exists('dev/dev_tools.rpy'):
        #    talk_menu.append((_("Dev Tools"), "dev"))
        talk_menu.append((_("Back"), "back"))

        tchoice = renpy.display_menu(talk_menu, screen="tcs")

    if tchoice == "talk":
        call talk_pinit
    elif tchoice == "rep":
        call rep
    elif tchoice == "mood":
        call mood
    elif tchoice == "say":
        call say
    elif tchoice == "cpi":
        call cpi
    elif tchoice == "kiss":
        call sayo_kiss_short
    elif tchoice == "dev":
        call dev
    else:
        $ ret = None
    
    if ret is False:
        jump talk_menu_wip

label tme:
    show sayori idle at t11
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
