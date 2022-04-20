

screen overlay(active=True):
    style_prefix "tc"
    zorder 50
    vbox:
        xpos 0.090
    #        xalign 0.05
        yanchor 1.0
        ypos 715    
    #        yalign 0.95
            
        #textbutton _("Talk") action Function(dlg)

        textbutton _("Talk") action [ SensitiveIf(active==True), Function(dlg)]

        textbutton _("Music") action [ SensitiveIf(active==True), Function(select_music)]

        textbutton _("Play") action [ SensitiveIf(active==True), Function(mg)]



screen hidden():

    tag menu
    use overlay
    imagemap:
        auto "mod_assets/images/gui_prefs_%s.png"

        hotspot (608, 276, 48, 45) action Call("boop")


screen hidden_fake():
    style_prefix "tc"
    zorder 50
    vbox:
        xpos 0.05
    #        xalign 0.05
        yanchor 1.0
        ypos 715
    #        yalign 0.95

        textbutton _("VGFsaw==") action Function(dlg)

        textbutton _("TXVzaWM=") action Function(select_music)

        textbutton _("UGxheQ==") action Function(mg)

style neat_menu_button is choice_button:
    xysize (250, None)
    padding (25, 5, 25, 5)
    top_padding 10
    bottom_padding 5

style neat_menu_button_text is choice_button_text:
    align (0.0, 0.0)
    text_align 0.0


label talk_pinit(irc=False):
    python:
        if (irc):
            _chat = Chat.chat_filt(
                chats.CHAT_DEFS.values(),
                unlocked=True,
                has_seen=True
            )

        else:
            _chat = Chat.chat_filt(
                chats.CHAT_DEFS.values(),
                unlocked=True
            )
        
        _chat.sort(key=lambda chat: chat.prompt)

        menu_entries = makedict(_chat)
    
    call screen neat_menu(menu_entries,(1020, 70, 250, 572), (740, 70, 250, 572), len(_chat))

    $ _selection = _return

    if isInstance(_selection, basestring):
        $ ats(_selection)
        jump cnc
    
    elif _choice == No:
        jump talk_menu_wip

    $ _return = None

    jump idle_loop

screen neat_menu(menu_entries, cls, ols, cat_length):

    style_prefix "neat_menu"

    fixed:
        anchor (0, 0)
        pos (cls[0], cls[1])
        xsize cls[2]
        ysize cls[3]

        bar:
            xalign -0.1

        vbox:
            ypos 0
            xanchor 0

            viewport:
                yfill False
                mousewheel True
                vbox:
                    textbutton _("Nevermind."):
                        action [
                            Return(False),
                            SetVariable("sel_cat", None)

                        ]
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound
                    
                    textbutton _(back):
                        style "neat_menu_button"
                        action [ Return(No)]
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound

                    null height 20
                
                    for b_name in menu_entries.iterkeys():
                        textbutton b_name:
                            style "neat_menu_button"
                            action SetVariable("sel_cat", b_name)
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                        null height 5

    if menu_entries.get(sel_cat):
        fixed:
            area ols
            
            bar:
                xalign -0.1
            
            vbox:
                ypos 0
                yanchor 0

                viewport:
                    yfill False
                    mousewheel True

                    vbox:
                        textbutton _("Nevermind."):
                            action [
                                Return(False),
                                SetVariable("sel_cat", None)
                            ]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound

                        null height 20
                        
                        for _chat in menu_entries.get(sel_cat):
                            textbutton _chat.prompt:
                                style "neat_menu_button"
                                action [
                                    Return(_chat.label),
                                    SetVariable("sel_var", None)
                                ]

                                hover_sound gui.hover_sound
                                activate_sound gui.activate_sound
                            
                            null height 5



