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

                # The maximum possible reflection angle, achieved when the ball
                # hits the corners of the paddle.
                self.MAX_REFLECT_ANGLE = math.pi / 3
                # A bit redundand, but math.pi / 3 is greater than 1, which is a problem.
                self.MAX_ANGLE = 0.9

                # If the ball is stuck to the paddle.
                self.stuck = True

                # The positions of the two paddles.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = (self.COURT_BOTTOM - self.COURT_TOP) / 2

                # The computer should aim at somewhere along the paddle, but
                # not always at the centre. This is the offset, measured from
                # the centre.
                self.ctargetoffset = self.get_random_offset()

                # The speed of Monika's paddle.
                self.computerspeed = 150.0 + self.CURRENT_DIFFICULTY * 30.0

                # Get an initial angle for launching the ball.
                init_angle = random.uniform(-self.MAX_REFLECT_ANGLE, self.MAX_REFLECT_ANGLE)

                # The position, dental-position, and the speed of the ball.
                self.bx = self.PADDLE_X_PLAYER + self.PADDLE_WIDTH + 0.1
                self.by = self.playery
                self.bdx = .5 * math.cos(init_angle)
                self.bdy = .5 * math.sin(init_angle)
                self.bspeed = 500.0 + self.CURRENT_DIFFICULTY * 25

                # Where the computer wants to go.
                self.ctargety = self.by + self.ctargetoffset

                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None
            

            def get_random_offset(self):
                return random.uniform(-self.PADDLE_RADIUS, self.PADDLE_RADIUS)

            def visit(self):
                return [ self.paddle, self.ball, self.player, self.sayori, self.ctb ]

            def check_bounce_off_top(self):
                # The ball wants to leave the screen upwards.
                if self.by < self.BALL_TOP and self.oldby - self.by != 0:

                    # The x value at which the ball hits the upper wall.
                    collisionbx = self.oldbx + (self.bx - self.oldbx) * ((self.oldby - self.BALL_TOP) / (self.oldby - self.by))

                    # Ignores the walls outside the field.
                    if collisionbx < self.BALL_LEFT or collisionbx > self.BALL_RIGHT:
                        return

                    self.bouncebx = collisionbx
                    self.bounceby = self.BALL_TOP

                    # Bounce off by teleporting ball (mirror position on wall).
                    self.by = -self.by + 2 * self.BALL_TOP

                    if not self.stuck:
                        self.bdy = -self.bdy

                    # Ball is so fast it still wants to leave the screen after mirroring, now downwards.
                    # Bounces the ball again (to the other wall) and leaves it there.
                    if self.by > self.BALL_BOTTOM:
                        self.bx = self.bouncebx + (self.bx - self.bouncebx) * ((self.bounceby - self.BALL_BOTTOM) / (self.bounceby - self.by))
                        self.by = self.BALL_BOTTOM
                        self.bdy = -self.bdy

                    if not self.stuck:
                        if self.playsounds:
                            renpy.sound.play(self.soundbeep, channel=1)

                    return True
                return False

            def check_bounce_off_bottom(self):
                # The ball wants to leave the screen downwards.
                if self.by > self.BALL_BOTTOM and self.oldby - self.by != 0:

                    # The x value at which the ball hits the lower wall.
                    collisionbx = self.oldbx + (self.bx - self.oldbx) * ((self.oldby - self.BALL_BOTTOM) / (self.oldby - self.by))

                    # Ignores the walls outside the field.
                    if collisionbx < self.BALL_LEFT or collisionbx > self.BALL_RIGHT:
                        return

                    self.bouncebx = collisionbx
                    self.bounceby = self.BALL_BOTTOM

                    # Bounce off by teleporting ball (mirror position on wall).
                    self.by = -self.by + 2 * self.BALL_BOTTOM

                    if not self.stuck:
                        self.bdy = -self.bdy

                    # Ball is so fast it still wants to leave the screen after mirroring, now downwards.
                    # Bounces the ball again (to the other wall) and leaves it there.
                    if self.by < self.BALL_TOP:
                        self.bx = self.bouncebx + (self.bx - self.bouncebx) * ((self.bounceby - self.BALL_TOP) / (self.bounceby - self.by))
                        self.by = self.BALL_TOP
                        self.bdy = -self.bdy

                    if not self.stuck:
                        if self.playsounds:
                            renpy.sound.play(self.soundbeep, channel=1)

                    return True
                return False

            def getCollisionY(self, hotside, is_computer):
                # Checks whether the ball went through the player's paddle on the x-axis while moving left or monika's paddle while moving right.
                # Returns the y collision-position and sets self.collidedonx

                self.collidedonx = is_computer and self.oldbx <= hotside <= self.bx or not is_computer and self.oldbx >= hotside >= self.bx;

                if self.collidedonx:

                    # Checks whether a bounce happened before potentially colliding with the paddle.
                    if self.oldbx <= self.bouncebx <= hotside <= self.bx or self.oldbx >= self.bouncebx >= hotside >= self.bx:
                        startbx = self.bouncebx
                        startby = self.bounceby
                    else:
                        startbx = self.oldbx
                        startby = self.oldby

                    # The y value at which the ball hits the paddle.
                    if startbx - self.bx != 0:
                        return startby + (self.by - startby) * ((startbx - hotside) / (startbx - self.bx))
                    else:
                        return startby

                # The ball did not go through the paddle on the x-axis.
                else:
                    return self.oldby

            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                # Figure out where we want to move the ball to.
                speed = dtime * self.bspeed

                # Stores the starting position of the ball.
                self.oldbx = self.bx
                self.oldby = self.by
                self.bouncebx = self.bx
                self.bounceby = self.by

                # Handles the ball-speed.
                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Bounces the ball up to one time, either up or down
                if not self.check_bounce_off_top():
                    self.check_bounce_off_bottom()

                # Handles Monika's targeting and speed.

                # If the ball goes through Monika's paddle, aim for the collision-y, not ball-y.
                # Avoids Monika overshooting her aim on lags.
                collisionby = self.getCollisionY(self.PADDLE_X_MONIKA, True)
                if self.collidedonx:
                    self.ctargety = collisionby + self.ctargetoffset
                else:
                    self.ctargety = self.by + self.ctargetoffset

                cspeed = self.computerspeed * dtime

                # Moves Monika's paddle. It wants to go to self.by, but
                # may be limited by it's speed limit.
                global lose_on_purpose
                if lose_on_purpose and self.bx >= self.COURT_WIDTH * 0.75:
                    if self.bx <= self.PADDLE_X_MONIKA:
                        if self.ctargety > self.computery:
                            self.computery -= cspeed
                        else:
                            self.computery += cspeed

                else:
                    cspeed = self.computerspeed * dtime

                    if abs(self.ctargety - self.computery) <= cspeed:
                        self.computery = self.ctargety
                    elif self.ctargety >= self.computery:
                        self.computery += cspeed
                    else:
                        self.computery -= cspeed

                # Limits the position of Monika's paddle.
                if self.computery > self.COURT_BOTTOM:
                    self.computery = self.COURT_BOTTOM
                elif self.computery < self.COURT_TOP:
                    self.computery = self.COURT_TOP
                

                def paddle(px, py, hotside, is_computer):

                    # Render the paddle image. We give it an 1280x720 area
                    # to render into, knowing that images will render smaller.
                    # (This isn't the case with all displayables. Solid, Frame,
                    # and Fixed will expand to fill the space allotted.)
                    # We also pass in st and at.
                    pi = renpy.render(self.paddle, self.COURT_WIDTH, self.COURT_HEIGHT, st, at)

                    # renpy.render returns a Render object, which we can
                    # blit to the Render we're making.
                    r.blit(pi, (int(px), int(py - self.PADDLE_RADIUS)))

                    # Checks whether the ball went through the paddle on the x-axis and gets the y-collision-posisiton.
                    collisionby = self.getCollisionY(hotside, is_computer)

                    # Checks whether the ball went through the paddle on the y-axis.
                    collidedony = py - self.PADDLE_RADIUS - self.BALL_HEIGHT / 2 <= collisionby <= py + self.PADDLE_RADIUS + self.BALL_HEIGHT / 2

                    # Checks whether the ball collided with the paddle
                    if not self.stuck and self.collidedonx and collidedony:
                        hit = True
                        if self.oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                        elif self.oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                        else:
                            hit = False

                        if hit:
                            # The reflection angle scales linearly with the
                            # distance from the centre to the point of impact.
                            angle = (self.by - py) / (self.PADDLE_RADIUS + self.BALL_HEIGHT / 2) * self.MAX_REFLECT_ANGLE

                            if angle >    self.MAX_ANGLE:
                                angle =   self.MAX_ANGLE
                            elif angle < -self.MAX_ANGLE:
                                angle =  -self.MAX_ANGLE

                            global pong_angle_last_shot
                            pong_angle_last_shot = angle

                            self.bdy = .5 * math.sin(angle)
                            self.bdx = math.copysign(.5 * math.cos(angle), -self.bdx)

                            global ball_paddle_bounces
                            ball_paddle_bounces += 1

                            # Changes where the computer aims after a hit.
                            if is_computer:
                                self.ctargetoffset = self.get_random_offset()

                            if self.playsounds:
                                renpy.sound.play(self.soundboop, channel=1)

                            self.bspeed += 125.0 + self.CURRENT_DIFFICULTY * 12.5
                            if self.bspeed > self.BALL_MAX_SPEED:
                                self.bspeed = self.BALL_MAX_SPEED

                # Draw the two paddles.
                paddle(self.PADDLE_X_PLAYER, self.playery, self.PADDLE_X_PLAYER + self.PADDLE_WIDTH, False)
                paddle(self.PADDLE_X_MONIKA, self.computery, self.PADDLE_X_MONIKA, True)

                # Draw the ball.
                ball = renpy.render(self.ball, self.COURT_WIDTH, self.COURT_HEIGHT, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                                int(self.by - self.BALL_HEIGHT / 2)))

                # Show the player names.
                player = renpy.render(self.player, self.COURT_WIDTH, self.COURT_HEIGHT, st, at)
                r.blit(player, (self.PADDLE_X_PLAYER, 25))

                # Show Monika's name.
                monika = renpy.render(self.monika, self.COURT_WIDTH, self.COURT_HEIGHT, st, at)
                ew, eh = monika.get_size()
                r.blit(monika, (self.PADDLE_X_MONIKA - ew, 25))

                # Show the "Click to Begin" label.
                if self.stuck:
                    ctb = renpy.render(self.ctb, self.COURT_WIDTH, self.COURT_HEIGHT, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, ((self.COURT_WIDTH - cw) / 2, 30))
                
                if self.bx < -200:

                    if self.winner == None:
                        global loss_streak_counter
                        loss_streak_counter += 1

                        if ball_paddle_bounces <= 1:
                            global instant_loss_streak_counter
                            instant_loss_streak_counter += 1
                        else:
                            global instant_loss_streak_counter
                            instant_loss_streak_counter = 0

                    global win_streak_counter
                    win_streak_counter = 0

                    self.winner = "sayori"

                    # Needed to ensure that event is called, noticing
                    # the winner.
                    renpy.timeout(0)
                
                elif self.bx > self.COURT_WIDTH + 200:

                    if self.winner == None:
                        global win_streak_counter
                        win_streak_counter += 1;

                    global loss_streak_counter
                    loss_streak_counter = 0

                    #won't reset if Monika misses the first hit
                    if ball_paddle_bounces > 1:
                        global instant_loss_streak_counter
                        instant_loss_streak_counter = 0

                    self.winner = "player"

                    renpy.timeout(0)

                renpy.redraw(self, 0.0)

                return r

            def event(self, ev, x, y, st):

                import pygame

                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                # Set the position of the player's paddle.
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y

                # If we have a winner, return him or her. Otherwise, ignore
                # the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()
                

