

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

python early:
    import io
    import datetime
    import traceback
    import string
    
    import pygame

    class CustomButton(renpy.Displayable):
        import pygame

        _STATE_IDLE = 0
        _STATE_HOVER = 1
        _STATE_DISABLED = 2

        _INDEX_TEXT = 0
        _INDEX_BUTTON = 1

        def __init__(self,
                idle_text,
                hover_text,
                disable_text,
                idle_back,
                hover_back,
                disable_back,
                xpos,
                ypos,
                width,
                height,
                hover_sound=None,
                activate_sound=None,
                enable_when_disabled=False,
                sound_when_disabled=False,
                return_value=True
            ):

            super(renpy.Displayable, self).__init__()

            self.xpos = xpos
            self.ypos = ypos
            self.width = width
            self.height = height
            self.hover_sound = hover_sound
            self.activate_sound = activate_sound
            self.enable_when_disabled = enable_when_disabled
            self.sound_when_disabled = sound_when_disabled
            self.return_value = return_value
            self.disabled = False
            self.hovered = False
            self._button_click = 1
            self._button_down = pygame.MOUSEBUTTONUP

            self._button_states = {
                self._STATE_IDLE: (idle_text, idle_back),
                self._STATE_HOVER: (hover_text, hover_back),
                self._STATE_DISABLED: (disable_text, disable_back)
            }


            self._state = self._STATE_IDLE
        
        def _isOverMe(self, x, y):

            return (
                0 <= (x - self.xpos) <= self.width
                and 0 <= (y - self.ypos) <= self.height
            )
        
        def _playActivateSound(self):

            if not self.disabled or self.sound_when_disabled:
                renpy.play(self.activate_sound, channel="sound")

        def _playHoverSound(self):

            if not self.disabled or self.sound_when_disabled:
                renpy.play(self.hover_sound, channel="sound")

        @staticmethod
        def create_st(
                text_str,
                incl_disb_text,
                *args,
                **kwargs
        ):

            if incl_disb_text:
                disb_button = Text(
                    text_str,
                    font=gui.default_font,
                    size=gui.text_size,
                    color=fae_globals.button_text_insensitive_color,
                    outlines=[]
                )
            
            else:
                disb_button = Null()
            
            return CustomButton(
                Text(
                    text_str,
                    font=gui.default_font,
                    size=gui.text_size,
                    color=fae_globals.choice_button_text_idle_color,
                    outlines=[]
                ),
                Text(
                    text_str,
                    font=gui.default_font,
                    size=gui.text_size,
                    color=fae_globals.button_text_hover_color,
                    outlines=[],
                ),
                disb_button,
                *args,
                **kwargs
            )
        
        @staticmethod
        def create_stb(
                text_str,
                incl_disb_text,
                *args,
                **kwargs
        ):
            
            if incl_disb_text:
                disb_button = Text(
                    text_str,
                    font=gui.default_font,
                    size=gui.text_size,
                    color=fae_globals.button_text_insensitive_color,
                    outlines=[]
                )
                disb_back = CustomButton._gen_bg("insensitive")
            else:
                disb_button = Null()
                disb_back = Null()

            return CustomButton(
                Text(
                    text_str,
                    font=gui.default_font,
                    size=gui.text_size,
                    color=fae_globals.button_text_idle_color,
                    outlines=[]
                ),
                Text(
                    text_str,
                    font=gui.default_font,
                    size=gui.text_size,
                    color=fae_globals.button_text_hover_color,
                    outlines=[],
                ),
                disb_button,
                CustomButton._gen_bg("idle"),
                CustomButton._gen_bg("hover"),
                disb_back,
                *args,
                **kwargs
            )
        
        @staticmethod
        def _gen_bg(prefix):

            gen_frame = prefixFrame(
                getPropFromStyle("choice_button", "background"),
                prefix
            )

            if gen_frame is None:

                return Frame(
                    fae_getTimeFile(
                        "mod_assets/buttons/generic/{0}_bg.png".format(prefix)
                    ),
                    Borders(5,5,5,5)
                )
            
            return gen_frame
        
        def disable(self):

            self.disabled = True,
            self._state = self._STATE_DISABLED
        
        def enable(self):

            self.disabled = False
            self._state = self._STATE_IDLE
        
        def getSize(self):

            return (self.width, self.height)
        
        def ground(self):

            if not self.disabled or self.enable_when_disabled:
                self.hovered = False
            
                if self.disabled:
                    self._state = self._STATE_DISABLED
                else:
                    self._state = self._STATE_IDLE
        
        def render(self, width, height, st, at):

            render_text, render_back = self._button_states[self._state]
            render_text = renpy.render(render_text, width, height, st, at)
            render_back = renpy.render(render_back, self.width, self.height, st, at)

            rt_w, rt_h = render_text.get_size()

            r = renpy.Render(self.width, self.height)

            r.blit(render_back, (0, 0))
            r.blit(
                render_text,
                (int((self.width - rt_w) / 2), int((self.height - rt_h) / 2))
            )

            return r
        
        def event(self, ev, x, y, st):

            if self._state != self._STATE_DISABLED or self.enable_when_disabled:

                if ev.type == pygame.MOUSEMOTION:
                    is_over_me = self._isOverMe(x, y)
                    if self.hovered:
                        if not is_over_me:
                            self.hovered = False
                            self._state = self._STATE_IDLE
                            renpy.redraw(self, 0.0)
                    
                    elif is_over_me:
                        self.hovered = True
                        self._state = self._STATE_HOVER
                        
                        if self.hover_sound:
                            self._playHoverSound()
                        
                        renpy.redraw(self, 0.8)
                
                elif (
                    ev.type == self._button_down
                    and ev.button == self._button_click
                ):
                    if self.hovered:
                        if self.activate_sound:
                            self._playActivateSound()
                        
                        return self.return_value
            
            return None
    
