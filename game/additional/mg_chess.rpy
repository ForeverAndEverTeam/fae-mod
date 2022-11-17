


default persistent._fae_chess_stats = {
    "wins": 0,
    "losses": 0,
    "draws": 0,
    "practice_wins": 0,
    "practice_losses": 0,
    "practice_draws": 0
}

default persistent._fae_chess_difficulty = (0, 1)

default persistent._fae_chess_quicksave = ""

default persistent._fae_chess_dlg_actions = defaultdict(int)

default persistent._fae_skip_file_checks = False

init python in fae_chess:
    import os
    import chess.pgn
    import store
    import random

    CHESS_SAVE_PATH = "/chess_games/"
    CHESS_SAVE_EXT = ".pgn"
    CHESS_SAVE_NAME = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ-_0123456789"
    CHESS_SAVE_PROMPT = "{0} | {1} | Turn: {2} | You: {3}"

    MODE_NORMAL = "normal_chess"
    MODE_BAD_CHESS = "badchess"
    MODE_960 = "chess960"

    REL_DIR = "chess_games/"

    CHESS_MENU_WAIT_VALUE = "MATTE"
    CHESS_MENU_WAIT_TIME = (
        _("I can't make this decision right now..."),
        CHESS_MENU_WAIT_VALUE,
        False,
        False,
        20
    )

    CHESS_NO_GAMES_FOUND = "NOGAMES"

    del_files = (
        "chess.rpyc",
    )

    gt_files = (
        "definitions.rpyc",
        "event-handler.rpyc",
        "script-topics.rpyc",
        "script-introduction.rpyc",
        "script-story-events.rpyc",
        "zz_pianokeys.rpyc",
        "zz_music_selector.rpyc"
    )

    IS_ONGOING = '*'

    CHESS_GAME_CONT = "USHO"

    CHESS_GAME_BACKUP = "foundyou"

    CHESS_GAME_FILE = "file"

    loaded_game_filename = None

    QS_LOST = 0

    QF_LOST_OFCN = 1

    QF_LOST_MAYBE = 2

    QF_LOST_ACDNT = 3

    QF_EDIT_YES = 4

    QF_EDIT_NO = 5

    PIECE_POOL = ('r', 'n', 'p', 'q', 'k', 'b')

    BASE_FEN = "{black_pieces_back}/{black_pieces_front}/8/8/8/8/{white_pieces_front}/{white_pieces_back} w -- 0 1"

    PIECE_POINT_DEFS = {
        "1": 0,
        "p": 1,
        "n": 3,
        "b": 3,
        "r": 5,
        "q": 9
    }

    LOWEST_SIDE_WORTH = 39

    HIGHEST_SIDE_WORTH = 70

    def _checkInProgressGame(pgn_game, sth):

        """
        Checks if the given pgn game is valid and in progress.

        FEED:
            pgn_game - pgn game to check
            sth - Sayori twitter handle
        RETURN:
            SEE isInProgressGame
        """

        if pgn_game is None:
            return None
            
        if pgn_game.headers["Result"] != "*":
            return None
            
        if pgn_game.headers["White"] == sth:
            the_player = "Black"
        elif pgn_game.headers["Black"] == sth:
            the_player = "White"
        
        else:
            return None
        

        board = pgn_game.board()
        for move in pgn_game.main_line():
            board.push(move)
        
        return (
            CHESS_PROMPT_FORMAT.format(
                pgn_game.headers["Date"].replace(".","-"),
                pgn_game.headers["Event"],
                board.fullmove_number,
                the_player
            ),
            pgn_game
        )
    
    def isInProgressGame(filename, sth):

        """
        Checks if the pgn game with the filename is in progress AND valid

        FEED:
            filename - self-explanatory.
        
        RETURN:
            tuple of the following:
                [0]: text to display on button
                [1]: chess.pgn.Game of the game
            or NONE if this is not valid.
        """

        if filename[-4:] != CHESS_SAVE_EXT:
            return None
            
        pgn_game = None
        with open(
            os.path.normcase(CHESS_SAVE_PATH + filename),
            "r"
        ) as loaded_game:
            pgn_game = chess.pgn.read_game(loaded_game)
        
        return _checkInProgressGame(pgn_game, sth)

    def _increment_chess_difficulty():

        level, sublevel = store.persistent._fae_chess_difficulty

        if sublevel == 5 and level < 9:
            level += 1
            sublevel = 1
        
        elif sublevel < 5:
            sublevel += 1
        
        else:
            return

        store.persistent._fae_chess_difficulty = (level, sublevel)

    
    def _decrement_chess_difficulty():

        level, sublevel = store.persistent._fae_chess_difficulty
        if sublevel == 1 and level > 0:
            level -= 1
            sublevel = 5
        
        elif sublevel > 1:
            sublevel -= 1
        
        else:
            return

        store.persistent._fae_chess_difficulty = (level, sublevel)

    
    def _get_player_colour(loaded_game):

        if loaded_game.headers["White"] == store.fae_sayori_twitter_handle:
            return store.chess.BLACK
        return store.chess.WHITE


    def _get_piece_chance(piece_type, selected_pieces_count_dict, available_points):

        prelim_value = (float(available_points) / PIECE_POINT_DEFS[piece_type]) - selected_pieces_count_dict[piece_type]

        return (
            piece_type,
            prelim_value if prelim_value >0 else 1
        )

    
    def select_piece(remaining_points, selected_pieces_count_dict):

        piece_pool = list()

        if remaining_points >= 3:
            piece_pool.extend([
                _get_piece_chance('b', selected_pieces_count_dict, remaining_points),
                _get_piece_chance('n', selected_pieces_count_dict, remaining_points)
            ])

            if remaining_points >= 5:
                piece_pool.append(_get_piece_chance('r', selected_pieces_count_dict, remaining_points))

                if remaining_points >= 9:
                    piece_pool.append(_get_piece_chance('q', selected_pieces_count_dict, remaining_points))
            
            selected_piece = store.fae_utilities.weightedChoice(piece_pool)
            selected_pieces_count_dict[selected_piece] += 1

            return selected_piece
        return 'p'

    
    def _gen_side(white=True, max_side_value=14):

        king_pos = random.randint(0, 7)

        back_row = list()
        front_row = list()

        selected_pieces_count = {
            'q': 0,
            'r': 0,
            'n': 0,
            'b': 0
        }

        side_indeces = range(0, 16)
        random.shuffle(side_indeces)

        max_side_value -= 14

        for ind in side_indeces:
            if ind == king_pos:
                piece_to_add = 'k'
            
            else:
                piece_to_add = select_piece(max_side_value, selected_pieces_count)

                max_side_value -= PIECE_POINT_DEFS[piece_to_add] - 1

            if white:
                piece_to_add = piece_to_add.capitalize()

            if ind < 8:
                back_row.append(piece_to_add)
            else:
                front_row.append(piece_to_add)
        

        random.shuffle(front_row)
        random.shuffle(back_row)

        if not white:
            back_row, front_row = front_row, back_row
        
        return "".join(front_row), "".join(back_row)

    def _validate_sides(white_front, white_back, black_front, black_back):

        def validate(king_id, enemy_front):

            queen = "q"
            queen_or_bishop = ("q", "b")

            if (
                enemy_front[king_id].lower() in (queen, "r")
                or (
                    king_id > 0
                    and enemy_front[king_id - 1].lower() == queen
                )
                or (
                    king_id < 7
                    and enemy_front[king_id + 1].lower() == queen
                )
                or (
                    king_id == 0
                    and (
                        enemy_front[5].lower() in queen_or_bishop
                        or enemy_front[6].lower() in queen_or_bishop
                    )
                )

                or (
                    king_id == 1
                    and (
                        enemy_front[5].lower() in queen_or_bishop
                        or enemy_front[6].lower() in queen_or_bishop
                        or enemy_front[7].lower() in queen_or_bishop
                    )
                )

                or (
                    king_id == 3
                    and (
                        enemy_front[6].lower() in queen_or_bishop
                        or enemy_front[7].lower() in queen_or_bishop
                    )
                )

                or (
                    king_id == 5
                    and (
                        enemy_front[0].lower() in queen_or_bishop
                        or enemy_front[1].lower() in queen_or_bishop
                    )
                )
                or (
                    king_id == 6
                    and (
                        enemy_front[0].lower() in queen_or_bishop
                        or enemy_front[1].lower() in queen_or_bishop
                        or enemy_front[2].lower() in queen_or_bishop
                    )
                )
                or (
                    king_id == 7
                    and (
                        enemy_front[1].lower() in queen_or_bishop
                        or enemy_front[2].lower() in queen_or_bishop
                    )
                )
            ):

                return False
            return True

        white_king_id = white_back.index("K")
        white_is_good = validate(white_king_id, black_front)

        black_king_id = black_back.index("k")
        black_is_good = validate(black_king_id, white_front)

        return white_is_good and black_is_good

    def generate_random_fen(is_player_white=True):

        difficulty = store.persistent._fae_chess_difficulty[0] * 6 + store.persistent._fae_chess_difficulty[1]

        p_value_adj = int(round(-((float(difficulty) - 27)**3) / 984))
        s_value_adj = -p_value_adj

        delta = abs(p_value_adj)

        base_piece_value = random.randint(LOWEST_SIDE_WORTH, HIGHEST_SIDE_WORTH)

        max_piece_value = max(min(base_piece_value + p_value_adj, HIGHEST_SIDE_WORTH), LOWEST_SIDE_WORTH)

        sayori_max_piece_value = max(min(base_piece_value + s_value_adj, HIGHEST_SIDE_WORTH), LOWEST_SIDE_WORTH)

        good_to_go = False
        attempts = 0

        while (
            not good_to_go
            and attempts < 10
        ):

            attempts += 1
            player_first_row, player_second_row = _gen_side(is_player_white, max_piece_value)
            sayori_first_row, sayori_second_row = _gen_side(not is_player_white, sayori_max_piece_value)

            if is_player_white:
                white_front = player_first_row
                white_back = player_second_row
                black_front = sayori_second_row
                black_back = sayori_first_row
            
            else:
                white_front = sayori_first_row
                white_back = sayori_second_row
                black_front = player_second_row
                black_back = player_first_row
            
            good_to_go = _validate_sides(white_front, white_back, black_front, black_back)
        

        if is_player_white:
            return BASE_FEN.format(
                black_pieces_back=sayori_first_row,
                black_pieces_front=sayori_second_row,
                white_pieces_front=player_first_row,
                white_pieces_back=player_second_row
            )
        
        else:
            return BASE_FEN.format(
                black_pieces_back=player_first_row,
                black_pieces_front=player_second_row,
                white_pieces_front=sayori_first_row,
                white_pieces_back=sayori_second_row
            )
    
    def generate_960_fen():

        king_position = random.randint(1, 6)

        left_rook_position = random.randint(0, king_position-1)
        right_rook_position = random.randint(king_position+1, 7)

        occupied_positions = frozenset((king_position, left_rook_position, right_rook_position))

        available_white_positions = _set(range(1, 9, 2)) - occupied_positions
        available_black_positions = _set(range(0, 8, 2)) - occupied_positions

        first_bishop_position = random.choice(tuple(available_white_positions))
        second_bishop_position = random.choice(tuple(available_black_positions))
        if bool(random.randint(0, 1)):
            first_bishop_position, second_bishop_position = second_bishop_position, first_bishop_position
        
        occupied_positions = frozenset((first_bishop_position, second_bishop_position))
        available_positions = (available_white_positions | available_black_positions) - occupied_positions

        queen_position = random.choice(tuple(available_positions))
        available_positions.remove(queen_position)

        first_knight_position, second_knight_position = available_positions

        pos_to_piece_defs = {
            king_position: "K",
            left_rook_position: "R",
            right_rook_position: "R",
            first_bishop_position: "B",
            second_bishop_position: "B",
            queen_position: "Q",
            first_knight_position: "N",
            second_knight_position: "N"
        }

        back_row_str = "".join(pos_to_piece_defs[i] for i in range(8))

        return BASE_FEN.format(
            black_pieces_back=back_row_str.lower(),
            black_pieces_front="pppppppp",
            white_pieces_front="PPPPPPPP",
            white_pieces_back=back_row_str
        )

    def enqueue_output(out, queue, lock):
        for line in iter(out.readline, b''):
            with lock:
                queue.appendleft(line)
        
        out.close()
    

