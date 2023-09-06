## screens.rpy

# This file declares all the screens and styles in DDLC.

## Initialization
################################################################################
init -1 python:

    layout.FAE_TT_NOTIF = (
        "Enabling this will let Sayori use your system notifications, and check if FaE is your active window"
    )

init offset = -1

# Enables the ability to add more settings in the game such as uncensored mode.
default extra_settings = True

## Color Styles
################################################################################

# This controls the color of outlines in the game like
# text, say, navigation, labels and such.
define -2 text_outline_color = "#3BB7FF"



################################################################################
## In-game screens
################################################################################

screen minigame(ai_mode):
    default chess = ChessDisplayable(chess_ai=ai_mode)
    add "bg chessboard"
    add chess
    if chess.winner:
        timer 6.0 action Return(chess.winner)
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    # If there's a side image, display it above the text. Do not display
    # on the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

            text prompt style "input_prompt"
            input id "input"


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## New as of 3.0.0
##    - You may now pass through argurments to the menu options to colorize
##      your menu as you like. Add (kwargs=[color hex or style name]) to your
##      menu option name and you get different buttons! 
##
##      Examples: "Option 1 (kwargs=#00fbff)" | "Option 2 (kwargs=#00fbff, #6cffff)"
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:

        for i in items:
            
            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    
                    $ kwarg = kwarg.replace(", ", ",").split(",")
                    
                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')
                    
                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]
                    
                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action


style talk_choice_button_text is choice_button_text

style talk_choice_vbox is choice_vbox:
    xcenter 250

style talk_choice_button is choice_button

screen talk_choice(items):
    style_prefix "talk_choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

screen fae_select_sidebar(items):

    style_prefix "choice"

    vbox:

        xpos 60

        for i in items:
            
            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    
                    $ kwarg = kwarg.replace(", ", ",").split(",")
                    
                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')
                    
                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]
                    
                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action




## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            #textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

#style quick_button is default
#style quick_button_text is button_text

init python:
    
    def FileActionMod(name, page=None, **kwargs):

        if renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))


################################################################################
# Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init 4 python:
    def FinishEnterName():
        global player

        if not player: 
            return
        
        
        if (
            fae_bad_name_list.search(player)
        ):

            renpy.call_in_new_context("fae_bad_name_input")
            player = ""
            renpy.show(
                "chibi demon",
                layer="screens",
                zorder=10
            )
            return
        
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")


label fae_bad_name_input:
    show screen navigation

    $ disable_esc()

    if not renpy.seen_label("fae_bad_name_input.first_time_bad_name"):

        label .first_time_bad_name:
            play sound "sfx/glitch3.ogg"
            window show

            hide screen name_input

            show screen confirm(message="Invalid Name", ok_action=Return)

            window auto
    else:
        hide screen name_input

        show screen confirm(message="Invalid Name", ok_action=Return)
    
    $ enable_esc()
    hide screen navigation
    return


screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        #if not persistent.autoload or not main_menu:

        if main_menu:

            #if persistent.playthrough == 1:
            #    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
            #else:
            textbutton _("Just Sayori") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

        else:

            textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

            textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

        textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]


        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
        #    if persistent.playthrough != 3:
            textbutton _("Main Menu") action NullAction(), Show("dialog", message="There's no point!\nYou'll just get back here!", ok_action=Hide("dialog")) #MainMenu()

        textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

        textbutton _("Submods") action [ShowMenu("submods"), SensitiveIf(renpy.get_screen("submods") == None)]

        textbutton _("QABs") action [ShowMenu("qab"), SensitiveIf(renpy.get_screen("qab") == None)]

        #textbutton _("About") action ShowMenu("about")

        if store.fae_notifs.can_show_notifs and not main_menu:
            textbutton _("Alerts") action [ShowMenu("notif_settings"), SensitiveIf(renpy.get_screen("notif_settings") == None)]

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=(None))# if main_menu else _confirm_quit))
        
        #if not main_menu:
        textbutton _("Return") action Return()
        #else:
        #    timer 1.75 action Start("autoload_yurikill")




## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    
    add "menu_bg"
    add "menu_art_s"
    frame:
        pass

        ## The use statement includes another screen inside this one. The actual
        ## contents of the main menu are in the navigation screen.
    use navigation

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    key "K_ESCAPE" action Quit(confirm=False)


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When this
## screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):

    # Add the backgrounds.
    if main_menu:
        #add gui.main_menu_background
        add "menu_bg"
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"
        #pass

        hbox:

            # Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"
            #    pass

            frame:
                style "game_menu_content_frame"
                #pass

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    #textbutton _("Return"):
        #style "return_button"

        #action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")




## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""




## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving. \nNot when we're sitting here doing nothing...", ok_action=Hide("dialog"))
            


screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.

            button:
                style "page_label"

                #key_events True
                xalign 0.5
                #action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                #textbutton _("<") action FilePagePrevious(max=9, wrap=True)

                #textbutton _("{#auto_page}A") action FilePage("auto")

                #textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                #textbutton _(">") action FilePageNext(max=9, wrap=True)




## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
init python:
    if renpy.windows:
        config.tts_voice = "Mark"
    elif renpy.macintosh:
        config.tts_voice = "Alex"
    else:
        config.tts_voice = "english_rp"

$ ostts=config.tts_voice

define persistent.animate_room = True

screen preferences():

    tag menu

    default tooltip = Tooltip("")

    use game_menu(_("Settings"), scroll="viewport"):


        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "generic_fancy_check"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                if config.developer:
                        vbox:
                            style_prefix "radio"
                            label _("Rollback Side")
                            textbutton _("Disable") action Preference("rollback side", "disable")
                            textbutton _("Left") action Preference("rollback side", "left")
                            textbutton _("Right") action Preference("rollback side", "right")

                #vbox:
                    #style_prefix "generic_fancy_check"
                    #label _("Graphics")

                    #textbutton _("Dark Mode"):
                        #action [Function(fae_settings._ui_change_wrapper, persistent._fae_dark_mode_enabled), Function(fae_settings._dark_mode_toggle)]
                        #selected persistent._fae_dark_mode_enabled

                vbox:
                    style_prefix "generic_fancy_check"
                    label _("Gameplay")
                    
                    textbutton _("Repeat Topics"):
                        action [
                            ToggleField(
                                object=persistent,
                                field="fae_repeat_chat",
                                true_value=True,
                                false_value=False
                            )
                        ]
                    textbutton _("Notifications") action [
                        ToggleField(
                            object=persistent,
                            field="_fae_notifs_enabled",
                            true_value=True,
                            false_value=False
                            
                            )
                        ]


            null height (4 * gui.pref_spacing)


            hbox:
                style_prefix "slider"
                box_wrap True

                python:

                    if fae_randchat_prev != persistent._fae_random_chat_freq:

                        fae_random_chat_rate.adjustRandFrequency(
                            persistent._fae_random_chat_freq
                        )
                    
                    rc_display = fae_random_chat_rate.getRandChatDisp(
                        persistent._fae_random_chat_freq
                    )

                    store.fae_randchat_prev = persistent._fae_random_chat_freq



                vbox:

                    hbox:
                        label _("Random Chatter  ")
                        label _("[[ " + rc_display + " ]")
                    
                    bar value FieldValue(
                        persistent,
                        "_fae_random_chat_freq",
                        range=4,
                        style="slider"
                    )
                    
                    #label _("Random Talk: {0}".format(fae_utilities.random_chat_rate.get_random_chat_frequency_desc()))

                    #bar value FieldValue(
                    #    object=persistent,
                    #    field="fae_random_chat_rate",
                    #    range=4,
                    #    style="slider",
                    #    step=1
                    #)

                vbox:

                    label _("Text Speed")

                    bar value FieldValue(_preferences, "text_cps", range=170, max_is_zero=False, style="slider", offset=30)

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    label _("Music Volume")
                    hbox:
                        bar value Preference("music volume")

                    label _("Sound Volume")
                    hbox:
                        bar value Preference("sound volume")


                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        style "check_button"
                        action Preference("all mute", "toggle")

            hbox:
            #We disable updating on the main menu because it causes graphical issues
            #due to the spaceroom not being loaded in
                

                textbutton _("Import DDLC Save Data"):
                    action Function(renpy.call_in_new_context, 'import_ddlc_persistent_in_settings')
                    style "navigation_button"

