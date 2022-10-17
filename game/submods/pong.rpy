# pong difficulty changes on win / loss. Determines sayori's paddle-movement-cap, the ball's start-speed, max-speed and acceleration.
default persistent._fae_pong_difficulty = 10
# increases the pong difficulty for the next game by the value this is set to. Resets after a finished match.
default persistent._fae_pong_difficulty_change_next_game = 0
# whether the player answered sayori he lets her win on purpose
default persistent._fae_pm_ever_let_sayori_win_on_purpose = False
# the day at which the difficulty change was initiated
default persistent._fae_pong_difficulty_change_next_game_date = datetime.date.today()

define PONG_DIFFICULTY_CHANGE_ON_WIN            = +1
define PONG_DIFFICULTY_CHANGE_ON_LOSS           = -1
define PONG_DIFFICULTY_POWERUP                  = +5
define PONG_DIFFICULTY_POWERDOWN                = -5
define PONG_PONG_DIFFICULTY_POWERDOWNBIG        = -10

#Triggering the same response twice in a row leads to a different response, not all responses reset this (on purpose)
define PONG_SAYORI_RESPONSE_NONE                                                = 0
define PONG_SAYORI_RESPONSE_WIN_AFTER_PLAYER_WON_MIN_THREE_TIMES                = 1
define PONG_SAYORI_RESPONSE_SECOND_WIN_AFTER_PLAYER_WON_MIN_THREE_TIMES         = 2
define PONG_SAYORI_RESPONSE_WIN_LONG_GAME                                       = 3
define PONG_SAYORI_RESPONSE_WIN_SHORT_GAME                                      = 4
define PONG_SAYORI_RESPONSE_WIN_TRICKSHOT                                       = 5
define PONG_SAYORI_RESPONSE_WIN_EASY_GAME                                       = 6
define PONG_SAYORI_RESPONSE_WIN_MEDIUM_GAME                                     = 7
define PONG_SAYORI_RESPONSE_WIN_HARD_GAME                                       = 8
define PONG_SAYORI_RESPONSE_WIN_EXPERT_GAME                                     = 9
define PONG_SAYORI_RESPONSE_WIN_EXTREME_GAME                                    = 10
define PONG_SAYORI_RESPONSE_LOSE_WITHOUT_HITTING_BALL                           = 11
define PONG_SAYORI_RESPONSE_LOSE_TRICKSHOT                                      = 12
define PONG_SAYORI_RESPONSE_LOSE_LONG_GAME                                      = 13
define PONG_SAYORI_RESPONSE_LOSE_SHORT_GAME                                     = 14
define PONG_SAYORI_RESPONSE_LOSE_EASY_GAME                                      = 15
define PONG_SAYORI_RESPONSE_LOSE_MEDIUM_GAME                                    = 16
define PONG_SAYORI_RESPONSE_LOSE_HARD_GAME                                      = 17
define PONG_SAYORI_RESPONSE_LOSE_EXPERT_GAME                                    = 18
define PONG_SAYORI_RESPONSE_LOSE_EXTREME_GAME                                   = 19


define pong_sayori_last_response_id = PONG_SAYORI_RESPONSE_NONE

define played_pong_this_session = False
define fae_pong_taking_break = False
define player_lets_sayori_win_on_purpose = False
define instant_loss_streak_counter = 0
define loss_streak_counter = 0
define win_streak_counter = 0
define lose_on_purpose = False
define sayori_asks_to_go_easy = False

# Need to be set before every game and be accessible outside the class
define ball_paddle_bounces = 0
define powerup_value_this_game = 0
define instant_loss_streak_counter_before = 0
define loss_streak_counter_before = 0
define win_streak_counter_before = 0
define pong_difficulty_before = 0
define pong_angle_last_shot = 0.0



init:

    image bg pong field = "mod_assets/games/pong/pong_field.png"

    python:
        import random
        import math

        class PongDisplayable(renpy.displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                self.paddle = Image("mod_assets/games/pong/pong.png")
                self.ball = Image("mod_assets/games/pong/pong_ball.png")
                self.player = Text(_("[player]"), size=36)
                self.sayori = Text(_("Sayori"), size=36)
                self.ctb = Text(_("Click to begin!"), size=36)

                self.playsounds = True
                self.soundboop = "mod_assets/sounds/pong_sounds/pong_boop.wav"
                self.soundbeep = "mod_assets/sounds/pong_sounds/pong_beep.wav"

                self.PADDLE_WIDTH = 8
                self.PADDLE_HEIGHT = 79
                self.PADDLE_RADIUS = self.PADDLE_HEIGHT / 2
                self.BALL_WIDTH = 15
                self.BALL_HEIGHT = 15
                self.COURT_TOP = 124
                self.COURT_BOTTOM = 654

                # Other variables
                self.CURRENT_DIFFICULTY = max(persistent._fae_pong_difficulty + persistent._fae_pong_difficulty_change_next_game, 0)

                self.COURT_WIDTH = 1280
                self.COURT_HEIGHT = 720

                self.BALL_LEFT = 80 - self.BALL_WIDTH / 2
                self.BALL_RIGHT = 1199 + self.BALL_WIDTH / 2
                self.BALL_TOP = self.COURT_TOP + self.BALL_HEIGHT / 2
                self.BALL_BOTTOM = self.COURT_BOTTOM - self.BALL_HEIGHT / 2

                self.PADDLE_X_PLAYER = 128                                      #self.COURT_WIDTH * 0.1
                self.PADDLE_X_MONIKA = 1152 - self.PADDLE_WIDTH                 #self.COURT_WIDTH * 0.9 - self.PADDLE_WIDTH

                self.BALL_MAX_SPEED = 2000.0 + self.CURRENT_DIFFICULTY * 100.0