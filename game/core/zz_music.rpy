init -1 python in sounds:
    import os
    import mutagen.mp3 as mutamp3
    import mutagen.oggopus as mutaopus
    import mutagen.oggvorbis as mutaogg
    import store


    #MUSICAL CONSTANTS (not quite as fun as musical chairs, but whatever)
    #SONG NAMES

    Bright_Lights = "Bright Lights"
    CB = "a2cb"
    Anji = "Anji"
    No_sound = "No Music"

    #FILE PATHS

    P_Bright_Lights = "mod_assets/bgm/bl.wav"
    P_CB = "mod_assets/bgm/a2cb.wav"
    P_Anji = "mod_assets/bgm/Anji.wav"
    P_No_sound = None

    def change_vol(channel="music", inc=True):
        direct = 1
        if not inc:
            direct = -1

        now_vol = _voltrans(getpvol(channel)+(direct*vol_change))
        setpvol(now_vol, channel)

    def getvol(channel):

        return renpy.audio.audio.get_channel(channel).context.secondary_volume

    def getpvol(channel):

        return renpy.game.preferences.volumes.get(
            renpy.audio.audio.get_channel(channel).mixer,
            0.0
        )

    def setpvol(value, channel):

        channel = renpy.audio.audio.get_channel(channel)
        if channel.mixer in renpy.game.preferences.volumes:
            renpy.game.preferences.volumes[channel.mixer] = _voltrans(value)

    def _voltrans(value):
        #Translating number to volume to be parsed
        if value < 0.0:
            return 0.0
        elif value > 1.0:
            return 1.0
        return value

    
    def GPMN():

        curr_filename = renpy.music.get_playing()

        if curr_filename:
            bracket_index = curr_filename.find(">")

            if bracket_index >=0:
                curr_filename = curr_filename[bracket_index:]
            
            for name,sounds in music_options:


                if sounds:
                    bracket_index = sounds.find(">")

                    if bracket_index >= 0:
                        check_sounds = sounds[bracket_index:]
                    else:
                        check_sounds = sounds
                else:
                    check_sounds = sounds
                
                if curr_filename == check_sounds:
                    return name
        return None

        
    
    ##################################################
    #SET UP THE MUSIC DATA TO BE PARSED IN THE SCREEN#
    ##################################################

    def musicmenu():

        global music_options
        global music_lists
        music_options = list()

        music_options.append((Bright_Lights, P_Bright_Lights))
        music_options.append((CB, P_CB))
        music_options.append((Anji, P_Anji))

        music_lists = __pagemake(music_options)


    def __pagemake(music_list):

        pagedict = dict()
        page = 0
        extras = music_list
        while len(extras) > 0:
            m_page, extras = __makepage(extras)
            pagedict[page] = m_page
            page += 1
        return pagedict
    
    def __makepage(music_list):

        return (music_list[:LIMIT], music_list[LIMIT:])


    def inList(filepath):

        for name,fpath in music_options:
            if filepath == fpath:
                return True
        return False



    LIMIT = 10
    playing_track = "mod_assets/bgm/bl.wav"
    sel_track = playing_track
    menuactive = False

    enabled = True


    vol_change = 0.1

    music_options = list()
    music_lists = dict() #Song pages shit


init 10 python in sounds:
    music_volume = getvol("music")


init 10 python:
    store.sounds.musicmenu()

    if not sounds.inList(persistent.playing_track):
        persistent.playing_track = None

    store.sounds.playing_track = persistent.playing_track
    store.sounds.sel_track = store.sounds.playing_track


###################
#MUSIC MENU STYLES#
###################

style neat_menu_navigation_frame is game_menu_navigation_frame
style neat_menu_content_frame is game_menu_content_frame
style neat_menu_viewport is game_menu_viewport
style neat_menu_side is game_menu_side
style neat_menu_label is game_menu_label
style neat_menu_label_text is game_menu_label_text
style neat_menu_return_button is return_button
style neat_menu_return_button_text is navigation_button_text
style neat_menu_prev_button is return_button
style neat_menu_prev_button_text is navigation_button_text






###################
#MUSIC MENU SCREEN#
###################

screen music_menu(m_page, page_no=0, page_extra=False):
    modal True

    $ import store.sounds as sounds

    if sounds.playing_track is None:
        $ return_value = sounds.No_sound
    else:
        $ return_value = sounds.playing_track
    
    key "noshift_M" action Return(return_value)
    key "noshift_m" action Return(return_value)

    zorder 200

    style_prefix "neat_menu"

    # this part copied from navigation menu
    vbox:
        style_prefix "neat_menu"

        xpos gui.navigation_xpos
#        yalign 0.4
        spacing gui.navigation_spacing

        # wonderful loop so we can dynamically add songs
        for name,sounds in m_page:
            textbutton _(name) action Return(sounds)

    vbox:

        yalign 1.0

        hbox:

            # dynamic prevous text, so we can keep button size alignments
            if page_no > 0:
                textbutton _("<<<< Prev"):
                    style "neat_menu_prev_button"
                    action Return(page_no - 1)

            else:
                textbutton _(""):
                    style "neat_menu_prev_button"
                    xsize 126
                    sensitive False

            if page_extra:
                textbutton _("Next >>>>"):
                    style "neat_menu_return_button"
                    action Return(page_no + 1)

        textbutton _(sounds.No_sound):
            style "neat_menu_return_button"
            action Return(sounds.No_sound)

        textbutton _("Return"):
            style "neat_menu_return_button"
            action Return(return_value)

    label "Music Menu"


label menu_show:

    python:
        import store.sounds as sounds
        sounds.menuactive = True
        track_sel = False
        active_page = 0

    while not track_sel:

        $ m_page = sounds.music_lists.get(active_page, None)

        if m_page is None:

            return sounds.No_sound
        
        $ n_page = (active_page + 1) in sounds.music_lists

        call screen music_menu(m_page, page_no=active_page, page_extra=n_page)

        $ active_page = _return
        $ track_sel = _return not in sounds.music_lists

    $ sounds.menuactive = False
    return _return


init python:
    import store.sounds as sounds

    def mute():

        vol = sounds.getpvol("music")

        sounds.setpvol(sounds.music_volume, "music")

    def red_vol():
        #REDUCE MUSIC

        sounds.change_vol(inc=False)

    def inc_vol():

        sounds.change_vol()


    def player(sounds, fadein=0.0, loop=True, set_per=False, fadeout=0.0, if_changed=False):
        

        if sounds is None:
            sounds = sounds.P_No_sound
            renpy.music.stop(channel="music", fadeout=fadeout)
        else:
            renpy.music.play(
                sounds,
                channel="music",
                loop=loop,
                synchro_start=True,
                fadein=fadein,
                fadeout=fadeout,
                if_changed=if_changed
            )
        sounds.playing_track = sounds
        sounds.sel_track = sounds

        if set_per:
            persistent.track_played = sounds


    def select_music():

        if sounds.enabled and not sounds.menuactive:

            sel_track = renpy.call_in_new_context("menu_show")
            if sel_track == sounds.No_sound:
                sel_track = sounds.P_No_sound

            if sel_track != sounds.playing_track:
                play_sounds(sel_track, set_per=True)
        
label music:
    s "Music! You can add your own too!"
    s "Eventually, that is ehehe"
    return
