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
