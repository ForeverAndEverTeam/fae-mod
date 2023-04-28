#Reversi/Othello
default persistent.reversi_winfactor = 30

init 10 python:
    #Convert functions
    #y >> 3 = y // 8, y << 3 = y * 8 (for bitwise-ops newbies)
    def reversi_n_to_xy(n, sx = 1, sy = None, ox = 0, oy = 0):
        y = n >> 3
        x = n & 7 #n % 8
        return (x * sx + ox, y * (sy or sx) + oy)
    def reversi_xy_to_n(x, y):
        return (y << 3) + x
                
    ## Board generation
    ## Each of 64 integers in `board` storages a cell's state:
    ##   0 = free
    ##   1 = white (Sayori's)
    ##   3 = black (Player's)
    def reversi_gen_board(scheme = 0):
        if scheme == 0: #Standard scheme
            b = [0] * 64
            #Initial disks
            b[27] = 3
            b[28] = 1
            b[35] = 1
            b[36] = 3
            return b
        raise ValueError("Reversi start scheme %s not found" % scheme)

    def reversi_prep(self, restart = False, *args, **kwargs):
        self.board = reversi_gen_board(kwargs.get("scheme") or 0)
        self.players_turn = True #Player always moves first
        self.state = 0 #0 = game not over, 1 = black wins, -1 = white wins, -2 = restart, 2 = draw game
        self.occupied_cells = [2, 2] #0 - Sayori's score; 1 - Player's score
        self.with_ai = kwargs.get('ai') if 'ai' in kwargs else True
        if not restart:
            self.score = [0, 0] #0 - Sayori's score; 1 - Player's score
        reversi_check_board(1)
        self.last_move = None
        self.no_moves = False
    
    ## Get the content of a cell
    ## If y is defined, returns the cell at {x;y}
    ## Otherwise, returns reversi.board[x]
    def reversi_cell(x, y = None):
        if not (y is None):
            try:
                return reversi.board[reversi_xy_to_n(x, y)]
            except IndexError:
                return 0
        elif not (x is None):
            try:
                return reversi.board[x]
            except IndexError:
                return 0
    
    ## Get a disks's sptite name
    def reversi_sprite(info):
        n = "reversi_" #Man piece sprites used
        if info == 3:
            n += 'black'
        else:
            n += 'white'
        return n
    
    ## Calculate the trajectory and distance (in cells) between two cells ((degree % 45)=0)
    def reversi_trajectory(a, b):
        a, b = tuple(reversi_n_to_xy(a)), tuple(reversi_n_to_xy(b))
        dx, dy = b[0]-a[0], b[1]-a[1]
        adx, ady = abs(dx), abs(dy)
        dist = max(adx, ady)
        try:
            dx, dy = dx//adx, dy//ady
        except:
            if dx == 0:
                return 0, dy//ady, dist
            return dx//adx, 0, dist
        return dx, dy, dist
    ##Reverse a disk's color
    def reversi_reverse(info):
        if info == 1:
            return 3
        elif info == 3:
            return 1
        return 0
    
    #Turn info class
    class ReversiMove:
        def __init__(self, who, cell, mate_cells):
            self.performer = who
            self.cell = cell #Cell where a new disk is placed
            self.mate_cells = mate_cells #Cells with disks that make a take line with the new disk
            self.undone = False
        
        def __str__(self):
            # Used for Reversi Notation Files (.rnf), an original format for Reversi logs/saves
            # See its specification in ../FileSpefications.md
            note = str(self.cell) + ":"
            note += ",".join(str(i) for i in self.mate_cells)
            return note
            
        def unite(self, other):
            for mate in other.mate_cells:
                self.mate_cells.add(mate)
        
        def perform(self, jump = None):
            cell = self.cell
            cell_x,cell_y = reversi_n_to_xy(cell)
            reversi.board[cell] = (self.performer << 1) + 1
            new_cells = 1
            enemy = 0 if self.performer else 1
            for mate in self.mate_cells:
                dx, dy, dist = reversi_trajectory(cell, mate)
                x, y = cell_x, cell_y
                for i in range(dist-1):
                    x += dx
                    y += dy
                    n = reversi_xy_to_n(x, y)
                    info = reversi_cell(n)
                    reversi.board[n] = reversi_reverse(info)
                    reversi.occupied_cells[enemy] -= 1
                new_cells += dist - 1
            reversi.occupied_cells[self.performer] += new_cells
            self.undone = False
            #print (True, self.cell, reversi_n_to_xy(self.cell))  
        
        def undo(self):
            if self.undone:
                raise ValueError("Can't undo undone move")
            cell = self.cell
            cell_x,cell_y = reversi_n_to_xy(cell)
            restored_cells = 1
            enemy = 0 if self.performer else 1
            for mate in self.mate_cells:
                dx, dy, dist = reversi_trajectory(cell, mate)
                x, y = cell_x, cell_y
                for i in range(dist-1):
                    x += dx
                    y += dy
                    n = reversi_xy_to_n(x, y)
                    info = reversi_cell(n)
                    reversi.board[n] = reversi_reverse(info)
                    reversi.occupied_cells[enemy] += 1
                restored_cells += dist - 1
            reversi.board[cell] = 0
            reversi.occupied_cells[self.performer] -= restored_cells
            self.undone = True
            #print (False, self.cell, reversi_n_to_xy(self.cell))
        
        def get_cost(self): #Get the turn's cost (positional evaluation + taken pieces' cost)
            cost = riversi_pos_eval(self.final, reversi_cell(self.start))
            for mate in self.mate_cells:
                dx, dy, dist = reversi_trajectory(self.cell, mate)
                cost = 10 * (dist-1)
            return cost
            
    
    #Return all the possiable turns with a certian disk as a mate
    def reversi_gen_moves(n, party = None):
        moves = []
        x, y = reversi_n_to_xy(n)
        cur_disk = reversi_cell(n)
        disk_party = (cur_disk & 2) >> 1
        if cur_disk & 1 != 0 and (party is None or disk_party == party):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    ix, iy = x, y
                    dist = 0
                    while True:
                        ix += dx
                        iy += dy
                        dist += 1
                        i = reversi_xy_to_n(ix, iy)
                        if i > 63 or ix > 7 or ix < 0 or iy > 7 or iy < 0:
                            break
                        info = reversi.board[i]
                        if info == 0:
                            if dist > 1:
                                moves.append(ReversiMove(disk_party, i, {n}))
                            break 
                        elif info == cur_disk:
                            break
        return moves
    
    #Return all the possiable turns
    def reversi_all_moves(party):
        all_moves = [None] * 64
        for i in range(64):
            moves = reversi_gen_moves(i, party)
            for move in moves:
                k = move.cell
                if all_moves[k] is None:
                    all_moves[k] = move
                else:
                    all_moves[k].unite(move)
        return all_moves
    
    def reversi_cur_party():
        return 1 if reversi.players_turn else 0
    
    def reversi_win_factor_alter(alter):
        persistent.reversi_winfactor += alter
        if persistent.reversi_winfactor < 0:
            persistent.reversi_winfactor = 0
        elif persistent.reversi_winfactor > 59:
            persistent.reversi_winfactor = 59
    
    def reversi_check_state():
        oc = reversi.occupied_cells
        if sum(oc) >= 64 or reversi.no_moves:
            if oc[1] > oc[0]:
                return 1
            elif oc[1] == oc[0]:
                return 2
            else:
                return -1
        return 0
    
    def reversi_check_board(party):
        reversi.selectable = reversi_all_moves(party)
    
    def reversi_get_depth(): #Get the depth value, used by the AI for move prediction
        return 1 + persistent.reversi_winfactor // 15
    
    def reversi_select(n):
        if n is None or reversi.board[n] != 0: #If the player tries to select a full cell or n is None
            reversi.selected = None
        elif not (n < 0 or n > 63):
            reversi.selected = n
    
    def reversi_finish_turn(check_state = True, skipped = False):
        reversi_select(None)
        reversi.players_turn = not reversi.players_turn
        reversi_check_board(reversi_cur_party())
        if check_state:
            reversi.state = reversi_check_state()
            if reversi.state == 0 and not reversi.players_turn and reversi.with_ai:
                renpy.call_in_new_context('mg_reversi_ai_turn')
            elif reversi.state != 0:
                renpy.invoke_in_new_context(renpy.pause, 1.5)
                renpy.call('mg_reversi_s_comment', reversi.state)
                return None
        #Skip turn when there's no any move opportunity
        if not any(x is not None for x in reversi.selectable):
            if not skipped:
                reversi_finish_turn(check_state, True)
            else:
                reversi.no_moves = True
                reversi_finish_turn(True, True)
            
    
    def reversi_click(n):
        reversi_select(n)
        if not (reversi.selected is None or reversi.selectable[n] is None):
            reversi.selectable[n].perform()
            reversi_finish_turn()
    
    def reversi_ai_turn():
        moves = reversi_best_move(0, 1)[1]#reversi_get_depth())[1]
        if len(moves):
            move = renpy.random.choice(moves)
            reversi.last_move = move
            move.perform()
        reversi_finish_turn()

    
    def reversi_best_move(party, depth = None, alpha = -64, beta = 64):
        moves = filter(lambda x: x is not None, reversi.selectable)
        if len(moves) == 0 or depth == 0 or sum(reversi.occupied_cells) >= 64:
            alpha = reversi.occupied_cells[party] - reversi.occupied_cells[0 if party else 1]
            return alpha, ()
        
        best_moves = []
        for move in moves:
            if alpha >= beta:
                break
            move.perform()
            last_player = reversi.players_turn
            reversi_finish_turn(False)
            total_eval = 0
            if last_player != reversi.players_turn:
                recursion_result = reversi_best_move(reversi_cur_party(), depth - 1, -beta, -alpha)
                total_eval = -recursion_result[0]
            else:
                recursion_result = reversi_best_move(reversi_cur_party(), depth, alpha, beta)
                total_eval = recursion_result[0]
            if total_eval > alpha:
                best_moves = [move]
                alpha = total_eval
            elif total_eval == alpha:
                best_moves.append(move)
            move.undo()
            reversi_finish_turn(False)
        return alpha, best_moves
    
    import copy
    def reversi_copy_board():
        return copy.copy(reversi.field)
    
    
    def reversi_debug_setState():
        new_state = renpy.invoke_in_new_context(renpy.input, _("Input the state ID"), allow = "0123456789-")
        new_state = int(new_state)
        reversi.state = new_state 
        renpy.call("mg_reversi_s_comment", new_state)
    
    def reversi_debug_restartScheme():
        scheme = renpy.invoke_in_new_context(renpy.input, _("Input the scheme ID"), allow = "0123456789-")
        scheme = int(scheme)
        reversi(True, scheme = scheme)

    
    
