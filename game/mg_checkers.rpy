#Checkers/Draughts (Russian variant)
default persistent.checkers_winfactor = 30

init 10 python:
    
    def checkers_start_pos(debug = 0):
        if debug == 0:
            f = [0] * 32
            for i in range(12):
                f[i] = 3
                f[31 - i] = 1
            return f
        elif debug == 1:
            f = [0] * 32
            for i in range(12):
                f[i] = 3
            f[13] = 1
            return f

    def checkers_prep(self, restart = False, *args, **kwargs):
        self.field = checkers_start_pos(kwargs.get("scheme") or 0)
        ## Each integer in self.field storages the below flags (0/1):
        ## 1 = free/occupied
        ## 2 = white/black
        ## 4 = man/king
        ## 8 = unselected/selected
        
        self.playerTurn = True # player plays as black while Sayori plays as white
        
        self.state = 0 #0 = game not over, 1 = black wins, -1 = white wins, -2 = restart, 2 = draw game
        self.left_pieces = [12, 12] #0 - player's, 1 - Sayori's
        self.selected = None
        self.possible_turns = []
        self.multiturn = False
        self.with_ai = kwargs.get('ai') if 'ai' in kwargs else True
        
        checkers.selectable = []
        checkers.unblocked = ([], [])
        checkers.atakes = [] #All posiable take without the selected piece's one
        checkers.selectable = checkers_check_board(checkers.selectable)
        
        checkers.asked_for_a_draw = False
        
        if not restart:
            self.score = [0, 0] #score[0] = Sayori's score (); score[1] = Player's score; 2 = 1 real point, 1 = half real point
        
    def checkers_n_to_xy(n, sx = 1, sy = None, ox = 0, oy = 0):
        x = (n & 3) << 1
        y = n >> 2
        if n & 7 > 3:
            x += 1
        return ox + x * sx, oy + y * (sy or sx)
    
    def checkers_xy_to_n(x, y):
        if y & 1:
            x -= 1
        if x & 1:
            return None # white cells are not in checkers.field
        return (y << 2) + (x >> 1)
        
    checkers = minigame(_("Checkers"), 'mg_checkers', checkers_prep)
    mg_list.append(checkers)
    
    def checkers_cell(x, y = None, board = None):
        board = board or checkers.field
    
        if not y is None:
            try:
                return board[checkers_xy_to_n(x, y)]
            except IndexError:
                return 0
        elif not x is None:
            return board[x]
        return 0
    
    def checkers_sprite(ch):
        n = "checkers_"
        if ch & 4:
            n += "king"
        else:
            n += "man"
        if ch & 2:
            n += 'B'
        else:
            n += 'W'
        return n
    
    def get_shift(n, ox, oy):
        sox = ox
        x, y = checkers_n_to_xy(n)
        x += ox
        
        if x < 0 or x > 7 or y + oy < 0 or y + oy > 7:
            return None
        
        n += 4 * oy
        if (y + oy) & 1:
            if ox > 0:
                ox -= (abs(oy) >> 1) + 1
        else:
            if ox < 0:
                ox += (abs(oy) >> 1) + 1
        n += ox
        
        return n, sox, oy
    
    def checkers_gen_turns(n, first = True, board = None, king = None, depth = 0, party = None):
        board = board or checkers.field
        turns = []
        
        x, y = checkers_n_to_xy(n)
        i = checkers_cell(n, board = board)
        if party is None:
            party = (i & 2) >> 1
        if king is None:
            king = (i & 4) >> 2
        
        takes = False
        
        
        if king:
            shifts = (get_shift(n, 1, -1), get_shift(n, -1, -1), get_shift(n, 1, 1), get_shift(n, -1, 1))
            
            def append(shift, tlist, lt):
                ni = board[shift[0]]
                
                if ni & 1 == 0:
                    if first or len(tlist) > 0 or (not depth and len(checkers_gen_turns(shift[0], False, board, True, depth + 1))):
                        if len(tlist):
                            lt.append((shift[0], tuple(tlist)))
                        else:
                            lt.append(shift[0])
                    return 1, get_shift(*shift)
                elif (ni & 2) >> 1 != party:
                    nni = get_shift(*shift)
                    
                    if nni and not board[nni[0]] & 1:
                        tlist.append(shift[0])
                        del lt[:]
                        lt.append((nni[0], tuple(tlist)))
                        return 2, nni
                
                return 0, get_shift(*shift)
                
            for si in range(4):
                shift = shifts[si]
                lt, ltk = [], []
                
                if shift is None:
                    continue
                
                ply = 1
                
                while ply < 9:
                    ply += 1
                    res, shift = append(shift, ltk, lt)
                    if not (res and shift):
                        break
                
                if len(ltk) > 0:
                    if not takes:
                        turns = []
                    turns += lt
                elif first and not takes:
                    turns += lt
                    
                takes = takes or len(ltk) > 0
                
            
        else:
            shifts = (get_shift(n, 1, -1), get_shift(n, -1, -1), get_shift(n, 1, 1), get_shift(n, -1, 1))
            
            for si in range(4):
                shift = shifts[si]
                
                if shift is None:
                    continue
                
                
                ni = board[shift[0]]
                
                
                if ni & 1 == 0:
                    t = si - (party << 1)
                    if first and t >= 0 and t < 2:
                        turns.append(shift[0])
                elif (ni & 2) >> 1 != party:
                    nni = get_shift(*shift)
                    
                    if nni and not board[nni[0]] & 1:
                        takes = True
                        turns.append((nni[0], (shift[0], )))
        
            turns = filter(lambda x: not takes or type(x) == tuple, turns)
        
        return turns
    
    def checkers_wf(alter):
        persistent.checkers_winfactor += alter
        if persistent.checkers_winfactor < 0:
            persistent.checkers_winfactor = 0
        elif persistent.checkers_winfactor > 59:
            persistent.checkers_winfactor = 59
    
    def checkers_check_state(board = None, left_pieces = None, unblocked = None):
        board = board or checkers.field
        left_pieces = left_pieces or checkers.left_pieces
        unblocked = unblocked or checkers.unblocked
    
        unb_lens = (len(unblocked[0]), len(unblocked[1]))
        
        men, kings = ([], []), ([], [])
        
        for i in range(32):
            n = board[i]
            if n & 4:
                kings[(n & 2) >> 1].append(i)
            else:
                men[(n & 2) >> 1].append(i)
        
        if not checkers.asked_for_a_draw and (len(men[0]) == 0 or len(men[1]) == 0):
            return 3
        elif unb_lens[1] == 0:
            if unb_lens[0] == 0:
                return 2
            else:
                return -1
        elif unb_lens[0] == 0:
            return 1
        
        return 0
    
    def checkers_check_board(add = None, party = None, board = None, selected = None, left_pieces = None, unblocked = None):
        board = board or checkers.field
        left_pieces = left_pieces or checkers.left_pieces
        selected = selected is None and checkers.selected or selected
        unblocked = unblocked or checkers.unblocked
        if add is None:
            add = checkers.atakes
        
        bl = range(32)
        
        if selected is not None:
            bl.remove(selected)
        
        
        del unblocked[0][:]
        del unblocked[1][:]
        
        for i in bl:
            n = board[i]
            if n & 1:
                turns = checkers_gen_turns(i, board = board)
                if len(turns) == 0:
                    continue
                elif party is None or n & 2 == party << 1:
                    if any(type(x) == tuple for x in turns):
                        add.append(i)
                unblocked[(n & 2) >> 1].append(i)
            else:
                board[i] = 0
        
        if type(add) == bool:
            return []
        return add
        
    def checkers_get_depth():
        return 1 + persistent.checkers_winfactor // 15
    
    def checkers_select(n, board = None, selected = None):
        board = board or checkers.field
        selected = selected is None and checkers.selected or selected
        
        if n is None or board[n] & 1 == 0:
            return None
        
        if selected is not None:
            board[selected] ^= 8
            checkers.possible_turns = []
        board[n] += 8
        
        checkers.possible_turns = checkers_gen_turns(n, board = board)
        
        return n
    
    def checkers_click(n):
        if n is None:
            return None
        
        
        for i in checkers.possible_turns:
            if checkers.selected is not None:
                if type(i) == tuple and i[0] == n:
                    if not checkers.multiturn:
                        checkers_check_board(party = True)
                    
                    for t in i[1]:
                        checkers_take(t)
                    checkers.selected = checkers_move(checkers.selected, n, True)[0]
                    
                    if checkers.selected is None:
                        
                        checkers.playerTurn = not checkers.playerTurn
                        del checkers.selectable[:]
                        checkers.selectable = checkers_check_board(checkers.selectable, False)
                        
                        for atake in checkers.atakes:
                            if len(checkers_gen_turns(atake, False)):
                                checkers_take(atake)
                        checkers.atakes = []
                        
                        checkers.state = checkers_check_state()
                        if checkers.state:
                            renpy.call("mg_checkers_s_comment", checkers.state)
                        else:
                            renpy.call_in_new_context("mg_checkers_s_turn")
                    break
                elif i == n:
                    checkers.selected = checkers_move(checkers.selected, n)[0]
                    
                    checkers.playerTurn = not checkers.playerTurn
                    del checkers.selectable[:]
                    checkers.selectable = checkers_check_board(checkers.selectable, False)
                    checkers.atakes = []
                    checkers.state = checkers_check_state()
                    if checkers.state:
                        renpy.call("mg_checkers_s_comment", checkers.state)
                    else:
                        renpy.call_in_new_context("mg_checkers_s_turn")
                    break
        else:
            if checkers.playerTurn and not checkers.multiturn and checkers_cell(n) & 2 == 2 and n in checkers.unblocked[True] and (not len(checkers.selectable) or n in checkers.selectable):
                checkers.selected = checkers_select(n)
    
    def checkers_ai_turn():
        f = checkers_copy_board()
        a, bt = checkers_best_turn(False)
        
        ##print(a)
        ##print("bt:", bt)
        
        
        ##print(a)
        
        checkers.field = f
        bt = renpy.random.choice(bt)
        checkers_check_board(party = False)
        checkers_do(bt)
        checkers_check_board(party = False)
        #print (bt)
        
        for atake in checkers.atakes:
            if len(checkers_gen_turns(atake, False)):
                checkers_take(atake)
        checkers.atakes = []
        
        checkers.playerTurn = True
        del checkers.selectable[:]
        checkers.selectable = checkers_check_board(checkers.selectable, True)
        ##print(checkers.selectable)
        
        checkers.atakes = []
        
        checkers.state = checkers_check_state()
        if checkers.state:
            renpy.call("mg_checkers_s_comment", checkers.state)

    
    def checkers_best_turn(party, depth = None, eval = 0, last_turn = None, alpha = float("-inf"), beta = float("inf")):
        if depth is None:
            depth = checkers_get_depth()
        #print(depth)
        
        if depth == 0 or checkers_check_state():
            ##print("End")
            if not last_turn:
                raise ValueError("last last_turn can't be None")
            return eval, [last_turn]
            
        
        turns = []
        bt = []
        
        
        del checkers.selectable[:]
        checkers.selectable = checkers_check_board(checkers.selectable, party)
        
        
        
        ##print(checkers.selectable)
        
        slt = checkers.unblocked[party]
        if len(checkers.selectable):
            slt = list(set(slt) & set(checkers.selectable))
        
        for i in slt:
            turns += checkers_ai_test_turn(i, party)[0]
        
        
        for turn in turns:
            if alpha >= beta:
                break
            
            checkers_do(turn)
            print(depth, turn)
            
            res = checkers_best_turn(not party, depth - 1, -(eval + checkers_eval_turn(turn)), turn, -beta, -alpha)
            total_eval, nt = -res[0], res[1]
            
            if total_eval > alpha:
                bt = [turn]
            else:
                bt.append(turn)
            
            checkers_undo(turn)
            print(-depth, turn)
        
        
        return alpha, bt
            
    
    def checkers_pos_eval(n, board = None):
        board = board or checkers.field
        eval = 0
        
        x = board[n]
        
        shifts = (get_shift(n, 1, -1), get_shift(n, -1, -1), get_shift(n, -1, 1), get_shift(n, 1, 1))
        
        for i in range(4):
            shift = shifts[i]
            
            if shift:
                p = board[shift[0]]
                
                if p & 1:
                    if p & 2 != x & 2:
                        if shifts[(i + 2) % 4] and board[shifts[(i + 2) % 4][0]] & 1 == 0:
                            return eval - 15
                    else:
                        eval += 5
                        if shifts[(i + 2) % 4] and board[shifts[(i + 2) % 4][0]] & 2 == x & 2:
                            eval += 5
                else:
                    if checkers_n_to_xy(shift[0])[1] == 7 * ((x & 2) >> 1):
                        eval += 20
        
        return eval
    
    import copy
    def checkers_copy_board(board = None):
        return copy.copy(board or checkers.field)
    
    def checkers_ai_test_turn(f, party, first = True, turns = None, takes = None, cleaned = False, real_f = None, king = None, depth = 0):
        if real_f is None:
            real_f = f
        
        n = checkers.field[real_f]
        
        if king is None:
            king = (checkers_n_to_xy(f)[1] == 7 * party) or (n & 4) >> 2
    
        turns = turns or []
        
        if takes is None:
            takes = []
        else:
            takes = list(takes)
        
        #print("king", king)
        pos_turns = checkers_gen_turns(f, first, party = party, king = king)
        #print("turns", pos_turns)
        
        ntk = False
        ld = depth
        
        
        if len(pos_turns) == 0:
            #print("No turns")
            return [], False, ld
        else:
            for turn in pos_turns:
                if type(turn) == tuple:
                    nt = list(takes)
                    for take in turn[1]:
                        ntt = (take, checkers.field[take])
                        if ntt in takes:
                            del nt[:]
                            break
                        elif ntt in nt:
                            break
                        else:
                            nt.append(ntt)
                    else:
                        
                        king = king or (checkers_n_to_xy(turn[0])[1] == 7 * party)
                        if first:
                            atakes = checkers_check_board([], party, selected = f)
                        else:
                            atakes = ()
                        
                        
                        turns, ntk, ld = checkers_ai_test_turn(turn[0], False, party, turns, nt, cleaned, real_f = real_f, king = (checkers_n_to_xy(turn[0])[1] == 7 * party) or (n & 4) >> 2, depth = depth + 1)
                        ntk = ntk or not (depth < ld, len(nt) > 0)
                        #print("ntk", ntk)
                        
                        if not ntk:
                            turns.append([real_f, turn[0], n & 4 + king] + nt)
                            #print("New Takes!")
                            ntk = True
                        #else:
                            #print("len", len(nt))
                        
                        for atake in atakes:
                            nt.append((atake, checkers.field[atake]))
                        
                else:
                    king = king or checkers_n_to_xy(turn)[1] == 7 * party
                    turns.append([real_f, turn, n & 4 + king])
        return turns, ntk, ld
    
        
    def checkers_eval_turn(turn):
        eval = 0
        for take in turn[2:]:
            eval += 10 * ((turn[1] & 4) >> 1) #Kings give more eval than men
        
        eval += checkers_pos_eval(turn[1])
        
        ##print(eval)
        return eval
    
    def checkers_do(turn, board = None, left_pieces = None):
        board = board or checkers.field
        left_pieces = left_pieces or checkers.left_pieces
        
        #print(turn)
        
        board[turn[0]], board[turn[1]] = board[turn[1]], board[turn[0]]
        for take in turn[3:]:
            party = (take[1] & 2) >> 1
            
            board[take[0]] = 0
            left_pieces[party] -= 1
        
        if turn[2]:
             board[turn[1]] |= 4
        
                
    
    def checkers_undo(turn, board = None, left_pieces = None):
        board = board or checkers.field
        left_pieces = left_pieces or checkers.left_pieces
        
        board[turn[0]], board[turn[1]] = board[turn[1]], board[turn[0]]
        for take in turn[3:]:
            party = (take[1] & 2) >> 1
            
            board[take[0]] = take[1]
            left_pieces[party] += 1
        
        if turn[2] & 1 == 1 and turn[2] & 4 == 0:
             board[turn[0]] -= 4
    
        
    
    def checkers_move(f, t, takes = False, board = None):
        board = board or checkers.field
        
        if type(t) == tuple:
            t = t[0]
        
        board[f], board[t] = board[t], board[f]
        party = (board[t] & 2) >> 1
        x, y = checkers_n_to_xy(t)
        
        if y == 7 * party:
            board[t] |= 4
        
        checkers.possible_turns = takes and checkers_gen_turns(t, False, board) or []
        checkers.possible_turns = filter(lambda x: type(x) == tuple, checkers.possible_turns)
        
        checkers.multiturn = len(checkers.possible_turns) > 0
        
        if checkers.multiturn:
            return t, takes
        else:
            return None, takes
    
    def checkers_take(n, board = None, left_pieces = None):
        left_pieces = left_pieces or checkers.left_pieces
        board = board or checkers.field
        
        i = board[n]
        party = (i & 2) >> 1
        
        i = 0
        left_pieces[party] -= 1
        board[n] = i
    
    def checkers_debug_setState():
        new_state = renpy.invoke_in_new_context(renpy.input, _("Input the state ID"), allow = "0123456789-")
        new_state = int(new_state)
        checkers.state = new_state 
        renpy.call("mg_checkers_s_comment", new_state)
    
    def checkers_debug_restartScheme():
        scheme = renpy.invoke_in_new_context(renpy.input, _("Input the scheme ID"), allow = "0123456789-")
        scheme = int(scheme)
        checkers(True, scheme = scheme)
    
    
