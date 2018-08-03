#Tic-Tac-Toe
init 10 python:
    def ttt_prep(self, restart = False, *args, **kwargs):
        self.field = [None] * 9 #True = Cross, False = Circle, None = Empty
        self.playerTurn = True
        self.state = 0 #0 = game not over, 1 = 45deg line, 2 = 135deg line; 3+x = vert. line on the x-th column,
        #6+y hor. line on the y-th row; -i = i for cross; 9 = draw game; -9 = retstart
        
        if not restart:
            self.score = [0, 0] #score[0] = Sayori's score (); score[1] = Player's score
            
            def ttt_check_line(id): # 1 = 45deg line, 2 = 135deg line; 3+x = vert. line on the x-th column, 6+y hor. line on the y-th row, 0 = whole field
                t_ids = None
                if id == 0:
                    tiles = range(9)
                elif id == 1:
                    t_ids = [0, 4, 8]
                elif id == 2:
                    t_ids = [2, 4, 6]
                elif id < 6:
                    id -= 3
                    t_ids = [id, id + 3, id + 6]
                else:
                    ti = (id-6) * 3
                    t_ids = [ti, ti + 1, ti + 2]
                
                clt, crt = 0, 0 #clt = circle tiles, crt = cross tiles
                for i in t_ids:
                    i = ttt.field[i]
                    if i is True:
                        crt += 1
                    elif i is False:
                        clt += 1
                return clt, crt, t_ids 
            
            def ttt_new_state():
                for i in range(1, 9):
                    clt, crt = ttt_check_line(i)[:2]
                    if clt == 3:
                        return i
                    elif crt == 3:
                        return -i
                
                for i in ttt.field:
                    if i is None:
                        return 0
                return 9
            
            def ttt_turn(i):
                if ttt.state == 0 and ttt.field[i] is None:
                    ttt.field[i] = ttt.playerTurn
                    ttt.playerTurn = not ttt.playerTurn
                    
                    fig = "circle"
                    if ttt.playerTurn:
                        fig = "cross"
                    renpy.play("mod_assets/sfx/ttt_"+ fig + ".ogg", "sound")
                    
                    ttt.state = ttt_new_state()
                    ttt_check_state()
                    if not ttt.playerTurn:
                        renpy.call_in_new_context("mg_ttt_s_turn")
                    
            def ttt_check_state():
                if ttt.state != 0:
                        if abs(ttt.state) < 9:
                            renpy.call_in_new_context("mg_ttt_s_comment", ttt.state < 0)
                            ttt(restart = True, winner = ttt.state < 0)
                        elif ttt.state == -9:
                            renpy.call_in_new_context("mg_ttt_s_comment", 3)
                            ttt(restart = True, winner = 0)
                        else:
                            renpy.call_in_new_context("mg_ttt_s_comment", 2)
                            ttt(restart = True)
            
            def ttt_ai():
                w_lines, l_lines, f_lines = [], [], []
                
                for i in range(1, 9):
                    clt, crt, line = ttt_check_line(i)
                    if clt == 2 and crt == 0:
                        w_lines.append(line)
                    elif crt == 2 and clt == 0:
                        l_lines.append(line)
                    elif clt > 0 and crt == 0:
                        f_lines.append(line)
                
                if len(w_lines):
                    line = renpy.random.choice(w_lines)
                    for i in line:
                        if ttt.field[i] is None:
                            return ttt_turn(i)
                if len(l_lines):
                    line = renpy.random.choice(l_lines)
                    for i in line:
                        if ttt.field[i] is None:
                            return ttt_turn(i)
                if len(f_lines):
                    line = renpy.random.choice(f_lines)
                    line = filter(lambda x: ttt.field[x] is None, line)
                    return ttt_turn(renpy.random.choice(line))
                else:
                    line = filter(lambda x: ttt.field[x] is None, range(9))
                    return ttt_turn(renpy.random.choice(line))
            
            self.new_state, self.check_state = ttt_new_state, ttt_check_state
            self.check_line, self.turn, self.ai = ttt_check_line, ttt_turn, ttt_ai
        
        elif not kwargs.get("winner") is None:
            w = kwargs['winner']
            self.score[w] += 1
        
    ttt = minigame(_("Tic-Tac-Toe"), 'mg_ttt', ttt_prep)
    mg_list.append(ttt)
    
    


image line_black = "mod_assets/images/minigames/line.png"
image line_red = "mod_assets/images/minigames/line_red.png"
image line_blue = "mod_assets/images/minigames/line_blue.png"

image ttt_cross:
    Text("X", font = "gui/font/s1.ttf", size = 240, color = "#f00", outlines = [])
    on show:
        alpha 0.5
        linear 0.25 alpha 1.0

image ttt_cross_cursor:
    Text("X", font = "gui/font/s1.ttf", size = 240, color = "#f00", outlines = [])
    alpha 0.25
    truecenter

