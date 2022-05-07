
init -1:
    default persistent.old_ui = False

image readablePos = DynamicDisplayable(renpy.curry(music_pos)("song_progress_text"))
image readableDur = DynamicDisplayable(renpy.curry(music_dur)("song_duration_text"))
image titleName = DynamicDisplayable(renpy.curry(dynamic_title_text)("music_player_music_text")) 
image authorName = DynamicDisplayable(renpy.curry(dynamic_author_text)("music_player_song_author_text")) 
image coverArt = DynamicDisplayable(refresh_cover_data) 
image songDescription = DynamicDisplayable(renpy.curry(dynamic_description_text)("music_player_song_author_text")) 
image rpa_map_warning = DynamicDisplayable(renpy.curry(rpa_mapping_detection)("music_player_song_author_text"))
image playPauseButton = DynamicDisplayable(auto_play_pause_button)

screen music_player:

    tag menu

    add "game_menu_bg"
    add "gui/overlay/main_menu.png"
    
    default bar_val = AdjustableAudioPositionValue()

    side "c l":
        
        viewport id "vpo":
            mousewheel True
            style_prefix ""
            style "music_player_viewport"

            has vbox
            spacing gui.navigation_spacing
            
            for st in soundtracks:
                textbutton "[st.name]":
                    style "music_player_list"
                    text_style "music_player_list_button"
                    if current_soundtrack:
                        action [SensitiveIf(current_soundtrack.name != st.name 
                                or current_soundtrack.author != st.author 
                                or current_soundtrack.description != st.description), 
                                SetVariable("current_soundtrack", st), 
                                SetVariable("pausedstate", False), 
                                Play("music_player", st.path, loop=loopSong, fadein=2.0)]
                    else:
                        action [SetVariable("current_soundtrack", st), 
                        SetVariable("pausedstate", False), 
                        Play("music_player", st.path, loop=loopSong, fadein=2.0)]

        vbar value YScrollValue("vpo") xpos 1.0 ypos 20

    if current_soundtrack:
        if current_soundtrack.cover_art:
            if persistent.old_ui:
                add "coverArt" at cover_art_fade(500, 200)
            else:
                add "coverArt" at cover_art_fade(505, 300)

        hbox:
            if persistent.old_ui:
                style "play_pause_buttonO_hbox"
            else:
                style "play_pause_buttonN_hbox"

            imagebutton:
                idle "mod_assets/music_player/backward.png"
                hover "mod_assets/music_player/backwardHover.png"
                action [SensitiveIf(renpy.music.is_playing(channel='music_player')), 
                        Function(current_music_backward)]

            add "playPauseButton"

            imagebutton:
                idle "mod_assets/music_player/forward.png"
                hover "mod_assets/music_player/forwardHover.png"
                action [SensitiveIf(renpy.music.is_playing(channel='music_player')), 
                        Function(current_music_forward)]

        hbox:
            if persistent.old_ui:
                style "music_optionsO_hbox"
            else:
                style "music_optionsN_hbox"

            imagebutton:
                idle ConditionSwitch("organizeAZ", "mod_assets/music_player/A-ZOn.png", 
                                    "True", "mod_assets/music_player/A-Z.png")
                hover "mod_assets/music_player/A-ZHover.png"
                action [ToggleVariable("organizeAZ", False, True), Function(resort)]
            imagebutton:
                idle ConditionSwitch("organizePriority", "mod_assets/music_player/priorityOn.png", 
                                    "True", "mod_assets/music_player/priority.png")
                hover "mod_assets/music_player/priorityHover.png"
                action [ToggleVariable("organizePriority", False, True), Function(resort)]
            imagebutton:
                idle ConditionSwitch("loopSong", "mod_assets/music_player/replayOn.png", 
                                    "True", "mod_assets/music_player/replay.png")
                hover "mod_assets/music_player/replayHover.png"
                action [ToggleVariable("loopSong", False, True)]
            imagebutton:
                idle ConditionSwitch("randomSong", "mod_assets/music_player/shuffleOn.png", 
                                    "True", "mod_assets/music_player/shuffle.png")
                hover "mod_assets/music_player/shuffleHover.png"
                action [ToggleVariable("randomSong", False, True)]
            if not persistent.old_ui:
                imagebutton:
                    idle "mod_assets/music_player/refreshList.png"
                    hover "mod_assets/music_player/refreshHover.png"
                    action [Function(refresh_list)]
                imagebutton:
                    idle ConditionSwitch("persistent.old_ui", "mod_assets/music_player/OldUI.png", 
                                        "True", "mod_assets/music_player/NewUI.png")
                    hover ConditionSwitch("persistent.old_ui", "mod_assets/music_player/OldUIHover.png", 
                                        "True", "mod_assets/music_player/NewUIHover.png")
                    action [ToggleField(persistent, "old_ui", False, True)]

        if persistent.old_ui:
            hbox:
                style "music_options_hboxB"

                imagebutton:
                    idle "mod_assets/music_player/refreshList.png"
                    hover "mod_assets/music_player/refreshHover.png"
                    action [Function(refresh_list)]
                imagebutton:
                    idle ConditionSwitch("persistent.old_ui", "mod_assets/music_player/OldUI.png", 
                                        "True", "mod_assets/music_player/NewUI.png")
                    hover ConditionSwitch("persistent.old_ui", "mod_assets/music_player/OldUIHover.png", 
                                        "True", "mod_assets/music_player/NewUIHover.png")
                    action [ToggleField(persistent, "old_ui", False, True)]

        bar:
            if persistent.old_ui:
                style "music_player_timeO_bar"
            else:
                style "music_player_timeN_bar"

            value bar_val
            hovered bar_val.hovered
            unhovered bar_val.unhovered

        if current_soundtrack.author:
            vbox:
                if persistent.old_ui:
                    hbox: 
                        vbox:
                            style_prefix "playerO"
                            add "titleName"
                        vbox:
                            style_prefix "playerBO"
                            add "authorName"
                else:
                    hbox:
                        vbox:
                            style_prefix "playerN"
                            add "titleName"
                    hbox:
                        vbox:
                            style_prefix "playerBN"
                            add "authorName"
                    hbox:
                        vbox:
                            style_prefix "playerCN"
                            if current_soundtrack.description:
                                add "songDescription"
        
        if persistent.old_ui:
            if current_soundtrack.description:
                viewport id "desc":
                    mousewheel True
                    style "music_player_description_viewport"

                    add "songDescription"

                vbar value YScrollValue("desc") xpos 1250 ypos 470 ysize 200
        
        if persistent.old_ui:
            bar value Preference ("music_player_mixer volume") style "music_player_volumeO_bar"
        else:
            bar value Preference ("music_player_mixer volume") style "music_player_volumeN_bar"

        imagebutton:
            if persistent.old_ui:
                style "volume_optionsO_hbox"
            else:
                style "volume_optionsN_hbox"
            idle ConditionSwitch("preferences.get_volume(\"music_player_mixer\") == 0.0", 
                                "mod_assets/music_player/volume.png", "True", 
                                "mod_assets/music_player/volumeOn.png")
            hover ConditionSwitch("preferences.get_volume(\"music_player_mixer\") == 0.0", 
                                "mod_assets/music_player/volumeHover.png", "True", 
                                "mod_assets/music_player/volumeOnHover.png")
            action [Function(mute_player)]
        
        if persistent.old_ui:
            hbox:
                xoffset 520
                yoffset 480
                
                add "readablePos"
                add "readableDur" xpos 100
        else:
            add "readablePos" xalign 0.28 yalign 0.78
            add "readableDur" xalign 0.79 yalign 0.78

    text "DDLC OST-Player v[ostVersion]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"
    
    if not config.developer:
        add "rpa_map_warning" xpos 0.23 ypos 0.9

    textbutton _("Return"):
        style "return_button"
        action [Return(), Function(check_paused_state), 
                If(not prevTrack, None, 
                Play('music', prevTrack, fadein=2.0))]

