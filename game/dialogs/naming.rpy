    
default persistent.fae_gave_bad_name = 0


init 0 python in fae_nicknames:
    import re
    import store.fae_globals as fae_globals
    from Enum import Enum

    class NameType(Enum):
        bad = 1
        like = 2

    SWEAR_LIST = {
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

    BAD_NAMES = re.compile('|'.join(SWEAR_LIST), re.IGNORECASE)

    def find_nickname_category(nickname):

        if not isinstance(nickname, basestring):
            return None
        
        else:

            nickname = nickname.lower().replace(" ", "")

            if re.search(BAD_NAMES, nickname):
                return NameType.bad
            else:
                return NameType.like


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="sayori_give_nickname",
            unlocked=True,
            prompt="Nicknames",
            conditional="persistent.fae_allow_nicknames",
            category=["Sayori"],
            random=False,
            affection_range=(fae_affection.ENAMOURED, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label sayori_give_nickname:

    if persistent.fae_allow_nicknames and persistent.fae_current_nickname == "Sayori":
        s abfcaoa "Sure!"
    
    else:
        if persistent.fae_gave_bad_name == 0:
            s abfcaoa "Another nickname?"
            s abfccaa "Sure!"
        
        elif persistent.fae_gave_bad_name == 1:
            s  abfcaca "A new nickname?"
            s  abfcaaa "Oki-doki."
        
        elif persistent.fae_gave_bad_name == 2:
            s abhfaca "Alright."
            s bbhfaaa "Please be nice this time, [player]..."
        
        
    
    $ nickname = renpy.input(prompt="What do you want to call me?", allow=fae_globals.STANDARD_ALPHABETICAL_CHARACTERS, length=10).strip()

    if nickname.lower() == "nevermind":
        s abfcaoa "Changed your mind, [player]?"
        s abfccaa "Alright then!"
        s abhfaoa "Let me know if you ever come up with a new nickname for me!"
        return
    
    else:
        $ nickname_category = fae_nicknames.find_nickname_category(nickname)
    
    if not nickname_category == fae_nicknames.NameType.like:


        if persistent.fae_gave_bad_name == 0:
            s bbhfaca "This isn't like you..."
            s bbhflfa "That hurt, [player]..."
            
            python:
                persistent.fae_gave_bad_name += 1
                Sayori.add_new_regret_awaiting(fae_regrets.RegretTypes.bad_name)
                Affection.percentageAffectionLoss(1)

        elif persistent.fae_gave_bad_name == 1:
            s bbhfacag "Again?"
            s bbhflfag "That really hurts, [player]..."

            python:
                persistent.fae_gave_bad_name += 1
                Sayori.add_new_regret_awaiting(fae_regrets.RegretTypes.bad_name)
                Affection.percentageAffectionLoss(2.5)
            
        elif persistent.fae_gave_bad_name == 2:
            s bbhfmbag "Seriously?"
            s bbhflcag "Please stop..."

            python:
                Affection.percentageAffectionLoss(5)
                persistent.fae_gave_bad_name += 1
                Sayori.add_new_regret_awaiting(fae_regrets.RegretTypes.bad_name)
        
        elif persistent.fae_gave_bad_name == 3:
            s cbhfacah "No."
            s cbhflfah "No more."

            #$ persistent.fae_allow_nicknames = False

            python:
                Affection.percentageAffectionLoss(25)
                persistent.fae_nickname_current_nickname = None
                persistent.fae_gave_bad_name += 1
                s_name = "Sayori"
                Sayori.add_new_regret_awaiting(fae_regrets.RegretTypes.bad_name)
     
    else:
        
        $ persistent.fae_nickname_current_nickname = nickname
        $ s_name = persistent.fae_nickname_current_nickname

        $ Affection.calculatedAffectionGain(5)

        s abfcaob "Aww that’s a great nickname! {w=0.5}{nw}" 
        extend abgccab "I love it!"
        s abgcaob "Thanks, [player]!"
        return
        
    
    return

        

    