image reversi_selectable:
    "mod_assets/images/minigames/checkers_selected.png"
    zoom 0.75
    
image reversi_cursor:
    
    im.MatrixColor("mod_assets/images/minigames/checkers_selected.png",
    (0, 0, 0, 0, 0,
    0, 0, 0, 0, 1,
    0, 1, 0, 0, 0,
    0, 0, 0, 0.5, 0))
    zoom 0.75

image reversi_white:
    "mod_assets/images/minigames/checkers_manW.png"
    zoom 0.75
image reversi_black:
    "mod_assets/images/minigames/checkers_manB.png"
    zoom 0.75

image reversi_board = "mod_assets/images/minigames/reversi_board.png"

screen mg_reversi_board(): #8x8 board with 75x75 cells
    add "paper" xalign 0.5 xzoom 1.1
    for move in reversi.selectable:
        if move is not None and (reversi.players_turn or config.developer):
            add "reversi_selectable" pos reversi_n_to_xy(move.cell, 75, -75, 442, 585)
    add "reversi_board" xalign 0.65 yalign 0.5
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

screen mg_reversi_scr():
    layer "master"
    zorder 100
    
    python:
        from math import sqrt
        sc = 0.8
        diag_sc = sqrt(sc*sc * 2)

    use mg_reversi_board()
    
    for y in range(8):
        for x in range(0, 8):
            $p = (442 + x * 75, 585 - y * 75)
            $n = reversi_xy_to_n(x, y)
            $i = reversi_cell(n)
            
            #Add a selection button
            if reversi.players_turn or not reversi.with_ai:
                button:
                    background None
                    pos p
                    xysize (70, 70)
                    anchor (0, 0)
                    hover_background "reversi_cursor"
                    keyboard_focus True
                    action Function(reversi_click, n)
            
            #Draw the piece sprite
            if i & 1:
                add reversi_sprite(i) pos p
            
                    
    vbox:
        pos (205, 85)
        spacing 5
        text "[s_name]: " + str(reversi.score[0]):# style s_text_style():
            if not reversi.players_turn:
                color "#6acdcd"
        text "[player]: " + str(reversi.score[1]):# style s_text_style():
            if reversi.players_turn:
                color "#f00"
        hbox:
            spacing 8
            text str(reversi.occupied_cells[0]) color "#6acdcd" xsize 60# style s_text_style()
            text ":" color "#000"# style s_text_style()
            text str(reversi.occupied_cells[1]) color "#f00" xsize 60# style s_text_style()
    vbox:
        style_prefix "choice"
        yalign 0.99
        xanchor 0
        pos (205, 600)
        spacing 5
        
        textbutton _("Restart (R)") xpadding 0 xsize 200 keysym 'r' action [SetField(reversi, 'state', -2), Function(renpy.call, "mg_reversi_s_comment", -2)]
        textbutton _("Quit (Q)") xpadding 0 xsize 200 keysym 'q' action Jump("mg_reversi_quit")
        if config.developer:
            textbutton _("Restart without AI (Shift+R)") xpadding 0 xsize 200 keysym 'shift_R' action Function(reversi, True, ai = False)
            textbutton _("Restart with a debug scheme (Alt+R)") xpadding 0 xsize 200 keysym 'alt_R' action Function(reversi_debug_restartScheme)
            textbutton _("Set state") xpadding 0 xsize 200 action Function(reversi_debug_setState)
            if reversi.last_move:
                if reversi.last_move.undone:
                    textbutton _("Redo (Z)") xpadding 0 xsize 200 keysym 'z' action Function(reversi.last_move.perform)
                else:
                    textbutton _("Undo (Z)") xpadding 0 xsize 200 keysym 'z' action Function(reversi.last_move.undo)

