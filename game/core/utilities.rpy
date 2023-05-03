init -999 python in fae_root:
    import store

    def falsify(affection):

        store.persistent.fae_bnc_unlocked = False
        store.persistent.fae_reversi_unlocked = False
        store.persistent.fae_custom_music_unlocked = False
        store.persistent.affection = affection



init python:

    def love(love_time=None):

        if love_time is None:
            love_time = datetime.datetime.now()
        persistent._fae_ily_last = love_time

    
    def time_love(time_since):

        check_time = datetime.datetime.now()

        if persistent._fae_ily_last is None or persistent._fae_ily_last > check_time:
            persistent._fae_ily_last = None
            return False
        
        return (check_time - persistent._fae_ily_last) <= time_since



init -1 python in fae_utilities:
    import re
    import store
    import store.fae_globals as fae_globals

    

    def save_game():

        

        store.Chat._save_chat_data()

        store.fae_outfits.FAEOutfit.store_all()

        #store.fae_events.FAEHoliday.storeAll()

        if store.persistent._affection_daily_bypasses > 5:
            store.persistent._affection_daily_bypasses = 5
        


        store.main_background.save()


init -999 python in fae_utilities:

    
    import datetime
    import os
    import store
    import pprint

    def __destroy_persistent(self):
            renpy.loadsave.location.unlink_persistent()
            renpy.persistent.should_save_persistent = False

    _logdir = os.path.join(renpy.config.basedir, "log")
    if not os.path.exists(_logdir):
        os.makedirs(_logdir)

    #We always want to log and keep history
    __main_log = renpy.renpy.log.open("log/log", append=True, flush=True)

    SEVERITY_INFO = 0
    SEVERITY_WARN = 1
    SEVERITY_ERR = 2

    LOGSEVERITY_MAP = {
        SEVERITY_INFO: "[{0}] [INFO]: {1}",
        SEVERITY_WARN: "[{0}] [WARNING]: {1}",
        SEVERITY_ERR: "[{0}] [ERROR]: {1}"
    }



    def log(message, logseverity=SEVERITY_INFO):
        """
        Writes a message to the main log file (DDLC/log/log.txt)

        IN:
            message - message to write to the log file
            logseverity - Severity level of the log message (Default: INFO)
        """
        global __main_log
        __main_log.write(
            LOGSEVERITY_MAP.get(
                logseverity,
                LOGSEVERITY_MAP[SEVERITY_INFO]
            ).format(datetime.datetime.now(), message)
        )

    def prettyPrint(object, indent=1, width=150):
        """
        Returns a PrettyPrint-formatted representation of an object as a dict.

        IN:
            object - the object to be converted
            indent - the level of indentation in the formatted string
            width - the maximum length of each line in the formatted string, before remaining content is shifted to next line

        OUT:
            Formatted string representation of object __dict__
        """
        return pprint.pformat(object.__dict__, indent, width)
    

    def doesExist(path):

        return os.path.isfile(path)
    
    def makedirifnot(path):

        if not os.path.exists(path) or doesExist(path):
            os.makedirs(path)
            return True
        
        return False
    
    def removeFileDir(path):

        if doesExist(path):
            try:
                os.remove(path)
                return True
            except Exception as exception:
                fae_log("Failed to delete file on path {0}; {1}".format(path, exception.message))
                return False
        else:
            renpy.notify("File doesn't exist.")
        return False
    
    def getDirFile(path, ext_list=None):

        return_file_items = []

        for file in os.listdir(path):
            if (not ext_list or any(file_extension == file.rpartition(".")[-1] for file_extension in ext_list)):
                return_file_items.append((file, os.path.join(path, file)))
        
        return return_file_items

    def RenpySubSub(string):

        return string.replace("[", "[[").replace("{", "{{")





default persistent._fae_random_chat_freq = fae_random_chat_rate.SOMETIMES
define fae_randchat_prev = persistent._fae_random_chat_freq
    
