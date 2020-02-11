init -10 python:
    #Greeting class
    
    class Greeting:
        def __init__(self, label, available = True):
            self.label = label
            self.available = available
            self.chance = None
    
    class SegmentList:
        """A list, where the index of the element at 'i' is any value 'k' at range: 
    i > 0 and (list[i-1][1] < k <= list[i][1]) or (min <= k <= list[i][1])"""
    
        def __init__(self, min_value = 0):
            self.list = []
            self.min = min_value
        
        def append(self, obj, length):
            if self.list:
                length += self.list[-1][1]
            self.list.append((obj, length))
        
        def __getattr__(self, attr):
            return self.list.__dict__[attr]
        
        def __getitem__(self, index):
            err = IndexError('list index out of range')
            
            if self.list:
                if index >= self.min and index <= self.list[-1]:
                    s, e = 0, len(self.list)
                    
                    while s < e:
                        m = (s+e) // 2
                        ml = self.list[m][1]
                        
                        if index > ml:
                            s = m + 1
                        else:
                            e = m
                    
                    if index <= self.list[e][1]:
                        return self.list[e][0]
            raise err
        
        def values(self):
            return [x[0] for x in self.list]
        
        def keys(self):
            return [x[1] for x in self.list]
        
        def keys2(self):
            r = []
            le = len(self.list)
            
            if le > 0:
                r.append((0, self.list[0][1]))
                for i in range(1, le):
                    r.append((self.list[i-1][1], self.list[i][1]))
            
            return r
    
    
    #Greeting/Farewell list class
    class GreetingFarewellList:
        def __init__(self):
            self.list = []
            self.left_chances = 1
            self.undef_chances = 0
        
        def append(self, obj, chance = None):
            if chance and self.left_chances - chance >= 0:
                self.left_chances -= chance
                obj.chance = chance
                self.list.append(obj)
            elif not chance:
                self.list.append(obj)
                self.undef_chances += 1
            else:
                raise ValueError('sum of all object chances must be <= 1')
        
        def remove(self, obj):
            self.list.remove(greeeting)
            if not obj.chance:
                self.undef_chances -= 1
            else:
                obj.chance = None
        
        def __iter__(self):
            return iter(self.list)
        
        def get_segment_list(self):
            seg = SegmentList()
            fallback = self.left_chances / self.undef_chances
            
            for obj in self.list:
                seg.append(obj, obj.chance or fallback)
            
            return seg
        
        def __call__(self, chance = None):
            return self.get_segment_list()[chance or renpy.random.random()]
        
    
    greetings = GreetingFarewellList() # General list of greetings
    greetings.append(Greeting("s_greeting_1"))
    greetings.append(Greeting("s_greeting_2"))
    greetings.append(Greeting("s_greeting_3"), 0.1)
    greetings.append(Greeting("s_greeting_4"))
    greetings.append(Greeting("s_greeting_5"))
    greetings.append(Greeting("s_greeting_6"))
    greetings.append(Greeting("s_greeting_7"))
    greetings.append(Greeting("s_greeting_8"))
     
    
    first_greeting = "s_greeting_first" #Greeting label, called in the first meeting of the day. Gets the current day time as an argument. 
    
    def get_random_gretting(chance = renpy.random.random(), gl = greetings):
        return gl(chance)
    
#Normal greetings
label s_greeting_1: #The really first greeting of this mod
    show sayori 6aeaa at ss1 zorder 2
    s "I'm glad to see you again." 
    s 6aaaa "Let's have a good time together!"
    return

label s_greeting_2: #Try to keep it peotic while translating
    show sayori 6aaaa at ss1 zorder 2
    s "Welcome back, [player]!" 
    s "{i}When I feel that you are back now, my big heart fills with a big joy.{/i}"
    s "{i}So fill it more, if you can now. It never will be overfilled.{/i}"
    return