label game_chess:

    python:

        loaded_game = None
        failed_to_load_save = True

        chessmode = fae_chess.MODE_NORMAL
        casual_rules = False
        practice_mod = False
        is_player_white = 0
        menu_category = "gamemode_select"
        loopback = False
        draw_lots = False

    
    if not renpy.seen_label("fae_chess_save_selected"):
        call fae_chess_save_migration from _call_fae_chess_save_migration

        if not _return:
            return

        elif _return == fae_chess.CHESS_NO_GAMES_FOUND:
            jump fae_chess_remenu
        
        $ loaded_game = _return
    
    elif len(persistent._fae_chess_quicksave) > 0:

        python:
            quicksaved_game = chess.pgn.read_game(
                StringIO.StringIO(persistent._fae_chess_quicksave)
            )

            quicksaved_game = fae_chess._checkInProgressGame(
                quicksaved_game,
                fae_sayori_twitter_handle
            )
        
        if quicksaved_game is None:
            $ failed_to_load_save = False

            python:
                import os
                import struct

                pgn_files = os.listdir(fae_chess.CHESS_SAVE_PATH)
                if pgn_files:

                    valid_files = list()
                    for filename in pgn_files:
                        in_prog_game = fae_chess.isInProgressGame(
                            filename,
                            fae_sayori_twitter_handle
                        )

                        if in_prog_game:
                            valid_files.append((filename, in_prog_game[1]))
                    
                    if len(valid_files) > 0:
                        for filename,pgn_game in valid_files:
                            store._fae_root.mangleFile(
                                fae_chess.CHESS_SAVE_PATH + filename,
                                mangle_length=len(str(pgn_game))*2
                            )
            
            $ persistent._fae_chess_quicksave = ""

            call fae_chess_dlg_quicksave_lost from _call_fae_chess_dlg_quicksave_lost

            if _return is not None:
                return

        jump fae_chess_remenu

    
    if persistent._fae_chess_skip_file_checks:
        $ loaded_game = quicksaved_game[1]
        s "Let's continue our unfinished game."

        if loaded_game:
            python:
                is_player_white = fae_chess._get_player_colour(loaded_game)

                practice_mode = eval(loaded_game.headers.get("Practice", "False"))
                casual_rules = eval(loaded_game.headers.get("CasualRules", "False"))
            
            jump fae_chess_start_chess
    
    python:
        quicksaved_game = quicksaved_game[1]

        quicksaved_filename = (quicksaved_game.headers["Event"] + fae_chess.CHESS_SAVE_EXT)
        quicksaved_filename_clean = (fae_chess.CHESS_SAVE_PATH + quicksaved_filename).replace("\\", "/")

        try:
            if os.access(quicksaved_filename_clean, os.R_OK):
                quicksaved_file = fae_chess.isInProgressGame(
                    quicksaved_filename,
                    fae_sayori_twitter_handle
                )
            else:
                fae_utilities.fae_log.error("Failed to access quickfile.")
                quicksaved_file = None
            
        except Exception as e:
            fae_utilities.fae_log.exception(e)
            quicksaved_file = None
    
    if quicksaved_file is None:
        $ failed_to_load_save = False

        $ fae_chess.loaded_game_filename = quicksaved_filename_clean

        call fae_chess_dlg_quickfile_lost from _call_fae_chess_dlg_quickfile_lost

        if _return == fae_chess.CHESS_GAME_CONT:
            python:
                try:
                    if os.access(quicksaved_filename_clean, os.R_OK):
                        quicksaved_file = fae_chess.isInProgressGame(
                            quicksaved_filename,
                            fae_sayori_twitter_handle
                        )
                    
                    else:
                        fae_utilities.fae_log.error("Failed to access quickfile.")
                        quicksaved_file = None
                
                except Exception as e:
                    fae_utilities.fae_log.exception(e)
                    quicksaved_file = None
        
        elif _return == fae_chess.CHESS_GAME_BACKUP:
            $ loaded_game = quicksaved_game
            jump .loadcheck
        
        else:
            $ persistent._fae_chess_quicksave = ""

            if _return is not None:
                return

            jump fae_chess_remenu
    
    python:
        quicksaved_file = quicksaved_file[1]

        is_same = str(quicksaved_game) == str(quicksaved_file)

    if not is_same:
        $ failed_to_load_save = False

        call fae_chess_dlg_quickfile_edited from _call_fae_chess_dlg_quickfile_edited

        if _return == fae_chess.CHESS_GAME_BACKUP:
            $ loaded_game = quicksaved_game
            jump .loadcheck
        
        elif _return == fae_chess.CHESS_GAME_FILE:
            $ loaded_game = quicksaved_file
            jump .loadcheck
        

        python:
            persistent._fae_chess_quicksave = ""

            try:
                os.remove(quicksaved_filename_clean)
            except:
                pass
        
        if _return is not None:
            return

        jump fae_chess_remenu

    else:

        $ loaded_game = quicksaved_game

        if failed_to_load_save:

            s "We still ahve a game in progress."
        
        label .load_check:
            pass

        s "Get ready!"
    
    if loaded_game:
        python:
            is_player_white = fae_chess._get_player_colour(loaded_game)

            practice_mode = eval(loaded_game.headers.get("Practice", "False"))
            casual_rules = eval(loaded_game.headers.get("CasualRules", "False"))

        jump fae_chess_start_chess

label fae_chess_remenu:

    python:
        menu_contents = {
            "gamemode_select": {
                "options": [
                    ("Normal Chess", fae_chess.MODE_NORMAL, False, (chessmode == fae_chess.MODE_NORMAL)),
                    ("Randomized Chess", fae_chess.MODE_BAD_CHESS, False, (chessmode == fae_chess.MODE_BAD_CHESS)),
                    ("Chess 960", fae_chess.MODE_960, False, (chessmode == fae_chess.MODE_960))
                ],
                "final_items": [
                    ("Ruleset", "ruleset_select", False, False, 20),
                    ("Practice or Play", "mode_select", False, False, 0),
                    ("Color", "colour_select", False, False, 0),
                    ("Let's play!", "confirm", False, False, 20),
                    ("Nevermind.", -1, False, False, 0)
                ]
            },
            "ruleset_select": {
                "options": [
                    ("Casual Rules", True, False, casual_rules),
                    ("Traditional Rules", False, False, not casual_rules),
                    ("What's the difference?", 0, False, False)
                ],
                "final_items": [
                    ("Gamemode", "gamemode_select", False, False, 20),
                    ("Practice or Play", "mode_select", False, False, 0),
                    ("Color", "colour_select", False, False, 0),
                    ("Let's play!", "confirm", False, False, 20),
                    ("Nevermind.", -1, False, False, 0)
                ]
            },
            "mode_select": {
                "options": [
                    ("Practice", True, False, practice_mode),
                    ("Play", False, False, not practice_mode)
                ],
                "final_items": [
                    ("Gamemode", "gamemode_select", False, False, 20),
                    ("Ruleset", "ruleset_select", False, False, 0),
                    ("Color", "colour_select", False, False, 0),
                    ("Let's play!", "confirm", False, False, 20),
                    ("Nevermind.", -1, False, False, 0)
                ]
            },
            "colour_select": {
                "options": [
                    ("White", True, False, is_player_white),
                    ("Black", False, False, is_player_white is False),
                    ("Let's draw lots!", 0, False, is_player_white is 0) #Is check here specifically for states
                ],
                "final_items": [
                    ("Gamemode", "gamemode_select", False, False, 20),
                    ("Ruleset", "ruleset_select", False, False, 0),
                    ("Practice or Play", "mode_select", False, False, 0),
                    ("Let's play!", "confirm", False, False, 20),
                    ("Nevermind.", -1, False, False, 0)
                ]
            }
        }

    
    show sayori aaabaa at t11

    $ menu_options = menu_contents[menu_category]["options"]
    $ final_items = menu_contents[menu_category]["final_items"]

    s "How would you like to play?[('{fast}' if loopback else '')]" nointeract

    call screen fae_gen_scrollable_menu(menu_options, fae_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, fae_ui.SCROLLABLE_MENU_XALIGN, *final_items)

    $ loopback = True

    # QUITTING OUT

    if _return == -1:
        show sayori at t11
        s "Alright [player]."
        return
    
    elif _return in menu_contents.keys():
        $ _history_list.pop()
        $ menu_category = _return

        jump fae_chess_remenu
    
    elif _return not in ("confirm", None):
        $ _history_list.pop()

        if menu_category == "gamemode_select":
            $ chessmode = _return
        
        elif menu_category == "ruleset_select":
            if _return is 0:
                show sayori at t11
                s "If we play with casual rules, we won't count stalemates as draws.{nw}"
                extend " Essentially, the player who is not trapped, is declared the winner."
            
            else:
                $ casual_rules = _return
            
        
        elif menu_category == "mode_select":
            $ practice_mode = _return
        
        elif menu_category == "colour_select":
            if _return is 0:
                $ drew_lots = True
                call fae_chess_draw_lots(False) from _call_fae_chess_draw_lots
            
            else:
                $ drew_lots = False
                $ is_player_white = _return
            
        
        jump fae_chess_remenu

    
    if is_player_white is 0:
        $ drew_lots = True
        call fae_chess_draw_lots from _call_fae_chess_draw_lots_1

label fae_chess_start_chess:

    python:
        if chessmode == fae_chess.MODE_NORMAL:
            starting_fen = None
        
        elif chessmode == fae_chess.MODE_960:
            starting_fen = fae_chess.generate_960_fen()
        
        else:
            starting_fen = fae_chess.generate_random_fen(is_player_white)
    
    window hide None
    show sayori aaabaa at t21
    python:
        quick_menu = False

        chess_displayable_obj = FAEChessDisplayable(
            is_player_white,
            pgn_game=loaded_game,
            practice_mode=practice_mode,
            starting_fen=starting_fen,
            casual_rules=casual_rules
        )
        chess_displayable_obj.show()
        results = chess_displayable_obj.game_loop()
        chess_displayable_obj.hide()

        quick_menu = True

        new_pgn_game, is_sayori_winner, is_surrender, num_turns = results

        game_result = new_pgn_game.headers["Result"]

    show sayori at t11

    $ Affection.getAffectionGain(0.5)

    if is_sayori_winner:
        $ persistent._fae_chess_Stats["practics_losses" if practice_mode else "losses"] += 1

        if is_surrender:
            if num_turns < 5:
                s "Don't give up so easily."
                s "I'm sure, if you keep trying, you can beat me."
            
            else:
                s "Giving up?"
                s "Alright."
        
        else:
            s "I win! Yay!"

            python:
                total_losses = persistent._fae_chess_stats.get("practice_losses", 0) + persistent._fae_chess_stats.get("losses", 0)
                total_wins = persistent._fae_chess_stats.get("practice_wins", 0) + persistent._fae_chess_stats.get("wins", 0)
            if float(total_wins)/total_losses < 0.3:
                call fae_chess_dlg_game_sayori_wins_often from _call_fae_chess_dlg_game_sayori_wins_often
            
            else:
                call fae_chess_dlg_game_sayori_wins_sometimes from _call_fae_chess_dlg_game_sayori_wins_sometimes
                s "Anyway..."

        if not is_surrender:

            $ fae_chess._decrement_chess_difficulty()
        
    
    elif game_result == fae_chess.IS_ONGOING:
        call fae_chess_savegame(allow_return=False) from _call_fae_chess_savegame
        return

    elif game_result == "1/2-1/2":
        if new_pgn_game.headers.get("DrawRequested"):
            s "Sure thing!"
            s "Long game!"
            $ line_start = "Great job though!"
        
        else:
            s "Looks like we have a draw."
            $ line_start = "But on the bright side"
        
        if not persistent._fae_ever_won["chess"]:
            s "[line_start], you're getting closer to beating me, [player]~"
        
        else:
            s "Nice work on getting this far, [player]~"
        
        $ persistent._fae_chess_stats["practice_draws" if practice_mode else "draws"] += 1
    

    # PLAYER WINS

    else:
        python:
            player_win_quips = [
                _("I'm sor proud.")
            ]
            persistent._fae_chess_stats["practice_wins" if practice_mode else "wins"] += 1

            if not persistent._fae_ever_won['chess']:
                persistent._fae_ever_won['chess'] = True
        
        if practice_mode:
            s "Congratulations, [player], you won!"

            $ undo_count = new_pgn_game.headers.get("UndoCount", 0)
            if not undo_count:
                s "Without a single undo! {w=0.2} {nw}"
                extend "That's amazing!"
            
            elif undo_count == 1:
                s "You only undid once. {w=0.2} {nw}"
                extend "Nice job!"
            
            elif undo_count <= 5:
                s "You only undid [undo_count] times too, great job."
            
            elif undo_count <= 10:
                s "[undo_count] undos, not bad. I'm sure we can lower that, with practice."
            
            else:
                s "You undid [undo_count] moves though... {w=0.2} {nw}"
                extend "But I'm sure we can get that lower with practice."
            
            s "[renpy.substitute(random.choice(player_win_quips))]"
        
        else:
            s "Great job, you won!"
            s "[renpy.substitute(random.choice(player_win_quips))]"
        
        s "Anyway..."

        $ fae_chess._increment_chess_difficulty()
    
    if loaded_game:
        call fae_chess_savegame(silent=True) from _call_fae_chess_savegame_1
        jump fae_chess_player_again_ask
    
    if is_surrender and num_turns < 5:
        return
    
    if num_turns > 4:
        s "Would you like to save this game?{nw}"
        $ _history_list.pop()
        menu:
            s "Would you like to save this game?{fast}"

            "Yes.":
                call fae_chess_savegame from _call_fae_chess_savegame_2
            
            "No.":
                pass


