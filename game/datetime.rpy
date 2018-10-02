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
    
    def get_time_of_day(h = None):
        h = get_now().hour if h is None else h
        if h < 6:
            return 0 # Night
        elif h < 11:
            return 1 # Morning
        elif h < 18:
            return 2 # Day
        elif h < 22:
            return 3 # Evening
        return 0 # Night
    
    def is_leap_year(y):
        return calendar.isleap(y)
    
    def get_max_day(m, y):
        r = calendar.monthrange(y, m)[1]
        return r