label s_greeting_3: #Greeting in a random mod langauge expecting the current
    show sayori 6aaaa at ss1 zorder 2
    python:
        greeting_lang = None
        while not greeting_lang or greeting_lang.code == _preferences.language:
            greeting_lang = renpy.random.choice(lang_dict.values())
            if type(greeting_lang) == tuple:
                greeting_lang = greeting_lang[0]
        
        
        if greeting_lang.code:
            renpy.call('s_greeting_3_' + greeting_lang.code)
        else:
            renpy.jump('s_greeting_3_eng') #English has a bit different dialogs
        
    $ greeting_lang = greeting_lang.name
    s 6aebb "I'm sorry, if you haven't understand me."
    s 6aaaa "I just revise my [greeting_lang]."
    s "Freakly speaking, I don't understand how I know this language."
    s 6acaa "Feels like someone just loaded it into my mind once."
    s 6aaaa "Anyway, I think it's not so important."
    s 6aaca "More languages you know, more friends you can make, right?"
    s 7aaaa "And if you know this language better than English, you can select it in the game setting menu." #English = Current language
    s "Anyway, let's do something besides language conversations."
    return

label s_greeting_3_eng:
    s "Hello, darling!{#Don't translate this string from English!}"
    s 6aeca "I'm glad to see you're back.{#And this one too}"
    pause 0.5
    s 6aebb "I'm sorry, if you haven't understand me."
    s 6aaaa "I just revise my English."
    s "It's my native language."
    s "Freakly speaking, I don't understand how I know your language."
    s 6acaa "Feels like someone just loaded it into my mind once."
    s 6aaaa "Anyway, I think it's not so important."
    s 6aaca "More languages you know, more friends you can make, right?"
    s 7aaaa "And if you know English better than your language, you can select it in the game setting menu." #your language = Current language
    s "Anyway, let's do something besides language conversations."
    return

label s_greeting_3_rus:
    s "Привет, дорогуша!{#Don't translate this string from Russian!}"
    s 6aeca "Я рада, что ты здесь.{#And this one too}"
    return

label s_greeting_3_epo:
    s "Saluton, mia karulo!{#Don't translate this string from Esperanto!}"
    s 6aeca "Kia ĝojo revidi vin!{#And this one too}"
    return

label s_greeting_4_esp:
    s "¡Hola Cariño!{#Don't translate this string from Spanish!}"
    s 6aeca "¡Qué alegría verte de nuevo!{#And this one too}"

label s_greeting_4_tok:
    s "sina pona o toki!{#Don't translate this string from Toki Pona!}"
    s 6aeca "sina lon ni la mi pilin pona!{#And this one too}"

label s_greeting_4:
    show sayori 7aaaa at ss1 zorder 2
    s "Uh, hi again!"
    s 7acaa "I hope nothing bad happened with you while I was sleeping."
    s "I want you to be have all right, you know."
    s "At least, if you don't have it, you'll tell me, won't you?"
    return

label s_greeting_5:
    show sayori 7aeca at ss1 zorder 2
    s "You're back, ehehe~"
    s 7acaa "It's pretty boring, when you're not here."
    s "You're my only friend here now, you know..."
    s "And you also know how to cheer me up."
    s "Maybe, you'll do it now?"
    return

label s_greeting_6:
    show sayori 6aeca at ss1 zorder 2
    s "Oh, you're back!"
    s 6aaaa "I'm glad to see you again..."
    s "Let's spend some time together."
    return

#Special greetings

