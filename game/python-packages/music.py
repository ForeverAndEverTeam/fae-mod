import os

music_comment = """
#I see you decided to add new music to the music list.
#
#Follow the below syntax:
#"Displayed Name" "Ren'Py filepath (relative to mod_assets/music)" #Single File
#"Displayed Name" ["filepath1", "filepath2", ...] #File list
#
#You can also use filepath music options (<from>, <to> & <loop>) in the filepaths
#I believe you have good taste in music
"""

compatible_formats = ["mp3", "ogg", "wav", "opus"]
MUSIC_CUSTOM_PREFIX = "mod_assets/music/"
music_list = []
MUSIC_FALLBACK = -1
music_list_len = 0

def music_register(name, path):
        global music_list, music_list_len
        music_list.append((name, path))
        music_list_len += 1

def read_list(filelist = "list.txt"):
        new = 0
        try:
            f = renpy.file(MUSIC_CUSTOM_PREFIX + filelist)
            fs = []
            
            for line in f.readlines():
                info = []
                pos = 0
                closed = True
                s = ""
                l = info
                le = len(line)
                
                while pos < le and line[pos] != '#' and line[pos] != '\n':
                    if line[pos] == '\"':
                        if pos > 0 and line[pos-1] == '\\':
                            s = s[:-1] + "\""
                        elif not closed:
                            closed = True
                            l.append(s)
                            s = ""
                        else:
                            closed = False
                    elif line[pos+1] == '[' and closed and line[pos] != '\\':
                        l = []
                    elif line[pos+1] == ']' and closed and line[pos] != '\\':
                        info.append(l)
                        l = info
                    elif not closed:
                        s += line[pos]
                    pos += 1
                
                if len(info) == 2 and (type(info[0]) == unicode or type(info[0]) == str):
                    pos = info[1].rfind('>') + 1
                    info[1] = info[1][:pos] + MUSIC_CUSTOM_PREFIX + info[1][pos:]
                    music_register(*info)
                    new += 1
        
        except IOError:
            if filelist != 'list.txt':
                return music_custom_find()
        
        return new

def autoscan(append = True, music_dir = MUSIC_CUSTOM_PREFIX):
    new = 0
    
    l = os.listdir(config.basedir + '/game/' + music_dir)
    l = filter(lambda x: x.rsplit('.', 1)[1] in compatible_formats, l)
    
    for i in l:
        il = len(i)
        
        found = not append
        
        if append:
            for j in music_list:
                if j[1].rsplit('/', 1)[-1].rsplit('>', 1)[-1] == i:
                    found = True
                    break
        
        if not found:
            music_register(i.split('.')[0], MUSIC_CUSTOM_PREFIX + '/' + i)
            new += 1
        
    return new

def print_list(filelist = "list.txt"):
    with file.open(config.basedir.replace('\\\\', '/') + '/' + filelist, 'w') as f:
        f.write(music_comment + '\n\n')
        for i in music_list:
            f.write("    ".join(i))
            f.write('\n')

def switch(id = MUSIC_FALLBACK):
        if id > (globals().get("music_list_len") or len(music_list)) - 1:
            return switch()
        renpy.music.stop()
        persistent.currentmusic = id
        if id >= 0:
            renpy.music.queue(music_list[id][1], loop=True)
