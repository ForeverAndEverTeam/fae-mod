init -990 python:
    import datetime
    import easter

    _easter = easter.easter(datetime.datetime.today().year)


init -100 python in fae_utilities:
    
    import store


    def get_total_gameplay_length():

        if store.persistent.fae_first_visit_date is not None:
            return datetime.datetime.now() - store.persistent.fae_first_visit_date

        else:
            return datetime.datetime.now() - datetime.datetime.today()

define FAE_NEW_YEARS_DAY = datetime.date(datetime.date.today().year, 1, 1)
define FAE_VALENTINES_DAY = datetime.date(datetime.date.today().year, 2, 14)
define FAE_EASTER = datetime.date(_easter.year, _easter.month, _easter.day)
define FAE_SAYORI_BIRTHDAY = datetime.date(datetime.date.today().year, 5, 1)
define FAE_HALLOWEEN = datetime.date(datetime.date.today().year, 10, 31)
define FAE_CHRISTMAS_EVE = datetime.date(datetime.date.today().year, 12, 24)
define FAE_CHRISTMAS_DAY = datetime.date(datetime.date.today().year, 12, 25)
define FAE_NEW_YEARS_EVE = datetime.date(datetime.date.today().year, 12, 31)

init -3 python:

    from collections import OrderedDict
    import datetime
    import re
    import store.fae_utilities as fae_utilities
    import store.fae_affection as fae_affection
    from Enum import Enum


    def fae_is_weekday():

        return datetime.datetime.now().weekday() < 5
    
    def fae_find_hour():

        return datetime.datetime.now().hour

    def fae_get_time_block():

        current_hour = fae_find_hour()
        if current_hour in range(3, 5):
            return FAETimeBlocks.early_morning
        elif current_hour in range(5, 9):
            return FAETimeBlocks.mid_morning
        elif current_hour in range(9, 12):
            return FAETimeBlocks.late_morning
        elif current_hour in range(12, 18):
            return FAETimeBlocks.afternoon
        elif current_hour in range(18, 22):
            return FAETimeBlocks.evening
        else:
            return FAETimeBlocks.night

    def fae_is_day():

        return datetime.time(persistent.fae_sunup) <= datetime.datetime.now().time() < datetime.time(persistent.fae_sundown)
    
    def fae_is_evening():
        if datetime.time(persistent.fae_sundown) <= datetime.datetime.now().time() < datetime.time(persistent.fae_moonup):
            return True
        else:
            return False
    
    def fae_is_night():
        if datetime.time(persistent.fae_moonup) >= datetime.datetime.now().time() > datetime.time(persistent.fae_sunup):
            return True


    
    class FAETimeBlocks(Enum):

        early_morning = 1

        mid_morning = 2

        late_morning = 3

        afternoon = 4

        evening = 5

        night = 6

        def __str__(self):
            return self.name

init -10 python:

    def fae_isO31(_date=None):
        if _date is None:
            _date = datetime.date.today()
        
        return _date == FAE_HALLOWEEN.replace(year=_date.year)
    
    def fae_isD25(_date=None):

        if _date is None:
            _date = datetime.date.today()
        
        return _date == FAE_CHRISTMAS_DAY.replace(year=_date.year)
    
    def fae_isNYE(_date=None):
       
        if _date is None:
            _date = datetime.date.today()

        return _date == FAE_NEW_YEARS_EVE.replace(year=_date.year)

    def fae_isNYD(_date=None):

        if _date is None:
            _date = datetime.date.today()
        
        return _date == FAE_NEW_YEARS_DAY.replace(year=_date.year)

    def fae_isF14(_date=None):

        if _date is None:
            _date = datetime.date.today()
        
        return _date == FAE_VALENTINES_DAY.replace(year=_date.year)

    def fae_isPlayerBday(_date=None, use_date_year=False):

        if _date is None:
            _date = datetime.date.today()
        
        if persistent._fae_player_bday is None:
            return False

        elif use_date_year:
            return _date == fae_player_bday_curr(_date)
        return _date == fae_player_bday_curr()

init -10 python:

    def fae_isplayer_bday(_date=None, use_date_year=False):

        if _date is None:
            _date = datetime.date.today()
        
        if persistent._fae_player_bday is None:
            return False

        elif use_date_year:
            return _date == fae_player_bday_curr(_date)
        
        return _date == fae_player_bday_curr()

init -11 python:
    
    def fae_player_bday_curr(_date=None):

        if _date is None:
            _date = datetime.date.today()
        if persistent._fae_player_bday is None:
            return None

        else:
            return store.fae_utilities.add_years(persistent._fae_player_bday, _date.year-persistent._fae_player_bday.year)