image checkers_selected:
    "mod_assets/images/minigames/checkers_selected.png"
    zoom 0.75
image checkers_move:
    "mod_assets/images/minigames/checkers_takeable.png"
    zoom 0.75
image checkers_takeable:
    "mod_assets/images/minigames/checkers_takeable.png"
    zoom 0.75
    alpha 0.75
    
image checkers_cursor:
    im.MatrixColor("mod_assets/images/minigames/checkers_selected.png",
    (0, 0, 0, 0, 0,
    0, 0, 0, 0, 1,
    0, 1, 0, 0, 0,
    0, 0, 0, 1, 0))
    alpha 0.5
    zoom 0.75

image checkers_manW:
    "mod_assets/images/minigames/checkers_manW.png"
    zoom 0.75
image checkers_manB:
    "mod_assets/images/minigames/checkers_manB.png"
    zoom 0.75
image checkers_kingW:
    "mod_assets/images/minigames/checkers_kingW.png"
    zoom 0.75
image checkers_kingB:
    "mod_assets/images/minigames/checkers_kingB.png"
    zoom 0.75

image checkers_board = im.Flip("mod_assets/images/minigames/checkerboard.png", True)

screen mg_checkers_board(selected = False, takeables = None): #8x8 board with 75x75 cells
    add "paper" xalign 0.5 xzoom 1.1
    add "checkers_board" xalign 0.65 yalign 0.5
    
    vbox:
        pos 1045, 80
        spacing 46
        
        for i in range(1, 9):
            text str(i) style "choice_button_text" color "#000"
    
    hbox:
        pos 475, 36
        spacing 58
        
        for i in "HGFEDCBA":
            text i style "choice_button_text" color "#000"
    
    if takeables:
        for t in takeables:
            if type(t) == tuple:
                add "checkers_move" pos checkers_n_to_xy(t[0], 75, -75, 442, 585)
                add "checkers_takeable" pos checkers_n_to_xy(t[0], 75, -75, 442, 585)
            elif t is not None:
                add "checkers_move" pos checkers_n_to_xy(t, 75, -75, 442, 585)
    
    if selected:
        add "checkers_selected" pos checkers_n_to_xy(selected, 75, -75, 442, 585)
    

