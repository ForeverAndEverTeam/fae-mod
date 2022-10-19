screen tcs(items):
    style_prefix "choice"

    #s "What should we talk about?"

    vbox:
        xcenter 250
        #ypos 800
        for i in items:
            textbutton i.caption action i.action

screen scs(items):
    style_prefix "choice"

    vbox:
        xcenter 250
        #ypos 800
        for i in items:
            textbutton i.caption action i.action


label talk_menu_wip:

    show sayori idle at t22

    $ Sayori.setInChat(True)

    #$ show_sayori_talk_menu()

    python:

        renpy.show("sayori idle", at_list=[t22])

        talk_menu = []
        talk_menu.append((_("Hey, [s_name]..."), "talk"))
        talk_menu.append((_("Can you tell me again about..."), "repeat"))
        talk_menu.append((_("I feel..."), "mood"))
        talk_menu.append((_("I want to say..."), "say"))
        talk_menu.append((_("Nevermind"), "nevermind"))

        renpy.say(s, store.fae_quips.talk_quip()[1], interact=False)
        madechoice = renpy.display_menu(talk_menu, screen="talk_choice")

    if madechoice == "talk":
        call talk_pinit from _call_talk_pinit
    
    elif madechoice == "repeat":
        call talk_pinit(True) from _call_talk_pinit_1
    
    elif madechoice == "mood":
        call mood_init from _call_mood_init
    
    elif madechoice == "say":
        call tell from _call_tell
    
    else:
        $ _return = None

    if _return is False:
        jump talk_menu_wip
    
label talk_menu_end:

    show sayori at t11

    jump ch30_loop


    #menu:
    #    s "What do you want to talk about?"

    #    "Hey, Sayori...":
    #        call talk_pinit
    #    "Can you tell me again about...":
    #        call talk_pinit(True)
    #    "I feel...":
    #        call mood_init
    #    "I want to say...":
    #        call tell
        
    #    "Nevermind":
    #        jump ch30_loop

    
    #return

    

init -2 python:

    def dlg():
        renpy.hide_screen('hidden1')
        renpy.jump('talk_menu_wip')
    
    def mg():
        renpy.hide_screen('hidden1')
        renpy.jump('mglist')
    
    def music_init():
        renpy.hide_screen('hidden1')
        renpy.jump('music_menu')

label mglist():

    show sayori idle at t22


    python:
        mg_list = []

        ttt = minigame(_("Tic-Tac-Toe"), 'mg_ttt', ttt_prep)
        mg_list.append(ttt)

        reversi = minigame(_("Reversi"), 'mg_reversi', reversi_prep)
        mg_list.append(reversi)

        bnc = minigame(_("Bows & Cows"), 'mg_bnc', bnc_prep)
        mg_list.append(bnc)

        #checkers = minigame(_("Checkers"), 'mg_checkers', checkers_prep)
        #mg_list.append(checkers)


    call screen minigame_ui() nopredict
    hide screen minigame_ui
    show screen hidden1(True)
    
    jump ch30_loop

screen minigame_ui():
    style_prefix "choice"
    
    vbox:
        xcenter 250
        
        for i in mg_list:
            if i.available:
                textbutton i.name action [Function(i), Hide("minigame_ui"), Jump("ch30_loop")]# Jump("main_loop")]
        
        textbutton _("Close") action [Hide("minigame_ui"), Return()]#Show("hidden1", None, True)]
    


#label try_force_quit:

#    $ renpy.jump("quit")

    #return
