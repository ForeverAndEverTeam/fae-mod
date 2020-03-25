#Date and time functions

init -10 python:
    import datetime, calendar
    
    weekday_list = (
    "{#weekday}Monday",
    "{#weekday}Tuesday",
    "{#weekday}Wednesday",
    "{#weekday}Thursday",
    "{#weekday}Friday",
    "{#weekday}Saturday",
    "{#weekday}Sunday"
    )
    
    month_list = (
    "{#month}January",
    "{#month}February",
    "{#month}March",
    "{#month}April",
    "{#month}May",
    "{#month}June",
    "{#month}July",
    "{#month}August",
    "{#month}September",
    "{#month}October",
    "{#month}November",
    "{#month}December",
    )
    
    def get_now(): # Short alias to datetime.datetime.now()
        return datetime.datetime.now()
    
    ## Time of day begining hour constants
    ## May become usual variables having `time` objects in the future, as the times of day will depend of the certian date
    TIME_MORNING = 6
    TIME_DAY = 11
    TIME_EVENING = 18
    TIME_NIGHT = 22
    def get_time_of_day(h = None, for_bg = True):
        h = get_now().hour if h is None else h
        if for_bg and persistent.day_night_cycle == 0:
            return 2 #Day
        elif h < TIME_MORNING:
            return 0 # Night
        elif h < TIME_DAY:
            return 1 # Morning
        elif h < TIME_EVENING:
            return 2 # Day
        elif h < TIME_NIGHT:
            return 3 # Evening
        return 0 # Night
    def get_time_transition_factor():
        """Return the number 0 to 1 that represent have much of the current time of day's last hour has already past"""
        if persistent.day_night_cycle < 2:
            return 0.0
        ct = get_now()
        h = ct.hour
        next_h = (h + 1) % 24
        if get_time_of_day(next_h) != get_time_of_day(h):
            return float(ct.minute) / 60 + float(ct.second) / 3600
        return 0.0
    
    def is_leap_year(y):
        return calendar.isleap(y)
    
    def get_max_day(m, y):
        r = calendar.monthrange(y, m)[1]
        return r
