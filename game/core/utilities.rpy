init -100 python in fae_utilities:

    import ctypes
    import random
    import math
    from collections import defaultdict

    def insert_sort(sort_list, item, key):

        index = len(sort_list) - 1
        while index >= 0 and key(sort_list[index]) > key(item):
            index -= 1

        sort_list.insert(index + 1, item)

    def nz_count(value_list):
        
        count = 0
        for value in value_list:
            count += int(value != 0)

        return count


    def ev_distribute(value_list, amt, nz=False):
       
        # determine effective size
        size = len(value_list)
        if nz:
            size -= nz_count(value_list)

        # deteremine distribution amount
        d_amt = amt / size

        # now distribute
        for index in range(len(value_list)):
            if not nz or value_list[index] > 0:
                value_list[index] += d_amt

        # leftovers
        return amt % size


    def lo_distribute(value_list, leftovers, reverse=False, nz=False):

        if nz:
            size = nz_count(value_list)
        else:
            size = len(value_list)

        # apply ev distribute if leftovesr is too large
        if leftovers >= size:
            leftovers = ev_distribute(value_list, leftovers, nz=nz)

        # dont add leftovers if none leftover
        if leftovers < 1:
            return

        # determine direction
        if reverse:
            indexes = range(len(value_list)-1, -1, -1)
        else:
            indexes = range(len(value_list))

        # apply leftovers
        index = 0
        while leftovers > 0 and index < len(indexes):
            real_index = indexes[index]
            if not nz or value_list[real_index] > 0:
                value_list[real_index] += 1
                leftovers -= 1

            index += 1


init -985 python in fae_utilities:

    
    def pdget(key, table, validator=None, defval=None):
        """
        Protected Dict GET
        Gets an item from a dict, using protections to ensure this item is
        valid

        IN:
            key - key of item to get
            table - dict to get from
            validator - function to call with the item to validate it
                If None, no validating done
                (Default: None)
            defval - default value to return if could not get from dict
        """
        if table is not None and key in table:

            item = table[key]

            if validator is None:
                return item

            if validator(table[key]):
                return item

        return defval
    import datetime

    def fae_getSessionLength():

        _now = datetime.datetime.now()
        return _now - store.fae_utilities.pdget(
            "current_session_start",
            persistent.sessions,
            #validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=_now
        )
    
    def fae_getAbsenceLength():

        return fae_getCurrSeshStart() - fae_getLastSeshEnd()
    
    def fae_getCurrSeshStart():
        
        return store.fae_utilities.pdget(
            "current_session_start",
            persistent.sessions,
            #validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=fae_getFirstSesh()
        )
    
    def fae_getFirstSesh():

        return store.fae_utilities.pdget(
            "first_session",
            persistent.sessions,
            #validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=datetime.datetime.now()
        )
    
    def fae_isFirstSeshPast(_date):

        return fae_getFirstSesh().date() > _date

    def fae_getLastSeshEnd():

        return store.fae_utilities.pdget(
            "last_session_end",
            persistent.sessions,
            #validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=fae_getFirstSesh()
        )
    
    def fae_TTDetected():

        return store.fae_globals.tt_detected
    

init -898 python in fae_globals:

    is_steam = "steamapps" in renpy.config.basedir.lower()


    
init 2 python:

    def fae_timePastSince(timekeeper, passed_time, _now=None):
        """
        Checks if a certain amount of time has passed since the time in the timekeeper
        IN:
            timekeeper:
                variable holding the time we last checked whatever it restricts
                (can be datetime.datetime or datetime.date)

            passed_time:
                datetime.timedelta of the amount of time which should
                have passed since the last check in order to return True

            _now:
                time to check against (If none, now is assumed, (Default: None))
        OUT:
            boolean:
                - True if it has been passed_time units past timekeeper
                - False otherwise
        """
        if timekeeper is None:
            return True

        elif _now is None:
            _now = datetime.datetime.now()

        #If our timekeeper is holding a datetime.date, we need to convert it to a datetime.datetime
        if not isinstance(timekeeper, datetime.datetime):
            timekeeper = datetime.datetime.combine(timekeeper, datetime.time())

        return timekeeper + passed_time <= _now

    def fae_hasRPYFiles():
        """
        Checks if there are rpy files in the gamedir
        """
        return len(fae_getRPYFiles()) > 0

    def fae_getRPYFiles():
        """
        Gets a list of rpy files in the gamedir
        """
        rpyCheckStation = store.FAEDockingStation(renpy.config.gamedir)

        return rpyCheckStation.getPackageList(".rpy")


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

        store.main_background.save()


