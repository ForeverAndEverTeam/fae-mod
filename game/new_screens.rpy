init python:
    import os, re
    
    music_list = [
    ("Just Monika", audio.m1), 
    ("Okay everyone!", audio.t5), 
    (_("Okay everyone! ([s_name] version)"), audio.tsayori), 
    ("Ohayou Sayori!", audio.t2), 
    ("Daijoubu!", audio.t8), 
    ("My Feelings", audio.t9), 
    (_("Play With Me (slow version)"), audio.t6s), 
    ("Play With Me", audio.t6), 
    ("My Confession", audio.t10),
    ("I Still Love You", audio.mend)
    ]
    MUSIC_FALLBACK = -1
    
    MUSIC_CUSTOM_PREFIX = "mod_assets/music/"
    
    def music_rigister(name, path):
        music_list.append((name, path))
        
    def music_custom_find(filelist = "list.txt"):
        global music_list_len
        
        try:
            f = renpy.file(MUSIC_CUSTOM_PREFIX + filelist)
            
            for line in f.readlines():
                info = []
                pos = 0
                closed = True
                s = ""
                l = info
                le = len(line)
                
                while pos < le and line[pos] != '#' and line[pos] != '\n':
                    if line[pos] == '\"':
                        if pos > 0 and line[pos-1] == '\\':
                            s = s[:-1] + "\""
                        elif not closed:
                            closed = True
                            l.append(s)
                            s = ""
                        else:
                            closed = False
                    elif line[pos+1] == '[' and closed and line[pos] != '\\':
                        l = []
                    elif line[pos+1] == ']' and closed and line[pos] != '\\':
                        info.append(l)
                        l = info
                    elif not closed:
                        s += line[pos]
                    pos += 1
                
                if len(info) == 2 and type(info[0]) == unicode:
                    pos = info[1].rfind('>') + 1
                    info[1] = info[1][:pos] + MUSIC_CUSTOM_PREFIX + info[1][pos:]
                    music_rigister(*info)
        
        except IOError:
            if filelist != 'list.txt':
                return music_custom_find()
        finally:
            music_list_len = len(music_list)
    
    music_custom_find()
    
    def music_switch(id = MUSIC_FALLBACK):
        if id > (globals().get("music_list_len") or len(music_list)) - 1:
            return music_switch()
        renpy.music.stop()
        persistent.currentmusic = id
        if id >= 0:
            renpy.music.queue(music_list[id][1], loop=True)
    
    #Mini-game info classreturn
    class minigame:
        
        def __init__(self, name, label = None, preparation = None):
            self.label = label
            self.name = name
            self.preparation = preparation
            self.available = True
        
        def __call__(self, *args, **kwargs):
            if self.preparation:
                self.preparation(self, *args, **kwargs)
            justIsSitting = False
            if self.label and not kwargs.get("restart"):
                renpy.call_in_new_context(self.label)
        
        def set_state(self, value):
            self.state = value
    
    mg_list = [] #mini-game list
    

screen talk_ui():
    style_prefix "choice"
    
    vbox:
        align (1.0, 0.5)
        offset (-10, 0)
        textbutton _("Ask a question") keysym '1' action Function(renpy.call, "s_topicmenu", 0)
        textbutton _("Repeat conversation") keysym '2' action Function(renpy.call, "s_topicmenu", 1)
        textbutton _("I feel...") keysym '3' action Function(renpy.call, "s_topicmenu", 2)
        textbutton _("Say goodbye") keysym '4' action Jump("s_farewell")
        textbutton _("Change information") keysym '5' action Function(renpy.call, "s_pinfo", True)
        if config.developer:
            textbutton "{i}Clean Sayori's memory{/i}" keysym '0' action [Function(reset_topics), Jump("s_talkmenu")]
        textbutton _("Close") keysym '6' action [Hide("talk_ui"), Jump("s_loop")]

screen music_ui(p = 0):
    default page = p
    
    style_prefix "choice"
    
    vbox:
        align (1.0, 0.5)
        offset (-10, 0)
        
        $keysym_i = 0
        
        for i in range(7 * page, min(7 * (page+1), music_list_len)):
            if persistent.currentmusic != i:
                $keysym_i += 1
                textbutton music_list[i][0] xpadding 0 keysym str(keysym_i) action [Function(music_switch, i),Hide("music_ui"), Jump("s_loop")]
        
        $del keysym_i
        
        hbox:
            spacing 324
            
            if music_list_len > 7:
                if page > 0:
                    textbutton ("<") xpadding 0 xsize 48 keysym '8' action SetScreenVariable("page", page-1) #Previous Page
                else:
                    null width 48
                if music_list_len >= (page+1) * 7:
                    textbutton (">") xpadding 0 xsize 48 keysym '9' action SetScreenVariable("page", page+1) #Next Page
        
        hbox:
            spacing 100
            
            if persistent.currentmusic > 0:
                textbutton _("Mute") xpadding 0 xsize 160 keysym '0' action [Function(music_switch, -1), Hide("music_ui"), Jump("s_loop")]
                textbutton _("Close") xpadding 0 xsize 160 action [Hide("music_ui"), Jump("s_loop")]
            else:
                textbutton _("Close") action [Hide("music_ui"), Jump("s_loop")]

