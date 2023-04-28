## splash.rpy
#default persistent.autoload = "ch30_autoload"
# This is where the splashscreen, disclaimer and menu code reside in.

# This python statement checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa'
# are in the game folder.
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs 
# and decompile them for the builds to work.
init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                renpy.error("DDLC archive files not found in /game folder. Check your installation and try again.")

    renpy.config.rollback_enabled = False
## Splash Message
# This python statement is where the splash messages reside in.
init python:
    import re

    menu_trans_time = 1
    # This variable is the default splash message that people will see when
    # the game launches.
    splash_message_default = "This game is an unofficial fan game that is unaffiliated with Team Salvato."
    # This array variable stores different kinds of splash messages you can use
    # to show to the player on startup.
    splash_messages = [
        "Please support Doki Doki Literature Club.",
        "Monika is watching you code."
    ]

    ### New in 3.0.0
    ## This recolor function allows you to recolor the GUI of DDLC easily without replacing
    ## the in-game assets.
    ##
    ## Syntax to use: recolorize("path/to/your/image", "#color1hex", "#color2hex", contrast value)
    ## Example: recolorize("gui/menu_bg.png", "#00a2ff", "#e6ffff", 1.25)

    def recolorize(path, blackCol="#3BB7FF", whiteCol="#A5DEFF", contr=1.29):
        return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)), im.matrix.colorize("#00f", "#fff")
            * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

# This image text shows the splash message when the game loads.
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Main Menu Images
# These image transforms store the images and positions of the game logo,
# the menu character sprites and main menu/pause menu screen images.

# This image shows the DDLC logo in the normal DDLC position.
image menu_logo:
    #"/mod_assets/DDLCModTemplateLogo.png"
    im.Composite((512, 512), (0, 0), recolorize("mod_assets/logo_bg.png"), (0, 0), "mod_assets/logo_fg.png")
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

# This image shows the main menu polka-dot image.
image menu_bg:
    topleft
    #"gui/menu_bg.png"
    recolorize("gui/menu_bg.png", "#12A2F6", "#A5DEFF", 1)
    menu_bg_move

# This image shows the pause menu polka-dot image.
image game_menu_bg:
    topleft
    #"gui/menu_bg.png"
    recolorize("gui/menu_bg.png", "#3BB7FF", "#A5DEFF", 1)
    menu_bg_loop

# This image transform shows the white fading effect in the main menu.
image menu_fade:
    "white"
    menu_fadeout

# These images show each respective characters' menu sprite and positions/animations.
image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# These images are the same as above but ghost themed for the secret ghost menu
# that appears rarely in-game .
image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# This image sprite shows a glitched Sayori menu sprite after Act 1 finishes.
image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

# This image shows the main menu screen in the main/pause menu.
image menu_nav:
    #"gui/overlay/main_menu.png"
    recolorize("gui/overlay/main_menu.png", "#3BB7FF")
    menu_nav_move

## Main Menu Effects
# These transforms and image transform store the effects that appear in the
# main menu on startup.

# This image transform shows a particle burst effect image to the main menu when
# the game starts.
image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

# This transform fades out the particle effects of the main menu
transform particle_fadeout:
    easeout 1.5 alpha 0

# This transform moves the polka-dot menu background to the upper-left.
transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

# This transform loops the polka-dot moving effect.
transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

# This transform moves the menu logo down to it's intended placement in-game.
transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

# This transform moves the main menu screen in-game to be visible.
transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

# This transform fades out the main menu screen. 
transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

# This transform takes in a z-axis, x-axis and zoom numbers and moves the menu
# sprites to where they appear in the game.
transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

## Team Salvato Splash Screen
# This image stores the Tean Salvato logo image that appears when the game starts.
image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# This image is a left over from DDLC's development that shows the splash message
# when the game starts.
image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# This init python statement checks if the character files are present in-game
# and writes them to the characters folder depending on the playthrough.
init python:
    if not persistent.do_not_delete:
        if renpy.android:
            if not os.access(os.environ['ANDROID_PUBLIC'] + "/characters/", os.F_OK):
                os.mkdir(os.environ['ANDROID_PUBLIC'] + "/characters")
        else:
            if not os.access(config.basedir + "/characters/", os.F_OK):
                os.mkdir(config.basedir + "/characters")
        restore_all_characters()

## These images are the background images shown in-game during the disclaimer.
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

## Startup Disclaimer
# This label calls the disclaimer screen that appears when the game starts.
label splashscreen:

    
    # This python statement grabs the username and process list of the PC.

    scene white
    
    default persistent.has_launched_before = False
    if not persistent.has_launched_before:
        $ quick_menu = False
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: http://ddlc.moe"
        menu:
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
            "I agree.":
                pass
        
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        scene white
        with Dissolve(1.5)

        #if not persistent._fae_imported_ddlc:
        #    call import_ddlc_persistent
        
        $ persistent.has_launched_before = True

        $ renpy.save_persistent()
        
        $ config.allow_skipping = False
    
    python:
        basedir = config.basedir.replace("\\", "/")

        with open(basedir + "/game/faerun", "w") as versfile:
            versfile.write(config.name + "|" + config.version + "\n")
    
    if persistent.autoload:
        jump autoload
    
    show white

    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.s1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)

    if renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = False

    

    if not persistent.fae_first_visit_date:
        $ persistent.fae_first_visit_date = datetime.datetime.now()
    

    return

label warningscreen:
    hide intro
    show warning
    pause 3.0


# This label checks if the save loaded matches the anti-cheat stored in the save.
label after_load:


    $ config.allow_skipping = False
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"

        $ renpy.utter_restart()

    return

label autoload:
    python:
        # Stuff that's normally done after splash
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        # Open the settings panel in the menu
        store._game_menu_screen = "preferences"
        renpy.block_rollback()

        # Fix the game context (normally done when loading save file)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # explicity remove keymaps we dont want
    $ config.keymap["debug_voicing"] = list()
    $ config.keymap["choose_renderer"] = list()

    # Pop the _splashscreen label which has _confirm_quit as False and other stuff
    $ renpy.pop_call()

    jump ch30_autoload



# This label loads the label saved in the autoload variable. 


# This label sets the main menu music to Doki Doki Literature Club before the
# menu starts
label before_main_menu:


    $ config.main_menu_music = audio.s1
    
    #$ store._game_menu_screen = "preferences"
    return


label confirm_quit:
    #python:
    $ fae_utilities.save_game()

    $ renpy.quit()
    return