label fae_chess_player_again_ask:
    s "Would you like to play again?{nw}"
    $ _history_list.pop()

    menu:
        s "Would you like to play again?{fast}"

        "Yes.":
            if drew_lots:
                call fae_chess_draw_lots from _call_fae_chess_draw_lots_2
            
            jump fae_chess_start_chess
        
        "Yes, but with different rules.":
            jump fae_chess_remenu
        
        "No.":
            s "Alright."
    
    return

label fae_chess_draw_lots(begin=True):

    show sayori at t11
    $ drew_lots = True
    $ lets_begin = "{w=0.2} Let's begin." if begin else ""

    if random.randint(0, 1) == 0:
        $ is_player_white = chess.WHITE
        s "I drew black![lets_begin]"
    else:
        $ is_player_white = chess.BLACK
        s "I drew white![lets_begin]"
    
    return

label fae_chess_savegame(silent=False, allow_return=True):

    label .save_start:

        pass

    if loaded_game:
        python:
            new_pgn_game.headers["Event"] = loaded_game.headers["Event"]

            save_filename = new_pgn_game.headers["Event"] + fae_chess.CHESS_SAVE_EXT

            file_path = fae_chess.CHESS_SAVE_PATH + save_filename

            loaded_game = None

    
    else:
        python:
            save_name = ""
            while len(save_name) == 0:
                save_name = fae_input(
                    "Enter a name for this game:",
                    allow=fae_chess.CHESS_SAVE_NAME,
                    lenght=15,
                    screen_kwargs={"use_return_button": allow_return}
                )

        if save_name == "cancel_input":
            return

        python:
            new_pgn_game.headers["Event"] = save_name

            save_filename = save_name + fae_chess.CHESS_SAVE_EXT

            file_path = fae_chess.CHESS_SAVE_PATH + save_filename

            if_file_exist = os.access(
                os.path.normcase(file_path),
                os.F_OK
            )

        if is_file_exist:
            s "We already have a game named '[save_name]'"

            s "Hall I overwrite it?{nw}"
            $ _history_list.pop()
            menu:
                s "Should I overwrite it?{fast}"

                "Yes":
                    pass

                "No.":
                    jump .save_start
    
    python:
        with open(file_path, "w") as pgn_file:
            pgn_file.write(str(new_pgn_game))
        
        if new_pgn_game.headers["Result"] == fae_chess.IS_ONGOING:
            persistent._fae_chess_quicksave = str(new_pgn_game)
        
        else:
            persistent._fae_chess_quicksave = ""
        

        display_file_path = fae_chess.REL_DIR + save_filename
    
    if not silent:
        s "I've saved our game in '[display_file_path]'"

        if not renpy.seen_label("fae_chess_savegame.pgn_explain"):

            label .pgn_explain:
                pass

            s "It's in a format called 'Portable Game Notation.'{w=0.2} {nw}"
            extend "You can find PGN analyzers onine to open it and see where you made your mistakes."

        if game_result == fae_chess.IS_ONGOING:
            s "Let's continue this game soon."
        
    return

label fae_chess_dlg_game_sayori_wins_often:
    s "Someday you'll beat me."

    if not persistent._fae_ever_won["chess"]:
        s "You'll beat me someday."
    return

label fae_chess_dlg_game_sayori_wins_sometimes:
    s "That was really fun."
    s "If you keep practicing, I'm sure you'll be better than me someday."

    if persistent._fae_chess_difficulty != (0, 1):
        s "Until then, I'll go a little easier."

    return

label fae_chess_confirm_context(prompt):

    call screen fae_chess_confirm(prompt)
    return _return


label fae_chess_save_migration:
    python:
        import chess.pgn
        import os
        import store.fae_chess as fae_chess

        pgn_files = os.listdir(fae_chess.CHESS_SAVE_PATH)
        sel_game = (fae_chess.CHESS_NO_GAMES_FOUND)

    if pgn_files:
        python:

            pgn_games = list()
            actual_pgn_games = list()
            game_dex = 0
            for filename in pgn_files:
                in_prog_game = fae_chess.isInProgressGame(
                    filename,
                    fae_sayori_twitter_handle
                )

                if in_prog_game:
                    pgn_games.append((
                        in_prog_game[0],
                        game_dex,
                        False,
                        False
                    ))
                    actual_pgn_games.append((in_prog_game[1], filename))
                    game_dex += 1

            game_count = len(pgn_games)
            pgn_games.sort()
            pgn_games.reverse()

        if game_count > 1:
            if renpy.seen_label("fae_chess_save_multi_dlg"):
                $ pick_text = _("You still need to pick a game to keep.")

            else:
                label fae_chess_save_multi_dlg:
                    s  "So I've been thinking, [player]..."
                    s  "Most people who leave in the middle of a chess game don't come back to start a new one."
                    s  "...So it makes no sense for me to keep track of more than one unfinished game between us."
                    s  "And since we have [game_count] games in progress..."
                    s  "I have to ask you to pick only one to keep.{w=0.2} Sorry, [player]."
                    $ pick_text = _("Pick a game you'd like to keep.")

            show sayori at t21
            $ renpy.say(s, pick_text, interact=False)

            call screen fae_gen_scrollable_menu(pgn_games, fae_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, fae_ui.SCROLLABLE_MENU_XALIGN, fae_chess.CHESS_MENU_WAIT_ITEM)

            show sayori at t11
            if _return == fae_chess.CHESS_MENU_WAIT_VALUE:
                # user backs out
                s "I see."
                s "In that case, please take your time."
                s "We'll play chess again once you've made your decision."
                return False

            else:
                # user selected a game
                s "Alright."
                python:
                    sel_game = actual_pgn_games.pop(_return)
                    for pgn_game in actual_pgn_games:
                        game_path = os.path.normcase(fae_chess.CHESS_SAVE_PATH + pgn_game[1])
                        try:
                            os.remove(os.path.normcase(game_path))
                        except:
                            fae_utilities.fae_log.error("Failed to remove game at: {0}".format(game_path))

        # we have one game, so return the game
        elif game_count == 1:
            $ sel_game = actual_pgn_games[0]

# FALL THROUGH
label fae_chess_save_selected:
    return sel_game[0]


label fae_chess_dlg_quicksave_lost:
    python:
        persistent._fae_chess_dlg_actions[fae_chess.QS_LOST] += 1
        qs_gone_count = persistent._fae_chess_dlg_actions[fae_chess.QS_LOST]

    s "Uh, [player]...{w=0.5} I think I messed up in saving our last game, and now I can't open it anymore."

    if qs_gone_count == 2:
        s "I'm really, really sorry, [player]..."
        show sayori
        pause 1.0
        s "But don't worry, I'll make it up to you...{w=0.3}{nw}"
        extend "by starting a new game!"
        s "Ahaha~"

    elif qs_gone_count == 3:
        s "I'm so clumsy, [player]...{w=0.3} I'm sorry."
        s "Let's start a new game instead."

    elif qs_gone_count % 5 == 0:
        s "This has happened [qs_gone_count] times now..."
        s "I wonder if this is a side effect of {i}someone{/i} trying to edit the saves.{w=1}.{w=1}."
        s "Anyway..."
        s "Let's start a new game."

    else:
        s "I'm sorry..."
        s "Let's start a new game instead."

    return None




label fae_chess_dlg_quickfile_lost:
    s "Well this is embarrassing..."
    s "I could have sworn that we had an unfinished game, but I can't find the save file."

    s "Did you mess with the saves, [player]?{nw}"
    $ _history_list.pop()
    menu:
        s "Did you mess with the saves, [player]?{fast}"

        "I deleted the save.":
            jump fae_chess_dlg_quickfile_lost_deleted

        "It was an accident!":
            jump fae_chess_dlg_quickfile_lost_accident

        "Maybe...":
            jump fae_chess_dlg_quickfile_lost_maybe

        "Of course not!":
            jump fae_chess_dlg_quickfile_lost_ofcoursenot


#Player deleted the saves
label fae_chess_dlg_quickfile_lost_deleted:
    s "Thanks for being honest with me, [player]."

    s "Did you not want to continue that game?{nw}"
    $ _history_list.pop()
    menu:
        s "Did you not want to continue that game?{fast}"

        "Yeah.":
            s "I understand, [player]."
            s "Let's start a new game~"

        "No.":
            s "Oh?"
            s "I guess you just deleted it by mistake then."
            s "Let's just start a new game."
    return

#Of course not flow
label fae_chess_dlg_quickfile_lost_ofcoursenot:
    python:
        persistent._fae_chess_dlg_actions[fae_chess.QF_LOST_OFCN] += 1
        qf_gone_count = persistent._fae_chess_dlg_actions[fae_chess.QF_LOST_OFCN]

    if qf_gone_count in [3,4]:
        s "..."
        s "[player],{w=0.2} did you..."
        s "Nevermind."
        s "Let's play a new game."

    elif qf_gone_count == 5:
        $ fae_loseAffection()
        s "..."
        s "[player],{w=0.2} this is happening way too much."
        s "I really don't believe you this time."
        pause 2.0
        s "I hope you're not messing with me."
        s "..."
        s "Whatever.{w=0.5} Let's just play a new game."

    elif qf_gone_count >= 6:
        python:
            fae_loseAffection(modifier=10)
            #NOTE: Chess is automatically locked due to its conditional. No need to manually lock it here
            fae_stripEVL("fae_unlock_chess")
            #Workaround to deal with people who havent seen the unlock chess label
            persistent._seen_ever["fae_unlock_chess"] = True
            #We use a simple value of true to establish a permanent disable
            persistent._fae_chess_timed_disable = True

        s "..."
        s "[player],{w=0.3} I don't believe you."
        s "If you're just going to throw away our chess games like that..."
        s "Then I don't want to play chess with you anymore!"
        return True

    else:
        s "Ah, yeah. You wouldn't do that to me."
        s "I must have misplaced the save file."
        s "Sorry, [player]."
        s "I'll make it up to you...{w=0.3}{nw}"
        extend "by starting a new game!"

    return None


## maybe sayori flow
label fae_chess_dlg_quickfile_lost_maybe:
    python:
        persistent._fae_chess_dlg_actions[fae_chess.QF_LOST_MAYBE] += 1
        qf_gone_count = persistent._fae_chess_dlg_actions[fae_chess.QF_LOST_MAYBE]

    if qf_gone_count == 1:
        s "[player]!{w=0.2} I should have known you were just messing with me!"
        jump fae_chess_quickfile_lost_filechecker

    if qf_gone_count == 2:
        s "[player]!{w=0.2} Stop messing with me!"
        jump fae_chess_quickfile_lost_filechecker

    else:
        $ persistent._fae_chess_skip_file_checks = True

        s "[player]! That's--"
        s "..."
        s "...not a problem at all."
        s "I knew you were going to do this again..."
        s "...so I kept a backup of our save!"
        s "You can't trick me anymore, [player]."
        s "Now let's continue our game."
        return store.fae_chess.CHESS_GAME_BACKUP


# maybe sayori file checking parts
label fae_chess_quickfile_lost_filechecker:
    $ game_file = fae_chess.loaded_game_filename

    if os.access(game_file, os.F_OK):
        jump fae_chess_dlg_quickfile_lost_maybe_save_found

    s "Can you put the save back so we can play?"

    show sayori

    #Loop setup
    python:
        seconds = 0
        file_found = False

    #FALL THROUGH