image ttt_circle: 
    Text("O", font = "gui/font/s1.ttf", size = 240, color = "#6acdcd", outlines = [])
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0

screen mg_ttt_grid(): #3x3 grid with 184x184px tiles
    add "paper" xalign 0.5
    for i in range(2):
        add "line_black" pos (360, 260 + 192*i) zoom 0.8
        add "line_black" pos (260 + 192*i, 80) rotate 90 zoom 0.8

screen mg_ttt_scr():
    layer "master"
    zorder 0
    
    python:
        from math import sqrt
        sc = 0.8
        diag_sc = sqrt(sc*sc * 2)

    use mg_ttt_grid()
    
    for x in range(3):
        for y in range(3):
            $i, p = ttt.field[3 * y + x], (260 + 192 * (x+1), 192 * (y+1))
            if i is True:
                add "ttt_cross" anchor (0.5, 0.5) pos p
            elif i is False:
                add "ttt_circle" anchor (0.5, 0.5) pos p
            if ttt.state == 0 and ttt.playerTurn:
                button:
                    background None
                    pos p
                    xysize (184, 184)
                    anchor (0.5, 0.5)
                    if i is None:
                        hover_background "ttt_cross_cursor"
                    keyboard_focus i is None
                    keysym 'K_KP' + str(3 * (2-x) + y + 1)
                    action Function(ttt.turn, 3 * y + x)
            
            if ttt.state != 0:
                $ color = ttt.state > 0 and 'blue' or 'red'
                $ state = abs(ttt.state)
                if state < 3:
                    add "line_"+color anchor (0.5, 0.5) xzoom diag_sc yzoom sc rotate (90 * state - 45) pos (640, 360)
                elif state < 6:
                    add "line_"+color anchor (0.5, 0.5) zoom sc rotate 90 pos (192 * state - 128, 360)
                else:
                    add "line_"+color anchor (0.5, 0.5) zoom sc pos (640, 192 * state - 984)
                    
    vbox:
        pos (360, 5)
        spacing 5
        
        text "[s_name]: " + str(ttt.score[0]) style s_text_style():
            if not ttt.playerTurn:
                color "#6acdcd"
        text "[player]: " + str(ttt.score[1]) style s_text_style():
            if ttt.playerTurn:
                color "#f00"
    vbox:
        style_prefix "choice"
        align (0.01, 0.99)
        spacing 5
        
        textbutton _("Restart (R)") xpadding 0 xsize 200 keysym 'r' action [Function(ttt.set_state, -9), Function(ttt.check_state)]
        textbutton _("Quit (Q)") xpadding 0 xsize 200 keysym 'q' action Jump("mg_ttt_quit")
    

label mg_ttt:
    $justIsSitting = False
    hide sayori
    show sayori 1a at i44 zorder 2
    call screen mg_ttt_scr() nopredict
    return

label mg_ttt_s_comment(id = 0): #Sayori's comment; 0/1 = Sayori's victory/defeat, 2 = draw, 3 = restart
    if id == 0:
        $randId = renpy.random.randint(0, 2)
        if randId == 0:
            s 2q "OK, I win this time."
            s "You should have better tactic next time."
        elif randId == 1:
            s 2r "I've finished my line!"
            s 2a "Just improve your tactic and try again."
        else:
            s 2e "Don't worry!"
            s "Maybe, you'll win next time."
    elif id == 1:
        $randId = renpy.random.randint(0, 1)
        if randId == 0:
            s 5b "OK, you win!"
            s 5a "Next time I'll be more cunning."
        else:
            s 1n "Oh, you've just finish your line."
            s 1l "You seem to be more cunning than me."
            s "Next time, I'll try better."
    elif id == 2:
        $randId = renpy.random.randint(0, 1)
        if randId == 0:
            s 1k "Oh, the field is full."
            s "And there's not any full line."
            s "Let's just try again."
        else:
            s 4q "Don't worry!"
            s "Tic-Tac-Toe games often end up with draw."
            s "Maybe, there will be a winner in a next game."
    else:
        $randId = renpy.random.randint(0, 1)
        if randId == 0:
            s 4o "Are you giving up?"
            s 4c "Then we'll start again, but I'll get a point for this round."
        else:
            s 3g "What's up [player]?"
            s "OK, I'll restart the game..."
            s 3r "But I'll be this round winner."
    return

label mg_ttt_s_turn:
    show sayori 1k at i44 zorder 2
    python:
        randTime = renpy.random.triangular(0.25, 2)
        renpy.pause(randTime)
        ttt.ai()
    show sayori 1a at i44 zorder 2
    pause 0.25
    return
    
label mg_ttt_quit:
    hide screen mg_ttt_scr
    hide sayori
    $show_s_mood(ss2)
    with dissolve
    python:
        justIsSitting = True
        if ttt.score[0] > ttt.score[1]:
            s_mood = 'vh'
        else:
            s_mood = 'h'
    return
