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
            self.list.append((obj, length))
        
        def __getattr__(self, attr):
            return self.list.__dict__[attr]
        
        def __getitem__(self, index):
            err = IndexError('list index out of range')
            
            if len(self.list) > 0:
                if index >= self.min:
                    if index <= self.list[0][1]:
                        return self.list[0][0]
                    else:
                        r = self.list[0][1]
                        for i in self.list[1:]:
                            r += i[1]
                            if index <= r:
                                return i[0]
                        else:
                            raise err
                else:
                    raise err
            else:
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
    s "You're my only friend now, you know..."
    s "And you also know how to cheer me up."
    s "Maybe, you'll do it now?"

label s_greeting_6:
    show sayori 7aaaa at ss1 zorder 2
    s "Oh, hi again!"
    s "I was surfing the internet, when you came back."
    s "And to be honest, even it don't give me as much joy as you give."
    s "So I'm glad, you're back."

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
            jump expression get_random_gretting().label
        else:
            s "Hello, [player]!"
    else:
        s "Good evening, [player]!"
        
    if bday:
        $ age = get_now().year - persistent.playerbdate.year
        s 6aaca "Whose birthday is today?"
        s 6aeca "It's your birthday!"
        s 6aeaa "Happy birthday, [player]!"
        s 8aebb "I'm sorry I have no present to you."
        s "I hope it doesn't upset you."
        s 6aaaa "Anyway, I'm glad you're older by a year."
        if age == 18:
            s "It means we finally are the same age now."
        s "Don't forget to make a birthday party."
        s 6abaa "...If you don't dislike them, of course."
        s 7aaaa "However, if you have come here, let's spend some time together."
    elif time_of_day != 1 or ee_chance > 0.1:
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
    
    return