init python in fae_utilities:

    import store
    import re
    import store.fae_globals as fae_globals

    def get_sesh_time():

        return datetime.datetime.now() - store.fae_globals.present_sesh_start
    
    def get_all_playtime():

        if store.persistent.fae_first_visit_date is not None:
            return datetime.datetime.now() - store.persistent.fae_first_visit_date
        
        else:
            return datetime.datetime.now() - datetime.datetime.today()
        
        
    
    def get_total_gameplay_seconds():

        return get_total_gameplay_length().total_seconds()

    def get_total_gameplay_minutes():

        return get_total_gameplay_length().total_seconds() / 60

    def get_total_gameplay_hours():
        
        return get_total_gameplay_length().total_seconds() / 3600

    def get_total_gameplay_days():
        
        return get_total_gameplay_length().total_seconds() / 86400

    def get_total_gameplay_months():
    
        return get_total_gameplay_length().total_seconds() / 2628000

    def get_time_in_session_descriptor():

        minutes_in_session = get_current_session_length().total_seconds() / 60

        if minutes_in_session <= 1:
            return "like a minute"

        elif minutes_in_session <= 3:
            return "a couple of minutes"

        elif minutes_in_session > 3 and minutes_in_session <= 5:
            return "like five minutes"

        elif minutes_in_session > 5 and minutes_in_session <= 10:
            return "around ten minutes"

        elif minutes_in_session > 10 and minutes_in_session <= 15:
            return "around fifteen minutes"

        elif minutes_in_session > 15 and minutes_in_session <= 20:
            return "around twenty minutes"

        elif minutes_in_session <= 30:
            return "about half an hour"

        else:
            return "a while"

    def get_player_initial():

        return list(store.player)[0]

define fae_spring_equinox = datetime.date(datetime.date.today().year,3,21)
define fae_summer_solstice = datetime.date(datetime.date.today().year,6,21)
define fae_fall_equinox = datetime.date(datetime.date.today().year,9,23)
define fae_winter_solstice = datetime.date(datetime.date.today().year,12,21)


init -1 python:

    def fae_isSpring(_date=None):

        if _date is None:
            _date = datetime.date.today()

        _date = _date.replace(datetime.date.today().year)

        if persistent._fae_south_hemisphere:
            return fae_fall_equinox <= _date < fae_winter_solstice
        else:
            return fae_spring_equinox <= _date < fae_summer_solstice
    
    def fae_isSummer(_date=None):


        if _date is None:
            _date = datetime.date.today()

        _date = _date.replace(datetime.date.today().year)

        if persistent._fae_south_hemisphere:
            return fae_winter_solstice <= _date or _date < fae_spring_equinox
        else:
            return fae_summer_solstice <= _date < fae_fall_equinox

    def fae_isFall(_date=None):
        """
        Checks if given date is during fall
        iff none passed in, then we assume today

        Note: If persistent._fae_north_hemisphere is none, we assume northern hemi

        RETURNS:
            boolean showing whether or not it's fall right now
        """
        if _date is None:
            _date = datetime.date.today()

        _date = _date.replace(datetime.date.today().year)

        if persistent._fae_south_hemisphere:
            return fae_spring_equinox <= _date < fae_summer_solstice
        else:
            return fae_fall_equinox <= _date < fae_winter_solstice

    def fae_isWinter(_date=None):
        """
        Checks if given date is during winter
        iff none passed in, then we assume today

        Note: If persistent._fae_north_hemisphere is none, we assume northern hemi

        RETURNS:
            boolean showing whether or not it's winter right now
        """
        if _date is None:
            _date = datetime.date.today()

        _date = _date.replace(datetime.date.today().year)

        if persistent._fae_south_hemisphere:
            return fae_summer_solstice <= _date < fae_fall_equinox
        else:
            return fae_winter_solstice <= _date or _date < fae_spring_equinox