screen mg_checkers_scr():
    layer "master"
    zorder 100
    
    python:
        from math import sqrt
        sc = 0.8
        diag_sc = sqrt(sc*sc * 2)

    use mg_checkers_board(checkers.selected, checkers.possible_turns)
    
    for y in range(8):
        for x in range(0, 8):
            $p = (442 + x * 75, 585 - y * 75)
            $n = checkers_xy_to_n(x, y)
            $i = checkers_cell(n)
            
            button:
                background None
                pos p
                xysize (70, 70)
                anchor (0, 0)
                hover_background "checkers_cursor"
                keyboard_focus True
                action Function(checkers_click, n)
            
            if i & 1:
                add checkers_sprite(i) pos p
            
                    
    vbox:
        pos (205, 85)
        spacing 5
        
        python:
            base_piece_str = "X" * 6 + "\n" + "X" * 6
            piece_str = [12 - checkers.left_pieces[0], 12 - checkers.left_pieces[1]]
            for i in range(2):
                if piece_str[i] > 8:
                    piece_str[i] += 1
            piece_str[0] = "{color=#f00}" + base_piece_str[:piece_str[0]] + "{/color}" + base_piece_str[piece_str[0]:]
            piece_str[1] = "{color=#6acdcd}" + base_piece_str[:piece_str[1]] + "{/color}" + base_piece_str[piece_str[1]:]
            
            def r_score(s):
                if s & 1:
                    return str(s / 2) + ".5"
                return str(s / 2)
            
        
        text "[s_name]: " + r_score(checkers.score[0]) style s_text_style():
            if not checkers.playerTurn:
                color "#6acdcd"
        text piece_str[0] color "#ccc" xsize 60  style s_text_style()
        text "[player]: " + r_score(checkers.score[1]) style s_text_style():
            if checkers.playerTurn:
                color "#f00"
        text piece_str[1] color "#ccc" xsize 60 style s_text_style()
    vbox:
        style_prefix "choice"
        yalign 0.99
        xanchor 0
        pos (205, 600)
        spacing 5
        
        textbutton _("Restart (R)") xpadding 0 xsize 200 keysym 'r' action [SetField(checkers, 'state', -2), Function(renpy.call, "mg_checkers_s_comment", -2)]
        textbutton _("Quit (Q)") xpadding 0 xsize 200 keysym 'q' action Jump("mg_checkers_quit")
        if config.developer:
            textbutton _("Restart without AI (Shift+R)") xpadding 0 xsize 200 keysym 'shift_R' action Function(checkers, True, ai = False)
            textbutton _("Restart with a debug scheme (Alt+R)") xpadding 0 xsize 200 keysym 'alt_R' action Function(checkers_debug_restartScheme)
            textbutton _("Set state") xpadding 0 xsize 200 action Function(checkers_debug_setState)