label fae_chess_quickfile_lost_maybe_filechecker_loop:
    hide screen fae_background_timed_jump

    #Run filechecks...
    $ file_found = os.access(game_file, os.F_OK)

    if file_found:
        hide screen fae_background_timed_jump
        jump fae_chess_dlg_quickfile_lost_maybe_filechecker_file_found

    elif seconds >= 60:
        hide screen fae_background_timed_jump
        jump fae_chess_dlg_quickfile_lost_maybe_filechecker_no_file

    show screen fae_background_timed_jump(4, "fae_chess_quickfile_lost_maybe_filechecker_loop")
    $ seconds += 4
    menu:
        "I deleted the save...":
            hide screen fae_background_timed_jump
            jump fae_chess_dlg_quickfile_lost_maybe_filechecker_no_file

label fae_chess_dlg_quickfile_lost_maybe_filechecker_file_found:
    s "Yay!{w=0.2} Thanks for putting it back, [player]."
    s "Now we can continue our game."
    show sayori
    return fae_chess.CHESS_GAME_CONT

label fae_chess_dlg_quickfile_lost_maybe_filechecker_no_file:
    s "[player]..."
    s "That's okay. Let's just play a new game."
    return None

# generic maybe sayori, found file
label fae_chess_dlg_quickfile_lost_maybe_save_found:
    s "Oh!"
    s "There's the save.{w=0.2} Thanks for putting it back, [player]."
    s "Now we can continue our game."
    return store.fae_chess.CHESS_GAME_CONT

## Accident sayori flow
label fae_chess_dlg_quickfile_lost_accident:
    python:
        persistent._fae_chess_dlg_actions[fae_chess.QF_LOST_ACDNT] += 1
        qf_gone_count = persistent._fae_chess_dlg_actions[fae_chess.QF_LOST_ACDNT]

    if qf_gone_count == 2:
        s "Again? Don't be so clumsy, [player]."
        s "But that's okay."
        s "We'll just play a new game instead."

    elif qf_gone_count >= 3:
        $ persistent._fae_chess_skip_file_checks = True
        s "I had a feeling this would happen again."
        s "So I kept a backup of our save!"
        s "Now we can continue our game~"
        return store.fae_chess.CHESS_GAME_BACKUP

    else:
        s "[player]...{w=0.3} {nw}"
        extend "That's okay.{w=0.3} Accidents happen."
        s "Let's play a new game instead."
    return None

### quickfile edited
# main label for quickfile edited flow
label fae_chess_dlg_quickfile_edited:
    s "[player]..."

    s "Did you edit the save file?{nw}"
    $ _history_list.pop()
    menu:
        s "Did you edit the save file?{fast}"

        "Yes.":
            jump fae_chess_dlg_quickfile_edited_yes

        "No.":
            jump fae_chess_dlg_quickfile_edited_no


## Yes Edit flow
label fae_chess_dlg_quickfile_edited_yes:
    python:
        persistent._fae_chess_dlg_actions[fae_chess.QF_EDIT_YES] += 1
        qf_edit_count = persistent._fae_chess_dlg_actions[fae_chess.QF_EDIT_YES]

    if qf_edit_count == 1:
        s 1dsc "I'm disappointed in you."
        s 1eka "But I'm glad that you were honest with me."

        # we want a timed menu here. Let's give the player 5 seconds to say sorry
        show screen fae_background_timed_jump(5, "fae_chess_dlg_quickfile_edited_yes.game_ruined")
        menu:
            "I'm sorry.":
                hide screen fae_background_timed_jump
                # light affection boost for being honest
                $ Affection.getAffectionGain(0.5)
                s "Apology accepted!"
                s "Luckily, I still remember a little bit of the last game, so we can continue it from there."
                return store.fae_chess.CHESS_GAME_BACKUP

            "...":
                label .game_ruined:
                    pass

                hide screen fae_background_timed_jump
                s "Since that game's been ruined, let's just play a new game."

    elif qf_edit_count == 2:
        python:
            persistent._fae_chess_timed_disable = datetime.datetime.now()
            Affection.getAffectionGain(0.5)

        s "I am incredibly disappointed in you..."
        s "Let's play chess some other time.{w=0.2} I don't feel like playing right now."
        return True

    else:
        $ Affection.getAffectionLoss()
        $ persistent._fae_chess_skip_file_checks = True

        s "I'm not surprised..."
        s "But I am prepared."
        s "I kept a backup of our game just in case you did this again."
        s "Now let's finish this game."
        return store.fae_chess.CHESS_GAME_BACKUP

    return None


## No Edit flow
label fae_chess_dlg_quickfile_edited_no:
    python:
        persistent._fae_chess_dlg_actions[fae_chess.QF_EDIT_NO] += 1
        qf_edit_count = persistent._fae_chess_dlg_actions[fae_chess.QF_EDIT_NO]

    if qf_edit_count == 1:
        $ Affection.getAffectionLoss()

        s "Hmm..."
        s "The save file looks different from how I last remembered it,{w=0.2} {nw}"
        extend "{nw}but maybe that's just my memory failing me..."
        s "Let's continue this game."
        return store.fae_chess.CHESS_GAME_FILE

    elif qf_edit_count == 2:
        $ Affection.getAffectionLoss(2)

        s "I see."
        s "..."
        s "Let's just continue this game."
        return store.fae_chess.CHESS_GAME_FILE

    else:
        $ Affection.getAffectionLoss(3)
        s "[player]..."
        s "I kept a backup of our game.{w=0.5} I know you edited the save file."
        s "I just-"
        $ _history_list.pop()
        s "I just{fast} can't believe you would cheat and {i}lie{/i} to me..."
        s "..."

        #NOTE: This is the ultimate choice, it dictates whether we delete everything or not
        show screen fae_background_timed_jump(3, "fae_chess_dlg_quickfile_edited_no.menu_silent")
        menu:
            "I'm sorry.":
                hide screen fae_background_timed_jump
                # light affection boost for apologizing
                $ Affection.getAffectionGain()
                python:
                    persistent._fae_chess_3_edit_sorry = True
                    persistent._fae_chess_skip_file_checks = True

                show sayori
                pause 1.0
                show sayori
                pause 1.0
                s "I forgive you, [player], but please don't do this to me again."
                s "..."
                return store.fae_chess.CHESS_GAME_BACKUP

            "...":
                label .menu_silent:
                    hide screen fae_background_timed_jump
                    jump fae_chess_dlg_pre_go_ham

#3rd time no edit, sorry, edit qs
label fae_chess_dlg_quickfile_edited_no_quicksave:
    python:
        persistent._fae_chess_timed_disable = datetime.datetime.now()
        Affection.getAffectionLoss()

    s "[player]..."
    s "I see you've edited my backup saves."
    s "If you want to be like that right now, then we'll play chess some other time."
    return True


#### end dialogue blocks ######################################################

# confirmation screen for chess
screen fae_chess_confirm(prompt):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"
    add fae_getTimeFile("gui/overlay/confirm.png")

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label prompt:
                style "confirm_prompt"
                text_color fae_globals.button_text_idle_colour
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action Return(True)
                textbutton _("No") action Return(False)

# promotion screen for chess
screen fae_chess_promote(q, r, n, b):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"
    add fae_getTimeFile("gui/overlay/confirm.png")

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _("Select piece to promote to"): # only use : if the choices are to the right of the label
                style "confirm_prompt"
                text_color fae_globals.button_text_idle_colour
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 10

                imagebutton idle q action Return('q')
                imagebutton idle r action Return('r')
                imagebutton idle n action Return('n')
                imagebutton idle b action Return('b')

label fae_chess_promote_context(is_player_white):
    $ _return = renpy.call_screen(
        "fae_chess_promote",
        q=FAEPiece.IMG_DEFS[FAEPiece.FP_COLOUR_LOOKUP[is_player_white] + ("Q" if is_player_white else "q")],
        r=FAEPiece.IMG_DEFS[FAEPiece.FP_COLOUR_LOOKUP[is_player_white] + ("R" if is_player_white else "r")],
        n=FAEPiece.IMG_DEFS[FAEPiece.FP_COLOUR_LOOKUP[is_player_white] + ("N" if is_player_white else "n")],
        b=FAEPiece.IMG_DEFS[FAEPiece.FP_COLOUR_LOOKUP[is_player_white] + ("B" if is_player_white else "b")]
    )

    return _return

            
