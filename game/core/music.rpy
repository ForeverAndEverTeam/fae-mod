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

style music_menu_navigation_frame is game_menu_navigation_frame
style music_menu_content_frame is game_menu_content_frame
style music_menu_viewport is game_menu_viewport
style music_menu_side is game_menu_side
style music_menu_label is game_menu_label
style music_menu_label_text is game_menu_label_text
style music_menu_return_button is return_button
style music_menu_return_button_text is navigation_button_text
style music_menu_prev_button is return_button
style music_menu_prev_button_text is navigation_button_text






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
    


    label "Music_menu"





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




label music:
    s "Music! You can add your own too!"
    s "Eventually, that is ehehe"
    return