################
#OBSOLETE SCREEN
################
#screen preferences():

#    tag menu

#    if renpy.mobile:
#        $ cols = 2
#    else:
#        $ cols = 4

#    use game_menu(_("Settings")):

#        viewport id "preferences":
#            scrollbars "vertical"
#            mousewheel True
#            draggable True



#            vbox:

#                yoffset 0
#                xoffset 50
                #if extra_settings:
                #    xoffset 35
                #else:
                #    xoffset 50

#                hbox:
#                    box_wrap True

#                    if renpy.variant("pc"):

#                        vbox:
#                            style_prefix "radio"
#                            label _("Display")
#                            textbutton _("Windowed") action Preference("display", "window")
#                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
#                    if config.developer:
#                        vbox:
#                            style_prefix "radio"
#                            label _("Rollback Side")
#                            textbutton _("Disable") action Preference("rollback side", "disable")
#                            textbutton _("Left") action Preference("rollback side", "left")
#                            textbutton _("Right") action Preference("rollback side", "right")

#                    vbox:
#                        style_prefix "check"
#                        label _("Skip")
#                        textbutton _("Unseen Text") action Preference("skip", "toggle")
#                        textbutton _("After Choices") action Preference("after choices", "toggle")
#                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

#                    vbox:
#                        style_prefix "check"
#                        label _("Chatter")
#                        textbutton _("Repeat Topics") action [
#                            ToggleField(
#                                object=persistent,
#                                field="repeat_chat",
#                                true_value=True,
#                                false_value=False)
#                        ]
#                hbox:
#                    style_prefix "slider"
#                    box_wrap True

#                    vbox:
#                        label _("Random Talk: {0}".format(sayo_utilities.rcf.get_desc()))

#                        bar value FieldValue(
#                            object=persistent,
#                            field="sayo_rctf",
#                            range=6,
#                            style="slider",
#                            step=1
#                        )


                #null height (4 * gui.pref_spacing)

#                hbox:
                    #if extra_settings:
                        #xoffset 15
#                    style_prefix "slider"
#                    box_wrap True

#                    vbox:

#                        label _("Text Speed")

#                        #bar value Preference("text speed")
#                        bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

#                        label _("Auto-Forward Time")

#                        bar value Preference("auto-forward time")

#                    vbox:
                        #if extra_settings:
                            #xoffset 15
                        
#                        if config.has_music:
#                            label _("Music Volume")

#                            hbox:
#                                bar value Preference("music volume")

#                        if config.has_sound:

#                            label _("Sound Volume")

#                            hbox:
#                                bar value Preference("sound volume")

#                                if config.sample_sound:
#                                    textbutton _("Test") action Play("sound", config.sample_sound)


#                        if config.has_voice:
#                            label _("Voice Volume")

#                            hbox:
#                                bar value Preference("voice volume")

#                                if config.sample_voice:
#                                    textbutton _("Test") action Play("voice", config.sample_voice)

#                        if config.has_music or config.has_sound or config.has_voice:
#                            null height gui.pref_spacing

#                            textbutton _("Mute All"):
#                                action Preference("all mute", "toggle")
#                                style "mute_all_button"

#                if config.developer:  
#                    hbox:
#                        vbox:
#                            textbutton _("Export Mod Icon as ICO"):
#                                action Function(saveIco, "mod_assets/DDLCModTemplateLogo.png")
#                                style "navigation_button"
                                
#    text "v[config.version]":
#                xalign 1.0 yalign 1.0
#                xoffset -10 yoffset -10
#                style "main_menu_version"




## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                $ what = filter_text_tags(h.what, allow=set([]))
                text what:
                    substitute False
        if not _history_list:
            label _("The dialogue history is empty.")