init python:
    import chess
    import chess.pgn
    import collections
    import subprocess
    # import platform
    import random
    import pygame
    import threading
    import io as StringIO
    import os

    #Only add the chess_games folder if we can even do chess
    if fae_games.is_platform_good_for_chess():
        try:
            file_path = os.path.normcase(config.basedir + fae_chess.CHESS_SAVE_PATH)

            if not os.access(file_path, os.F_OK):
                os.mkdir(file_path)
            fae_chess.CHESS_SAVE_PATH = file_path

        except:
            fae_utilities.fae_log.error("Chess game folder could not be created '{0}'".format(file_path))


    #START: DISPLAYABLES AND RELATED CLASSES
    class FAEChessDisplayableBase(renpy.Displayable):
        """
        Base chess displayable for chess things

        Inherit this for custom implementations like proper games or for teaching use
        """
        MOUSE_EVENTS = (
            pygame.MOUSEMOTION,
            pygame.MOUSEBUTTONUP,
            pygame.MOUSEBUTTONDOWN
        )

        #Put the static vars up here
        SAYORI_WAITTIME = 50
        # SAYORI_DEPTH = 1
        SAYORI_OPTIMISM = 33
        # SAYORI_THREADS = 1

        START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        BOARD_IMAGE = Image("mod_assets/games/chess/chess_board.png")
        PIECE_HIGHLIGHT_RED_IMAGE = Image("mod_assets/games/chess/piece_highlight_red.png")
        PIECE_HIGHLIGHT_GREEN_IMAGE = Image("mod_assets/games/chess/piece_highlight_green.png")
        PIECE_HIGHLIGHT_YELLOW_IMAGE = Image("mod_assets/games/chess/piece_highlight_yellow.png")
        PIECE_HIGHLIGHT_MAGENTA_IMAGE = Image("mod_assets/games/chess/piece_highlight_magenta.png")
        MOVE_INDICATOR_PLAYER = Image("mod_assets/games/chess/move_indicator_player.png")
        MOVE_INDICATOR_SAYORI = Image("mod_assets/games/chess/move_indicator_sayori.png")

        #The sizes of the images.
        BOARD_BORDER_WIDTH = 15
        BOARD_BORDER_HEIGHT = 15
        PIECE_WIDTH = 57
        PIECE_HEIGHT = 57
        BOARD_WIDTH = BOARD_BORDER_WIDTH * 2 + PIECE_WIDTH * 8
        BOARD_HEIGHT = BOARD_BORDER_HEIGHT * 2 + PIECE_HEIGHT * 8

        INDICATOR_HEIGHT = 96
        BUTTON_WIDTH = 120
        BUTTON_HEIGHT = 35
        BUTTON_INDICATOR_X_SPACING = 10
        BUTTON_Y_SPACING = 10

        #Vertical and horizontal offsets to modify the position of the entire board and game
        #NOTE: These are from the left/bottom of the screen respectively
        DISP_X_OFFSET = 200
        DISP_Y_OFFSET = 200

        ##Calculate positions
        #X and Y positions of the TOP LEFT corner of the board
        BOARD_X_POS = int(1280 - BOARD_WIDTH - DISP_X_OFFSET)
        BOARD_Y_POS = int(720 - BOARD_HEIGHT - DISP_Y_OFFSET)

        #Base piece positions
        BASE_PIECE_Y = BOARD_Y_POS + BOARD_BORDER_HEIGHT
        BASE_PIECE_X = BOARD_X_POS + BOARD_BORDER_WIDTH

        #X position of buttons/indicator
        BUTTON_INDICATOR_X = int(BOARD_X_POS + BOARD_WIDTH + BUTTON_INDICATOR_X_SPACING)

        #Indicator Y position
        INDICATOR_Y = int(BOARD_Y_POS + ((BOARD_HEIGHT - INDICATOR_HEIGHT)/ 2))

        #Absolute indicator position
        INDICATOR_POS = (BUTTON_INDICATOR_X, INDICATOR_Y)

        #Button Positions
        DRAWN_BUTTON_Y_TOP = BOARD_Y_POS
        DRAWN_BUTTON_Y_MID = DRAWN_BUTTON_Y_TOP + BUTTON_HEIGHT + BUTTON_Y_SPACING
        DRAWN_BUTTON_Y_MID_LOW = DRAWN_BUTTON_Y_MID + BUTTON_HEIGHT + BUTTON_Y_SPACING
        DRAWN_BUTTON_Y_BOT = BOARD_Y_POS + BOARD_HEIGHT - BUTTON_HEIGHT

        #Win states
        STATE_BLACK_WIN = "0-1"
        STATE_WHITE_WIN = "1-0"

        #Reflect over x, reflect over y tuples
        COORD_REFLECT_DEFS = {
            True: (False, True), #White reflects over y
            False: (True, False) #Black reflects over x
        }

        #Button handling bits
        def __init__(
            self,
            is_player_white,
            pgn_game=None,
            starting_fen=None,
            casual_rules=False,
            player_move_prompts=None,
            sayori_move_quips=None
        ):
            renpy.Displayable.__init__(self)

            #Some core vars
            self.num_turns = 0
            self.move_stack = list()
            self.casual_rules = casual_rules

            #Are we sensitive to the user input?
            self.sensitive = True

            #TODO: Make these quips category ordered so we can have specialized ones for different scenarios
            self.player_move_prompts = player_move_prompts
            self.sayori_move_quips = sayori_move_quips

            #Check if these exist, if not we add them in and default them to empty lists
            if "_visible_buttons" not in self.__dict__:
                self._visible_buttons = list()

            if "_visible_buttons_winner" not in self.__dict__:
                self._visible_buttons_winner = list()

            #Now handle setup for a potential engine
            self.additional_setup()

            # Board for integration with python-chess.
            self.board = None

            self.undo_count = 0
            self.move_history = list()

            #If we're basing off an existing pgn, let's load the relevant data
            if pgn_game:
                #Casual rules
                self.casual_rules = eval(pgn_game.headers.get("CasualRules", "False"))

                #Correct the starting FEN
                self.starting_fen = pgn_game.headers.get("FEN", "None")

                #Load this game into the board, push turns
                self.board = FAEBoard.from_board(pgn_game.board(), self.casual_rules)

                #Now push all the moves
                for move in pgn_game.main_line():
                    self.board.push(move)

                #Whose turn?
                self.current_turn = self.board.turn

                #Colors?
                self.is_player_white = fae_chess._get_player_colour(pgn_game)

                #Last move
                last_move = self.board.peek().uci()
                self.last_move_src, self.last_move_dst = FAEChessDisplayableBase.uci_to_coords(last_move)

                #Practice mode
                self.practice_mode = eval(pgn_game.headers.get("Practice", "False"))

                #Check if we lost in practice
                self.practice_lost = eval(pgn_game.headers.get("PracticeLost", "False"))

                #Undo count
                self.undo_count = int(pgn_game.headers.get("UndoCount", 0))

                #Move history
                self.move_history = eval(pgn_game.headers.get("MoveHist", "[]"))

                #And finally, the fullmove number
                self.num_turns = self.board.fullmove_number

            else:
                #Start off with traditional board, or initialize with the starting fen if using a custom scenario
                self.board = FAEBoard(fen=starting_fen, casual_rules=casual_rules)

                #Stuff we need to save to the board
                self.today_date = datetime.date.today().strftime("%Y.%m.%d")

                #New board, so white goes first
                self.current_turn = chess.WHITE

                #However, if we have a starting FEN, then we need to check who's move it is
                if starting_fen is not None:
                    ind_of_space = starting_fen.find(' ')

                    #Verify validity of this and only set if we can. Otherwise we'll assume the stock order (white's turn)
                    if ind_of_space > 0:
                        self.current_turn = starting_fen[ind_of_space + 1 : ind_of_space + 2] == 'w'

                #Set up player colour
                self.is_player_white = is_player_white

                #Set up last move
                self.last_move_src = None
                self.last_move_dst = None

            self.selected_piece = None
            self.possible_moves = set([])
            self.is_game_over = False

            #If this's true, we interrupt the game loop and hide the displayable
            self.quit_game = False

            #Set up a pgn (could be None, in which case we are playing a fresh game)
            self.pgn_game = pgn_game

            #Requested highlights to draw, contains board-coord tuples of squares to highlight
            self.requested_highlights = set()

            #If it's Sayori's turn, send her the board positions so that she can start analyzing.
            if not self.is_player_turn():
                self.start_sayori_analysis()

            #Set buttons
            self.set_button_states()

            #Now run a conversion to turn all `chess.Piece`s into `FAEPiece`s
            self.piece_map = dict()
            self.update_pieces()

        #START: NON-IMPLEMENTED FUNCTIONS
        def additional_setup(self):
            """
            Additional setup instructions for the displayable

            Implement to use an engine or add some other setup

            NOTE: IMPLEMENTATION OF THIS IS OPTIONAL.
            It is only required to initialize a chess engine
            """
            return

        def start_sayori_analysis(self):
            """
            Starts Sayori's analysis of the board

            Implement to allow a chess engine to analyze the board and begin predicting moves

            NOTE: IMPLEMENTATION OF THIS IS OPTIONAL.
            It is only required if and only if we want Sayori to play using an engine rather than manually queued moves
            """
            return NotImplemented

        def poll_sayori_move(self):
            """
            Polls for a Sayori move

            Implement to automate Sayori's moves (use for an engine)

            NOTE: IMPLEMENTATION OF THIS IS OPTIONAL.
            It is only required if and only if we want Sayori to play using an engine rather than manually queued moves
            """
            return NotImplemented

        def set_button_states(self):
            """
            Sets button states

            NOTE: IMPLEMENTATION OF THIS IS OPTIONAL.
            If is only required for chess displayables which would need to manage any buttons for states
            """
            return NotImplemented

        def check_buttons(self, ev, x, y, st):
            """
            Runs button checks/functions if pressed

            Should be implemnted as necessary for provided buttons

            NOTE: REQUIRED for displayables with buttons added, otherwise their actions will never execute

            THROWS:
                NotImplementedError - Provided the displayable has buttons and is run
            """
            raise NotImplementedError("Function 'check_buttons' was not implemented.")

        def handle_sayori_move(self):
            """
            Handles Sayori's move

            Re-implement to allow Sayori's moves to be handled by an engine
            """
            if not self.move_stack:
                return

            move_str = self.move_stack.pop(0)

            self.__push_move(move_str)

        def handle_player_move(self, *args):
            """
            Handles the player's move

            Re-implement to allow the player to move pieces
            """
            if self.is_game_over:
                return

            if not self.move_stack:
                return

            move_str = self.move_stack.pop(0)

            self.__push_move(move_str)

        #END: Non-implemented functions
        def toggle_sensitivity(self):
            """
            Toggles sensitivity of this displayable

            OUT:
                new sensitivity as a boolean
            """
            self.sensitive = not self.sensitive
            return self.sensitive

        def queue_move(self, move_str):
            """
            Queues a move to the player move stack

            IN:
                move_str - uci move string
            """
            self.move_stack.append(move_str)

        def is_player_turn(self):
            """
            Checks if it's currently the player's turn
            """
            return self.is_player_white == self.current_turn

        def check_redraw(self):
            """
            Checks if we need to redraw the FAEPieces on the board and redraws if necessary
            """
            if self.board.request_redraw:
                self.update_pieces()

            self.board.request_redraw = False

        def update_pieces(self):
            """
            Updates the position of all FAEPieces
            """
            #Empty the piece map
            self.piece_map = dict()

            #And refill it
            for position, Piece in self.board.piece_map().items():
                FAEPiece.fromPiece(
                    Piece,
                    FAEChessDisplayableBase.square_to_board_coords(position),
                    self.piece_map
                )

        def get_piece_at(self, px, py):
            """
            Gets the piece at the given coordinates

            OUT:
                chess.Piece if exists at that location
                None otherwise
            """
            return self.piece_map.get((px, py), None)

        def request_highlight(self, board_pos):
            """
            Requests the renderer to draw a highlight on the square at the specified square

            IN:
                board_pos - position string representing the board square to highlight (example a2)
            """
            x = FAEChessDisplayableBase.uci_alpha_to_x_coord(board_pos[0])
            y = int(board_pos[1]) - 1

            self.requested_highlights.add((x, y))

        def remove_highlight(self, board_pos):
            """
            Removes a requested highlight from the board-coordinates provided

            IN:
                board_pos - position string representing the board square to remove the highlight
            """
            x = FAEChessDisplayableBase.uci_alpha_to_x_coord(board_pos[0])
            y = int(board_pos[1]) - 1

            self.requested_highlights.discard((x, y))

        def __push_move(self, move_str):
            """
            Internal function which pushes a uci move to the board and all FAEPieces, handling promotions as necessary

            IN:
                move_str - uci string representing the move to push

            NOTE: This does NOT verify validity
            """
            #Step 1: Get our move locations
            (x1, y1), (x2, y2) = FAEChessDisplayableBase.uci_to_coords(move_str)

            #Now get the piece
            piece = self.get_piece_at(x1, y1)

            #Move the piece
            piece.move(x2, y2)

            #Promote it if we need to
            if len(move_str) > 4:
                piece.promote_to(move_str[4])

            #Add this undo if it's the player's turn
            if self.is_player_turn():
                self.move_history.append(self.board.fen())

            self.last_move_src = (x1, y1)
            self.last_move_dst = (x2, y2)

            #We push the move here because we need to update fens and game history
            self.board.push_uci(move_str)

            #Check if we need to redraw FAEPieces
            self.check_redraw()

            #'not self.current_turn' is the equivalent of saying the current turn is Black's turn, as chess.BLACK is False
            if not self.current_turn:
                self.num_turns += 1

            #It's player's turn
            self.current_turn = not self.current_turn
            self.is_game_over = self.board.is_game_over()

        def game_loop(self):
            """
            Runs the game loop
            """
            while not self.quit_game:
                # Sayori turn actions
                if not self.is_player_turn() and not self.is_game_over:
                    renpy.show("sayori 1dsc")
                    renpy.say(
                        m,
                        renpy.random.choice(
                            self.sayori_move_quips["check"] if self.board.is_check() else self.sayori_move_quips["generic"]
                        ),
                        False
                    )
                    store._history_list.pop()
                    self.handle_sayori_move()

                # prepare a quip before the player turn loop
                should_update_quip = False
                quip = renpy.random.choice(
                    self.player_move_prompts["check"] if self.board.is_check() else self.player_move_prompts["generic"]
                )

                # player turn actions
                # 'is_game_over' is to allow interaction at the end of the game
                while self.is_player_turn() or self.is_game_over:
                    # we always reshow Sayori here
                    renpy.show("sayori 1eua")
                    if not self.is_game_over:
                        if (
                            should_update_quip
                            and "{fast}" not in quip
                        ):
                            quip = quip + "{fast}"

                        should_update_quip = True
                        renpy.say(m, quip, False)
                        store._history_list.pop()

                    # interactions are handled in the event method
                    interaction = ui.interact(type="minigame")
                    # Check if the palyer wants to quit the game
                    if self.quit_game:
                        return interaction
            return None

        def show(self):
            """
            Shows this displayable
            """
            ui.layer("minigames")
            ui.implicit_add(self)
            ui.close()

        def hide(self):
            """
            Hides this displayable
            """
            ui.layer("minigames")
            ui.remove(self)
            ui.close()

        def is_player_winner(self):
            """
            Checks if Sayori has won the game

            OUT:
                boolean:
                    - True if Sayori has won the game
                    - False if not, or the game is still in progress
            """
            result = self.board.result()

            return(
                (result == FAEChessDisplayableBase.STATE_WHITE_WIN and self.is_player_white) #Player is white, so sayori is black
                or (result == FAEChessDisplayableBase.STATE_BLACK_WIN and not self.is_player_white) #Player is black, so sayori is white
            )

        # Renders the board, pieces, etc.
        def render(self, width, height, st, at):
            #SETUP
            #The Render object we'll be drawing into.
            renderer = renpy.Render(width, height)

            # Prepare the board as a renderer.
            board = renpy.render(FAEChessDisplayableBase.BOARD_IMAGE, 1280, 720, st, at)

            # Prepare the highlights as a renderers.
            highlight_red = renpy.render(FAEChessDisplayableBase.PIECE_HIGHLIGHT_RED_IMAGE, 1280, 720, st, at)
            highlight_green = renpy.render(FAEChessDisplayableBase.PIECE_HIGHLIGHT_GREEN_IMAGE, 1280, 720, st, at)
            highlight_yellow = renpy.render(FAEChessDisplayableBase.PIECE_HIGHLIGHT_YELLOW_IMAGE, 1280, 720, st, at)
            highlight_magenta = renpy.render(FAEChessDisplayableBase.PIECE_HIGHLIGHT_MAGENTA_IMAGE, 1280, 720, st, at)

            #Get our mouse pos
            mx, my = fae_getMousePos()

            #Since different buttons show during the game vs post game, we'll sort out what's shown here
            visible_buttons = list()
            if self.is_game_over:
                # point to the correct visible button list
                visible_buttons = [
                    (b.render(width, height, st, at), b.xpos, b.ypos)
                    for b in self._visible_buttons_winner
                ]

            else:
                # otherwise use the regular buttons list
                visible_buttons = [
                    (b.render(width, height, st, at), b.xpos, b.ypos)
                    for b in self._visible_buttons
                ]

            #(Re)draw the board.
            renderer.blit(board, (FAEChessDisplayableBase.BOARD_X_POS, FAEChessDisplayableBase.BOARD_Y_POS))

            # Draw the move indicator
            renderer.blit(
                renpy.render((
                        FAEChessDisplayableBase.MOVE_INDICATOR_PLAYER
                        if self.is_player_turn() else
                        FAEChessDisplayableBase.MOVE_INDICATOR_SAYORI
                    ),
                    1280, 720, st, at),
                FAEChessDisplayableBase.INDICATOR_POS
            )

            #Draw the buttons
            for b in visible_buttons:
                renderer.blit(b[0], (b[1], b[2]))

            #If we have a last move, we should render that now
            if self.last_move_src and self.last_move_dst:
                #Get our highlight colour
                highlight = highlight_magenta if self.is_player_turn() else highlight_green

                #Render the from highlight
                renderer.blit(
                    highlight,
                    FAEChessDisplayableBase.board_coords_to_screen_coords(
                        self.last_move_src,
                        FAEChessDisplayableBase.COORD_REFLECT_DEFS[self.is_player_white]
                    )
                )
                #And the to highlight
                renderer.blit(
                    highlight,
                    FAEChessDisplayableBase.board_coords_to_screen_coords(
                        self.last_move_dst,
                        FAEChessDisplayableBase.COORD_REFLECT_DEFS[self.is_player_white]
                    )
                )

            #Do possible move highlighting here
            if self.selected_piece and self.possible_moves:
                #There's possible moves, we need to filter things out
                possible_moves_to_draw = filter(
                    lambda x: FAEChessDisplayableBase.square_to_board_coords(x.from_square) == (self.selected_piece[0], self.selected_piece[1]),
                    self.possible_moves
                )

                for move in possible_moves_to_draw:
                    renderer.blit(
                        highlight_green,
                        FAEChessDisplayableBase.board_coords_to_screen_coords(
                            FAEChessDisplayableBase.square_to_board_coords(move.to_square),
                            FAEChessDisplayableBase.COORD_REFLECT_DEFS[self.is_player_white]
                        )
                    )

            #Now render requested highlights if any
            for hl in self.requested_highlights:
                renderer.blit(highlight_yellow, FAEChessDisplayableBase.board_coords_to_screen_coords(hl))

            #Draw the pieces on the Board renderer.
            for piece_location, Piece in self.piece_map.items():
                #Unpack the location
                ix, iy = piece_location

                #Copy this for future use
                iy_orig = iy
                ix_orig = ix

                #White
                if self.is_player_white:
                    iy = 7 - iy

                #Black
                else:
                    #Black player should be reversed X
                    ix = 7 - ix

                x, y = FAEChessDisplayableBase.board_coords_to_screen_coords((ix, iy))

                #Don't render the currently held piece again
                if (
                    self.selected_piece is not None
                    and ix_orig == self.selected_piece[0]
                    and iy_orig == self.selected_piece[1]
                ):
                    renderer.blit(highlight_yellow, (x, y))
                    continue

                piece = self.get_piece_at(ix_orig, iy_orig)

                possible_move_str = None
                blit_rendered = False

                if piece is None:
                    continue

                if (
                    self.selected_piece is None
                    and not self.is_game_over
                    and self.is_player_turn()
                    and mx >= x and mx < x + FAEChessDisplayableBase.PIECE_WIDTH
                    and my >= y and my < y + FAEChessDisplayableBase.PIECE_HEIGHT
                    and (
                        (piece.is_white and self.is_player_white)
                        or (not piece.is_white and not self.is_player_white)
                    )
                ):
                    renderer.blit(highlight_green, (x, y))

                #Winner check
                if self.is_game_over:
                    result = self.board.result()

                    #Black won
                    if piece.symbol == "K" and result == FAEChessDisplayableBase.STATE_BLACK_WIN:
                        renderer.blit(highlight_red, (x, y))

                    #White won
                    elif piece.symbol == "k" and result == FAEChessDisplayableBase.STATE_WHITE_WIN:
                        renderer.blit(highlight_red, (x, y))

                #Render the piece
                piece.render(width, height, st, at, x, y, renderer)

            if self.selected_piece is not None:
                #Draw the selected piece.
                piece = self.get_piece_at(self.selected_piece[0], self.selected_piece[1])

                px, py = fae_getMousePos()
                px -= FAEChessDisplayableBase.PIECE_WIDTH / 2
                py -= FAEChessDisplayableBase.PIECE_HEIGHT / 2
                piece.render(width, height, st, at, px, py, renderer)

            #Ask that we be re-rendered ASAP, so we can show the next frame.
            renpy.redraw(self, 0)

            #Return the Render object.
            return renderer

        #Handles events.
        def event(self, ev, x, y, st):
            #Buttons are always sensitive since they are only semi-part of this displayable
            #Are we in mouse button things
            if ev.type in self.MOUSE_EVENTS:
                ret_value = None
                #Run button checks if there are any in a function which requires implementation
                if self._visible_buttons or self._visible_buttons_winner:
                    ret_value = self.check_buttons(ev, x, y, st)

                if ret_value is not None:
                    return ret_value

            elif config.developer and ev.type == pygame.KEYDOWN:
                # debug keys for dev testing
                if ev.key == pygame.K_d:
                    # toggle draw button state
                    if self._button_draw.disabled:
                        self._button_draw.enable()
                    else:
                        self._button_draw.disable()

            #Board events however respect the displayable state
            if self.sensitive:
                # Mousebutton down == possibly select the piece to move
                if (
                    ev.type == pygame.MOUSEBUTTONDOWN
                    and ev.button == 1
                    and not self.is_game_over# don't allow to move pieces if the game is over
                ):
                    # continue
                    px, py = self.get_piece_pos()
                    test_piece = self.get_piece_at(px, py)
                    if (
                        self.is_player_turn()
                        and test_piece is not None
                        and (
                            (test_piece.is_white and self.is_player_white)
                            or (not test_piece.is_white and not self.is_player_white)
                        )
                    ):
                        piece = test_piece

                        self.possible_moves = self.board.legal_moves
                        self.selected_piece = (px, py)
                        return "mouse_button_down"

                # Mousebutton up == possibly release the selected piece
                if (
                    ev.type == pygame.MOUSEBUTTONUP
                    and ev.button == 1
                ):
                    self.handle_player_move()

                    self.selected_piece = None
                    self.possible_moves = set([])
                    return "mouse_button_up"

            return None

        def get_piece_pos(self):
            """
            Gets the piece position of the current piece held by the mouse

            OUT:
                Tuple of coordinates (x, y) marking where the piece is
            """
            mx, my = fae_getMousePos()
            mx -= FAEChessDisplayableBase.BASE_PIECE_X
            my -= FAEChessDisplayableBase.BASE_PIECE_Y
            px = mx / FAEChessDisplayableBase.PIECE_WIDTH
            py = my / FAEChessDisplayableBase.PIECE_HEIGHT

            #White
            if self.is_player_white:
                py = 7 - py

            #Black
            else:
                #Black player should be reversed X
                px = 7 - px

            if py >= 0 and py < 8 and px >= 0 and px < 8:
                return (px, py)

            return (None, None)

        @staticmethod
        def coords_to_uci(x, y):
            """
            Converts board coordinates to a uci move

            IN:
                x - x co-ord of the piece
                y - y co-ord of the piece

            OUT:
                the move represented in the uci form
            """
            x = chr(x + ord('a'))
            y += 1
            return "{0}{1}".format(x, y)

        @staticmethod
        def uci_to_coords(uci):
            """
            Converts uci to board-coordinates

            IN:
                uci - uci move to convert to coords

            OUT:
                list of tuples, [(x1, y1), (x2, y2)] representing from coords -> to coords
            """
            x1 = FAEChessDisplayableBase.uci_alpha_to_x_coord(uci[0])
            x2 = FAEChessDisplayableBase.uci_alpha_to_x_coord(uci[2])
            y1 = int(uci[1]) - 1
            y2 = int(uci[3]) - 1

            return [(x1, y1), (x2, y2)]

        @staticmethod
        def uci_alpha_to_x_coord(alpha):
            """
            Converts a uci alphabet (a-h) to an x-coord for the board

            IN:
                alpha - alphabet to convert to a board x-coord
            """
            return ord(alpha) - 97

        @staticmethod
        def square_to_board_coords(sq_num):
            """
            Converts from square number to board coords

            IN:
                sq_num - square number to convert

            OUT:
                tuple - (x, y) coords representing board coordinates for the square provided
            """
            return (sq_num % 8, sq_num / 8)

        @staticmethod
        def board_coords_to_screen_coords(pos_tuple, inversion_tuple=(False,False)):
            """
            Converts board coordinates to (x, y) coordinates to use to position things on screen

            IN:
                pos_tuple - (x, y) tuple representing coordinates which need to be converted
                inversion_tuple - (x_invert, y_invert) tuple representing direction to invert piece coords

            OUT:
                Tuple - (x, y) coordinates for the screen to use
            """
            x = pos_tuple[0]
            y = pos_tuple[1]

            if inversion_tuple[0]:
                x = FAEChessDisplayableBase.invert_coord(x)
            if inversion_tuple[1]:
                y = FAEChessDisplayableBase.invert_coord(y)

            return (
                int(FAEChessDisplayableBase.BASE_PIECE_X + (x * FAEChessDisplayableBase.PIECE_WIDTH)),
                int(FAEChessDisplayableBase.BASE_PIECE_Y + (y * FAEChessDisplayableBase.PIECE_HEIGHT))
            )

        @staticmethod
        def invert_coord(value):
            """
            Inverts a board coordinate

            IN:
                value - coordinate part (x or y) to invert
            """
            return 7 - value


    class FAEPiece(object):
        """
        FAEChessPiece

        A better implementation of chess.Piece which also manages piece location in addition to colour and symbol

        PROPERTIES:
            colour - Color of the piece:
                True - white
                False - black
            symbol - letter symbol representing the piece. If capital, the piece is white
            piece_map - the map containing all the pieces (the FAEPiece object will be stored in it)
            x_pos - x coordinate of this piece on the board
            y_pos - y coordinate of this piece on the board
        """

        #Default base piece filepath
        DEF_PIECE_FP_BASE = "mod_assets/games/chess/pieces/{0}{1}.png"

        #Color map
        FP_COLOUR_LOOKUP = {
            True: "w",
            False: "b"
        }

        IMG_DEFS = {
            colour + (symbol.upper() if colour == "w" else symbol): Image("mod_assets/games/chess/pieces/{0}{1}.png".format(colour, (symbol.upper() if colour == "w" else symbol)))
            for colour in FP_COLOUR_LOOKUP.values()
            for symbol in fae_chess.PIECE_POOL
        }

        def __init__(
            self,
            is_white,
            symbol,
            posX,
            posY,
            piece_map
        ):
            """
            FAEPiece constructor

            IN:
                is_white - Whether or not the piece is white
                symbol - letter symbol representing the piece. If capital, the piece is white
                posX - x position of the piece
                posY - y position of the piece
                piece_map - Map to store this piece in
            """
            self.is_white = is_white
            self.symbol = symbol

            #Store an internal reference to the piece map so we can execute moves from the piece
            self.piece_map = piece_map

            #Store the internal reference to this piece's image fp for use in rendering
            self.__piece_image = FAEPiece.IMG_DEFS[FAEPiece.FP_COLOUR_LOOKUP[is_white] + symbol]

            #Internal reference to the position
            self.x_pos = posX
            self.y_pos = posY

            #And add it to the piece map
            piece_map[(posX, posY)] = self

        def __eq__(self, other):
            """
            Checks if this piece is the same as another piece
            """
            if not isinstance(other, FAEPiece):
                return False
            return self.symbol == other.symbol

        def __repr__(self):
            """
            Handles a representation of this piece
            """
            return "FAEPiece which: {0} and symbol: {1}".format("is white" if self.is_white else "is black", self.symbol)

        @staticmethod
        def fromPiece(piece, pos_tuple, piece_map):
            """
            Initializes a FAEPiece from a chess.Piece object

            IN:
                piece - piece to base the FAEPiece off of
                pos_tuple - (x, y) tuple representing the piece's board coords

                SEE: __init__ for the rest of the parameters

            OUT:
                FAEPiece
            """
            return FAEPiece(
                piece.colour,
                piece.symbol(),
                pos_tuple[0],
                pos_tuple[1],
                piece_map
            )

        def get_type(self):
            """
            Gets the type of piece as the lowercase letter that is its symbol

            OUT:
                The lower only symbol, representing the type of piece this is
            """
            return self.symbol.lower()

        def get_location(self):
            """
            Gets the location of this piece

            OUT:
                Tuple, (x, y) coords representing the location of the piece on the board
            """
            return (self.x_pos, self.y_pos)

        def promote_to(self, promoted_piece_symbol):
            """
            Promotes this piece and builds a new render for it

            IN:
                promoted_piece_symbol - Symbol representing the piece we're promoting to
            """
            self.symbol = promoted_piece_symbol.upper() if self.is_white else promoted_piece_symbol
            #Update the piece image
            self.__piece_image = FAEPiece.IMG_DEFS[FAEPiece.FP_COLOUR_LOOKUP[self.is_white] + self.symbol]

        def move(self, new_x, new_y):
            """
            Moves the piece from the given position, to the given position
            """
            self.piece_map.pop((self.x_pos, self.y_pos))

            #Adjust internal positions
            self.x_pos = new_x
            self.y_pos = new_y

            #Add back to the piece map
            self.piece_map[(new_x, new_y)] = self

        def render(self, width, height, st, at, x, y, renderer):
            """
            Internal render call to render the pieces. To be called by the board

            IN:
                width - screen width
                height - screen height
                st - start time
                at - animation time
                x - x position on the board to render the piece
                y - y position on the board to render the piece
                renderer to draw this piece on
            """
            renderer.blit(
                renpy.render(self.__piece_image, width, height, st, at),
                (x, y)
            )

    class FAEBoard(chess.Board):
        """
        Extension class for the chess.Board class
        """
        def __init__(self, fen=None, chess960=False, casual_rules=False):
            """
            FAEBoard constructor

            IN (New property):
                casual_rules:
                    - Whether or not we'll be using casual rules
                    (Default: False)

            Same as chess.Board constructor, adds two properties
            """
            if fen is None:
                fen = chess.STARTING_FEN

            super(FAEBoard, self).__init__(fen, chess960)

            #Flag for needing to request a redraw for the board
            self.request_redraw = False
            self.casual_rules = casual_rules

        @staticmethod
        def from_board(Board, casual_rules=False):
            """
            Initializes a FAEBoard from a chess.Board

            IN:
                Board - chess.Board to convert
                casual_rules - Whether or not we're using casual rules

            OUT:
                FAEBoard object representing the given Board.
            """
            return FAEBoard(Board.fen(), Board.chess960, casual_rules)

        def push(self, move):
            """
            push override

            Updates the position with the given move and puts it onto the
            move stack

            Also sets a flag which the FAEChessDisplayableBase can use to manage redrawing FAEPieces

            IN:
                chess.Move to push
            """
            # Remember game state.
            self.stack.append(chess._BoardState(self))
            self.move_stack.append(move)

            move = self._to_chess960(move)

            # Reset en passant square.
            ep_square = self.ep_square
            self.ep_square = None

            # Increment move counters.
            self.halfmove_clock += 1
            if not self.turn:
                self.fullmove_number += 1

            # On a null move, simply swap turns and reset the en passant square.
            if not move:
                self.turn = not self.turn
                return

            # Drops.
            if move.drop:
                self._set_piece_at(move.to_square, move.drop, self.turn)
                self.turn = not self.turn
                return

            # Zero the half-move clock.
            if self.is_zeroing(move):
                self.halfmove_clock = 0

            from_bb = chess.BB_SQUARES[move.from_square]
            to_bb = chess.BB_SQUARES[move.to_square]

            promoted = self.promoted & from_bb
            piece_type = self._remove_piece_at(move.from_square)
            capture_square = move.to_square
            captured_piece_type = self.piece_type_at(capture_square)

            #Update castling rights
            self.castling_rights = self.clean_castling_rights() & ~to_bb & ~from_bb

            if piece_type == chess.KING and not promoted:
                if self.turn:
                    self.castling_rights &= ~chess.BB_RANK_1
                else:
                    self.castling_rights &= ~chess.BB_RANK_8

            elif captured_piece_type == chess.KING and not self.promoted & to_bb:
                if self.turn and chess.square_rank(move.to_square) == 7:
                    self.castling_rights &= ~chess.BB_RANK_8

                elif not self.turn and chess.square_rank(move.to_square) == 0:
                    self.castling_rights &= ~chess.BB_RANK_1

            #Handle special pawn moves
            if piece_type == chess.PAWN:
                diff = move.to_square - move.from_square

                if diff == 16 and chess.square_rank(move.from_square) == 1:
                    self.ep_square = move.from_square + 8

                elif diff == -16 and chess.square_rank(move.from_square) == 6:
                    self.ep_square = move.from_square - 8

                elif move.to_square == ep_square and abs(diff) in [7, 9] and not captured_piece_type:
                    #Remove pawns captured en passant
                    down = -8 if self.turn == chess.WHITE else 8
                    capture_square = ep_square + down
                    captured_piece_type = self._remove_piece_at(capture_square)

                    #FAEPiece needs to redraw, ASAP
                    self.request_redraw = True

            #Promotion
            if move.promotion:
                promoted = True
                piece_type = move.promotion

            #Castling
            castling = piece_type == chess.KING and self.occupied_co[self.turn] & to_bb

            if castling:
                a_side = chess.square_file(move.to_square) < chess.square_file(move.from_square)

                self._remove_piece_at(move.from_square)
                self._remove_piece_at(move.to_square)

                if a_side:
                    self._set_piece_at(chess.C1 if self.turn == chess.WHITE else chess.C8, chess.KING, self.turn)
                    self._set_piece_at(chess.D1 if self.turn == chess.WHITE else chess.D8, chess.ROOK, self.turn)

                else:
                    self._set_piece_at(chess.G1 if self.turn == chess.WHITE else chess.G8, chess.KING, self.turn)
                    self._set_piece_at(chess.F1 if self.turn == chess.WHITE else chess.F8, chess.ROOK, self.turn)

                #FAEPiece needs to redraw, ASAP
                self.request_redraw = True

            # Put the piece on the target square.
            if not castling and piece_type:
                was_promoted = self.promoted & to_bb
                self._set_piece_at(move.to_square, piece_type, self.turn, promoted)

                if captured_piece_type:
                    self._push_capture(move, capture_square, captured_piece_type, was_promoted)

            # Swap turn.
            self.turn = not self.turn

        def result(self, claim_draw=False):
            """
            Gets the game result.

            ``1-0``, ``0-1`` or ``1/2-1/2`` if the
            :func:`game is over <chess.Board.is_game_over()>`. Otherwise, the
            result is undetermined: ``*``.
            """
            # Chess variant support.
            if self.is_variant_loss():
                return "0-1" if self.turn == chess.WHITE else "1-0"
            elif self.is_variant_win():
                return "1-0" if self.turn == chess.WHITE else "0-1"
            elif self.is_variant_draw():
                return "1/2-1/2"

            #Checkmate
            if self.is_checkmate():
                #self.turn being True means white turn
                return "0-1" if self.turn else "1-0"

            #Draw claimed
            if claim_draw and self.can_claim_draw():
                return "1/2-1/2"

            #Seventyfive-move rule or fivefold repetition
            if self.is_seventyfive_moves() or self.is_fivefold_repetition():
                return "1/2-1/2"

            #Insufficient material
            if self.is_insufficient_material():
                return "1/2-1/2"

            #Stalemate
            if not any(self.generate_legal_moves()):
                if self.casual_rules:
                    return "0-1" if self.turn else "1-0"
                return "1/2-1/2"

            #Still in progress
            return "*"

    class FAEChessDisplayable(FAEChessDisplayableBase):
        def __init__(
            self,
            is_player_white,
            pgn_game=None,
            starting_fen=None,
            practice_mode=False,
            casual_rules=False
        ):

            self.practice_mode = practice_mode
            self.starting_fen = starting_fen
            self.casual_rules = casual_rules

            self.surrendered = False
            self.practice_lost = False

            #Init the 4 buttons
            self._button_save = FAEButtonDisplayable.create_stb(
                _("Save"),
                True,
                FAEChessDisplayableBase.BUTTON_INDICATOR_X,
                FAEChessDisplayableBase.DRAWN_BUTTON_Y_TOP,
                FAEChessDisplayableBase.BUTTON_WIDTH,
                FAEChessDisplayableBase.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            self._button_giveup = FAEButtonDisplayable.create_stb(
                _("Surrender"),
                True,
                FAEChessDisplayableBase.BUTTON_INDICATOR_X,
                FAEChessDisplayableBase.DRAWN_BUTTON_Y_MID,
                FAEChessDisplayableBase.BUTTON_WIDTH,
                FAEChessDisplayableBase.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            self._button_draw = FAEButtonDisplayable.create_stb(
                _("Call Draw"),
                True,
                FAEChessDisplayableBase.BUTTON_INDICATOR_X,
                FAEChessDisplayableBase.DRAWN_BUTTON_Y_MID_LOW,
                FAEChessDisplayableBase.BUTTON_WIDTH,
                FAEChessDisplayableBase.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            #If player is Black, this button is enabled until Sayori's first move.
            #Not sure why, but defaulting buttons to disable at first is fine.
            self._button_draw.disable()

            self._button_done = FAEButtonDisplayable.create_stb(
                _("Done"),
                False,
                FAEChessDisplayableBase.BUTTON_INDICATOR_X,
                FAEChessDisplayableBase.DRAWN_BUTTON_Y_TOP,
                FAEChessDisplayableBase.BUTTON_WIDTH,
                FAEChessDisplayableBase.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            self._button_undo = FAEButtonDisplayable.create_stb(
                _("Undo"),
                True,
                FAEChessDisplayableBase.BUTTON_INDICATOR_X,
                FAEChessDisplayableBase.DRAWN_BUTTON_Y_BOT,
                FAEChessDisplayableBase.BUTTON_WIDTH,
                FAEChessDisplayableBase.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            #Init the base displayable
            super(FAEChessDisplayable, self).__init__(
                is_player_white,
                pgn_game,
                starting_fen,
                casual_rules,
                player_move_prompts={
                    "generic": [
                        "It's your turn, [player].",
                        "Your move, [player]~",
                        "What will you do, I wonder...",
                        "Alright, your turn, [player]~",
                        "You got this, [player]!"
                    ],
                    "check": [
                        "[fae_quipExp('3tfb')]Check!",
                        "[fae_quipExp('3huu')]I've got you now, [player]!",
                        "[fae_quipExp('3hub')]Looks like you're in check!"
                    ]
                },
                sayori_move_quips={
                    "generic": [
                        "Alright, let's see...",
                        "Okay, my turn...",
                        "Let's see what I can do.",
                        "I think I'll try this...",
                        "Okay, I'll move this here then."
                    ],
                    "check": [
                        "[fae_quipExp('1eusdlc')]Uh oh...",
                        "[fae_quipExp('1rksdlc')]Hmm...{w=0.2}I need to get out of this...",
                        "[fae_quipExp('1etc')]What's the right move here..."
                    ]
                }
            )

            if self.practice_mode:
                #Setup the visible buttons list
                self._visible_buttons = [
                    self._button_save,
                    self._button_undo,
                    self._button_giveup,
                    self._button_draw
                ]

                self._visible_buttons_winner = [
                    self._button_done,
                    self._button_undo
                ]

            else:
                self._visible_buttons = [
                    self._button_save,
                    self._button_giveup,
                    self._button_draw
                ]

                self._visible_buttons_winner = [
                    self._button_done
                ]

        def __del__(self):
            self.stockfish.stdin.close()
            self.stockfish.wait()

        def poll_sayori_move(self):
            """
            Polls stockfish for a move for Sayori to make

            OUT:
                move - representing the best move stockfish found
            """
            with self.lock:
                res = None
                while self.queue:
                    line = self.queue.pop()
                    match = re.match(r"^bestmove (\w+)", line)
                    if match:
                        res = match.group(1)

            return res

        def start_sayori_analysis(self):
            """
            Starts Sayori's analysis of the board
            """
            self.stockfish.stdin.write("position fen {0}\n".format(self.board.fen()))
            self.stockfish.stdin.write("go depth {0}\n".format(persistent._fae_chess_difficulty[1]))
            self.stockfish.stdin.write("go movetime {0}\n".format(self.SAYORI_WAITTIME))

        def additional_setup(self):
            """
            Additional stockfish setup to get the game going using it as Sayori's engine
            """
            # Stockfish engine provides AI for the game.
            def open_stockfish(path, startupinfo=None):
                """
                Runs stockfish

                IN:
                    path - filepath to the stockfish application
                    startupinfo - startup flags
                """
                try:
                    return subprocess.Popen(
                        os.path.join(renpy.config.gamedir, path).replace('\\', '/'),
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        startupinfo=startupinfo
                    )

                #Catch the permission error
                except OSError as os_err:
                    if not renpy.windows:
                        renpy.show("sayori", at_list=[t11])
                        renpy.say(s, "Hmm, that's odd. It seems some permissions were changed and I can't get chess running on your system.")
                        renpy.show("sayori 3eua")
                        renpy.say(s, "Hold on a second, [player]. I'm going to try something quickly.{w=0.3}.{w=0.3}.{w=0.3}{nw}")

                        
                        try:
                            stockfish_proc = subprocess.Popen(
                                os.path.join(renpy.config.gamedir, path).replace('\\', '/'),
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                startupinfo=startupinfo
                            )

                            renpy.show("sayori", at_list=[t11])
                            renpy.say(s, "Yay! We should be able to play now~")
                            renpy.show("sayori", at_list=[t21])
                            return stockfish_proc

                        #If it still doesn't work, just log it and fail out
                        except Exception as ex:
                            os_err = ex

                    fae_utilities.fae_log.exception(os_err)
                    renpy.jump("fae_chess_cannot_work_embarrassing")

                #Basically a last resort jump. If this happens it pretty much means you launched FAE from commandline
                except Exception as ex:
                    fae_utilities.fae_log.exception(ex)
                    renpy.jump("fae_chess_cannot_work_embarrassing")

            # Launch the appropriate version based on the architecture and OS.
            if not fae_games.is_platform_good_for_chess():
                # This is the last-resort check, the availability of the chess game should be checked independently beforehand.
                renpy.jump("fae_chess_cannot_work_embarrassing")

            is_64_bit = sys.maxsize > 2**32

            if renpy.windows:
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

                self.stockfish = open_stockfish(
                    'mod_assets/games/chess/stockfish_8_windows_x{0}.exe'.format("64" if is_64_bit else "32"),
                    startupinfo
                )

            elif is_64_bit:
                fp = "mod_assets/games/chess/stockfish_8_{0}_x64".format("linux" if renpy.linux else "macosx")

                os.chmod(config.basedir + "/game/".format(fp), 0755)
                self.stockfish = open_stockfish(fp)

            #Set Sayori's parameters
            self.stockfish.stdin.write("setoption name Skill Level value {0}\n".format(persistent._fae_chess_difficulty[0]))
            self.stockfish.stdin.write("setoption name Contempt value {0}\n".format(self.SAYORI_OPTIMISM))
            self.stockfish.stdin.write("setoption name Ponder value False\n")

            #And set up facilities for asynchronous communication
            self.queue = collections.deque()
            self.lock = threading.Lock()
            thrd = threading.Thread(target=store.fae_chess.enqueue_output, args=(self.stockfish.stdout, self.queue, self.lock))
            thrd.daemon = True
            thrd.start()

        def check_buttons(self, ev, x, y, st):
            """
            Runs button checks/functions if pressed
            """
            # inital check for winner
            if self.is_game_over:
                if self._button_done.event(ev, x, y, st):
                    #User clicks Done
                    self.quit_game = True
                    return self._quitPGN()

                elif self._button_undo.event(ev, x, y, st):
                    return self.undo_move()

            # inital check for buttons
            elif self.is_player_turn():
                if self._button_save.event(ev, x, y, st):
                    wants_save = renpy.call_in_new_context("fae_chess_confirm_context", prompt=_("You'd like to continue later?"))
                    if wants_save:
                        #User wants to save this game
                        self.quit_game = True
                        return self._quitPGN()

                elif self._button_draw.event(ev, x, y, st):
                    #User wants to request a draw
                    self.quit_game = True
                    return self._quitPGN(2)

                elif self._button_undo.event(ev, x, y, st):
                    return self.undo_move()

                elif self._button_giveup.event(ev, x, y, st):
                    wants_quit = renpy.call_in_new_context("fae_chess_confirm_context", prompt=_("Are you sure you want to give up?"))
                    if wants_quit:
                        #User wishes to surrender
                        self.quit_game = True
                        return self._quitPGN(1)

        def undo_move(self):
            """
            Undoes the last move

            OUT:
                None
            """
            #user wants to undo the last move
            #NOTE: While the chess.Board object has a pop function, we cannot use it here due to the nature of saving these as
            #pgn files. As such we pop somewhat inefficiently, but we do it such that the fen can always be used to restore
            last_move_fen = self.move_history.pop(-1)

            #Remove the last move since we've undone
            old_board = self.board
            old_board.move_stack = old_board.move_stack[:len(old_board.move_stack)-2]
            old_board.stack = old_board.stack[:len(old_board.stack)-2]

            #Update the board to the undo
            self.board = FAEBoard(fen=last_move_fen)

            #Now transfer the move data
            self.board.move_stack = old_board.move_stack
            self.board.stack = old_board.stack
            self.board.fullmove_number = old_board.fullmove_number - 1
            #Restore the last move if we can
            if self.board.move_stack:
                last_move_uci = self.board.move_stack[-1].uci()
                self.last_move_src, self.last_move_dst = FAEChessDisplayableBase.uci_to_coords(last_move_uci)

            else:
                self.last_move_src = None
                self.last_move_dst = None

            #Adjust FAEPieces
            self.update_pieces()

            #Increment the undo counter
            self.undo_count += 1

            #If this is checkmate, mark this as a practice loss
            if self.is_game_over:
                self.practice_lost = True
                self.is_game_over = False

            self.set_button_states()
            return None

        def handle_player_move(self):
            """
            Manages player move
            """
            #Sanity check
            if self.is_game_over:
                self.set_button_states()
                return

            px, py = self.get_piece_pos()

            move_str = None

            if px is not None and py is not None and self.selected_piece is not None:
                move_str = self.coords_to_uci(self.selected_piece[0], self.selected_piece[1]) + self.coords_to_uci(px, py)

                #Promote if needed
                if (
                    chess.Move.from_uci(move_str + 'q') in self.possible_moves
                    and self.get_piece_at(self.selected_piece[0], self.selected_piece[1]).get_type() == 'p'
                    and (py == 0 or py == 7)
                ):
                    #Set selected piece to None to drop it
                    self.selected_piece = None

                    #Now call the promotion screen
                    promote = renpy.call_in_new_context("fae_chess_promote_context", self.is_player_white)
                    move_str += promote

            if move_str is None:
                return

            if chess.Move.from_uci(move_str) in self.possible_moves:
                self.__push_move(move_str)
                self.set_button_states()

                #Setup Sayori's go
                if not self.is_game_over:
                    self.start_sayori_analysis()

        def handle_sayori_move(self):
            """
            Manages Sayori's move
            """
            # Poll Sayori for moves if it's her turn
            if not self.is_game_over:
                #Queue a Moni move if this is implemented
                sayori_move = self.poll_sayori_move()

                if sayori_move is not None:
                    #Now verify legality
                    sayori_move_check = chess.Move.from_uci(sayori_move)

                    if self.board.is_legal(sayori_move_check):
                        #Sayori is thonking
                        renpy.pause(1.5)

                        #Push her move
                        self.__push_move(sayori_move)

                        #Set the buttons
                        self.set_button_states()

        def set_button_states(self):
            """
            Manages button states
            """
            if not self.is_game_over and self.is_player_turn():
                #Considering this is a more casual environment, we're using a modified version of the 50 move rule to allow draw requests
                if self.board.halfmove_clock >= 40:
                    self._button_draw.enable()
                else:
                    self._button_draw.disable()

                #Can give up from the get go
                if self.board.fullmove_number > 0:
                    self._button_giveup.enable()

                else:
                    self._button_giveup.disable()

                #At least one move, so we can give up, save, and undo if in practice mode
                if self.board.fullmove_number > 1:
                    self._button_save.enable()

                else:
                    self._button_save.disable()

                #Game isn't over, but since we could undo from a checkmate, we'll disable the done button
                self._button_done.disable()

            else:
                self._button_giveup.disable()
                self._button_save.disable()

                #If the game is over, then we should enable done
                if self.is_game_over:
                    self._button_done.enable()

            #Since we can undo a checkmate, we basically want to be able to undo only if Sayori has checkmated the player
            if (
                self.practice_mode
                and self.move_history
                and self.is_player_turn()
                and not self.is_player_winner()
            ):
                self._button_undo.enable()

            else:
                self._button_undo.disable()

        def _quitPGN(self, quit_reason=0):
            """
            Generates a pgn of the board, and depending on if we are
            doing previous game or not, does appropriate header
            setting

            IN:
                quit_reason - reason the game was quit
                    0 - Normal savegame/victor found
                    1 - Player surrendered
                    2 - Player requested draw
                    (Default: 0)

                giveup - True if the player surrendered, False otherwise
                requested_draw - whether or not the player requested a draw

            RETURNS: tuple of the following format:
                [0]: chess.pgn.Game object of this game
                [1]: True if sayori won, False if not
                [2]: True if player gaveup, False otherwise
                [3]: number of turns of this game
            """
            new_pgn = chess.pgn.Game.from_board(self.board)

            if quit_reason == 1:
                #Player is playing white
                if self.is_player_white:
                    new_pgn.headers["Result"] = FAEChessDisplayableBase.STATE_BLACK_WIN
                #Player is playing black
                else:
                    new_pgn.headers["Result"] = FAEChessDisplayableBase.STATE_WHITE_WIN

            elif quit_reason == 2:
                new_pgn.headers["Result"] = "1/2-1/2"
                #And a special header to indicate this was a requested draw
                new_pgn.headers["DrawRequested"] = True

            #Sayori's ingame name will be her twitter handle
            #Player plays white
            if self.is_player_white:
                new_pgn.headers["White"] = persistent.playername
                new_pgn.headers["Black"] = fae_sayori_twitter_handle

            #Player plays black
            else:
                new_pgn.headers["White"] = fae_sayori_twitter_handle
                new_pgn.headers["Black"] = persistent.playername

            # date, site, and fen
            new_pgn.headers["Site"] = "FAE"
            new_pgn.headers["Date"] = datetime.date.today().strftime("%Y.%m.%d")
            new_pgn.headers["FEN"] = self.starting_fen if self.starting_fen is not None else FAEChessDisplayableBase.START_FEN
            new_pgn.headers["SetUp"] = "1"

            #Hist related to undo + practice mode
            new_pgn.headers["Practice"] = self.practice_mode
            new_pgn.headers["CasualRules"] = self.casual_rules
            new_pgn.headers["MoveHist"] = self.move_history
            new_pgn.headers["UndoCount"] = self.undo_count

            #Store this just to mark the pgn that it was lost in practice
            new_pgn.headers["PracticeLost"] = self.practice_lost

            return (
                new_pgn,
                (
                    (
                        new_pgn.headers["Result"] == FAEChessDisplayableBase.STATE_WHITE_WIN
                        and not self.is_player_white #Player is black, so sayori is white
                    )
                    or (
                        new_pgn.headers["Result"] == FAEChessDisplayableBase.STATE_BLACK_WIN
                        and self.is_player_white #Player is white, so sayori is black
                    )
                ),
                quit_reason == 1, #Did player surrender?
                self.board.fullmove_number
            )