label mg_checkers:
    $justIsSitting = False
    show sayori 6aaaa at ss1i
    call screen mg_checkers_scr() nopredict
    return

label mg_checkers_s_comment(id = 0): #Sayori's comment; -1/1 = Sayori's victory/defeat, 2 = draw, -2 = restart, 3 = ask for a draw
    if id < 3:
        hide screen mg_checkers_scr
    
    
    if id == -1:
        $randId = renpy.random.randint(0, 2)
        if randId == 0:
            s 6aaca "Okay, I win this game."
            s "You should have a better strategy next time."
        elif randId == 1:
            s 6acaa "Uh, you have no more turns."
            s "Just work on your tactics and try again."
        else:
            s 6acaa "Don't worry!"
            s "Maybe you'll win next time."
    elif id == 1:
        $randId = renpy.random.randint(0, 1)
        if randId == 0:
            s 6aaca "Okay, you win!"
            s 6aeca "Next time I'll be more crafty."
        else:
            s 6aebb "You have just smashed all my army."
            s 6aaaa "You seem to be more clever than me."
            s "Next time I'll try harder."
    elif id == 2:
        $randId = renpy.random.randint(0, 2)
        if randId == 0:
            s 6acaa "This battle ended up without any result..."
            s "Despite the talent of both the commanders."
            s "But the war seems to go on, doesn't it?"
        elif randId == 1:
            s 6acaa "I'm surprised as much as you are."
            s "So, let's just share the point."
        else:
            s 6acab "If checkers is a battle simulator, than draw game is the worse game!"
            s "Because so much people died but their sacrifice is absolutely vain after all."
            s "But maybe, the next one won't be so."
    elif id == -2:
        $randId = renpy.random.randint(0, 1)
        if randId == 0:
            s 6acab "Are you giving up?"
            s 6aaaa "Then we'll start again, but I'll get a point for this game."
        else:
            s 6acaa "What's up, [player]?"
            s "Do you think, you'll lose?"
            s 6aaca "Or you just want to do a honorable thing?"
            s 6acaa "Anyway, according to the game rules, you lose this game."
            s "But maybe, you'll will win me next time."
    else:
        pause 1.5
        hide screen mg_checkers_scr
        
        s 8abaa "Don't you think, that this game is going to be endless?"
        menu:
            s "I think you should take a draw, shouldn't you?"
            
            "Yes":
                $checkers.state = 2
                call mg_checkers_s_comment(2)
            "No":
                $checkers.state = 0
                $checkers.asked_for_a_draw = True
                jump mg_checkers
    
    python:
        if id < 0:
            checkers_wf(id)
            checkers.score[0] += 2
        elif id == 1:
            checkers_wf(1)
            checkers.score[1] += 2
        else:
            checkers.score[0] += 1
            checkers.score[1] += 1
        checkers(True)
    
    return

label mg_checkers_s_turn:
    python:
        if checkers.with_ai and len(checkers.unblocked[1]):
            randTime = renpy.random.triangular(0.25, 2)
            renpy.pause(randTime)
            checkers_ai_turn()
    pause 0.25
    return
    
label mg_checkers_quit:
    hide screen mg_checkers_scr
    $show_s_mood(ss1)
    with dissolve
    python:
        justIsSitting = True
        if checkers.score[0] > checkers.score[1]:
            s_mood = 'vh'
        else:
            s_mood = 'h'
    return