transform cover_art_fade(x,y):
    anchor(0.5, 0.5)
    pos(x, y)
    size(350, 350)
    alpha 0
    linear 0.2 alpha 1

style play_pause_buttonO_hbox:
    pos (335, 520)
    spacing 25

style music_optionsO_hbox is play_pause_buttonO_hbox:
    pos (335, 570)

style volume_optionsO_hbox is play_pause_buttonO_hbox:
    pos (325, 475)
 
# controls title formatting
style playerO_vbox:
    xoffset 330 
    yoffset 390
    xsize 510
    xfill True

# controls artist formatting
style playerBO_vbox is playerO_vbox: 
    xpos 15
    xsize 420

style music_player_timeO_bar:
    xsize 450
    pos (320, 460)
    thumb "gui/slider/horizontal_hover_thumb.png"

style music_player_volumeO_bar:
    xsize 120
    pos (373, 490)
    thumb "gui/slider/horizontal_hover_thumb.png"

## New UI
style play_pause_buttonN_hbox is play_pause_buttonO_hbox:
    pos (715, 400)

style music_optionsN_hbox is music_optionsO_hbox:
    pos (715, 450)

style volume_optionsN_hbox is play_pause_buttonO_hbox:
    pos (1080, 504)

style playerN_vbox is playerO_vbox: 
    xoffset 700
    yoffset 208
    xsize 570

style playerBN_vbox is playerN_vbox:
    xpos 6

style playerCN_vbox is playerBN_vbox

style music_player_timeN_bar is music_player_timeO_bar:
    xsize 710
    pos (330, 520)

style music_player_volumeN_bar is music_player_volumeO_bar:
    pos (1130, 520)

style music_options_hboxB is play_pause_buttonO_hbox:
    pos (335, 610)

style music_player_list:
    left_padding 5

style music_player_list_button is navigation_button_text: 
    font "mod_assets/music_player/riffic-bold.ttf"
    size gui.text_size
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    line_spacing 5

style music_player_music_text is navigation_button_text:
    font "mod_assets/music_player/riffic-bold.ttf"
    color "#000"
    outlines [(0, "#000", 0, 0)]
    hover_outlines []
    insensitive_outlines []
    size 36

style music_player_song_author_text:
    #font "mod_assets/music_player/NotoSansSC-Light.otf"
    size 22
    outlines[]
    color "#000"

style song_progress_text:
    font "gui/font/Halogen.ttf"
    size 25
    outlines[]
    color "#000"
    xalign 0.28 
    yalign 0.78

style song_duration_text is song_progress_text:
    xalign 0.79 
    yalign 0.78

style music_player_description_viewport:
    pos (640, 520)
    size (580, 200)
    xfill True

style music_player_description_text is music_player_song_author_text

style music_player_viewport:
    pos(20, 20)
    xsize 210
    ysize 600