init python:
    import music
    music.config, music.renpy = config, renpy
    music.persistent = persistent
    
    music.music_list = [
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
    music.music_list_len = len(music.music_list)
    
    music.read_list()
    scaned_new = music.autoscan()
    
    #Mini-game info classreturn
    class minigame:
        
        def __init__(self, name, label = None, preparation = None):
            self.label = label
            self.name = name
            self.preparation = preparation
            self.available = True
        
        def __call__(self, *args, **kwargs):
            global justIsSitting
            
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
        textbutton _("Ask a question") keysym '1' action Function(renpy.call, "s_topicmenu", 0, 0)
        textbutton _("Repeat conversation") keysym '2' action Function(renpy.call, "s_topicmenu", 1, 1)
        textbutton _("I feel...") keysym '3' action Function(renpy.call, "s_topicmenu", 2)
        textbutton _("I want to say...") keysym '4' action Function(renpy.call, "s_saymenu")
        # textbutton _("Ask for...") keysym '4' action Function(renpy.call, "s_topicmenu", 4)
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
        
        for i in range(7 * page, min(7 * (page+1), music.music_list_len)):
            if persistent.currentmusic != i:
                $keysym_i += 1
                textbutton music.music_list[i][0] xpadding 0 keysym str(keysym_i) action [Function(music.switch, i),Hide("music_ui"), Jump("s_loop")]
        
        $del keysym_i
        
        hbox:
            spacing 324
            
            if music.music_list_len > 8:
                if page > 0:
                    textbutton ("<") xpadding 0 xsize 48 keysym 'K_LEFT' action SetScreenVariable("page", page-1) #Previous Page
                else:
                    null width 48
                if music.music_list_len >= (page+1) * 7:
                    textbutton (">") xpadding 0 xsize 48 keysym 'K_RIGHT' action SetScreenVariable("page", page+1) #Next Page
        
        hbox:
            spacing 100
            
            if persistent.currentmusic > 0:
                textbutton _("Mute") xpadding 0 xsize 160 keysym '0' action [Function(music.switch, -1), Hide("music_ui"), Jump("s_loop")]
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

screen topic_ui(ss, cat = 0): #0 = questions, 1 = repeat, 2= feelings, 3 = poetry; #[TopicCategory] show the category
    default subscreen = ss
    default cat = cat
    default page = 0
    
    style_prefix "choice"
    
    vbox:
        align (1.0, 0.5)
        offset (-10, 0)
        
        if subscreen == 0:
            for i in question_cats:
                textbutton i.name action [SetScreenVariable("subscreen", i), SetScreenVariable("cat", 0)]
            textbutton _("Back") action [Hide("topic_ui"), Jump("s_talkmenu")]
        elif subscreen == 1:
            for i in topic_cats:
                if i.name and (config.developer or i.seen):
                    textbutton i.name action [SetScreenVariable("subscreen", i), SetScreenVariable("cat", 1)]
            textbutton _("Back") action [Hide("topic_ui"), Jump("s_talkmenu")]
        elif subscreen == 2:
            for i in moods:
                textbutton i[0] action [Function(renpy.call, "s_react", i[1])]
            textbutton _("Back") action [Hide("topic_ui"), Jump("s_talkmenu")]
        elif subscreen == 4:
            textbutton _("Change appearance") action [Function(renpy.call, "s_customizationmenu")]
            textbutton _("Back") action [Hide("topic_ui"), Jump("s_talkmenu")]
        else:
            if cat == 0:
                for i in (subscreen[7 * page: 7 * page + 7] if len(subscreen.topics) > 8 else subscreen.topics):
                    textbutton i.name xpadding 10 action [Function(subscreen, i), Return()] text_italic not i.seen
            elif cat == 1:
                $topic_list = subscreen.topics if config.developer else subscreen.seen_list
                for i in (topic_list[7 * page: 7 * page + 7] if len(topic_list) > 8 else topic_list):
                    if i.show_prompt:
                        textbutton i.name xpadding 10 text_italic not i.seen action [Function(subscreen, i), Return()]
            elif cat == 3:
                $lc = cur_lang().code or 'eng'
                $topic_list = subscreen.topics if config.developer else subscreen.seen_list
                for i in (topic_list[7 * page: 7 * page + 7] if len(topic_list) > 8 else topic_list):
                    textbutton (i.poem.title.get(lc) or i.poem.title['eng']) text_italic not i.seen xpadding 10 action [Function(subscreen, i), Return()]
            
        hbox:
            spacing 324
            
            if type(subscreen) != int:
                $list_len = len(filter(lambda x: x.show_prompt, subscreen.topics)) if cat == 0 or config.developer else subscreen.seen_len
                #label str(list_len)
                if page > 0:
                    textbutton ("<") xpadding 0 xsize 48 keysym 'K_LEFT' action SetScreenVariable("page", page-1) #Previous Page
                else:
                    null width 48
                if list_len > 8 and page < list_len // 7:
                    textbutton (">") xpadding 0 xsize 48 keysym 'K_RIGHT' action SetScreenVariable("page", page+1) #Next Page
        if type(subscreen) != int and cat < 3:
            textbutton _("Back") action [SetScreenVariable("subscreen", cat), SetScreenVariable("page", 0)]
        textbutton _("Close") action [Hide("topic_ui"), Jump("s_loop")]

screen say_ui():
    default page = p
    
    style_prefix "choice"
    
    vbox:
        align (1.0, 0.5)
        offset (-10, 0)
        
        textbutton _("I love you") action [Hide("say_ui"), Jump("s_love_you")]
        textbutton _("Goodbye") action [Hide("say_ui"), Jump("s_farewell")]
        textbutton _("Nothing{#Say Entry}") action [Hide("say_ui"), Jump("s_loop")]

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

screen customize_ui():
    default cur_hair = 0
    default processed = False
    
    if not processed:
        python:
            cl = {
                'hair': CUSTOM_TEMPLATES['hair']
            }
            
            nl = {}
            
            for i in cl:
                li = cl[i]
                if type(cl[i]) != dict:
                    li = li[0]
                L = []
                v = li.values()
                k = li.keys()
                for j in range(len(v)):
                    L.append(k[j])
                    if k[j] == persistent.customization[i]:
                        SetScreenVariable("cur_" + i, j)()
                nl[i] = L
                    
                SetScreenVariable("cl", nl)()
                SetScreenVariable("processed", True)()
                
                
            def set_custom(l, t, i):
                persistent.customization[t] = l[t][i]
                SetScreenVariable("cur_" + t, i)()
            
            lens = {
                'hair': len(cl['hair'])
            }
            
    
    textbutton "<" action Function(set_custom, cl, 'hair', (cur_hair - 1) if cur_hair > 0 else (lens['hair'] - 1)):
        style "choice_button"
        anchor (0.5, 0.5)
        xpadding 0
        xsize 42
        ycenter 0.15
        xalign 0.1
    textbutton ">" action Function(set_custom, cl, 'hair', (cur_hair + 1) % lens['hair']):
        style "choice_button"
        anchor (0.5, 0.5)
        xpadding 0
        xsize 42
        ycenter 0.15
        xalign 0.9
    
    textbutton "OK!" action Return():
        style "choice_button"
        xcenter 0.5
        yalign 0.95

screen feat_ui():
    default selectable = persistent.playthrough > 5 and justIsSitting
    style_prefix "choice"
    if selectable:
        pass#use sayori_touchable
    vbox:
        align (0.01, 0.99)
        spacing 5
        
        if selectable:
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
    call screen talk_ui
    jump s_loop
    
label s_musicmenu(page = 0):
    $show_s_mood(ss2, True)
    hide screen feat_ui
    call screen music_ui(page)
    jump s_loop

label s_topicmenu(subscreen = 0, t = 0):
    $show_s_mood(ss2, True)
    hide screen feat_ui
    hide screen talk_ui
    call screen topic_ui(subscreen, t)
    jump s_loop

label s_saymenu:
    $show_s_mood(ss2, True)
    hide screen feat_ui
    hide screen talk_ui
    call screen say_ui
    jump s_loop

label s_gamemenu():
    $show_s_mood(ss2, True, 'vh')
    hide screen feat_ui
    call screen minigame_ui() nopredict
    jump s_loop

label s_customizationmenu():
    $show_s_mood(ss1, False)
    hide screen feat_ui
    hide screen talk_ui
    call screen customize_ui()
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