label game_pong:

    
    if played_pong_this_session:
        if fae_pong_taking_break:
            s "Ready to try again?"
            s "Give me your hardest{nw}"
            s "Give me your{fast} best shot!"

            $ fae_pong_taking_break = False

        else:
            s "You want to play again?"
            s "Sure!"
    else:
        $ played_pong_this_session = True

    
    $ pong_sayori_last_response_id = PONG_SAYORI_RESPONSE_NONE

    call demo_minigame_pong from _call_demo_minigame_pong
    return

label demo_minigame_pong:

    window hide None

    scene bg pong field

    $ ball_paddle_bounces = 0
    $ pong_difficulty_before = persistent._fae_pong_difficulty
    $ powerup_value_this_game = persistent._fae_pong_difficulty_change_next_game
    $ loss_streak_counter_before = loss_streak_counter
    $ win_streak_counter_before = win_streak_counter
    $ instant_loss_streak_counter_before = instant_loss_streak_counter

    python:
        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    
    scene spaceroom

    $ persistent._fae_pong_difficulty_change_next_game = 0;

    if winner == "monika":
        $ new_difficulty = persistent._fae_pong_difficulty + PONG_DIFFICULTY_CHANGE_ON_LOSS

        $ inst_dialogue = store.fae_pong.DLG_WINNER

    else:
        $ new_difficulty = persistent._fae_pong_difficulty + PONG_DIFFICULTY_CHANGE_ON_WIN

        $ inst_dialogue = store.fae_pong.DLG_LOSER

        #Give player XP if this is their first win
        if not persistent._fae_ever_won['pong']:
            $ persistent._fae_ever_won['pong'] = True
    
    if new_difficulty < 0:
        $ persistent._fae_pong_difficulty = 0
    else:
        $ persistent._fae_pong_difficulty = new_difficulty
    
    s "Would you like to play again?"

    $ history_list.pop()

    menu:
        s "Would you like to play again?{fast}"

        "Yes":
            
            jump demo_minigame_pong
        
        "No.":
            if winner == "monika":
                if renpy.seen_label(store.fae_pong.DLG_WINNER_END):
                    $ end_dialogue = store.fae_pong.DLG_WINNER_FAST
                else:
                    $ end_dialogue = store.fae_pong.DLG_WINNER_END

            else:
                if renpy.seen_label(store.fae_pong.DLG_LOSER_END):
                    $ end_dialogue = store.fae_pong.DLG_LOSER_FAST
                else:
                    $ end_dialogue = store.fae_pong.DLG_LOSER_END

            call expression end_dialogue from _fae_pong_end_dialogue
    return

