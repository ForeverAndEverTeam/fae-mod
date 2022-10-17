

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
            #validator=store.mas_ev_data_ver._verify_dt_nn,
            defval=_now
        )
    
    def fae_getAbsenceLength():

        return fae_getCurrSeshStart() - fae_getLastSeshEnd()
    
    def fae_getCurrSeshStart():
        
        return store.fae_utilities.pdget(
            "current_session_start",
            persistent.sessions,
            #validator=store.mas_ev_data_ver._verify_dt_nn,
            defval=fae_getFirstSesh()
        )
    
    def fae_getFirstSesh():

        return store.fae_utilities.pdget(
            "first_session",
            persistent.sessions,
            #validator=store.mas_ev_data_ver._verify_dt_nn,
            defval=datetime.datetime.now()
        )
    
    def fae_isFirstSeshPast(_date):

        return fae_getFirstSesh().date() > _date

    def fae_getLastSeshEnd():

        return store.fae_utilities.pdget(
            "last_session_end",
            persistent.sessions,
            #validator=store.mas_ev_data_ver._verify_dt_nn,
            defval=fae_getFirstSesh()
        )
    
    def fae_TTDetected():

        return store.fae_globals.tt_detected
    

init -898 python in fae_globals:

    is_steam = "steamapps" in renpy.config.basedir.lower()


    
init 2 python:

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
        return False
    
    def getDirFile(path, ext_list=None):

        return_file_items = []

        for file in os.listdir(path):
            if (not ext_list or any(file_extension == file.rpartition(".")[-1] for file_extension in ext_list)):
                return_file_items.append((file, os.path.join(path, file)))
        
        return return_file_items

    def RenpySubSub(string):

        return string.replace("[", "[[").replace("{", "{{")





    

    
init python in fae_utilities.random_chat_rate:
    import store

    NEVER = 0
    RARELY = 1
    SOMETIMES = 2
    FREQUENT = 3
    OFTEN = 4

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

    def get_random_chat_frequency_desc():

        return _RANDOM_CHAT_FREQUENCY_DESC_DEFS.get(store.persistent.fae_random_chat_rate)
    
    def get_random_chat_timer():

        return _RANDOM_CHAT_FREQUENCY_TIMER_DEFS.get(store.persistent.fae_random_chat_rate)

default persistent.fae_random_chat_rate = fae_utilities.random_chat_rate.SOMETIMES
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
        "(m[a4][s5]t[eu]r-?b[a8][t+]?[e3]?|masochist)",
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
            persistent.fae_random_chat_rate is not fae_utilities.random_chat_rate.NEVER
            and datetime.datetime.now() > LCC + datetime.timedelta(minutes=fae_utilities.random_chat_rate.get_random_chat_timer())
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
            
        pass
    

    def qh_check():

        fae_sky.reload_sky()

        pass
    

    def hh_check():

        pass
    
    def h_check():

        #main_background.reset_checker()

        
        pass
    
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

        pass



init -999 python in fae_ev_data_ver:

    import builtins

    import datetime


    def _verify_bool(val, allow_none=True):
        return _verify_item(val, bool, allow_none)


    def _verify_dict(val, allow_none=True):
        return _verify_item(val, builtins.dict, allow_none)


    def _verify_list(val, allow_none=True):
        return _verify_item(val, builtins.list, allow_none)


    def _verify_dt(val, allow_none=True):
        if (
                isinstance(val, datetime.datetime)
                and val.year < 1900
            ):
            return False
        return _verify_item(val, datetime.datetime, allow_none)


    def _verify_dt_nn(val):
        return _verify_dt(val, False)
    
    def _verify_int(val, allow_none=True):
        return _verify_item(val, int, allow_none)


    def _verify_int_nn(val):
        return _verify_int(val, False)


    def _verify_str(val, allow_none=True):
        if val is None:
            return allow_none

        return isinstance(val, str) or isinstance(val, unicode)


    def _verify_td(val, allow_none=True):
        if val is None:
            return allow_none
        return _verify_item(val, datetime.timedelta, allow_none)


    def _verify_td_nn(val):
        return _verify_td(val, False)


    def _verify_tuli(val, allow_none=True):
        if val is None:
            return allow_none

        return isinstance(val, builtins.list) or isinstance(val, tuple)


    def _verify_tuli_nn(val):
        return _verify_tuli(val, False)


    def _verify_tuli_aff(val, allow_none=True):
        if val is None:
            return allow_none

        return isinstance(val, tuple) and len(val) == 2


    def _verify_item(val, _type, allow_none=True):
        """
        Verifies the given value has the given type/instance

        IN:
            val - value to verify
            _type - type to check
            allow_none - If True, None should be considered good value,
                false means bad value
                (Default: True)

        RETURNS: True if the given value has the given type/instance,
            false otherwise
        """
        if val is None:
            return allow_none

        # otherwise check item
        return isinstance(val, _type)


init -998 python in fae_ev_data_ver:

    import time
    import renpy
    import store


    def _verify_per_mtime():
        """
        verifies persistent data and ensure mod times are not in the future
        """
        curr_time = time.time()

        # check renpy persistent mtime
        if renpy.persistent.persistent_mtime > curr_time:
            renpy.persistent.persistent_mtime = curr_time

        # then save location mtime
        if renpy.loadsave.location is not None:
            locs = renpy.loadsave.location.locations
            if locs is not None and len(locs) > 0 and locs[0] is not None:
                if locs[0].persistent_mtime > curr_time:
                    locs[0].persistent_mtime = curr_time

        # then individual mtimes
        for varkey in store.persistent._changed:
            if store.persistent._changed[varkey] > curr_time:
                store.persistent._changed[varkey] = curr_time

    # verify
    try:
        _verify_per_mtime()
        valid_times = True
    except:
        valid_times = False
        store.fae_utilities.fae_log.error("[EARLY]: Failed to verify mtimes")

    