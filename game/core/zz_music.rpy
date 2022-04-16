init -1 python in sounds:
    import os
    import mutagen.mp3 as muta3
    import mutagen.oggopus as mutaopus
    import mutagen.oggvorbis as mutaogg
    import store
    
    
    #MUSICAL CONSTANTS (not quite as fun as musical chairs, but whatever)
    
    #SONG NAMES

    Bright_Lights = "Bright Lights"
    CB = "a2cb"
    An = "Anji"
    Eurobeat_Reality = "Your Reality (Eurobeat Version)"
    Sayori_Piece = "Sayori Piece #1"
    Sayori2 = "Sayori Piece #2"
    She = "She"
    Is = "Is"
    Gonna = "Gonna"
    Kill = "Kill"
    Me = "Me"
    Me2 = "Me2"
    NO_SOUND = "No Music"

    #FILE PATHS

    P_Bright_Lights = "mod_assets/bgm/bl.wav"
    P_CB = "mod_assets/bgm/a2cb.wav"
    P_An = "mod_assets/bgm/Anji.wav"
    P_Eurobeat_Reailty = "mod_assets/bgm/eurobeatreality.ogg"
    P_Sayori_Piece = "mod_assets/bgm/eurobeatreality.ogg"
    P_Sayori2 = "mod_assets/bgm/eurobeatreality.ogg"
    P_She = "mod_assets/bgm/eurobeatreality.ogg"
    P_Is = "mod_assets/bgm/eurobeatreality.ogg"
    P_Gonna = "mod_assets/bgm/eurobeatreality.ogg"
    P_Kill = "mod_assets/bgm/eurobeatreality.ogg"
    P_Me = "mod_assets/bgm/eurobeatreality.ogg"
    P_Me2 = "mod_assets/bgm/eurobeatreality.ogg"
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

        chan = renpy.audio.audio.get_channel(channel)
        if chan.mixer in renpy.game.preferences.volumes:
            renpy.game.preferences.volumes[chan.mixer] = _voltrans(value)

    def _voltrans(value):
        #Translating number to volume to be parsed
        if value < 0.0:
            return 0.0
        elif value > 1.0:
            return 1.0
        return value

    
    def GPMN():
        
        #Gets name of currently playing song

        curr_filename = renpy.music.get_playing()

        if curr_filename:
            bracket_endex = curr_filename.find(">")

            if bracket_endex >=0:
                curr_filename = curr_filename[bracket_endex:]
            
            for name,sound in music_options:


                if sound:
                    bracket_endex = sound.find(">")

                    if bracket_endex >= 0:
                        check_sound = sound[bracket_endex:]
                    else:
                        check_sound = sound
                else:
                    check_sound = sound
                
                if curr_filename == check_sound:
                    return name
        return None

        
    
    ##################################################
    #SET UP THE MUSIC DATA TO BE PARSED IN THE SCREEN#
    ##################################################

    def initmusicmenu():

        global music_options
        global music_lists
        music_options = list()

        #music_options.append((Bright_Lights, P_Bright_Lights))
        #music_options.append((CB, P_CB))
        #music_options.append((An, P_An))
        #music_options.append((Sayori_Piece, P_Sayori_Piece))
        #music_options.append((Sayori2, P_Sayori2))
        music_options.append((She, P_She))
        music_options.append((Is, P_Is))
        music_options.append((Gonna, P_Gonna))
        music_options.append((Kill, P_Kill))
        music_options.append((Me, P_Me))
        #music_options.append((Me2, P_Me2))

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

        disp_name = None

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


    def _getMP3(filepath):

        try:
            return muta3.EasyMP3(filepath)
        except:
            return None
        
    def _MP3Name(_sound_file):

        return _OGGName(_sound_file)
    

    def _getOgg(filepath):

        try:
            return mutaogg.OggVorbis(filepath)
        except:
            return None
    
    def _OGGName(_sound_file):

        sound_names = _sound_file.tags.get(MT_TITLE, [])
        sound_artists = _sound_file.tags.get(MT_ARTIST, [])

        if not sound_names:

            return None

        selected_name = sound_names[0]

        if sound_artists:
            selected_art = sound_artists[0]
            return selected_art + " - " + selected_name
        
        return selected_name

    
    def _getOpus(filepath):
        try:
            return mutaopus.OggOpus(filepath)
        except:
            return None


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

    
    def inList(filepath):

        for name,fpath in music_options:
            if filepath == fpath:
                return True
        return False
    

    LIMIT = 10
    playing_track = "mod_assets/bgm/bl.wav"
    selected_track = playing_track
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

    store.sounds.initmusicmenu()

    if not sounds.inList(persistent.playing_track):
        persistent.playing_track = None

    store.sounds.playing_track = persistent.playing_track
    store.sounds.selected_track = store.sounds.playing_track
    #persistent.playing_track = store.sounds.Eurobeat_Reality


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
style neat_menu_frame is game_menu_outer_frame:
    background "mod_assets/m_frame.png"

style neat_menu_button is navigation_button
style neat_menu_button_text is navigation_button_text
    #properties gui.button_text_properties("navigation_button")
    #font "gui/font/s1.ttf"
    #color "#fff"
    #outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    #hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    #insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]






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
        style "neat_menu_frame"

        hbox:

            frame:
                style "neat_menu_navigation_frame"

            frame:
                style "neat_menu_content_frame"

                transclude

    # this part copied from navigation menu
        vbox:
            style_prefix "neat_menu"

            xpos gui.navigation_xpos
    #        yalign 0.4
            spacing gui.navigation_spacing

            # wonderful loop so we can dynamically add songs
            for name,sound in m_page:
                textbutton _(name) action Return(sound)

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

    def red_vol():
        #REDUCE MUSIC

        sounds.change_vol(inc=False)

    def inc_vol():

        sounds.change_vol()

    def mute():

        vol = sounds.getpvol("music")

        if (
            now_vol > 0.0

            ):
                sounds.music_volume = now_vol
                sounds.setpvol(0.0, "music")
        else:
            sounds.setpvol(sounds.music_volume, "music")


    def player(sound, fadein=0.0, loop=True, set_per=False, fadeout=0.0, if_changed=False):
        

        if sound is None:
            sound = sounds.P_NO_SOUND
            renpy.music.stop(channel="music", fadeout=fadeout)
        
        else:
            renpy.music.play(
                sound,
                channel="music",
                loop=loop,
                synchro_start=True,
                fadein=fadein,
                fadeout=fadeout,
                if_changed=if_changed
            )


        sounds.playing_track = sound
        sounds.selected_track = sound

        if set_per:
            persistent.playing_track = sound

    def begin_song():

        if persistent.playing_track is not None:
            player(persistent.playing_track, if_changed=True)

    def select_music():

        if sounds.enabled and not sounds.menuactive:

            selected_track = renpy.call_in_new_context("menu_show")
            if selected_track == sounds.NO_SOUND:
                selected_track = sounds.P_NO_SOUND

            if selected_track != sounds.playing_track:
                player(selected_track, set_per=True)
        
label music:
    s "Music! You can add your own too!"
    s "Eventually, that is ehehe"
    return