init -1 python in fae_random_chat_rate:
    import store

    NEVER = 0
    RARELY = 1
    SOMETIMES = 2
    FREQUENT = 3
    OFTEN = 4

    OFTEN_WAIT = 5
    FREQUENT_WAIT = 15
    SOMETIMES_WAIT = 40
    RARELY_WAIT = 20*60
    NEVER_WAIT = 0

    SPAN_MULTIPLIER = 3

    SLIDER_DEFS = {
        NEVER: NEVER_WAIT,
        RARELY: RARELY_WAIT,
        SOMETIMES: SOMETIMES_WAIT,
        FREQUENT: FREQUENT_WAIT,
        OFTEN: OFTEN_WAIT
    }

    SLIDER_DEFS_DISP = {
        NEVER: "Never",
        RARELY: "Rarely",
        SOMETIMES: "Sometimes",
        FREQUENT: "Frequent",
        OFTEN: "Often"
    }

    _RANDOM_CHAT_FREQUENCY_TIMER_DEFS = {
        0: 999,
        1: 30,
        2: 15,
        3: 5,
        4: 2,
    }

    _RANDOM_CHAT_FREQUENCY_DESC_DEFS = {
        0: "Never",
        1: "Rarely",
        2: "Sometimes",
        3: "Frequent",
        4: "Often",
    }

    rand_low = SOMETIMES
    rand_high = SOMETIMES * SPAN_MULTIPLIER
    randchat_time_left = 0


    def adjustRandFrequency(slider_value):

        """
        Changes the random amount based on slider

        FEED:
            slider_value: value from the random chat rate slider
            Value will be between 0 and 4
        """

        global rand_low
        global rand_high

        slider_setting = SLIDER_DEFS.get(slider_value, 4)


        rand_low = slider_setting
        rand_high = slider_setting * SPAN_MULTIPLIER
        store.persistent.fae_random_chat_rate = slider_value

        setWaitingTime()
    
    def getRandChatDisp(slider_value):

        """
        Uses the slider value and displays relevant string

        FEED:
            slider_value: value from the random chat rate slider
        
        RESULT:
            string that correlates to the random chat setting
        """

        return SLIDER_DEFS_DISP.get(slider_value, "UNKNOWN")

    def setWaitingTime():

        """
        Sets the wait time for the next topic. Depends on random chat setting
        """

        global randchat_time_left

        randchat_time_left = renpy.random.randint(rand_low, rand_high)

    def get_random_chat_frequency_desc():

        return _RANDOM_CHAT_FREQUENCY_DESC_DEFS.get(store.persistent.fae_random_chat_rate)
    
    def get_random_chat_timer():

        return _RANDOM_CHAT_FREQUENCY_TIMER_DEFS.get(store.persistent.fae_random_chat_rate)
    
    def wait():

        """
        Pauses Ren'Py for a short time.
        Events before a random topic can be handled.
        """

        global randchat_time_left

        WAITING_TIME = 5

        if randchat_time_left > WAITING_TIME:
            randchat_time_left -= WAITING_TIME
            renpy.pause(WAITING_TIME, hard=True)
        
        elif randchat_time_left > 0:
            waitFor = randchat_time_left
            randchat_time_left = 0
            renpy.pause(waitFor, hard=True)

        else:
            randchat_time_left = 0
            renpy.pause(WAITING_TIME, hard=True)
    
    def waitedLongEnough():

        """
        Is the waiting time done?

        RESULT:
            True if wait time is up, otherwise False
        """

        global randchat_time_left

        return randchat_time_left == 0 and rand_low != 0


#default persistent.fae_random_chat_rate = fae_utilities.random_chat_rate.SOMETIMES
default persistent.fae_repeat_chat = False