screen minigame_ui():
    style_prefix "choice"
    
    vbox:
        align (1.0, 0.5)
        offset (-10, 0)
        
        for i in mg_list:
            if i.available:
                textbutton i.name action [Function(i), Hide("minigame_ui"), Jump("s_loop")]
        
        textbutton _("Close") action [Hide("minigame_ui"), Jump("s_loop")]

screen topic_ui(ss): #0 = questions, 1 = repeat, 2= feelings; #[TopicCategory] show the category
    default subscreen = subscreen
    
    style_prefix "choice"
    
    vbox:
        align (1.0, 0.5)
        offset (-10, 0)
        
        if subscreen == 0:
            for i in question_cats:
                textbutton i.name action SetScreenVariable("subscreen", i)
            textbutton _("Back") action [Hide("topic_ui"), Jump("s_talkmenu")]
        elif subscreen == 1:
            for i in topic_cats:
                if i.name and (config.developer or i.seen):
                    textbutton i.name action SetScreenVariable("subscreen", i)
            textbutton _("Back") action [Hide("topic_ui"), Jump("s_talkmenu")]
        elif subscreen == 2:
            for i in moods:
                textbutton i[0] action [Function(renpy.call, "s_react", i[1])]
            textbutton _("Back") action [Hide("topic_ui"), Jump("s_talkmenu")]
        else:
            if subscreen in topic_cats:
                for i in subscreen:
                    if config.developer or i.seen:
                        textbutton i.name action [Function(subscreen, i)]
                        textbutton _("Back") action SetScreenVariable("subscreen", 1)
            else:
                for i in subscreen:
                    textbutton i.name action [Function(subscreen, i)] text_italic not i.seen
                        
                textbutton _("Back") action SetScreenVariable("subscreen", 0)
        textbutton _("Close") action [Hide("topic_ui"), Jump("s_loop")]

screen pinfo_ui(): #Player info screen
    default selected_field = None
    default bdate = [persistent.playerbdate.year, persistent.playerbdate.month, persistent.playerbdate.day]
    
    frame:
        align (1.0, 0.5)
        offset (-10, 0)
        background Frame("gui/button/choice_idle_background.png", 5, 5)
        has vbox
        
        style_prefix "choice"
        spacing 5
        anchor (0.5, 1.0)
        offset(0, 64)
        label _("Name:")
        
        input:
            allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
            value VariableInputValue("player") 
            length 12 
            xalign 0
        
        label _("Birth date:")
        
        hbox:
            spacing 3
            
            spinner key 0 dict bdate minv 1 maxv 9999 zfill 4
            label "-" yoffset 16
            spinner key 1 dict bdate minv 1 maxv 12 zfill 2 xsize 50
            label "-" yoffset 16
            spinner key 2 dict bdate minv 1 maxv get_max_day(bdate[1], bdate[2]) zfill 2 xsize 50
        
        label _("Gender:")
        hbox:
            python:
                def ch_gender(g):
                    persistent.playergender = g
                    gender = persistent.playergender
            
            style_prefix "radio"
            
            textbutton _("Male") action [Function(ch_gender, False), SelectedIf(persistent.playergender is False)]
            textbutton _("Female") action [Function(ch_gender, True), SelectedIf(persistent.playergender is True)]
            textbutton _("Other") action [Function(ch_gender, None), SelectedIf(persistent.playergender is None)]
            
        textbutton _("OK") xpadding 0 xsize 150 xalign 0.5 action [Return(bdate), SensitiveIf(len(player))]

screen feat_ui():
    style_prefix "choice"
    
    vbox:
        align (0.01, 0.99)
        spacing 5
        
        if persistent.playthrough > 5:
            textbutton _("Talk (T)") xpadding 0 xsize 200 keysym 't' action Jump("s_talkmenu")
            textbutton _("Music (M)") xpadding 0 xsize 200 keysym 'm' action Jump("s_musicmenu")
            textbutton _("Play (P)") xpadding 0 xsize 200 keysym 'p' action Jump("s_gamemenu")
        else:
            textbutton _("Talk (T)") xpadding 0 xsize 200 action NullAction()
            textbutton _("Music (M)") xpadding 0 xsize 200 action NullAction()
            textbutton _("Play (P)") xpadding 0 xsize 200 action NullAction()


label s_talkmenu:
    $show_s_mood(ss2, True)
    hide screen feat_ui
    hide screen topic_ui
    call screen talk_ui()
    jump s_loop
    
label s_musicmenu(page = 0):
    $show_s_mood(ss2, True)
    hide screen feat_ui
    call screen music_ui(page)
    jump s_loop

label s_topicmenu(subscreen = 0):
    $show_s_mood(ss2, True)
    hide screen feat_ui
    hide screen talk_ui
    call screen topic_ui(subscreen)
    jump s_loop

label s_gamemenu():
    $show_s_mood(ss2, True, 'vh')
    hide screen feat_ui
    call screen minigame_ui() nopredict
    jump s_loop


label s_pinfo(jump_to_s_loop = False):
    $show_s_mood(ss2, True)
    hide screen feat_ui
    call screen pinfo_ui()
    $ persistent.playername = player
    $persistent.playerbdate = datetime.date(*_return)
    
    if jump_to_s_loop:
        jump s_loop
    return
