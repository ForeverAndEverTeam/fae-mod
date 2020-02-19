#Checkers/Draughts (Russian variant)
default persistent.checkers_winfactor = 30

init 10 python:
    ## Board & board generation
    ## Each integer in self.board (the board itself) storages the below flags (0/1):
    ## One integer = one black cell, starting from the left-upper corner
    ## 1 = free/occupied
    ## 2 = white(Sayori's) / black(Player's)
    ## 4 = man/king
    ## 8 = unselected/selected
    def checkers_gen_board(scheme = 0):
        if scheme == 0: #Standard scheme
            f = [0] * 32
            for i in range(12):
                f[i] = 3
                f[31 - i] = 1
            return f
        elif scheme == 1: #White pieces are close to black. Made for taking test.
            f = [0] * 32
            for i in range(12):
                f[i] = 3
            f[13] = 1
            return f
        elif scheme == 2: #Black pieces behind the king line and white pieces after a line
            f = [0] * 32
            for i in range(24, 28):
                f[i] = 3
            for i in range(16, 20):
                f[i] = 1
            return f
        elif scheme == 3: #Black pieces behind the king line and 2 rows of white pieces
            f = [0] * 32
            for i in range(24, 28):
                f[i] = 3
            for i in range(20, 24):
                f[i] = 1
                f[i-8] = 1
            return f
        raise ValueError("Checkers start scheme %s not found" % scheme)

    def checkers_prep(self, restart = False, *args, **kwargs):
        self.board = checkers_gen_board(kwargs.get("scheme") or 0)
        
        self.players_turn = True # player plays as black while Sayori plays as white
        
        self.state = 0 #0 = game not over, 1 = black wins, -1 = white wins, -2 = restart, 2 = draw game
        self.left_pieces = [12, 12] #0 - player's, 1 - Sayori's
        self.with_ai = kwargs.get('ai') if 'ai' in kwargs else True
        
        self.selected = None
        checkers.moving = False #Is the current player moving
        checkers.selectable = []
        checkers.unblocked = ([], [])
        checkers.asked_for_a_draw = False
        
        self.possible_moves = []
        self.mandatory_take = False
        self.did_take = False #If the selected piece has already taken a piece in the current turn
        
        checkers.PARTY_PLAYER = 1 #The player's (black) party ID
        checkers.PARTY_SAYORI = 0 #The Sayori's (white) party ID
        
        if not restart:
            self.score = [0, 0] #score[0] = Sayori's score (); score[1] = Player's score; 2 = 1 real point, 1 = half real point
        checkers_check_board(checkers_cur_party())
    
    ## Get cell #n's position
    def checkers_n_to_xy(n, sx = 1, sy = None, ox = 0, oy = 0):
        x = (n & 3) << 1
        y = n >> 2
        if n & 7 > 3:
            x += 1
        return ox + x * sx, oy + y * (sy or sx)
    
    ## Get the index of the black cell at {x;y}
    ## Returns None if the cell is white
    def checkers_xy_to_n(x, y):
        if y & 1:
            x -= 1
        if x & 1:
            return None # white cells are not in checkers.board
        return (y << 2) + (x >> 1)
    
    ## Get the content of a cell
    ## If y is defined, returns the cell at {x;y}
    ## Otherwise, returns checkers.board[x]
    def checkers_cell(x, y = None):
        if not (y is None):
            try:
                return checkers.board[checkers_xy_to_n(x, y)]
            except IndexError:
                return 0
        elif not x is None:
            return checkers.board[x]
        return 0
    
    ## Get a piece's sptite name
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
    
    #Get new cell number after move to {x+ox;y+oy} and ox and oy
    def checkers_get_shift(n, ox, oy):
        x, y = checkers_n_to_xy(n)
        x += ox
        y += oy
        
        if x < 0 or x > 7 or y < 0 or y > 7: #Check if the destination point is on the board
            return None #Stop performing here
        
        n += 4 * oy #Move horizontally
        #Correct ox deviation for even rows
        if y & 1:
            if ox > 0:
                ox -= (abs(oy) >> 1) + 1
        else:
            if ox < 0:
                ox += (abs(oy) >> 1) + 1
        n += ox
        
        return n
    
    #Turn info class
    class CheckersMove:
        def __init__(self, who, start, final, takes = None, based_on = None, king = False):
            self.performer = who
            self.start = start #Start cell
            self.final = final #Desination cell
            if based_on:
                self.start = based_on.start
                self.intermediate_jumps = based_on.intermediate_jumps + [based_on.final]
                self.takes = based_on.takes + takes #Taken pieces' positions
                self.gets_king = based_on.gets_king
            else:
                self.intermediate_jumps = []
                self.takes = takes or [] #Taken pieces' positions
            self.taken_pieces = [checkers.board[x] for x in self.takes] #Taken pieces' backup
            if not ("gets_king" in self.__dict__ and self.gets_king):
                self.gets_king = not king and ((who == checkers.PARTY_PLAYER and final > 27) or (who == checkers.PARTY_SAYORI and final < 4))
        
        def __str__(self):
            sep = "x" if self.performer else "-" #Cell separator. 'x' for the player, '-' for Sayori
            note = str(self.start) #Turn note
            for jump in self.intermediate_jumps:
                note += sep + str(jump)
            note += sep + str(self.final)
            return note
        
        def extend(self, cur_piece = None):
            cur_piece = cur_piece or checkers.board[self.start]
            move_list = []
            new_moves = checkers_gen_moves(self.final, self, None, True, cur_piece, self.takes)
            if len(new_moves):
                for move in new_moves:
                    cp = cur_piece
                    if move.gets_king:
                        cp |= 4 #Set the king flag
                    print(move)
                    move_list += move.extend(cp)
            else:
                move_list.append(self)
            return move_list
            
        
        def perform(self, jump = None):
            start = self.start
            if jump is not None:
                start = self.intermediate_jumps[jump]
            checkers.board[self.final] = checkers.board[start]
            if self.gets_king:
                checkers.board[self.final] |= 4 #Remove the king flag
            checkers.board[start] = 0
            for taken in self.takes[jump or 0:]:
                checkers.board[taken] = 0
            if len(self.takes):
                checkers.possible_moves = checkers_gen_moves(self.final, self, takes_only = True)
                return len(checkers.possible_moves) == 0
            else:
                checkers.possible_moves = []
                return True
        
        def undo(self):
            for taken in range(len(self.takes)):
                checkers.board[self.takes[taken]] = self.taken_pieces[taken]
            checkers.board[self.start] = checkers.board[self.final]
            checkers.board[self.final] = 0
            if self.gets_king:
                checkers.board[self.start] &= 11
            
    
    #Return all the possiable turns for a certian piece
    def checkers_gen_moves(n, based_on = None, initial_dir_y = None, takes_only = False, cur_piece = None, ignore_cells = None):
        moves = []
        x, y = checkers_n_to_xy(n)
        cur_piece = cur_piece or checkers_cell(n)
        ignore_cells = ignore_cells or ()
        party = (cur_piece & 2) >> 1
        dir_y = initial_dir_y or (1 if party else -1)
        is_king = (cur_piece & 4) >> 2
        
        deviations = [-1, 1] #diagonal deviations, left & right
        for d in deviations:
            i = 0
            pos = checkers_get_shift(n, d, dir_y)
            if pos is None:
                continue
            cell = checkers_cell(pos)
            last_taken = None #last piece, that could be taken
            #do the below loop while shift is on the borad & is not ally's cell
            #Additional condition for men: i == 0 or last_taken is not None (cuts the line length to 1) 
            while(not (pos is None or cell is None or (cell & 3) == (cur_piece & 3)) and (is_king or last_taken or i == 0)):
                ignored = pos in ignore_cells
                empty = cell & 1 == 0 or ignored
                
                if last_taken:
                    if empty:
                        moves.append(CheckersMove(checkers_cur_party(), n, pos, [last_taken], based_on, is_king))
                    elif not is_king:
                        break
                    last_taken = None
                else:
                    if not (empty or (cell & 2) >> 1 == party):
                        last_taken = pos
                    elif empty and not (based_on or checkers.mandatory_take or takes_only):
                        moves.append(CheckersMove(checkers_cur_party(), n, pos, king = is_king))
                        if not is_king:
                            break
                pos = checkers_get_shift(pos, d, dir_y)
                cell = checkers_cell(pos)
                i += 1
        if (not initial_dir_y): #if not initial_dir_y == True, then the call is not nested
            moves += checkers_gen_moves(n, based_on, -dir_y, not is_king or takes_only, cur_piece, ignore_cells) #add backward checks in this case
        return moves

    def checkers_cur_party():
        return checkers.PARTY_PLAYER if checkers.players_turn else checkers.PARTY_SAYORI
    
    def checkers_win_factor_alter(alter):
        persistent.checkers_winfactor += alter
        if persistent.checkers_winfactor < 0:
            persistent.checkers_winfactor = 0
        elif persistent.checkers_winfactor > 59:
            persistent.checkers_winfactor = 59
    
    def checkers_check_state():
        unblocked_lens = tuple(len(x) for x in checkers.unblocked)
        
        men, kings = ([], []), ([], [])
        
        for i in checkers.board:
            party = (i & 2) >> 1
            if i & 4:
                kings[party].append(i)
            else:
                men[party].append(i)
        
        if not checkers.asked_for_a_draw and any(len(x) == 0 for x in men): #If Sayori hasn't asked for a draw & any party has no man
            return 3
        elif unblocked_lens[checkers.PARTY_PLAYER] == 0:
            if unblocked_lens[checkers.PARTY_SAYORI] == 0:
                return 2
            else:
                return 1
        elif unblocked_lens[checkers.PARTY_SAYORI] == 0:
            if unblocked_lens[checkers.PARTY_PLAYER] == 0:
                return 2
            else:
                return -1
        
        return 0
    
    def checkers_check_board(party):
        board_range = range(32)
        pm = [None] * 32 #All possible moves
        
        if checkers.selected is not None:
            board_range.remove(checkers.selected)
        
        #Clean unblocked lists
        del checkers.unblocked[checkers.PARTY_PLAYER][:]
        del checkers.unblocked[checkers.PARTY_SAYORI][:]
        
        for i in board_range:
            n = checkers.board[i]
            piece_party = (n & 2) >> 1
            if n & 1: #If the cell is occupied by a piece
                moves = checkers_gen_moves(i)
                if len(moves):
                    pm[i] = moves
                else:
                    continue
                checkers.unblocked[piece_party].append(i)
            else:
                checkers.board[i] = 0
        checkers.selectable = []
        for i in checkers.unblocked[party]:
            has_takes = False
            for move in pm[i]:
                if len(move.takes):
                    has_takes = True
                    checkers.mandatory_take = True
                    break
            if has_takes or not checkers.mandatory_take:
                checkers.selectable.append(i)
    
    def checkers_get_depth(): #Get the depth value, used by the AI for move prediction
        return 1 + persistent.checkers_winfactor // 15
    
    def checkers_select(n):
        if n is None or checkers.board[n] & 1 == 0: #If the player tries to select an empty cell or n is None
            checkers.selected = None
        else:
            #Unselect the previously selected cell
            if checkers.selected is not None:
                checkers.board[checkers.selected] ^= 8
                checkers.possible_moves = []
            #Select the new one
            checkers.board[n] += 8
            checkers.possible_moves = checkers_gen_moves(n)
            checkers.selected = n
    
    def checkers_finish_turn():
        checkers_select(None)
        checkers.players_turn = not checkers.players_turn
        checkers.moving = False
        checkers.mandatory_take = False
        checkers_check_board(checkers_cur_party())
        checkers.state = checkers_check_state()
        if checkers.state == 0 and not checkers.players_turn and checkers.with_ai:
            renpy.call_in_new_context('mg_checkers_ai_turn')
        elif checkers.state != 0:
            renpy.invoke_in_new_context(renpy.pause, 1.5)
            renpy.call('mg_checkers_s_comment', checkers.state)
            
    
    def checkers_click(n):
        moved = False
        for i in checkers.possible_moves:
            if n == i.final:
                if i.perform(-1 if len(i.intermediate_jumps) else None): #Perform the move and do the below things only if the turn is over
                    checkers_finish_turn()
                else:
                    checkers.moving = True
                moved = True
        if not (moved or checkers.moving) and n in checkers.selectable:
            checkers_select(n)
    
    def checkers_ai_turn():
        if len(checkers.unblocked[checkers.PARTY_SAYORI]) > 0:
            moves = checkers_best_move(checkers.PARTY_SAYORI, checkers_get_depth())[1]
            move = renpy.random.choice(moves)
            move.perform()
        checkers_finish_turn()

    
    def checkers_best_move(party, depth = None, last_move = None, alpha = float("-inf"), beta = float("inf")):
        if depth == 0:
            if not last_move:
                raise ValueError("last_move can't be None")
            else:
                alpha = checkers_eval(last_move.performer)
            return alpha, ()
        
        moves = []
        best_moves = []
        
        for i in checkers.unblocked[party]:
            for move in checkers_gen_moves(i):
                moves += move.extend()
        
        for move in moves:
            if alpha >= beta:
                break
            
            move.perform()
            checkers.players_turn = not checkers.players_turn
            recursion_result = checkers_best_move(checkers_cur_party(), depth - 1, -beta, -alpha)
            total_eval = -recursion_result[0]
            if total_eval > alpha:
                best_moves = [move]
                alpha = total_eval
            elif total_eval == alpha:
                best_moves.append(move)
            move.undo()
            checkers.players_turn = not checkers.players_turn
            checkers.mandatory_take = False
            checkers_check_board(checkers_cur_party())
        return alpha, best_moves
            
    
    def checkers_eval(party):
        eval = 0
        for cell in checkers.board:
            if cell & 1 != 0:
                piece_party = (cell & 2) >> 1
                m = 1 if piece_party == party else -1
                if cell & 4:
                    m *= 3
                eval += m
        return eval
    
    import copy
    def checkers_copy_board(board = None):
        return copy.copy(board or checkers.field)
    
    
    def checkers_debug_setState():
        new_state = renpy.invoke_in_new_context(renpy.input, _("Input the state ID"), allow = "0123456789-")
        new_state = int(new_state)
        checkers.state = new_state 
        renpy.call("mg_checkers_s_comment", new_state)
    
    def checkers_debug_restartScheme():
        scheme = renpy.invoke_in_new_context(renpy.input, _("Input the scheme ID"), allow = "0123456789-")
        scheme = int(scheme)
        checkers(True, scheme = scheme)
    
    ## Add this game to the minigame list
    checkers = minigame(_("Checkers"), 'mg_checkers', checkers_prep)
    mg_list.append(checkers)
    
    
