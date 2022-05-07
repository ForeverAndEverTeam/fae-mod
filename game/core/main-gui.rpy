

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

        #textbutton _("Music") action [ SensitiveIf(active==True), Function(select_music)]

        textbutton _("Music") action [ShowMenu("music_player"), Function(get_music_channel_info), Stop('music', fadeout=2.0), Function(refresh_list)]

        textbutton _("Play") action [ SensitiveIf(active==True), Function(mg)]



screen hidden(active=True):

    tag menu
    use overlay
    imagemap:
        auto "mod_assets/images/gui_prefs_%s.png"

        hotspot (608, 276, 48, 45) action Call("boop")


screen hidden_fake(active=False):
    style_prefix "tc"
    zorder 50
    vbox:
        xpos 0.090
    #        xalign 0.05
        yanchor 1.0
        ypos 715
    #        yalign 0.95

        textbutton _("VGFsaw==") action [ SensitiveIf(active==True), Function(dlg)]

        textbutton _("TXVzaWM=") action [ SensitiveIf(active==True), Function(select_music)]

        textbutton _("UGxheQ==") action [ SensitiveIf(active==True), Function(mg)]


#style neat_menu_button is choice_button:
#    xysize (250, None)
#    padding (25, 5, 25, 5)
#    top_padding 10
#    bottom_padding 5

#style neat_menu_button_text is choice_button_text:
#    align (0.0, 0.0)
#    text_align 0.0

#style neat_menu_button_italic is neat_menu_button

#style neat_menu_button_text_italic is neat_menu_button_text:
#    italic True



label talk_pinit(irc=False):
    python:
        if (irc):
            _chats = Chat.chat_filt(
                chats.CHAT_DEFS.values(),
                random=True,
                unlocked=True,
                has_seen=True
            )

        else:
            _chats = Chat.chat_filt(
                chats.CHAT_DEFS.values(),
                random=False,
                unlocked=True
            )
        
        _chats.sort(key=lambda chat: chat.prompt)

        menu_parts = makedict(_chats)
    
    call screen neat_menu(
        menu_parts=menu_parts,
        cls=(50, 50, 480, 550), 
        ols=(50, 50, 480, 550), 
        cat_length=len(_chats))

    $ _selection = _return

    if isinstance(_selection, basestring):
        $ ats(_selection)
        jump cnc
    
    elif _selection == "No":
        jump talk_menu_wip

    $ _return = None

    jump idle_loop


init offset = -1

define prior_adjust = ui.adjustment()

define curr_adjust = ui.adjustment()

define sel_cat = None

#define scroll_align = -0.1


#style talk_menu_button is choice_button:
#    xysize (250, None)
#    padding (25, 5, 25, 5)
#    top_padding 10
#    bottom_padding 5

#style talk_menu_button_text is choice_button_text:
#    align (0.0, 0.0)
#    text_align 0.0

#style talk_menu_button_italic is talk_menu_button

#style talk_menu_button_text_italic is talk_menu_button_text:
#    italic True



#style sayo_scroller is vscrollbar:
#    xpos 450
#    yalign 0.5

#    ysize 700



screen neat_menu1(items):
    style_prefix "tcs_b"

    vbox:
        xcenter 250
        for i in items:
            textbutton i.caption action i.action


screen neat_menu(menu_parts, cls, ols, cat_length):

    tag menu

    default page = 0

    style_prefix "choice"

    fixed:
        anchor (0, 0)
        pos (cls[0], cls[1])
        xsize cls[2]
        ysize cls[3]

        #bar:
        #    adjustment prior_adjust
            #style "sayo_scroller"
        #    xalign 0

        vbox:
            #ypos 7
            #xanchor 0

            viewport:
                yadjustment prior_adjust
                yfill False
                mousewheel True
                vbox:
                    if cat_length == 0:
                        textbutton _("Nevermind."):
                            action [
                                Return(False),
                                SetVariable("sel_cat", None)
                            ]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                    else:
                        textbutton _("back"):
                            style "choice_button"
                            action [ Return(False),
                            Function(prior_adjust.change, 0)]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound

                        #null height 20
                
                    for b_name in menu_parts.iterkeys():
                        textbutton b_name:
                            style "choice_button"
                            action [ SetVariable("sel_cat", b_name)]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                        #null height 5

    if menu_parts.get(sel_cat):
        
        #$ renpy.hide_screen(menu, None)

        fixed:
            area ols

            #bar:
            #    adjustment curr_adjust
            #    style "sayo_scroller"
            #    xalign -0.1

            vbox:
                #ypos 7
                #xanchor 0

                viewport:
                    yadjustment curr_adjust
                    yfill False
                    mousewheel True

                    vbox:
                        textbutton _("Nevermind."):
                            action [
                                #Return("No"),
                                Jump("talk_menu_wip"),
                                Function(prior_adjust.change, 0),
                                SetVariable("sel_cat", None)
                            ]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound

                        #null height 20

                        for _chat in menu_parts.get(sel_cat):
                            $ display_text = _chat.prompt if (_chat.seen_no > 0 or _chat.random) else "{i}[_chat.prompt]{/i}"
                            
                            

                            textbutton display_text:
                                style "choice_button"
                                action [ Return(_chat.label), Function(prior_adjust.change, 0), SetVariable("sel_cat", None) ]
                                hover_sound gui.hover_sound
                                activate_sound gui.activate_sound
                        hbox:
                            spacing 324
                            if page > 0:
                                textbutton ("<") xpadding 0 xsize 48 keysym 'K_LEFT' action SetScreenVariable("page", page-1) #Previous Page
                            else:
                                null width 48
                            textbutton (">") xpadding 0 xsize 48 keysym 'K_RIGHT' action SetScreenVariable("page", page+1)
                            #else:
                                #null width 48

                            #null height 5



