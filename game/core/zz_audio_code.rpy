
# Based off ost.py from Renpy-Universal-Player but Ren'Py 6 compatible

init python:
    import random
    import re
    import os
    import json
    import pygame_sdl2
    from tinytag import TinyTag

    # Creation of Music Room and Code Setup
    ostVersion = 2.1
    renpy.audio.music.register_channel("music_player", mixer="music_player_mixer", loop=False)
    if renpy.windows:
        gamedir = renpy.config.gamedir.replace("\\", "/")
    elif renpy.android:
        try: os.mkdir(os.path.join(os.environ["ANDROID_PUBLIC"], "game"))
        except: pass
        gamedir = os.path.join(os.environ["ANDROID_PUBLIC"], "game")
    else:
        gamedir = renpy.config.gamedir


    # Lists for holding media types
    autoDefineList = []
    manualDefineList = []
    soundtracks = []
    file_types = ('.mp3', '.ogg', '.opus', '.wav')

    # Stores soundtrack in progress
    current_soundtrack = False

    # Stores positions of track/volume/default priority
    time_position = 0.0
    time_duration = 3.0
    old_volume = 0.0
    priorityScan = 2

    # Stores paused track/player controls
    current_soundtrack_pause = False
    prevTrack = False
    randomSong = False
    loopSong = False
    organizeAZ = False
    organizePriority = True
    pausedstate = False

    random.seed()

    class soundtrack:
        def __init__(self, name="", path="", priority=2, author="", byteTime=False, 
                    description="", cover_art=False, unlocked=True):
            self.name = name
            self.path = path
            self.priority = priority
            self.author = author
            self.byteTime = byteTime
            self.description = description
            if not cover_art:
                self.cover_art = "mod_assets/music_player/nocover.png"
            else:
                self.cover_art = cover_art
            self.unlocked = unlocked

    @renpy.exports.pure
    class AdjustableAudioPositionValue(renpy.ui.BarValue):
        def __init__(self, channel='music_player', update_interval=0.0):
            self.channel = channel
            self.update_interval = update_interval
            self.adjustment = None
            self._hovered = False

        def get_pos_duration(self):
            if not renpy.audio.music.is_playing(self.channel):
                pos = time_position
            else:
                pos = renpy.audio.music.get_pos(self.channel) or 0.0
            duration = time_duration

            return pos, duration

        def get_song_options_status(self):
            return loopSong, randomSong

        def get_adjustment(self):
            pos, duration = self.get_pos_duration()
            self.adjustment = renpy.ui.adjustment(value=pos, range=duration, 
                                                changed=self.set_pos, adjustable=True)

            return self.adjustment

        def hovered(self):
            self._hovered = True

        def unhovered(self):
            self._hovered = False

        def set_pos(self, value):
            loopThis = self.get_song_options_status()
            if (self._hovered and pygame_sdl2.mouse.get_pressed()[0]):
                renpy.audio.music.play("<from {}>".format(value) + current_soundtrack.path,
                                    self.channel)
                if loopThis:
                    renpy.audio.music.queue(current_soundtrack.path, self.channel, 
                                        loop=True)

        def periodic(self, st):

            pos, duration = self.get_pos_duration()
            loopThis, doRandom = self.get_song_options_status()

            if pos and pos <= duration:
                self.adjustment.set_range(duration)
                self.adjustment.change(pos)
                        
            if pos > duration - 0.20:
                if loopThis:
                    renpy.audio.music.play(current_soundtrack.path, self.channel, loop=True)
                elif doRandom:
                    random_song()
                else:
                    next_track()

            return self.update_interval 

    def music_pos(style_name, st, at):
        global time_position

        if renpy.audio.music.get_pos(channel='music_player') is not None:
            time_position = renpy.audio.music.get_pos(channel='music_player')

        readableTime = convert_time(time_position)
        d = renpy.text.text.Text(readableTime, style=style_name) 
        return d, 0.20

    def music_dur(style_name, st, at):
        global time_duration
            
        if current_soundtrack.byteTime:
            time_duration = current_soundtrack.byteTime
        else:
            time_duration = renpy.audio.music.get_duration(
                                                        channel='music_player') or time_duration 

        readableDuration = convert_time(time_duration) 
        d = renpy.text.text.Text(readableDuration, style=style_name)     
        return d, 0.20

    def dynamic_title_text(style_name, st, at):
        title = len(current_soundtrack.name)

        if title <= 21: 
            songNameSize = int(37) 
        elif title <= 28:
            songNameSize = int(29)
        else:
            songNameSize = int(23)

        d = renpy.text.text.Text(current_soundtrack.name, style=style_name, substitute=False, 
                                size=songNameSize)
        return d, 0.20

    def dynamic_author_text(style_name, st, at):
        author = len(current_soundtrack.author)

        if author <= 32:
            authorNameSize = int(25)
        elif author <= 48:
            authorNameSize = int(23)
        else:
            authorNameSize = int(21)

        d = renpy.text.text.Text(current_soundtrack.author, style=style_name, substitute=False, 
                                size=authorNameSize)
        return d, 0.20

    def refresh_cover_data(st, at):
        d = renpy.display.im.image(current_soundtrack.cover_art)
        return d, 0.20

    def dynamic_description_text(style_name, st, at):
        desc = len(current_soundtrack.description)

        if desc <= 32:
            descSize = int(25)
        elif desc <= 48:
            descSize = int(23)
        else:
            descSize = int(21)

        d = renpy.text.text.Text(current_soundtrack.description, style=style_name, 
                                substitute=False, size=descSize) 
        return d, 0.20

    def auto_play_pause_button(st, at):
        if renpy.audio.music.is_playing(channel='music_player'):
            if pausedstate:
                d = renpy.display.behavior.ImageButton("mod_assets/music_player/pause.png")
            else:
                d = renpy.display.behavior.ImageButton("mod_assets/music_player/pause.png", 
                                                    action=current_music_pause)
        else:
            d = renpy.display.behavior.ImageButton("mod_assets/music_player/play.png", 
                                                action=current_music_play)
        return d, 0.20

    def rpa_mapping_detection(style_name, st, at):
        try: 
            renpy.exports.file("RPASongMetadata.json")
            return renpy.text.text.Text("", size=23), 0.0
        except:
            return renpy.text.text.Text("{b}Warning:{/b} The RPA metadata file hasn't been generated. Songs in the {i}track{/i} folder that are archived into a\nRPA won't work without it. Set {i}config.developer{/i} to {i}True{/i} in order to generate this file.", style=style_name, size=20), 0.0

    def convert_time(x):
        hour = ""

        if int (x / 3600) > 0:
            hour = str(int(x / 3600))
        
        if hour != "":
            if int((x % 3600) / 60) < 10:
                minute = ":0" + str(int((x % 3600) / 60))
            else:
                minute = ":" + str(int((x % 3600) / 60))
        else:
            minute = "" + str(int(x / 60))

        if int(x % 60) < 10:
            second = ":0" + str(int(x % 60))
        else:
            second = ":" + str(int(x % 60))

        return hour + minute + second

    def current_music_pause():
        global current_soundtrack_pause, pausedstate
        pausedstate = True

        if not renpy.audio.music.is_playing(channel='music_player'):
            return
        else:
            soundtrack_position = renpy.audio.music.get_pos(channel = 'music_player') #+ 1.6

        if soundtrack_position is not None:
            current_soundtrack_pause = ("<from " + str(soundtrack_position) + ">" 
                                + current_soundtrack.path)

        renpy.audio.music.stop(channel='music_player',fadeout=0.0)

    def current_music_play():
        global pausedstate
        pausedstate = False

        if not current_soundtrack_pause:
            renpy.audio.music.play(current_soundtrack.path, channel = 'music_player', fadein=0.0)
        else:
            renpy.audio.music.play(current_soundtrack_pause, channel = 'music_player', fadein=0.0)
        
    def current_music_forward():
        global current_soundtrack_pause

        if renpy.audio.music.get_pos(channel = 'music_player') is None:
            soundtrack_position = time_position + 5
        else:
            soundtrack_position = renpy.audio.music.get_pos(channel = 'music_player') + 5

        if soundtrack_position >= time_duration: 
            current_soundtrack_pause = False
            if randomSong:
                random_song()
            else:
                next_track()
        else:
            current_soundtrack_pause = ("<from " + str(soundtrack_position) + ">" 
                                + current_soundtrack.path)

            renpy.audio.music.play(current_soundtrack_pause, channel = 'music_player')

    def current_music_backward():
        global current_soundtrack_pause

        if renpy.audio.music.get_pos(channel = 'music_player') is None:
            soundtrack_position = time_position - 5
        else:
            soundtrack_position = renpy.audio.music.get_pos(channel = 'music_player') - 5

        if soundtrack_position <= 0.0:
            current_soundtrack_pause = False
            next_track(back=True)
        else:
            current_soundtrack_pause = ("<from " + str(soundtrack_position) + ">" 
                                + current_soundtrack.path)
                
            renpy.audio.music.play(current_soundtrack_pause, channel = 'music_player')

    def next_track(back=False):
        global current_soundtrack

        for index, item in enumerate(soundtracks):
            if (current_soundtrack.description == item.description 
                and current_soundtrack.name == item.name):
                try:
                    if back:
                        current_soundtrack = soundtracks[index-1]
                    else:
                        current_soundtrack = soundtracks[index+1]
                except:
                    if back:
                        current_soundtrack = soundtracks[-1]
                    else:
                        current_soundtrack = soundtracks[0]
                break

        if current_soundtrack != False:
            renpy.audio.music.play(current_soundtrack.path, channel='music_player', loop=loopSong)

    def random_song():
        global current_soundtrack

        unique = 1
        if soundtracks[-1].path == current_soundtrack.path:
            pass
        else:
            while unique != 0:
                a = random.randrange(0, len(soundtracks)-1)
                if current_soundtrack != soundtracks[a]:
                    unique = 0
                    current_soundtrack = soundtracks[a]

        if current_soundtrack != False:
            renpy.audio.music.play(current_soundtrack.path, channel='music_player', loop=loopSong)

    def mute_player():
        global old_volume

        if renpy.game.preferences.get_volume("music_player_mixer") != 0.0:
            old_volume = renpy.game.preferences.get_volume("music_player_mixer")
            renpy.game.preferences.set_volume("music_player_mixer", 0.0)
        else:
            if old_volume == 0.0:
                renpy.game.preferences.set_volume("music_player_mixer", 0.5)
            else:
                renpy.game.preferences.set_volume("music_player_mixer", old_volume)

    def refresh_list():
        scan_song()
        if renpy.config.developer or renpy.config.developer == "auto":
            rpa_mapping()
        resort()

    def resort():
        global soundtracks
        soundtracks = [] 

        for obj in autoDefineList:
            if obj.unlocked:
                soundtracks.append(obj)
        for obj in manualDefineList:
            if obj.unlocked:
                soundtracks.append(obj)

        if organizeAZ:
            soundtracks = sorted(soundtracks, key=lambda soundtracks: 
                soundtracks.name)
        if organizePriority:
            soundtracks = sorted(soundtracks, key=lambda soundtracks: 
                soundtracks.priority)

    def get_info(path, tags):   
        sec = tags.duration
        try:
            image_data = tags.get_image()

            with open(os.path.join(gamedir, "python-packages/binaries.txt"), "rb") as a:
                lines = a.readlines()

            jpgbytes = bytes("\\xff\\xd8\\xff")
            utfbytes = bytes("o\\x00v\\x00e\\x00r\\x00\\x00\\x00\\x89PNG\\r\\n")

            jpgmatch = re.search(jpgbytes, image_data) 
            utfmatch = re.search(utfbytes, image_data) 

            if jpgmatch:
                cover_formats=".jpg" 
            else:
                cover_formats=".png" 

                if utfmatch: # addresses itunes cover descriptor fixes
                    image_data = re.sub(utfbytes, lines[2], image_data)

            coverAlbum = re.sub(r"\[|\]|/|:|\?",'', tags.album) 
            
            with open(os.path.join(gamedir, 'custom_bgm/covers', coverAlbum + cover_formats), 'wb') as f:
                f.write(image_data)

            art = coverAlbum + cover_formats
            return tags.title, tags.artist, sec, art, tags.album, tags.comment
        except TypeError:
            return tags.title, tags.artist, sec, None, tags.album, tags.comment

    def scan_song():
        global autoDefineList

        exists = []
        for x in autoDefineList[:]:
            try:
                renpy.exports.file(x.path)
                exists.append(x.path)    
            except:
                autoDefineList.remove(x)
        
        for x in os.listdir(gamedir + '/custom_bgm'):
            if x.endswith((file_types)) and "custom_bgm/" + x not in exists:
                path = "custom_bgm/" + x
                tags = TinyTag.get(gamedir + "/" + path, image=True) 
                title, artist, sec, altAlbum, album, comment = get_info(path, tags)
                def_song(title, artist, path, priorityScan, sec, altAlbum, album, 
                        comment, True)

    def def_song(title, artist, path, priority, sec, altAlbum, album, comment, 
                unlocked=True):
        if title is None:
            title = str(path.replace("custom_bgm/", "")).capitalize()
        if artist is None or artist == "":
            artist = "Unknown Artist"
        if altAlbum is None or altAlbum == "":
            altAlbum = "mod_assets/music_player/nocover.png" 
        else:
            altAlbum = "custom_bgm/covers/"+altAlbum
            try:
                renpy.exports.image_size(altAlbum)
            except:
                altAlbum = "mod_assets/music_player/nocover.png" 
        if album is None or album == "": 
            description = "Non-Metadata Song"
        else:
            if comment is None: 
                description = album
            else:
                description = album + '\n' + comment 
                
        class_name = re.sub(r"-|'| ", "_", title)

        class_name = soundtrack(
            name = title,
            author = artist,
            path = path,
            byteTime = sec,
            priority = priority,
            description = description,
            cover_art = altAlbum,
            unlocked = unlocked
        )
        autoDefineList.append(class_name)

    def rpa_mapping():
        data = []
        try: os.remove(os.path.join(gamedir, "RPASongMetadata.json"))
        except: pass
        for y in autoDefineList:
            data.append ({
                "class": re.sub(r"-|'| ", "_", y.name),
                "title": y.name,
                "artist": y.author,
                "path": y.path,
                "sec": y.byteTime,
                "altAlbum": y.cover_art,
                "description": y.description,
                "unlocked": y.unlocked,
            })
        with open(gamedir + "/RPASongMetadata.json", "a") as f:
            json.dump(data, f)

    def rpa_load_mapping():
        try: renpy.exports.file("RPASongMetadata.json")
        except: return

        with renpy.exports.file("RPASongMetadata.json") as f:
            data = json.load(f)

        for p in data:
            title, artist, path, sec, altAlbum, description, unlocked = (p['title'], 
                                                                        p['artist'], 
                                                                        p["path"], 
                                                                        p["sec"], 
                                                                        p["altAlbum"], 
                                                                        p["description"], 
                                                                        p["unlocked"])

            p['class'] = soundtrack(
                name = title,
                author = artist,
                path = path,
                byteTime = sec,
                priority = priorityScan,
                description = description,
                cover_art = altAlbum,
                unlocked = unlocked
            )
            autoDefineList.append(p['class'])

    def get_music_channel_info():
        global prevTrack

        prevTrack = renpy.audio.music.get_playing(channel='music')
        if prevTrack is None:
            prevTrack = False

    def check_paused_state():
        if not current_soundtrack or pausedstate:
            return
        else:
            #current_music_play()
            return

    try: os.mkdir(gamedir + "/custom_bgm")
    except: pass
    try: os.mkdir(gamedir + "/custom_bgm/covers")
    except: pass

    for x in os.listdir(gamedir + '/custom_bgm/covers'):
        os.remove(gamedir + '/custom_bgm/covers/' + x)

    scan_song()
    if renpy.config.developer or renpy.config.developer == "auto":
        rpa_mapping()
    else:
        rpa_load_mapping()
    resort()