init -999 python in fae_utilities:

    
    import datetime
    import os
    import store
    import pprint

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

        global rand_low
        global rand_high

        slider_setting = SLIDER_DEFS.get(slider_value, 4)


        rand_low = slider_setting
        rand_high = slider_setting * SPAN_MULTIPLIER
        store.persistent.fae_random_chat_rate = slider_value

        setWaitingTime()
    
    def getRandChatDisp(slider_value):

        return SLIDER_DEFS_DISP.get(slider_value, "UNKNOWN")

    def setWaitingTime():

        global randchat_time_left

        randchat_time_left = renpy.random.randint(rand_low, rand_high)

    def get_random_chat_frequency_desc():

        return _RANDOM_CHAT_FREQUENCY_DESC_DEFS.get(store.persistent.fae_random_chat_rate)
    
    def get_random_chat_timer():

        return _RANDOM_CHAT_FREQUENCY_TIMER_DEFS.get(store.persistent.fae_random_chat_rate)
    
    def wait():

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

        global randchat_time_left

        return randchat_time_left == 0 and rand_low != 0


#default persistent.fae_random_chat_rate = fae_utilities.random_chat_rate.SOMETIMES
default persistent.fae_repeat_chat = True


init 3 python:

    fae_bad_nickname_list = [
        r"\bfag\b",
        r"\bho\b",
        r"\bhoe\b",
        r"\btit\b",
        "abortion",
        "anal",
        "annoying",
        "anus",
        "arrogant",
        "(?<![blmprs])ass(?!i)",
        "atrocious",
        "awful",
        "bastard",
        "beast",
        "bitch",
        "blood",
        "boob",
        "boring",
        "bulli",
        "bully",
        "bung",
        "butt(?!er|on)",
        "cheater",
        "cock",
        "conceited",
        "condom",
        "coom",
        "corrupt",
        "cougar",
        "crap",
        "crazy",
        "creepy",
        "criminal",
        "cruel",
        "cum",
        "cunt",
        "damn",
        "demon",
        "dick",
        "dilf",
        "dildo",
        "dirt",
        "disgusting",
        "douche",
        "dumb",
        "egoist",
        "egotistical",
        "evil",
        "faggot",
        "failure",
        "fake",
        "fetus",
        "filth",
        "foul",
        "fuck",
        "garbage",
        "gay",
        "gey",
        "gilf",
        "gross",
        "gruesome",
        "hate",
        "heartless",
        "hideous",
        "hitler",
        "hore",
        "horrible",
        "horrid",
        "hypocrite",
        "idiot",
        "imbecile",
        "immoral",
        "insane",
        "irritating",
        "jerk",
        "jigolo",
        "jizz",
        "junk",
        "(?<!s)kill",
        "kunt",
        "lesbian",
        "lesbo",
        "lezbian",
        "lezbo",
        "(?<!fami)liar",
        "loser",
        r"\bmad\b",
        "maniac",
        "masochist",
        "milf",
        #"monika",
        "monster",
        "moron",
        "murder",
        "narcissist",
        "nasty",
        "natsuki",
        "nefarious",
        "nigga",
        "nigger",
        "nuts",
        "panti",
        "pantsu",
        "panty",
        "pedo",
        "penis",
        "plaything",
        "poison",
        "porn",
        "pretentious",
        "psycho",
        "puppet",
        "pussy",
        "(?<!g)rape",
        "repulsive",
        "retard",
        "rogue",
        "rump",
        "sadist",
        "selfish",
        "semen",
        "shit",
        "sick",
        "slaughter",
        r"\bslave\b",
        "slut",
        "sociopath",
        "soil",
        "sperm",
        "stink",
        "stupid",
        "suck",
        "tampon",
        "teabag",
        "terrible",
        "thot",
        "tits",
        "titt",
        "tool",
        "torment",
        "torture",
        "toy",
        "trap",
        "trash",
        "troll",
        "ugly",
        "useless",
        "vain",
        "vile",
        "vomit",
        "waste",
        "whore",
        "wicked",
        "witch",
        "worthless",
        "wrong",
        "yuri"
    ]

    #Base list for good nicknames. Apply modifiers for specifying the use
    #These trigger a good response
    fae_good_nickname_list_base = [
        "angel",
        "beautiful",
        "beauty",
        "best",
        "cuddl",
        "cute",
        "cutie",
        "darling",
        "gorgeous",
        "greatheart",
        "hero",
        "honey",
        "kind",
        "love",
        "pretty",
        "princess",
        "queen",
        "senpai",
        "sunshine",
        "sweet"
    ]

    #Modifier for the player's name choice
    fae_good_nickname_list_player_modifiers = [
        "king",
        "prince"
    ]

    #Modifier for Sayori's nickname choice
    fae_good_nickname_list_sayori_modifiers = [
        "sayo",
    ]

    fae_good_player_nickname_list = fae_good_nickname_list_base + fae_good_nickname_list_player_modifiers
    fae_good_sayori_nickname_list = fae_good_nickname_list_base + fae_good_nickname_list_sayori_modifiers

    #awkward names
    fae_awkward_nickname_list = [
        r"\b(step[-\s]*)?bro(ther|thah?)?",
        r"\b(step[-\s]*)?sis(ter|tah?)?",
        r"\bdad\b",
        r"\bloli\b",
        r"\bson\b",
        r"\bmama\b",
        r"\bmom\b",
        r"\bmum\b",
        r"\bpapa\b",
        r"\bwet\b",
        "aroused",
        "aunt",
        "batman",
        "baka",
        "breeder",
        "bobba",
        "boss",
        "catwoman",
        "cousin",
        "daddy",
        "deflowerer",
        "erection",
        "finger",
        "horny",
        "kaasan",
        "kasan",
        "lick",
        "master",
        "masturbat",
        "mistress",
        "moani",
        r"m[ou]m+[-\s]*ika",
        r"mom+[ay]",
        "mother",
        "naughty",
        "okaasan",
        "okasan",
        "orgasm",
        "overlord",
        "owner",
        "penetrat",
        "pillow",
        "sex",
        "spank",
        "superman",
        "superwoman",
        "thicc",
        "thighs",
        "uncle",
        "virgin"
    ]
    fae_good_player_name_comp = re.compile('|'.join(fae_good_player_nickname_list), re.IGNORECASE)
    fae_bad_name_comp = re.compile('|'.join(fae_bad_nickname_list), re.IGNORECASE)
    fae_awk_name_comp = re.compile('|'.join(fae_awkward_nickname_list), re.IGNORECASE)


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

    def show_calendar():

        renpy.call_in_new_context("fae_start_calendar_read_only")

    LCC = datetime.datetime.now()
    PRIOR_CHECK_MINUTELY = datetime.datetime.now()
    PRIOR_CHECK_HOURLY = PRIOR_CHECK_MINUTELY.hour
    PRIOR_CHECK_DAILY = PRIOR_CHECK_MINUTELY.day

    def minute_check():

        #checkReaction()

        #fae_clearNotifs()

        fae_utilities.save_game()

        Affection.DayAffectionGainChecker()

        store.fae_utilities.log(
            message="Affection level is {0}".format(
                store.persistent.affection
            ),
            logseverity=store.fae_utilities.SEVERITY_INFO
        )

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

                atq("silence_is_golden")
            
        return
    

    def qh_check():

        fae_sky.reload_sky()

        return
    

    def hh_check():

        return
    
    def h_check():


        
        return
    
    def d_check():

        fae_sky.reload_sky()

        if persistent.fae_last_visit_date.year != datetime.datetime.now().year:
            fae_events.resetHolidays()
        

        persistent.fae_last_visit_date = datetime.datetime.now()

        holiday_list = fae_events.selectHolidays()

        if holiday_list:
            holiday_list.sort(key = lambda holiday: holiday.priority)
            while len(holiday_list) > 0:
                holiday = holiday_list.pop()
                atq(holiday.label)

                if len(holiday_list) > 0:
                    atq("event_interlude")
                
                else:
                    atq("ch30_loop")
            
            renpy.jump("cnc")

        return