label mg_reversi:
    # $justIsSitting = False
    show sayori abhfaaa at t11
    call screen mg_reversi_scr() nopredict
    return

label mg_reversi_s_comment(id = 0): #Sayori's comment; -1/1 = Sayori's victory/defeat, 2 = draw, -2 = restart, 3 = ask for a draw
    pause 1.5
    hide screen mg_reversi_scr
    
    if id == -1: # Sayori wins
        $random_id = renpy.random.randint(0, 2)
        if random_id == 0:
            s ebbccea "Yay! I won this game!"
            s abgcaoa "Don't worry, you'll have better luck next time~"
        elif random_id == 1:
            s abgckda "Oh, the board is full."
            s "And you have less pieces."
            s abgcaoa "Well, maybe you'll have more next time!"
        else:
            s ebgccaa "Don't worry!"
            s "Maybe you'll win next time."
            s abagiia "You'll just have to watch out for my ultra smart moves~."
    elif id == 1: # Player wins
        $random_id = renpy.random.randint(0, 2)
        if random_id == 0:
            s abagaha "Okay, you win!"
            s gbagiaa "But know I'll be more crafty next time!"
        elif random_id == 1:
            s bbegboaj "Woah, you're better than me at this game."
            s "Maybe, I should pay more attention next round."
        else:
            s abagkgaj "Wait, you took more pieces than me!"
            s bbagciaj "I should probably be more attentive next time."
    elif id == 2: # Draw
        $random_id = renpy.random.randint(0, 1)
        if random_id == 0:
            s eahcaoa "Hey, we split the board in half!"
            s gahdkdaj "Unless I messed up my math."
            s abfdcoa "But a draw is also a result, isn't it?"
        else:
            s ebbcaoa  "Hey, we have the same number of pieces!"
            s ebgccqa "We really seem to have {i}soooooooooo{/i} much in common, ehehe~"
    elif id == -2: # Restart
        $random_id = renpy.random.randint(0, 1)
        if random_id == 0:
            s ebhfada "Are you giving up?"
            s abhfcaa "Ok, we'll start again, but I'll get a point for this game."
        else:
            s ebagaba "What's up, [player]?"
            s "Do you think you'll lose?"
            s ebagbca "Or do you just want to do a nice thing?"
            s abhfcaa "Anyways, according to the game rules, I'll get a point for this game."
            s "But maybe, you'll win next time."
    python:
        if id < 0:
            reversi_win_factor_alter(id)
            reversi.score[0] += 1
        elif id == 1:
            reversi_win_factor_alter(1)
            reversi.score[1] += 1
        else:
            reversi.score[0] += 1
            reversi.score[1] += 1
        reversi(True)
    
    return


label mg_reversi_ai_turn:
    python:
        randTime = renpy.random.triangular(0.25, 2)
        renpy.pause(randTime)
        reversi_ai_turn()
    pause 0.25
    return
    
label mg_reversi_quit:
    hide screen mg_reversi_scr
    
    with dissolve

    return