init -990 python in fae_globals:

    import re
    import store

    sesh_start = store.datetime.datetime.now()

    #pia = False

    allow_force_quit = True

    current_label = None

    last_label = None
    
    _CURSE_LIST = {
        "(?<![blmprs])ass(?!i)",
        "(^d[il1]ck$|d[il1]ckhead)",
        "(^dink$|dirsa)",
        "^fag{1,2}$",
        "[s5]h[i1]t",
        "(a_s_s|a55)",
        "anu[s5]",
        "(ar5e|arrse|^arse$)",
        "((b|l3)[i1]a?[t+7]ch)",
        "(bolloc?k)",
        "([ck]ock|cok)",
        "([ck]um|cunil|kunil)",
        "(doosh|duche)",
        "eja[ck]ul.*",
        "(f4nny|fanny|fanyy)",
        "([4f](uc?|oo|ec|cu)[kx]|f_u_c_k)",
        "god-dam",
        "(hoare?|hoer|hore)",
        "(horniest|horny)",
        "jack-?off",
        "ji[sz]m",
        "(m[a4][s5]t[eu]r-?b[a8][t+]?[e3]?|faeochist)",
        "m[o0]-?f[o0]",
        "n[1i]gg",
        "orgasi?m",
        "phuc?[kq]",
        "(porn|pron)",
        "puss[eiy]",
        "(rimjaw|rimming)",
        "(scroat|scrote|scrotum)",
        "(sh[i\!1][t+]e?|s_h_i_t)",
        "(testical|testicle)",
        "(^tit$|t[1i]tt[1i]e[5s]|teets|teez)",
        "(tw[4a]t|twunt)",
        "(willies|willy)",
        "^balls$",
        "^bum$",
        "^coon$",
        "^ho$",
        "^hoe$",
        "^nob$",
        "^tit$",
        "4r5e",
        "^aids$",
        "^anal$",
        "b!tch",
        "b[0o]+b(?!er|on)",
        "ballbag",
        "ballsack",
        "bastard",
        "beastial",
        "beastiality",
        "bellend",
        "bestial",
        "bestiality",
        "bloody",
        "blowjob",
        "boiolas",
        "boner",
        "breasts",
        "buceta",
        "bugger",
        "bunnyfucker",
        "butt(?!er|on)",
        "c0ck",
        "c0cksucker",
        "carpetmuncher",
        "cawk",
        "chink",
        "cipa",
        "clit|cl1t",
        "cnut",
        "crap",
        "cunt",
        "cyalis",
        "cyberfuc*",
        "damn",
        "dildo",
        "dog-fucker",
        "doggin",
        "donkeyribber",
        "dyke",
        "fatass",
        "felching",
        "fellat",
        "flange",
        "fudgepacker",
        "gangbang",
        "gaylord",
        "gaysex",
        "goatse",
        "goddamn",
        "h1tl3r",
        "h1tler",
        "hardcoresex",
        "(^hell$|^hellspawn$)",
        "heshe",
        "hitler",
        "homo",
        "hotsex",
        "^jap$",
        "jerk-off",
        "kawk",
        "knob",
        "kondum",
        "labia",
        "lmfao",
        "^lust$",
        "muff",
        "mutha",
        "nazi",
        "numbnuts",
        "nutsack",
        "p0rn",
        "pawn",
        "pecker",
        "pedo",
        "penis",
        "phonesex",
        "pigfucker",
        "pimpis",
        "piss",
        "poop",
        "prick",
        "pube",
        "rectum",
        "retard",
        "s.o.b.",
        "sadist",
        "schlong",
        "screw",
        "semen",
        "sex",
        "shag",
        "shemale",
        "skank",
        "slut",
        "smegma",
        "smut",
        "snatch",
        "son-of-a-bitch",
        "spac",
        "spunk",
        "tosser",
        "turd",
        "v14gra|v1gra",
        "vagina",
        "viagra",
        "vulva",
        "w00se",
        "wang",
        "wank",
        "whoar",
        "whore",
        "xrated",
        "xxx"
    }

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init python:

    

    LCC = datetime.datetime.now()
    PRIOR_CHECK_MINUTELY = datetime.datetime.now()
    PRIOR_CHECK_HOURLY = PRIOR_CHECK_MINUTELY.hour
    PRIOR_CHECK_DAILY = PRIOR_CHECK_MINUTELY.day

    def minute_check():

        #checkReaction()

        #fae_clearNotifs()

        fae_utilities.save_game()

        Affection.checkResetDailyAffectionGain()


        if (
            persistent._fae_random_chat_freq is not fae_random_chat_rate.NEVER
            #and datetime.datetime.now() > LCC + datetime.timedelta(minutes=fae_random_chat_rate.get_random_chat_timer())
            and not persistent._event_list
        ):


            if not persistent.fae_repeat_chat:
                chat_pool = Chat.chat_filt(
                    chats.CHAT_DEFS.values(),
                    unlocked=True,
                    random=True,
                    affection=Affection._getAffectionStatus(),
                    has_seen=False
                )
            
            else:
                chat_pool = Chat.chat_filt(
                    chats.CHAT_DEFS.values(),
                    unlocked=True,
                    random=True,
                    affection=Affection._getAffectionStatus(),
                    no_categories=["Setup"]
                )
            
            if chat_pool:
                if (not persistent.fae_repeat_chat):
                    store.persistent._oot = False
                
                #Affection.getAffectionGain()
                atq(random.choice(chat_pool).label)
            
            elif not store.persistent.fae_repeat_chat and not store.persistent._oot:

                ats("silence_is_golden")
            
        return
    

    def qh_check():

        fae_sky.reload_sky()

        return
    

    def hh_check():

        return
    
    def h_check():


        
        return
    
    def d_check():

        reset()

        fae_sky.reload_sky()

               

        persistent.fae_last_visit_date = datetime.datetime.now()

        
        return