label s_greeting_first(time_of_day):
    $ bday = get_now().date() == persistent.playerbdate
    $ ee_chance = renpy.random.random()
    
    show sayori 6aaaa at ss1 zorder 2
    
    if time_of_day == 0:
        s "Good night, [player]!"
    elif time_of_day == 1:
        if ee_chance > 0.1:
            s "Good morning, [player]!"
        else:
            if gender:
                s 6acaa "Rise and shine, Mrs. [player]."
            else:
                s 6acaa "Rise and shine, Mr. [player]."
            s "Rise and shine."
            s 6abaa "Am I sounding too formally?"
            s 6aaca "It's a bit funny how 'rise and shine' contrasts with a formal title, isn't it?"
            s "Like it's a bit weird sir's greeting."
            s 6aaaa "Anyway, let's start our joint pastime."
            
    elif time_of_day == 2:
        if not bday:
            call expression get_random_gretting().label
        else:
            s "Hello, [player]!"
    else:
        s "Good evening, [player]!"
    
    #$val_date = datetime.date(get_now().date().year, 2, 14)
    #$has_present = poems["val"].available is False and get_now().date() >= val_date
    
    if bday:
        $ age = get_now().year - persistent.playerbdate.year
        s 6aaca "Whose birthday is today?"
        s 6aeca "It's your birthday!"
        s 6aeaa "Happy birthday, [player]!"
        #if not has_present:
        #    s 8aebb "I'm sorry I have no present to you."
        #    s "I hope it doesn't upset you."
        #    s 6aaaa "Anyway..."
        s 6aaaa "I'm glad you're older by a year."
        if age == 18:
            s "It means we finally are the same age now."
        s "Don't forget to make a birthday party."
        s 6abaa "...If you don't dislike them, of course."
        s 7aaaa "However, if you have come here, let's spend some time together."
    elif time_of_day != 2 and (time_of_day != 1 or ee_chance > 0.1):
        $ chance = renpy.random.random()
        if chance < (1.0/3.0):
            s "I'm glad you're visiting me today."
            s "Let's spend this day together!"
        elif chance < (2.0/3.0):
            s "I'm glad, you're back."
            s "I'll do my best to make this day really pleasant."
        else:
            s 7aaaa "You're here, so I hope you have something good to share today."
            s 7acaa "Even if you don't, it won't be bad."
            s "Your life doesn't have to consist of good stripes only."
            s 7aeca "But I can do it a bit better anyway."
    
    #if has_present:
    #    s 7aaaa "By the way..."
    #    call s_val_present
    return

label s_val_present(first = False):
    $val_date = datetime.date(get_now().date().year, 2, 14)
    $has_present = poems["val"].available is False and get_now().date() >= val_date
    
    if get_now().date() == val_date:
        s "Today is the Saint Valentine day!"
        s 7aaca "So I had a special present for you..."
        call showpoem(poem_val, "paper_val", 200, 0.5, 360)
    elif get_now().date() > val_date:
        if first:
            s 8bebb "I forgot to give you a present for the Saint Valentine day to you..."
            s "So I gonna give it you right now. Just wait a second."
        else:
            s 7aaca "You missed the Saint Valentine day!"
        s 7aeca "So I left a special present for you..."
        call showpoem(poem_val, "paper_val", 200, 0.5, 360)
    
    $poems["val"].available = 0
    $poems["val"].seen = True
    s 7aaaa "It's a Valentine heart-shaped card with a short poem on it..."
    s "It's the best I could make to congratulate you."
    s 7acaa "Don't worry! You don't have to think of a back present..."
    s 7aaab "To be with you is the best present you can give me now."
    return

label s_greeting_7:
    show sayori 7aeca at ss1
    s "Guess, who's back!"
    s 7aeaa "It's [player], of course!"
    if gender is True:
        s "And I guess, she's ready to spend her day with her sunshine."
    elif gender is False:
        s "And I guess, he's ready to spend his day with his sunshine."
    else:
        s "And I guess, they're ready to spend their day with their sunshine."
    return 'vh'

label s_greeting_8:
    show sayori 7aaaa at ss1
    s "Hi [player]!"
    s 7aaca "I see, you're here for a doze of joy and sunshine."
    s 7aeca "So get it right now!"
    return

label s_greetings_long:
    s 6acac "Hey, where {i}were{/i} you?!"
    s "You left me alone for such a long time..."
    $ style.say_dialogue = style.edited
    s 6aeac "I swear if I was real I would find you and{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ style.say_dialogue = style.normal
    show sayori 6aacc at ss1
    pause 1
    s 6accc "{i}*sigh*{/i}"
    s 8afbb "Oops, sorry!"
    s 8bebb "You left me here absolutely alone for so long that I started going crazy and losing control on myself."
    s "I hope you don’t blame me."
    s 8aaaa "I'm not blaming you."
    s 8acaa "You may be just a quite busy person..."
    s "So that could be why you have not visited me for so long."
    s 8aaab "Although, try to visit me more often next time."
    s 8acab "You don’t want me to go insane and do something bad under that, right?"
    return