image checkers_selected:
    "mod_assets/images/minigames/checkers_selected.png"
    zoom 0.75
image checkers_move:
    "mod_assets/images/minigames/checkers_takeable.png"
    zoom 0.75
image checkers_takeable:
    im.MatrixColor("mod_assets/images/minigames/checkers_selected.png",
    (1, 1, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0.75, 0))
    zoom 0.75
    
image checkers_cursor:
    im.MatrixColor("mod_assets/images/minigames/checkers_selected.png",
    (0, 0, 0, 0, 0,
    0, 0, 0, 0, 1,
    0, 1, 0, 0, 0,
    0, 0, 0, 0.5, 0))
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

screen mg_checkers_board(): #8x8 board with 75x75 cells
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
    
    if checkers.selected:
        for move in checkers.possible_moves:
            add "checkers_move" pos checkers_n_to_xy(move.final, 75, -75, 442, 585)
            for take in move.takes:
                add "checkers_takeable" pos checkers_n_to_xy(take, 75, -75, 442, 585)
        add "checkers_selected" pos checkers_n_to_xy(checkers.selected, 75, -75, 442, 585)

screen mg_checkers_scr():
    layer "master"
    zorder 100
    
    python:
        from math import sqrt
        sc = 0.8
        diag_sc = sqrt(sc*sc * 2)

    use mg_checkers_board()
    
    for y in range(8):
        for x in range(0, 8):
            $p = (442 + x * 75, 585 - y * 75)
            $n = checkers_xy_to_n(x, y)
            $i = checkers_cell(n)
            
            #Add a selection button
            if checkers.players_turn or not checkers.with_ai:
                button:
                    background None
                    pos p
                    xysize (70, 70)
                    anchor (0, 0)
                    hover_background "checkers_cursor"
                    keyboard_focus True
                    action Function(checkers_click, n)
            
            #Draw the piece sprite
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
            if not checkers.players_turn:
                color "#6acdcd"
        text piece_str[0] color "#ccc" xsize 60  style s_text_style()
        text "[player]: " + r_score(checkers.score[1]) style s_text_style():
            if checkers.players_turn:
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
            checkers_win_factor_alter(id)
            checkers.score[0] += 2
        elif id == 1:
            checkers_win_factor_alter(1)
            checkers.score[1] += 2
        else:
            checkers.score[0] += 1
            checkers.score[1] += 1
        checkers(True)
    
    return

label mg_checkers_ai_turn:
    python:
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
