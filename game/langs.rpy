# Mod language functions
init -10 python:
    from collections import OrderedDict
    
    class GameLang:
        def __init__(self, code, name = None, unicode = True, s_names = ("Sayori", ), unix_code = None, wip = False):
            self.code = code #Stands for the language's ISO 639-3 code (excepting English, whose value is None) and the Ren'py language name
            self.name = name or code #Full language name (should be translatable)
            self.unicode = unicode #Does language use non-ASCII characters? (Then we replace all ASCII fonts with their Unicode analogs)
            self.s_names = s_names #Tuple of Sayori's name variants in the language
            self.unix_code = unix_code or code[:2] # Unix locale code's 2 first letters
            self.wip = False if (wip is None) else wip #the language pack is not complete, so it's available only for developers
    
    lang_dict = OrderedDict() #Language list
    lang_dict["eng"] = GameLang(None, _("English"), False, ("Sayori", ), "en"),
    lang_dict["rus"] = GameLang("rus", _("Russian"), True, ("Сайори", "Саёри")), #Key sould be equal value.code (exp. English)
    lang_dict["epo"] = GameLang("epo", _("Esperanto"), True, ("Sajori", "Sayori"), "eo"),
    lang_dict["esp"] = GameLang("esp", _("Spanish"), False, ("Sayori", ), "es")
    lang_dict["tok"] = GameLang("tok", _("Toki Pona"), False, ("Sajoli", "Sajowi"), "tok", True)
    lang_dict["zho"] = GameLang("zho", _("Chinese"), True, ("纱世里", ), "zh")
    
    def cur_lang():
        lang = lang_dict.get(_preferences.language) or lang_dict["eng"]
        if type(lang) == tuple:
            lang = lang[0]
        return lang
    
    def get_s_names(lang = None):
        if not lang:
            lang = _preferences.language
        lang = lang_dict.get(lang)
        if type(lang) == tuple:
            lang = lang[0]
        return lang and lang.s_names or get_s_names("eng")
    
    s_name_list = ["sayori", "sajori", "сайори", "саёри", "саери", "纱世里", "sajoli", "sajowi"] #All known by the mod auther(s) lowercased variants of Sayori's name
    
    def s_text_style(lang = None):
        if not lang:
            lang = cur_lang()
        
        if lang.code == "zho":
            return "sayori_text_zho"
        elif lang.unicode:
            return "sayori_text_unicode"
        else:
            return "sayori_text"
    
    try:
        lang = None
        
        if renpy.windows:
            import locale, subprocess
            
            lang = subprocess.check_output("wmic os get Locale", shell=True)
            lang = int(lang.split('\n')[1], 16)
            lang = locale.windows_locale.get(lang) or "en"
            lang = lang[:2]
            
        else:
            import os
            
            lang = os.environ.get("LANG") or 'en'
            lang = lang[:2]
            
        for l in lang_dict.values():
            if type(l) == tuple:
                l = l[0]
            if l.unix_code == lang:
                config.default_language = l.code
                break
    except:
        pass