python early:
    import renpy.text.textsupport as textsupport
    from renpy.text.textsupport import TAG, PARAGRAPH
    def filter_text_tags(s, allow=None, deny=None):
        if (allow is None) and (deny is None):
            raise Exception("Only one of the allow and deny keyword arguments should be given to filter_text_tags.")
        if (allow is not None) and (deny is not None):
            raise Exception("Only one of the allow and deny keyword arguments should be given to filter_text_tags.")
        tokens = textsupport.tokenize(unicode(s))
        rv = [ ]
        for tokentype, text in tokens:
            if tokentype == PARAGRAPH:
                rv.append("\n")
            elif tokentype == TAG:
                kind = text.partition("=")[0]
                if kind and (kind[0] == "/"):
                    kind = kind[1:]
                if allow is not None:
                    if kind in allow:
                        rv.append("{" + text + "}")
                else:
                    if kind not in deny:
                        rv.append("{" + text + "}")
            else:
                rv.append(text)
        return "".join(rv)


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

#screen help():
#
#    tag menu
#
#    default device = "keyboard"
#
#    use game_menu(_("Help"), scroll="viewport"):
#
#        style_prefix "help"
#
#        vbox:
#            spacing 15
#
#            hbox:
#
#                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
#                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
#
#                if GamepadExists():
#                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
#
#            if device == "keyboard":
#                use keyboard_help
#            elif device == "mouse":
#                use mouse_help
#            elif device == "gamepad":
#                use gamepad_help
#
#
#screen keyboard_help():
#
#    hbox:
#        label _("Enter")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Space")
#        text _("Advances dialogue without selecting choices.")
#
#    hbox:
#        label _("Arrow Keys")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Escape")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Ctrl")
#        text _("Skips dialogue while held down.")
#
#    hbox:
#        label _("Tab")
#        text _("Toggles dialogue skipping.")
#
#    hbox:
#        label _("Page Up")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Page Down")
#        text _("Rolls forward to later dialogue.")
#
#    hbox:
#        label "H"
#        text _("Hides the user interface.")
#
#    hbox:
#        label "S"
#        text _("Takes a screenshot.")
#
#    hbox:
#        label "V"
#        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
#
#
#screen mouse_help():
#
#    hbox:
#        label _("Left Click")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Middle Click")
#        text _("Hides the user interface.")
#
#    hbox:
#        label _("Right Click")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Mouse Wheel Up\nClick Rollback Side")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Mouse Wheel Down")
#        text _("Rolls forward to later dialogue.")
#
#
#screen gamepad_help():
#
#    hbox:
#        label _("Right Trigger\nA/Bottom Button")
#        text _("Advance dialogue and activates the interface.")
#
#    hbox:
#        label ("Left Trigger\nLeft Shoulder")
#        text _("Roll back to earlier dialogue.")
#
#    hbox:
#        label _("Right Shoulder")
#        text _("Roll forward to later dialogue.")
#
#    hbox:
#        label _("D-Pad, Sticks")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Start, Guide")
#        text _("Access the game menu.")
#
#    hbox:
#        label _("Y/Top Button")
#        text _("Hides the user interface.")
#
#    textbutton _("Calibrate") action GamepadCalibrate()
#
#
#style help_button is gui_button
#style help_button_text is gui_button_text
#style help_label is gui_label
#style help_label_text is gui_label_text
#style help_text is gui_text
#
#style help_button:
#    properties gui.button_properties("help_button")
#    xmargin 8
#
#style help_button_text:
#    properties gui.button_text_properties("help_button")
#
#style help_label:
#    xsize 250
#    right_padding 20
#
#style help_label_text:
#    size gui.text_size
#    xalign 1.0
#    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen name_input(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

            #hbox:
            #    xalign 0.5
            #    style_prefix "radio_pref"
            #    textbutton "Male" action NullAction()
            #    textbutton "Female" action NullAction()
            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen dialog(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat


screen reload(message, ok_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 50

                textbutton _("Restart") action Quit(confirm=True)


            hbox:
                xalign 0.5
                spacing 50

                textbutton _("I'll do it myself") action Hide("reload")

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            if in_sayori_kill and message == layout.QUIT:
                add "confirm_glitch" xalign 0.5

            else:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action


init -2 python:

    def ingame_regret_await_check():

        if Sayori.isInGame():
            fae_regrets.add_new_regret_awaiting(fae_regrets.RegretTypes.CHEATING)

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat



## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


screen notif_settings():

    tag menu
    use game_menu(("Alerts"), scroll="viewport"):

        default tooltip = Tooltip("")

        vbox:
            style_prefix "generic_fancy_check"
            hbox:
                spacing 25
                textbutton _("User Notifications"):
                    action [ToggleField(
                                object=persistent,
                                field="_fae_notifs_enabled",
                                true_value=True,
                                false_value=False)]
                    
                    hovered tooltip.Action(layout.FAE_TT_NOTIF)
        
    text tooltip.value:
        xalign 0 yalign 1.0
        xoffset 300 yoffset -10
        style "main_menu_version"
                
## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## BSOD screen ##################################################################
## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.
## You may only use this file/feature only for DDLC mods and not for DDLC patchers,
## unofficial fixes, etc.
##
## This screen is used to fake a BSOD/kernel panic on the players' computer 
## on all platforms (Mobile devices defaults to the Linux BSOD).
##
## Syntax:
##     bsodCode - The error code message you want to show the player. Defaults to 
##                DDLC_ESCAPE_PLAN_FAILED if no message is given.
##     bsodFile (Windows 7 and Linux Only) - The fake file name that caused the 
##                error. Defaults to libGLESv2.dll if no file name is given.
##     rsod (Windows 11 Only) - Swaps the Windows 11 BSOD with a RSOD.
##
## Examples:
##     show screen bsod("DOKI_DOKI", "renpy32.dll", False) 
##     show screen bsod("EILEEN_EXCEPTION_NOT_HANDLED", rsod=True) 

init python:
    import subprocess
    import platform

    cursor = 0

    def fakePercent(st, at, winver):

        if int(0 + (st * 5)) < 100:
            percent = int(0 + (st * 5))
        else:
            percent = 100

        if winver == 8:
            d = Text("we'll restart for you. (" + str(percent) + "% complete)\n", style="bsod_win8_text", size=26)
        else:
            d = Text(str(percent) + "% complete", style="bsod_win10_text", line_leading=25)

        if percent < 100:
            return d, renpy.random.randint(1, 3)
        else:
            return d, None

    def constantCursor(st, at):
        global cursor
        if cursor == 0:
            cursor = 1
            return Text("  _", style="bsod_linux_text"), 0.5
        else:
            cursor = 0
            return Text("   ", style="bsod_linux_text"), 0.5


    if renpy.windows:
        try: osVer = tuple(map(int, subprocess.check_output("powershell (Get-WmiObject -class Win32_OperatingSystem).Version", shell=True).split("."))) # Vista+
        except: osVer = tuple(map(int, platform.version().split("."))) or (5, 1, 2600) # XP returns JIC (though who uses XP today?)

screen bsod(bsodCode="DDLC_ESCAPE_PLAN_FAILED", bsodFile="libGLESv2.dll", rsod=False):

    layer "master"

    if renpy.windows:

        if osVer < (6, 2, 9200): # Windows 7
            
            add Solid("#000082")

            vbox:

                style_prefix "bsod_win7"

                text "A problem has been detected and Windows has been shut down to prevent damage to your computer."
                text "The problem seems to be caused by the following file: " + bsodFile.upper()
                text bsodCode.upper()
                text "If this is the first time you've seen this Stop error screen, restart your computer. If this screens appears again, follow these steps:"
                text "Check to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need."
                text "If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode."
                text "Technical information:"
                text "*** STOP: 0x00000051 (OXFD69420, 0x00000005, OXFBF92317" + ", 0x00000000)\n"
                text "*** " + bsodFile.upper() + "  -  Address FBF92317 base at FBF102721, Datestamp 3d6dd67c"

        elif osVer < (10, 0, 10240): # Windows 8/8.1
            
            add Solid("#1273aa")

            style_prefix "bsod_win8"

            vbox:

                xalign 0.5
                yalign 0.4

                text ":(" style "bsod_win8_sad_text"
                text "Your PC ran into a problem and needs to restart."
                text "We're just collecting some error info, and then"
                add DynamicDisplayable(fakePercent, 8)
                text "If you'd like to know more, you can search online later for this error: " + bsodCode.upper() style "bsod_win8_sub_text"

        else: # Windows 10 (up to 21H1)/Windows 11/Windows 11 RSOD
            
            if osVer < (10, 0, 22000):
            
                add Solid("#0078d7")

            else:

                if not rsod:

                    add Solid("#000000")
                    python:
                        blackCol = "#0078d7"

                else:

                    add Solid("#d40e0eff")
                    python:
                        blackCol = "#f00"

            style_prefix "bsod_win10"

            vbox:

                xalign 0.3
                yalign 0.3

                text ":(" style "bsod_win10_sad_text"

                if osVer < (10, 0, 22000):

                    text "Your PC ran into a problem and needs to restart. We're"
                    text "just collecting some error info, and then we'll restart for"
                    text "you."

                else:

                    text "Your device ran into a problem and needs to restart."
                    text "We're just collecting some error info, and then you can"
                    text "restart."

                add DynamicDisplayable(fakePercent, 10)

                hbox:

                    if osVer < (10, 0, 22000):

                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/frame.png", im.matrix.colorize("#0078d7", "#fff"), ) at bsod_qrcode(100)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text "For more information about this issue and possible fixes, visit https://www.windows.com/stopcode" style "bsod_win10_info_text" line_leading 25
                            text "If you call a support person, give them this info:" style "bsod_win10_sub_text" line_leading 25
                            text "Stop code: " + bsodCode.upper() style "bsod_win10_sub_text"

                    else:

                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/frame.png", im.matrix.colorize(blackCol, "#fff"), ) at bsod_qrcode(150)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text "For more information about this issue and possible fixes, visit" style "bsod_win10_info_text" line_leading 25
                            text "https://www.windows.com/stopcode\n" style "bsod_win10_info_text"
                            text "If you call a support person, give them this info:" style "bsod_win10_sub_text"
                            text "Stop code: " + bsodCode.upper() style "bsod_win10_sub_text"
        
    elif renpy.macintosh:

        add Solid("#222")

        add im.MatrixColor("mod_assets/DDLCModTemplateLogo.png", im.matrix.desaturate() * im.matrix.brightness(-0.36)) at bsod_qrcode(440) xalign 0.5 yalign 0.54
        vbox:

            style_prefix "bsod_mac"
            xalign 0.53
            yalign 0.51

            text "You need to restart your computer. Hold down the Power\n"
            text "button until it turns off, then press the Power button again." line_spacing 25
            text "Redémarrez l'ordinateur. Enfoncez le bouton de démarrage\n"
            text "jusqu'à l'extinction, puis appuyez dessus une nouvelle fois." line_spacing 25
            text "Debe reiniciar el o rdenador. Mantenga pulsado el botón de\n"
            text "arranque hasta que se apague y luego vuelva a pulsarlo." line_spacing 25
            text "Sie müssen den Computer neu starten. Halten Sie den\n"
            text "Ein-/Ausschalter gedrückt bis das Gerät ausgeschaltet ist\n"
            text "und drücken Sie ihn dann erneut." line_spacing 25
            text "Devi riavviare il computer. Tieni premuto il pulsante di\n"
            text "accensione finché non si spegne, quindi premi di nuovo il\n"
            text "pulsante di accensione."

    else:

        add Solid("#000")

        vbox:
            style_prefix "bsod_linux"

            text "metaverse-pci.c:v[config.version] 9/22/2017 Metaverse Enterprise Solutions\n"
            text "  https://www.metaverse-enterprise.com/network/metaverse-pci.html"
            text "hda0: METAVERSE ENTERPRISE VIRTUAL HARDDISK, ATA DISK drive"
            text "ide0 at 0x1f0 - 0x1f7, 0x3f6 on irq 14"
            text "hdc: METAVERSE ENTERPRISE VIRTUAL CD-ROM, ATAPI CD/DVD-ROM drive"
            text "ide1 at 0x444 - 0x910, 0x211 on irq 15"
            text "fd0: METAVERSE ENTERPRISE VIRTUAL FLOPPY, ATA FLOPPY drive"
            text "ide2 at 0x7363-0x6e6565, 0x4569 on irq 16"
            text "ACPI: PCI Interrupt Link [[LNKC]] ebabked at IRQ 10"
            text "ACPI: PCI Interrupt 0000:00:03:.0[[A]] -> Link [[LNKC]] -> GSI 10 (level, low) -> IRQ 10"
            text "eno1: Metaverse Enterprise LIB-0922 found at 0xc453, IRQ 10, 09:10:21:86:75:30"
            text "hda: max request size: 512KiB"
            text "hda: 2147483648 sectors (1 TB) w/256KiB Cache, CHS=178/255/63, (U)DMA"
            text "hda: hda1"
            text "hdc: ATAPI 4x CD-ROM drive, 512kB Cache, (U)DMA"
            text "Uniform CD-ROM driver Revision: 3.20"
            text "Done."
            text "Begin: DDLC.so"
            text "Done."
            text "DDLC.so: global natsukiTime undeclared."
            text "DDLC.so: global sayoriTime undeclared."
            text "DDLC.so: global yuriTime undeclared."
            text "DDLC.so: global monikaTime undeclared."
            text "DDLC.so: SUCCESS."
            text "Begin: DDLC.so -> linux-4.12.14"
            text "/init: /init: 151: " + bsodCode.upper() + ": 0xforce=panic"
            text "Kernel panic - not syncing: Attempted to kill init!"
            add DynamicDisplayable(constantCursor)

    add Solid("#000000") at bsod_transition

            
transform bsod_transition:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

transform bsod_qrcode(x):
    size(x,x)

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

screen qab():
    tag menu

    use game_menu(("Hotkeys"), scroll="viewport"):

        default tooltip = GetTooltip("")

        # making each indivual list a vbox essentially lets us auto-align
        vbox:
            spacing 25

            hbox:
                style_prefix "check"
                vbox:
                    label _("General")
                    spacing 10
                    text _("Music")
                    text _("Play")
                    text _("Talk")
                    text _("Bookmark")
                    text _("Fullscreen")
                    text _("Screenshot")
                    text _("Settings")

                vbox:
                    label _("")
                    spacing 10
                    text _("M")
                    text _("P")
                    text _("T")
                    text _("B")
                    text _("F")
                    text _("S")
                    text _("Esc")

            hbox:
                style_prefix "check"
                vbox:
                    label _("Music")
                    spacing 10
                    text _("Volume Up")
                    text _("Volume Down")
                    text _("Mute")

                vbox:
                    label _("")
                    spacing 10
                    text _("+")
                    text _("-")
                    text _("Shift-M")

    # there are lesser used hotkeys in Help that aren't needed here
    text "Click 'Help' for the complete list.":
        xalign 1.0 yalign 0.0
        xoffset -10
        style "main_menu_version"


screen fae_jump_timer(time, expiry_label):
    timer time action Jump(expiry_label)


screen submods():

    tag menu

    use game_menu(("submods")):

        viewport id "scroll":
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                style_prefix "check"
                xfill True
                xmaximum 1000

                for i in sorted(store.fae_extras.dictionary_submods.values(), key=lambda x: x.name):
                    vbox:
                        xfill True
                        xmaximum 1000

                        label i.name:
                            yanchor 0
                            xalign 0
                            text_text_align 0.0
                        
                        $ authors = "{{space=20}}By {0}".format(i.creator)


                        text "[authors]":
                            yanchor 0
                            xalign 0
                            text_align 0.0
                            style "main_menu_version"
                        
                        if i.description:
                            text i.description text_align 0.0

