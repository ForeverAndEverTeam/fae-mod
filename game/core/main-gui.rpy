

screen hidden1(active=False): 

    style_prefix "tc"
    imagemap:
        auto "mod_assets/images/gui_prefs_%s.png"

        hotspot (608, 276, 48, 45) action [ Function(boop)]
    zorder 50
    vbox:
        xpos 0.090
        yanchor 1.0
        ypos 715    


        textbutton _("Talk") action [ SensitiveIf(active==True), Function(dlg)]


        textbutton _("Music") action [ SensitiveIf((active==True) and persistent.fae_custom_music_unlocked), Jump("music_menu")]

        textbutton _("Play") action [ SensitiveIf(active==True), Function(mg)]

        textbutton _("Calendar") action [ SensitiveIf(active==True), Function(show_calendar)]


screen hidden_fake(active=False):
    style_prefix "tc"
    zorder 50
    vbox:
        xpos 0.090
        yanchor 1.0
        ypos 715

        textbutton _("VGFsaw==") action [ SensitiveIf(active==True), Function(dlg)]

        textbutton _("TXVzaWM=") action [ SensitiveIf(active==True), Jump("music_menu")]

        textbutton _("UGxheQ==") action [ SensitiveIf(active==True), Function(mg)]

        textbutton _("Q2FsZW5kYXI=") action [ SensitiveIf(active==True), Function(show_calendar)]




label tell:
    show sayori idle at t22

    python:

        say_menu = []
        if time_love(time_since=datetime.timedelta(0,10)):
            say_menu.append((_("I love you too!"), "love_too"))
        else:
            say_menu.append((_("I love you!"), "love"))
        
        say_menu.append((_("I want to tell you something..."), "compliment"))
        
        say_menu.append((_("I'm sorry."), "sorry"))

        say_menu.append((_("Goodbye"), "farewell"))

        
        say_menu.append((_("Back"), "back"))

        schoice = renpy.display_menu(say_menu, screen="tcs")

    if schoice == "love":
        $ ats("sayo_love")
        jump cnc
    
    elif schoice == "love_too":
        $ ats("love_too")
        jump cnc
    
    elif schoice == "sorry":
        jump regret_init
    
    elif schoice == "compliment":
        jump compliment_init
    
    elif schoice == "farewell":
        jump farewell_options
    
    elif schoice == "back":
        jump talk_menu_wip
    
    return


label boop:

    s "Did you just boop me?"
    s "Ehehehe~"
    return


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
        cls=(50, 70, 250, 572), 
        ols=(350, 70, 250, 572), 
        cat_length=len(_chats))

    $ _selection = _return

    if isinstance(_selection, basestring):
        $ ats(_selection)
        jump cnc
    
    elif _selection == -1:
        jump talk_menu_wip

    $ _return = None

    jump ch30_loop


init offset = -1

define prior_adjust = ui.adjustment()

define curr_adjust = ui.adjustment()

define sel_cat = None

define scroll_align = -0.1


style t_m_button is choice_button:
    xysize (250, None)
    padding (25, 5, 25, 5)
    top_padding 10
    bottom_padding 5

style t_m_button_text is choice_button_text:
    align (0.0, 0.0)
    text_align 0.0

style t_m_button_italic is categorized_menu_button

style t_m_button_text_italic is categorized_menu_button_text:
    italic True



screen neat_menu1(items):
    style_prefix "tcs_b"

    vbox:
        xcenter 250
        for i in items:
            textbutton i.caption action i.action


screen neat_menu(menu_parts, cls, ols, cat_length):

    style_prefix "t_m"

    fixed:
        anchor (0, 0)
        pos (cls[0], cls[1])
        xsize cls[2]
        ysize cls[3]

        bar:
            adjustment prior_adjust
            style "sayo_scroller"
            xalign -0.1

        vbox:
            ypos 0
            yanchor 0

            viewport:
                yadjustment prior_adjust
                yfill False
                mousewheel True
                vbox:
                    if cat_length == 0:
                        textbutton _("Nevermind."):
                            action [
                                Return(-1),
                                Function(prior_adjust.change, 0),
                                SetVariable("sel_cat", None)
                            ]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                    else:
                        textbutton _("Back"):
                            style "t_m_button"
                            action [ Return(-1), Function(prior_adjust.change, 0) ]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound

                        null height 20
                
                    for b_name in menu_parts.keys():
                        textbutton b_name:
                            style "t_m_button"
                            action SetVariable("sel_cat", b_name)
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                        null height 10

    if menu_parts.get(sel_cat):
        

        fixed:
            area ols

            bar:
                adjustment curr_adjust
                style "sayo_scroller"
                xalign -0.1

            vbox:
                ypos 0
                yanchor 0

                viewport:
                    yadjustment curr_adjust
                    yfill False
                    mousewheel True

                    vbox:
                        textbutton _("Nevermind."):
                            action [
                                Return(-1),
                                Function(prior_adjust.change, 0),
                                SetVariable("sel_cat", None)
                            ]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound

                        null height 20

                        for _chat in menu_parts.get(sel_cat):
                            $ display_text = _chat.prompt if (_chat.seen_no > 0 or _chat.random) else "{i}[_chat.prompt]{/i}"
                            
                            textbutton display_text:
                                style "t_m_button"
                                action [ Return(_chat.label), Function(prior_adjust.change, 0), SetVariable("sel_cat", None) ]
                                hover_sound gui.hover_sound
                                activate_sound gui.activate_sound
                            
                            null height 5



################
#SCROLLABEL MENU
################
screen neat_menu_scroll(items, last_item=None):
    


    style_prefix "choice"
    fixed:

        area (70, 40, 560, 440)
        vbox:
            ypos 0
            yanchor 0.0

            if last_item:
                textbutton last_item[0]:
                    style "t_m_button"
                    #xsize 
                    action Return(last_item[1])
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                
                null height 20
            
            viewport:
                id "viewport"
                yfill False
                mousewheel True

                vbox:
                    for prompt, _value in items:
                        textbutton prompt:
                            style "t_m_button"
                            action Return(_value)
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound
                    
                    null height 5
        bar:
            style "sayo_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align

style sayo_scroller is vscrollbar:
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)

style n_m_vbox is vbox:
    xalign 0.0
    ypos 260
    yanchor 0.5
    spacing 5

style n_m_button is choice_button:
    xysize (540, None)
    padding (25, 5, 25, 5)

style n_m_button_text is choice_button_text:
    text_align 0.0
    align (0.0, 0.0)

style n_m_new_button is n_m_button

style n_m_new_button_text is n_m_button_text:
    italic True

style n_m_s_button is n_m_button

style n_m_s_button_text is n_m_button_text:
    bold True

style t_n_m_vbox is vbox:
    xalign 0.5
    ypos 260
    yanchor 0.5
    spacing 5

style t_n_m_button is choice_button:
    xysize (240, None)
    padding (25, 5, 25, 5)

style t_n_m_button_text is choice_button_text:
    align (0.0, 0.0)
    text_align 0.0

style t_n_m_n_button is t_n_m_button

style t_n_m_n_button_text is t_n_m_button_text:
    italic True

style t_n_m_n_s_button is t_n_m_button

style t_n_m_n_s_button_text is t_n_m_button_text:
    bold True