init 10 python in fae_time:

    import store

    PLUGIN_PP_SPRING = "pp_spring"
    PLUGIN_PP_SUMMER = "pp_summer"
    PLUGIN_PP_FALL = "pp_fall"
    PLUGIN_PP_WINTER = "pp_winter"

    def _pp_spring():

        store.fae_submod_utilities.getAndRunFunctions(key=PLUGIN_PP_SPRING)

    
    def _pp_summer():


        store.fae_submod_utilities.getAndRunFunctions(key=PLUGIN_PP_SUMMER)

    
    def _pp_fall():

        store.fae_submod_utilities.getAndRunFunctions(key=PLUGIN_PP_FALL)

    
    def _pp_winter():

        store.fae_submod_utilities.getAndRunFunctions(key=PLUGIN_PP_WINTER)

    
    _season_pp_defs = {
        1: _pp_spring,
        2: _pp_summer,
        3: _pp_fall,
        4: _pp_winter
    }


    _prog_defs = {
        1: 2,
        2: 3,
        3: 4,
        4: 1
    }


    _season_defs = {
        1: store.fae_isSpring,
        2: store.fae_isSummer,
        3: store.fae_isFall,
        4: store.fae_isWinter
    }

    def _seasonNow():

        for _id, logic in _season_defs.items():
            if logic():
                return _id
        
        return 3
    
    def _seasonalReset(prev_season):

        curr_season = _seasonNow()

        if prev_season == curr_season:

            _season_pp_defs[curr_season]()
            return curr_season
        
        while prev_season != curr_season:
            prev_season = _prog_defs.get(prev_season, curr_season)

            if prev_season in _season_pp_defs:
                _season_pp_defs[prev_season]()
        
        return curr_season

init 900 python:

    persistent._fae_current_season = store.fae_time._seasonalReset(
        persistent._fae_current_season
    )

init -999 python in fae_ev_data_ver:
    import builtins
    import renpy
    import datetime

    def _verify_int(val, allow_none=True):
        return _verify_item(val, int, allow_none)


    def _verify_int_nn(val):
        return _verify_int(val, False)
    

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

    def _verify_str(val, allow_none=True):
        if val is None:
            return allow_none

        return isinstance(val, str) or isinstance(val, unicode)

    def _verify_dt(val, allow_none=True):
        if (
                isinstance(val, datetime.datetime)
                and val.year < 1900
            ):
            return False
        return _verify_item(val, datetime.datetime, allow_none)


    def _verify_dt_nn(val):
        return _verify_dt(val, False)

    def _verify_td(val, allow_none=True):
        if val is None:
            return allow_none
        return _verify_item(val, datetime.timedelta, allow_none)


    def _verify_td_nn(val):
        return _verify_td(val, False)


init -995 python in fae_utilities:

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

init -985 python:
    import datetime
    # global stuff that should be defined somewhat early

    def fae_getSessionLength():
        """
        Gets length of current session, IF this cannot be determined, a
        time delta of 0 is returned
        """
        _now = datetime.datetime.now()
        return _now - store.fae_utilities.pdget(
            "current_session_start",
            persistent.sessions,
            validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=_now
        )


    def fae_getAbsenceLength():
        """
        Gets time diff between current session start and last session end
        aka the diff between last session and this
        if not found, time delta of 0 is returned
        """
        return fae_getCurrSeshStart() - fae_getLastSeshEnd()


    def fae_getCurrSeshStart():
        """
        Returns the current session start datetime
        If there is None, we use first session
        """
        return store.fae_utilities.pdget(
            "current_session_start",
            persistent.sessions,
            validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=fae_getFirstSesh()
        )


    def fae_getFirstSesh():
        """
        Returns the first session datetime.

        If we could not get it, datetime.datetime.now() is returnd
        """
        return store.fae_utilities.pdget(
            "first_session",
            persistent.sessions,
            validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=datetime.datetime.now()
        )

    def fae_isFirstSeshPast(_date):
        """
        Checks if the first session is past the given date

        IN:
            _date - datetime.date to check against

        OUT:
            boolean:
                - True if first sesh is past given date
                - False otherwise
        """
        return fae_getFirstSesh().date() > _date

    def fae_getLastSeshEnd():
        """
        Returns datetime of the last session
        NOTE: if there was no last session, we use first session instead
        """
        return store.fae_utilities.pdget(
            "last_session_end",
            persistent.sessions,
            validator=store.fae_ev_data_ver._verify_dt_nn,
            defval=fae_getFirstSesh()
        )


    def fae_getTotalPlaytime():
        """
        Gets total playtime.

        RETURNS: total playtime as a timedelta. If not found, we return a
            time delta of 0
        """
        return store.fae_utilities.pdget(
            "total_playtime",
            persistent.sessions,
            validator=store.fae_ev_data_ver._verify_td_nn,
            defval=datetime.timedelta(0)
        )


    def fae_getTotalSessions():
        """
        Gets total sessions

        REUTRNS: total number of sessions. If not found, we return 1
        """
        return store.fae_utilities.pdget(
            "total_sessions",
            persistent.sessions,
            validator=store.fae_ev_data_ver._verify_int_nn,
            defval=1
        )


    def fae_TTDetected():
        """
        Checks if time travel was detected
        NOTE: TT detection occurs at init -890
        """
        return store.fae_globals.tt_detected