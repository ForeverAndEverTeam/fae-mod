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
    NO_SOUND = "No Music"

    #FILE PATHS

    P_Bright_Lights = "mod_assets/bgm/bl.wav"
    P_CB = "mod_assets/bgm/a2cb.wav"
    P_Anji = "mod_assets/bgm/Anji.wav"
    P_NO_SOUND = None

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


    def __musicFinder(music_list):

        if not os.access(cmdir, os.F_OK):
            return

        found_audio = os.listdir(cmdir)
        found_oggs = [
            ogg_file
            for ogg_file in found_audio
            if (
                isValidExt(ogg_file)
                and os.access(cmdir + ogg_file, os.R_OK)
            )
        ]

        if len(found_oggs) == 0:
            return
        
        for ogg_file in found_oggs:

            filepath = cmdir + ogg_file

            _sound_file, _ext = _getSoundFile(filepath)

            if _sound_file is not None:

                disp_name = _findName(_sound_file, _ext, ogg_file)

                loop_prefix = _findLoop(_sound_file, _ext)


                music_list.append((
                    scrubText(disp_name),
                    loop_prefix + sm_reldir + ogg_file
                ))

                store.persistent.custom_music = True
    
    def _getSoundFile(filepath):
        
        
        if filepath.endswith(EXT_MP3):
            return (_getMP3(filepath), EXT_MP3)

        elif filepath.endswith(EXT_OGG):
            return (_getOgg(filepath), EXT_OGG)

        elif filepath.endswith(EXT_OPUS):
            return (_getOpus(filepath), EXT_OPUS)

        # otherwise, failure
        return (None, None)


    def _findName(_sound_file, _ext, _filename):

        if _sound_file.tags is not None:
            if _ext == EXT_MP3:
                disp_name = _MP3Name(_sound_file)
            
            elif _ext == EXT_OGG:
                disp_name = _OGGName(_sound_file)
            
            elif _ext == EXT_OPUS:
                disp_name = _OGGName(_sound_file)
        
        if not disp_name:

            return _filename[:-(len(_ext))]
        return disp_name


    def _getMP3(_sound_file):

        return _getOgg(_sound_file)

    def _getOgg(_sound_file):

        sound_names = _sound_file.tags.get(MT_TITLE, [])
        sound_artists = _sound_file.tags.get(MT_ARTIST, [])

        if not sound_names:
            return None
        
        sel_name = sound_names[0]

        if sound_artists:
            sel_art = sound_artists[0]
            return sel_art + " - " + sel_name
        
        return sel_name


    def inList(filepath):

        for name,fpath in music_options:
            if filepath == fpath:
                return True
        return False
    

    def isValidExt(filename):

        for ext in VALID_EXT:
            if filename.endswith(ext):
                return True
        return False
    

    def scrubText(unclean):
        
        bad_text = ("{", "}", "[", "]")

        # NOTE: for bad text, we just replace with empty
        cleaned_text = unclean
        for bt_el in bad_text:
            cleaned_text = cleaned_text.replace(bt_el, "")

        return cleaned_text



    LIMIT = 10
    playing_track = "mod_assets/bgm/bl.wav"
    sel_track = playing_track
    menuactive = False

    enabled = True


    vol_change = 0.1

    music_options = list()
    music_lists = dict() #Song pages shit

    cmdir = "custom_bgm"
    sm_reldir = "../" + cmdir + "/"

    # valid extensions for music
    # NOTE: Renpy also supports WAV, but only uncompressed PCM, so lets not
    #   assume that the user knows how to change song formats.
    EXT_OPUS = ".opus"
    EXT_OGG = ".ogg"
    EXT_MP3 = ".mp3"
    VALID_EXT = [
        EXT_OPUS,
        EXT_OGG,
        EXT_MP3
    ]

    # metadata tags
    MT_TITLE = "title"
    MT_ARTIST = "artist"

init 10 python in sounds:
    music_volume = getvol("music")


init 10 python:
    
    store.sounds.cmdir = (
        config.basedir + "/" + store.sounds.cmdir + "/"
    ).replace("\\", "/")



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
style m_frame is game_menu_outer_frame:
    background "mod_assets/m_frame.png"







###################
#MUSIC MENU SCREEN#
###################

screen music_menu(m_page, page_no=0, page_extra=False):
    modal True

    $ import store.sounds as sounds

    if sounds.playing_track is None:
        $ return_value = sounds.NO_SOUND
    else:
        $ return_value = sounds.playing_track
    
    key "noshift_M" action Return(return_value)
    key "noshift_m" action Return(return_value)

    zorder 200

    style_prefix "neat_menu"

    frame:
        style "m_frame"

        hbox:

            frame:
                style "neat_menu_nav"

            frame:
                style "neat_menu_content"

                transclude

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

        textbutton _(sounds.NO_SOUND):
            style "neat_menu_return_button"
            action Return(sounds.NO_SOUND)

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

            return sounds.NO_SOUND
        
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
            sounds = sounds.P_NO_SOUND
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
            if sel_track == sounds.NO_SOUND:
                sel_track = sounds.P_NO_SOUND

            if sel_track != sounds.playing_track:
                player(sel_track, set_per=True)
        
label music:
    s "Music! You can add your own too!"
    s "Eventually, that is ehehe"
    return
