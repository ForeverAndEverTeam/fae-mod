#Bull and cows
init 10 python:
    def bnc_prep(self, restart = False, *args, **kwargs):
        self.state = 0 #0 = game not over, 1 = player won, -1 = player lost
        self.guessed = ""
        self.guessed_len = 0
        self.lifes = 0
        self.bulls = 0
        self.cows = 0
        
        ns = "0123456789" #All selectable numbers
        for i in range (renpy.random.randint(3, 6)):
            n = renpy.random.choice(ns) #Selected number
            self.guessed += n
            ns = ns.replace(n, "") #Remove the selected number from ns
        self.guessed_len = len(self.guessed)
        self.lifes = self.guessed_len
        self.last = "_ " * self.guessed_len
        
        def bnc_check(answer):
            self.last = ""
            self.bulls, self.cows = 0, 0
            for i in range(self.guessed_len):
                if answer[i] == self.guessed[i]:
                    self.bulls += 1
                    self.last += "{color=#00cc00}" + answer[i] + "{/color} "
                elif answer[i] in self.guessed:
                    self.cows += 1
                    self.last += "{color=#ffff00}" + answer[i] + "{/color} "
                else:
                    self.last += "{color=#ff0000}" + answer[i] + "{/color} "
            if self.bulls == self.guessed_len:
                self.state = 1
            else:
                self.lifes -= 1
                if self.lifes <= 0:
                    self.state = -1
            return self.state
        
        self.check = bnc_check
        
        if restart:
            renpy.call(self.label)

screen mg_bnc_scr():
    layer "master"
    zorder 100
    
    vbox:
        label _("Tries left: [bnc.lifes]")
        label _("Last answer: [bnc.last]")
        label "{color=#00cc00}Bulls: [bnc.bulls]{/color}"
        label "{color=#ffff00}Cows: [bnc.cows]{/color}"
        if config.developer:
            yoffset 1
            label _("{i}Right answer: [bnc.guessed]{/i}")
    
    vbox:
        style_prefix "choice"
        align (0.01, 0.99)
        spacing 5
        
        textbutton _("Restart (R)") xpadding 0 xsize 200 keysym 'r' action Function(renpy.call, "mg_bnc_s_comment", -1, True)
        textbutton _("Quit (Q)") xpadding 0 xsize 200 keysym 'q' action Jump("mg_bnc_quit")
    

label mg_bnc:
    # $ setupRPC("Playing Bows and Cows")
    $ Sayori.setInGame(True)
    #$justIsSitting = False
    #$show_s_mood(ss1)
    # TODO: LEAVE CONDITION
    #show s gbaabira "did you- just try to close and reopen the game to play bows and cows again >:|"

    if persistent.cooldown is not None:
        if persistent.cooldown >= datetime.datetime.now():
            $ persistent.cooldown = None
        else:
            s gbaaipa "..."
            return
    else:
        pass

    call mg_bnc_s_comment(0) from _call_mg_bnc_s_comment
    show screen mg_bnc_scr() nopredict
    python:
        while bnc.state == 0:
            bnc_answer = ""
            prompt = __("Guess the number:")
            invalid_answers = 0
            while True:
                bnc_answer = str(renpy.input(prompt, allow = "0123456789", length = bnc.guessed_len))
                if len(bnc_answer) == 0:
                    pass
                elif len(bnc_answer) != bnc.guessed_len:
                    invalid_answers += 1
                    if invalid_answers < 5:
                        prompt = __("Wrong length! Your answer should consist of [bnc.guessed_len] different digits.")
                    elif invalid_answers == 5:
                        s_mood = 's'
                        #show_s_mood(ss1)
                        prompt = __("It stops being funny, [player].")
                    elif invalid_answers == 6:
                        prompt = __("Come on, give a valid answer already!")
                    elif invalid_answers == 7:
                        #s_mood = 'b'
                        #show_s_mood(ss1)
                        prompt = __("Just type as more numbers as you can. This field has the needed max length anyway.")
                    elif invalid_answers == 8:
                        #s_mood = 'a'
                        #show_s_mood(ss1)
                        prompt = __("I'm getting annoyed, [player].")
                    elif invalid_answers == 9:
                        prompt = __("Further error will cost you a try.")
                    elif bnc.lifes > 2:
                        bnc.lifes -= 1
                        prompt = __("I warned you.")
                    elif bnc.lifes == 2:
                        bnc.lifes -= 1
                        mr = _("mr.")
                        if gender is True:
                            mr = _("mrs.")
                        prompt = __("Last chance, [mr] I Can't Count Up To [bnc.guessed_len].")
                    else:
                        bnc.lifes -= 1
                        renpy.call("mg_bnc_s_comment", -2)
                        break
                else:
                    break
            #s_mood = 'h'
            #show_s_mood(ss1)
            bnc.check(bnc_answer)
    #if s_mood != "a":
    call mg_bnc_s_comment(bnc.state) from _call_mg_bnc_s_comment_1
    return

label mg_bnc_s_comment(state = -1, restart = False): #Sayori's comment. 0 = initial, -2 = annoyed, other = state reaction
    hide screen mg_bnc_scr
    if state == 0: # Starting prompt
        s abaaaoa "I propose you a number of [bnc.guessed_len] digits..."
        s "Try to guess it."
    elif state == -1: # Game end (restart or out of tries.)
        if restart:
            s bbaaada "Are you giving up?"
        else:
            s abaacia "Your tries are over."
        if bnc.bulls + bnc.cows == bnc.guessed_len: # NO CLUE WHAT THIS IS. FUCK THIS CODE
            s "You were close to the right answer."
        elif restart:
            s abaadaa"OK, I'll tell you the right answer."
        s abaaloa "The right number was {i}[bnc.guessed]{/i}."
        s ebaacqa"Let me think of another number."
        $ bnc(restart = True)
    elif state == 1: # Correct answer
        s abaacoa "You're right. It was {i}[bnc.guessed]{/i}!"
        s abaaaea "Let's play one more time."
        $ bnc(restart = True)
    elif state == -2: # If you try to guess past the amount you're allowed to guess
        s gbaaipa "OK, you win, {i}meanie{/i}!"
        s "I'm really annoyed right now..."
        $ mg_list.remove(bnc)
        s gbaabpa "So I don't want to play this game with you anymore."
        s "I won't lose next time."
        $ persistent.cooldown = datetime.datetime.now() + datetime.timedelta(minutes=5)
        return


    
label mg_bnc_quit:
    $ Sayori.setInGame(False)
    hide screen mg_bnc_scr
    # $ setupRPC("In the spaceroom")
    #$s_mood = 'h'
    #$show_s_mood(ss1)
    return