init -1 python in fae_pong:

    DLG_WINNER = "fae_pong_dlg_winner"
    DLG_WINNER_FAST = "fae_pong_dlg_winner_fast"
    DLG_LOSER = "fae_pong_dlg_loser"
    DLG_LOSER_FAST = "fae_pong_dlg_loser_fast"

    DLG_WINNER_END = "fae_pong_dlg_winner_end"
    DLG_LOSER_END = "fae_pong_dlg_loser_end"


    DLG_BLOCKS = (
        DLG_WINNER,
        DLG_WINNER_FAST,
        DLG_WINNER_END,
        DLG_LOSER,
        DLG_LOSER_FAST,
        DLG_LOSER_END
    )


label fae_pong_dlg_winner:

    if sayori_asks_to_go_easy and ball_paddle_bounces == 1:
        s "Ehehehe~"
        s "I know I asked you to go easy on me, but this isn't what I had in mind..."
        s "I do appreciate the gesture though~"
        $ sayori_asks_to_go_easy = False

    elif sayori_asks_to_go_easy and ball_paddle_bounces <= 9:
        s "Yay, I won!"
        show sayori at t11 zorder SAYO_ZORDER with dissolve
        s "Thanks. I appreciate it~"
        $ sayori_asks_to_go_easy = False

    
    elif ball_paddle_bounces == 1:

        #Once
        if instant_loss_streak_counter == 1:
            s "Ahaha, that's unfortunate..."

        #Twice
        elif instant_loss_streak_counter == 2:
            s "[player],{w=0.1} you missed again..."

        #Thrice
        elif instant_loss_streak_counter == 3:
            s  "[player]!"

            if persistent._fae_pm_ever_let_monika_win_on_purpose:
                $ menu_response = _("Are you letting me win on purpose again?")
            else:
                $ menu_response = _("Are you letting me win on purpose?")

            s  "[menu_response]"
            $ _history_list.pop()
            menu:
                s "[menu_response]{fast}"

                "...Maybe.":
                    s  "Ehehe!~"
                    s  "Thank you, [player]~"
                    #show monika  at t11 zorder MAS_MONIKA_Z with dissolve_monika
                    s "But you know,{w=0.1} I don't mind losing to you every now and then."

                    if persistent._fae_pm_ever_let_monika_win_on_purpose:
                        s  "I like to see you win just as much as you like to see me win~"

                    $ player_lets_monika_win_on_purpose = True
                    $ persistent._fae_pm_ever_let_monika_win_on_purpose = True

                "No.":
                    if persistent._fae_pm_ever_let_monika_win_on_purpose:
                        show sayori idle
                        s "Are you {i}sure?{/i}{nw}"
                        $ _history_list.pop()
                        menu:
                            s "Are you {i}sure?{/i}{fast}"

                            "Yes":
                                call fae_pong_dlg_sorry_assuming

                            "No":
                                s "[player]!"
                                s "Stop teasing me!"
                                $ player_lets_monika_win_on_purpose = True
                                $ lose_on_purpose = True

                    else:
                        call fae_pong_dlg_sorry_assuming
        else:
            if player_lets_monika_win_on_purpose:
                s "Aren't you getting tired of letting me win, [player]?"
            else:
                s "..."

                #Just so we don't get this every time, feels a little more genuine
                if random.randint(1,3) == 1:
                    s "Come on, [fae_get_player_nickname(regex_replace_with_nullstr='my ')]!"
                    s "You can do it, I believe in you!"

    #Monika wins a game after the player let her win on purpose at least three times
    elif instant_loss_streak_counter_before >= 3 and player_lets_monika_win_on_purpose:
        s "Nice try [player],{w=0.1} {nw}"
        extend "but I can win by myself!"
        s "Ahaha!"

    #Monika wins after telling the player she would win the next game
    elif powerup_value_this_game == PONG_DIFFICULTY_POWERUP:
        s "Ehehe~"

        if persistent._fae_pong_difficulty_change_next_game_date == datetime.date.today():
            s "Didn't I tell you I would win this time?"
        else:
            $ p_nickname = fae_get_player_nickname(regex_replace_with_nullstr='my ')
            s "Remember, [p_nickname]?{w=0.1} {nw}"
            extend "I told you I'd win our next match."

    #Monika wins after going easy on the player
    elif powerup_value_this_game == PONG_DIFFICULTY_POWERDOWN:
        s "Ah..."
        s "Try again, [player]!"

        $ persistent._fae_pong_difficulty_change_next_game = PONG_PONG_DIFFICULTY_POWERDOWNBIG

    #Monika wins after going even easier on the player
    elif powerup_value_this_game == PONG_PONG_DIFFICULTY_POWERDOWNBIG:
        s "Ahaha..."
        s "I really hoped you'd win this game."
        s "Sorry about that, [fae_get_player_nickname(regex_replace_with_nullstr='my ')]!"

    #The player has lost 3, 8, 13, ... matches in a row.
    elif loss_streak_counter >= 3 and loss_streak_counter % 5 == 3:
        s "Come on, [player], I know you can beat me..."
        s "Keep trying!"

    #The player has lost 5, 10, 15, ... matches in a row.
    elif loss_streak_counter >= 5 and loss_streak_counter % 5 == 0:
        s "I hope you're having fun, [fae_get_player_nickname(regex_replace_with_nullstr='my ')]."
        s "I wouldn't want you to get upset over a game, after all."
        s "We can always take a break and play again later if you want."

    #Monika wins after the player got a 3+ winstreak
    elif win_streak_counter_before >= 3:
        $ p_nickname = fae_get_player_nickname(regex_replace_with_nullstr='my ')
        s "Ahaha!"
        s "Sorry [p_nickname],{w=0.1} {nw}"
        extend "but it looks like your luck's run out."
        s "Now it's my time to shine~"

        $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_AFTER_PLAYER_WON_MIN_THREE_TIMES

    #Monika wins a second time after the player got a 3+ winstreak
    elif pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_AFTER_PLAYER_WON_MIN_THREE_TIMES:
        s "Ehehe!"
        s "Keep up, [player]!{w=0.3} {nw}"
        extend "It looks like your streak is over!"

        $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_SECOND_WIN_AFTER_PLAYER_WON_MIN_THREE_TIMES

    #Monika wins a long game
    elif ball_paddle_bounces > 9 and ball_paddle_bounces > pong_difficulty_before * 0.5:
        if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_LONG_GAME:
            s "Playing against you is really tough, [player]."
            s "Keep it up and you'll beat me, I'm sure of it!"
        else:
            s "Well played, [player], you're really good!"
            s "But so am I,{w=0.1} {nw}"
            extend 1hub "ahaha!"

        $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_LONG_GAME

    #Monika wins a short game
    elif ball_paddle_bounces <= 3:
        if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_SHORT_GAME:
            s "Another quick win for me~"
        else:
            s "Ehehe,{w=0.1} {nw}"
            extend "I got you with that one!"

        $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_SHORT_GAME

    #Monika wins by a trickshot
    elif pong_angle_last_shot >= 0.9 or pong_angle_last_shot <= -0.9:
        if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_TRICKSHOT:
            s "Ah...{w=0.3}{nw}"
            extend "it happened again."
            s "Sorry about that, [player]!"
        else:
            s "Sorry, [player]!"
            s "I didn't mean for it to bounce around that much..."

        $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_TRICKSHOT

    #Monika wins a game
    else:
        #Easy
        if pong_difficulty_before <= 5:
            if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_EASY_GAME:
                s "You can do it, [fae_get_player_nickname(regex_replace_with_nullstr='my ')]!"
                s "I believe in you~"
            else:
                s "Concentrate, [player]."
                m 3hub "Keep trying, I know you'll beat me soon!"

            $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_EASY_GAME

        #Medium
        elif pong_difficulty_before <= 10:
            if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_MEDIUM_GAME:
                m 1hub "I win another round~"
            else:
                if loss_streak_counter > 1:
                    m 3hub "Looks like I won again~"
                else:
                    m 3hua "Looks like I won~"

            $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_MEDIUM_GAME

        #Hard
        elif pong_difficulty_before <= 15:
            if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_HARD_GAME:
                m 1hub "Ahaha!"
                m 2tsb "Am I playing too well for you?"
                m 1tsu "I'm just kidding, [player]."
                m 3hub "You're pretty good!"
            else:
                if loss_streak_counter > 1:
                    m 1hub "I win again~"
                else:
                    m 1huu "I win~"

            $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_HARD_GAME

        #Expert
        elif pong_difficulty_before <= 20:
            if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_EXPERT_GAME:
                m 2tub "It feels good to win!"
                m 2hub "Don't worry, I'm sure you'll win again soon~"
            else:
                if loss_streak_counter > 1:
                    m 2eub "I win another round!"
                else:
                    m 2eub "I win this round!"

            $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_EXPERT_GAME

        #Extreme
        else:
            if pong_monika_last_response_id == PONG_MONIKA_RESPONSE_WIN_EXTREME_GAME:
                m 2duu "Not bad, [fae_get_player_nickname(regex_replace_with_nullstr='my ')]."
                m 4eua "I gave it everything I had, so don't feel too bad for losing from time to time."
            else:
                m 2hub "This time, the win is mine!"
                m 2efu "Keep up, [player]!"

            $ pong_monika_last_response_id = PONG_MONIKA_RESPONSE_WIN_EXTREME_GAME

    return

    




