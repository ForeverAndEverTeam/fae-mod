#Date and time functions

init -10 python:
    import datetime, calendar
    
    def get_now(): # Short alias to datetime.datetime.now()
        return datetime.datetime.now()
    
    def get_day_num(d = get_now().day, m = get_now().month, y = get_now().year):
        r = datetime.date(y, m, d).isocalendar()
        return 7 * (r - 1) + r[2]
    
    def get_time_of_day(h = get_now().hour):
        if h < 6:
            return 0 # Night
        elif h < 11:
            return 1 # Morning
        elif h < 18:
            return 2 # Day
        elif h < 22:
            return 3 # Evening
        return 0 # Night
    
    def is_leap_year(y = get_now().year):
        return calendar.isleap(y)
    
    def get_max_day(m = get_now().month, y = get_now().year):
        r = calendar.monthrange(y, m)[1]
        return r
    
    