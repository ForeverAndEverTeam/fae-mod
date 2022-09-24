init -1 python:
    
    import json
    import copy
    from renpy.display.layout import Container
    from store.fae_calendar import CAL_TYPE_EV,CAL_TYPE_REP
    

    class CalendarEncoder(json.JSONEncoder):

        def default(self, item):
            if isinstance(item, set):
                return list(item)
            
            return json.JSONEncoder.default(self, item)

    class FAECALENDAR(renpy.Displayable):
    

        import pygame
        import datetime
        import store.chat_handler as chat_handler


        #CONSTANT STUFF
        VIEW_WIDTH = 1280
        VIEW_HEIGHT = 720

        #EXIT BUTTON POS  & SIZE

        EXIT_BUTTON_WIDTH = 74
        EXIT_BUTTON_HEIGHT = 74
        EXIT_BUTTON_X = 1041
        EXIT_BUTTON_Y = 60


        #DAY BUTTON STUFF
        DAY_BUTTON_WIDTH = 128
        DAY_BUTTON_HEIGHT = 65
        DAY_NAME_BUTTON_HEIGHT = 35


        #INIT POSITION FOR SHOWING STUFF IN CALENDAR

        INITIAL_POSITION_X = 192
        INITIAL_POSITION_Y = 155

        #TITLE POS
        TITLE_POS_Y = 115

        #INTERNAL AREA
        INTERNAL_WIDTH = DAY_BUTTON_WIDTH * 7

        #AWRROW BUTTON SIZE
        ARROW_BUTTON_SIZE = 20

        #SIZE OF THE DAY NUMBER INSIDE DAY BLOCK
        DAY_NUMBER_TEXT_SIZE = 13

        #NOTE INSIDE DAY
        NOTE_TEXT_SIZE = 19

        #X INSIDE CLOSE BUTTON

        CALENDAR_CLOSE_X_SIZE = 45


        #RETURN VALUES

        CALENDAR_CLOSE = "CLOSE"
        CALENDAR_MONTH_INCREASE = "MONTH_INCR"
        CALENDAR_MONTH_DECREASE = "MONTH_DECR"
        CALENDAR_YEAR_INCREASE = "YEAR_INCR"
        CALENDAR_YEAR_DECRESE = "YEAR_DECR"


        #COLOUR OF DAY NO.
        DAY_NUMBER_COLOR = "#000000"

        #NOTE COLOUR
        NOTE_COLOR = "#181818"

        #FONT CALENDAR
        NOTE_FONT = "gui/font/s1.ttf"

        #MONTH NAMES ARRAY
        MONTH_NAMES = ["Unknown", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        #DAY NAMES ARRAY
        DAY_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        #MOUSE EVENTS
        MOUSE_EVENTS = (
            pygame.MOUSEMOTION,
            pygame.MOUSEBUTTONUP,
            pygame.MOUSEBUTTONDOWN
        )


        #YEAR LIMITS
        MIN_VIEWABLE_YEAR = 200
        MIN_SELECTABE_YEAR = 1900
        MAX_VIEWABLE_YEAR = 7000
        MID_POINT_YEAR = 2000


        #PANE CONSTANTS

        EVENT_X = 800
        EVENT_Y = 40
        EVENT_W = 450
        EVENT_H = 640
        EVENT_XALIGN = 0.96
        EVENT_AREA = (EVENT_X, EVENT_Y, EVENT_W, EVENT_H)
        EVENT_RETURN = "< GO BACK"


        def __init__(self, select_date=False):

            super(renpy.Displayable, self).__init__()

            self.calendar_background = renpy.displayable("mod_assets/calendar/calendar_bg.png")

            self.can_select_date = select_date


            self.database = store.fae_calendar.calendar_database

            self.background = Solid(
                "#000000B2",
                xsize=self.VIEW_WIDTH,
                ysize=self.VIEW_HEIGHT
            )


            #Default view to correct month
            self.today = datetime.date.today()

            self.selected_month = self.today.month
            self.selected_year = self.today.year

            self.const_buttons = []
            self.day_buttons = []
            self.day_button_texts = []

            button_close = Image("mod_assets/calendar/calendar_close.png")

            button_close_hover = Image("mod_assets/calendar/calendar_close_hover.png")

            button_day_name = Image("mod_assets/calendar/calendar_day_name_bg.png")

            button_left_arrow = Image("mod_assets/calendar/calendar_left_arrow.png")

            button_right_arrow = Image("mod_assets/calendar/calendar_right_arrow.png")

            button_left_arrow_hover = Image("mod_assets/calendar/calendar_left_arrow_hover.png")

            button_right_arrow_hover = Image("mod_assets/calendar/calendar_right_arrow_hover.png")


            if select_date:
                self.text_title = Text(
                    "Select a date",
                    font=gui.default_font,
                    size=33,
                    color="#ffffff",
                    outlines=[]
                )
            
            else:
                self.text_title = Text(
                    "Calendar",
                    font=gui.default_font,
                    size=33,
                    color="#ffffff",
                    outlines=[]
                )
            
            i = 0
            for day in self.DAY_NAMES:


                button_day_text = Text(
                    "{#weekday}" + day,
                    font=gui.default_font,
                    size=17,
                    color=self.DAY_NUMBER_COLOR,
                    outlines=[]
                )
            
                button_day_button = CustomButton(
                    button_day_text,
                    button_day_text,
                    button_day_text,
                    button_day_name,
                    button_day_name,
                    button_day_name,
                    self.INITIAL_POSITION_X + (i * self.DAY_BUTTON_WIDTH),
                    self.INITIAL_POSITION_Y + self.DAY_NAME_BUTTON_HEIGHT,
                    self.DAY_BUTTON_WIDTH,
                    self.DAY_NAME_BUTTON_HEIGHT,
                    hover_sound=None,
                    activate_sound=None,
                    return_value=None
                )

                self.const_buttons.append(button_day_button)

                i = i + 1

            button_text_close = Text(
                "X",
                font=gui.default_font,
                size=self.CALENDAR_CLOSE_X_SIZE,
                color="#ffb0ed",
                outlines=[]
            )

            button_text_close_hover = Text(
                "X",
                gui.default_font,
                size=self.CALENDAR_CLOSE_X_SIZE,
                color="#ffd3f4",
                outlines=[]
            )


            self.button_exit = CustomButton(
                button_text_close,
                button_text_close_hover,
                button_text_close,
                button_close,
                button_close_hover,
                button_close,
                self.EXIT_BUTTON_X,
                self.EXIT_BUTTON_Y,
                self.EXIT_BUTTON_WIDTH,
                self.EXIT_BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound,
                return_value=self.CALENDAR_CLOSE
            )


            button_empty_text = Text(
                "",
                font=gui.default_font,
                size=12,
                color="#ffb0ed",
                outlines=[]
            )


            self.button_month_decrease = CustomButton(
                button_empty_text,
                button_empty_text,
                button_empty_text,
                button_left_arrow,
                button_left_arrow_hover,
                button_left_arrow,
                self.INITIAL_POSITION_X + 100,
                self.INITIAL_POSITION_Y + 10,
                self.ARROW_BUTTON_SIZE,
                self.ARROW_BUTTON_SIZE,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound,
                return_value=self.CALENDAR_MONTH_DECREASE
            )

            self.button_month_increase = CustomButton(
                button_empty_text,
                button_empty_text,
                button_empty_text,
                button_right_arrow,
                button_right_arrow_hover,
                button_right_arrow,
                self.INITIAL_POSITION_X + 330,
                self.INITIAL_POSITION_Y + 10,
                self.ARROW_BUTTON_SIZE,
                self.ARROW_BUTTON_SIZE,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound,
                return_value=self.CALENDAR_MONTH_INCREASE
            )


            self.button_year_decrease = CustomButton(
                button_empty_text,
                button_empty_text,
                button_empty_text,
                button_left_arrow,
                button_left_arrow_hover,
                button_left_arrow,
                self.INITIAL_POSITION_X + self.INTERNAL_WIDTH - self.ARROW_BUTTON_SIZE - 330,
                self.INITIAL_POSITION_Y + 10,
                self.ARROW_BUTTON_SIZE,
                self.ARROW_BUTTON_SIZE,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound,
                return_value=self.CALENDAR_YEAR_DECRESE
            )

            self.button_year_increase = CustomButton(
                button_empty_text,
                button_empty_text,
                button_empty_text,
                button_right_arrow,
                button_right_arrow_hover,
                button_right_arrow,
                self.INITIAL_POSITION_X + self.INTERNAL_WIDTH - self.ARROW_BUTTON_SIZE - 100,
                self.INITIAL_POSITION_Y + 10,
                self.ARROW_BUTTON_SIZE,
                self.ARROW_BUTTON_SIZE,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound,
                return_value=self.CALENDAR_YEAR_INCREASE
            )


            self.const_buttons.append(self.button_exit)
            self.const_buttons.append(self.button_month_decrease)
            self.const_buttons.append(self.button_month_increase)
            self.const_buttons.append(self.button_year_decrease)
            self.const_buttons.append(self.button_year_increase)

            self._setupDayButtons()
        
        def _setupDayButtons(self):

            button_day_bg = Image("mod_assets/calendar/calendar_day_bg.png")
        
            button_day_bg_disabled = Image("mod_assets/calendar/calendar_day_disabled_bg.png")

            button_day_bg_hover = Image("mod_assets/calendar/calendar_day_hover_bg.png")

            button_today_bg = Image("mod_assets/calendar/calendar_today_bg.png")

            button_today_bg_disabled = Image("mod_assets/calendar/calendar_today_disabled_bg.png")

            button_today_bg_hover = Image("mod_assets/calendar/calendar_today_hover_bg.png")

            self.text_current_month = Text(
                "{#month}" + self.MONTH_NAMES[self.selected_month],
                font=gui.default_font,
                size=21,
                color=self.DAY_NUMBER_COLOR,
                outlines=[]
            )

            self.text_current_year = Text(
                str(self.selected_year),
                font=gui.default_font,
                size=21,
                color=self.DAY_NUMBER_COLOR,
                outlines=[]
            )

            # init day buttons array
            self.day_buttons = []
            self.day_button_texts = []

            # set the note style attributes
            note_font = self.NOTE_FONT
            note_text_size = self.NOTE_TEXT_SIZE
            note_color = self.NOTE_COLOR
            note_ystart = 1

            # get relevant date info
            day = datetime.timedelta(days=1)
            first_day = datetime.datetime(self.selected_year, self.selected_month, 1)

            # get the first_day of the week that has the first day of current month
            while first_day.weekday() != 6:
                first_day = first_day - day

            # init the array that will hold the dates we're displaying
            self.dates = []

            # get all the dates we'll be displaying  and store them on the array
            for i in range(42):
                self.dates.append(first_day + datetime.timedelta(days=i))
            
            
            events = self.database[self.selected_month]

            #if self.selected_month == 3 and not fae_isLeapYear(self.selected_year):

            #    events = copy.deepcopy(events)
            #    events[1].update(self.database[2][29])
            
            #else:
            #pass
            
            initial_y = self.INITIAL_POSITION_Y + (self.DAY_NAME_BUTTON_HEIGHT * 2)

            for i in range(6):

                for j in range(7):

                    current_date = self.dates[j + (i * 7)]
                    ret_val = None
                    many_events = False
                    day_bg_disabled = button_day_bg_disabled
                    today_bg_disabled = button_today_bg_disabled

                    event_labels = list()

                    if current_date.month == self.selected_month:
                        _todays_events = events[current_date.day]

                        for k in _todays_events:
                            e = _todays_events[k]

                            if e[0] == CAL_TYPE_EV:

                                #ev = get_chat(k)
                                ev = get_chat(k)

                                if self._isEvInYear(ev, self.selected_year):
                                    event_labels.append(fae_getChatCL(k))
                            
                            if e[0] == CAL_TYPE_REP:

                                if e[2] is not None and ( not e[2] or self.selected_year in e[2]):

                                    event_labels.append(e[1])
                        
                        if len(event_labels) > 3:
                            many_events = True
                            if not self.can_select_date:
                                ret_val = event_labels
                    
                    if not event_labels or len(event_labels) < 3:

                        event_labels.extend([""] * 3)
                    
                    if current_date.month == self.selected_month:
                        day_bg_disabled = button_day_bg
                        today_bg_disabled = button_today_bg

                        if self.can_select_date:
                            ret_val = current_date
                    
                    final_bg_idle = button_day_bg
                    final_bg_hover = button_day_bg_hover
                    final_bg_disabled = day_bg_disabled


                    if (current_date.day == self.today.day) and (current_date.month == self.today.month) and (current_date.year == self.today.year):

                        final_bg_idle = button_today_bg
                        final_bg_hover = button_today_bg_hover
                        final_bg_disabled = today_bg_disabled
                    

                    button_pos = (self.INITIAL_POSITION_X + (j * self.DAY_BUTTON_WIDTH),
                        initial_y + (i * self.DAY_BUTTON_HEIGHT))
                    
                    day_button = CustomButton(
                        Null(),
                        Null(),
                        Null(),
                        final_bg_idle,
                        final_bg_hover,
                        final_bg_disabled,
                        button_pos[0],
                        button_pos[1],
                        self.DAY_BUTTON_WIDTH,
                        self.DAY_BUTTON_HEIGHT,
                        hover_sound=gui.hover_sound,
                        activate_sound=gui.activate_sound,
                        return_value=ret_val
                    )

                    if current_date.month != self.selected_month or (not self.can_select_date and not many_events):

                        day_button.disable()
                    
                    self.day_buttons.append(day_button)

                    text_container = Container(
                        pos=button_pos,
                        xsize=self.DAY_BUTTON_WIDTH,
                        ysize=self.DAY_BUTTON_HEIGHT
                    )

                    day_number_text = Text(
                        str(current_date.day),
                        font=gui.default_font,
                        size=self.DAY_NUMBER_TEXT_SIZE,
                        color=self.DAY_NUMBER_COLOR,
                        outlines=[],
                        pos=(self.DAY_BUTTON_WIDTH - 7, 5),
                        xanchor=1.0
                    )
                    text_container.add(day_number_text)

                    for k in range(3):

                        if len(event_labels[k]) != 0:
                            note_text = Text(
                                __(event_labels[k]),
                                font=note_font,
                                size=note_text_size,
                                color=note_color,
                                outlines=[],
                                pos=(8, note_ystart + k * 17)
                            )
                            text_container.add(note_text)

                    if many_events:

                        ellipsis_text = Text(
                            "...",
                            font=gui.default_font,
                            size=16,
                            color=self.DAY_NUMBER_COLOR,
                            outlines=[],
                            pos=(self.DAY_BUTTON_WIDTH - 7, 43),
                            xanchor=1.0
                        )
                        text_container.add(ellipsis_text)

                    self.day_button_texts.append((text_container, button_pos))
        
        def _showScrollableEventList(self,events):

            event_list_title = ("Events for the day:", False, True)

            event_list_items = [(e, False, False) for e in events]

            final_item = (self.EVENT_RETURN, False, False, False, 20)

            renpy.call_in_new_context("fae_show_calendar_detail", event_list_items, self.EVENT_AREA, self.EVENT_XALIGN, first_item=event_list_title, final_item=final_item)


        def _xcenter(self, v_width, width):

            return int((v_width - width) / 2)
        

        def _buttonSelect(self, ev, x, y, st):

            for button in self.const_buttons:
                ret_val = button.event(ev, x, y, st)
                if ret_val:
                    return ret_val
            
            for button in self.day_buttons:
                ret_val = button.event(ev, x, y, st)
                if ret_val:
                    return ret_val
            
            return None
        
        def _yearSanityChecks(self):

            if self.selected_year < self.MIN_VIEWABLE_YEAR:
                self.selected_year = self.MIN_VIEWABLE_YEAR + 5
            
            if self.selected_year > self.MAX_VIEWABLE_YEAR:
                self.selected_year = self.MAX_VIEWABLE_YEAR - 5
        

        def _changeYear(self, ascend=True, set_to=None):

            if set_to is not None:
                self.selected_year = set_to
            elif ascend:
                self.selected_year = self.selected_year + 1
            else:
                self.selected_year = self.selected_year - 1

            self._yearSanityChecks()

            self._setupDayButtons()
        

        def _changeMonth(self, ascend=True):

            if ascend:

                self.selected_month = self.selected_month + 1

                # check if we need to increment the year
                if self.selected_month >=13:
                    self.selected_month = 1
                    self.selected_year = self.selected_year + 1
            else:

                self.selected_month = self.selected_month - 1

                # check if  we need to decrement the year
                if self.selected_month <=0:
                    self.selected_month = 12
                    self.selected_year = self.selected_year - 1

            self._yearSanityChecks()

            self._setupDayButtons()
        

        def _isEvInYear(self, ev, year):

            if ev.years is not None:

                return len(ev.years) == 0 or year in ev.years
            
            return ev.start_date is not None and ev.start_date.year == year
        
        def render(self, width, height, st, at):

            back = renpy.render(self.background, width, height, st, at)

            calendar_bg = renpy.render(self.calendar_background, width, height, st, at)

            calendar_title = renpy.render(self.text_title, width, height, st, at)

            month_label = renpy.render(self.text_current_month, width, height, st, at)

            year_label = renpy.render(self.text_current_year, width, height, st, at)

            titlew, titleh = calendar_title.get_size()
            monw, monh = month_label.get_size()
            yearw, yearh = year_label.get_size()


            titlex = self._xcenter(self.INTERNAL_WIDTH, titlew)
            monthx = self._xcenter(250, monw) + 100
            yearx = self.INTERNAL_WIDTH - yearw - self._xcenter(250, yearw) - 100

            self.width, self.height = calendar_bg.get_size()

            r = renpy.Render(width, height)

            r.blit(back,(0,0))

            r.blit(calendar_bg, (190, 103))

            r.blit(month_label, (self.INITIAL_POSITION_X + monthx, self.INITIAL_POSITION_Y + 8))

            r.blit(year_label, (self.INITIAL_POSITION_X + yearx, self.INITIAL_POSITION_Y + 8))

            r.blit(calendar_title, (self.INITIAL_POSITION_X + titlex, self.TITLE_POS_Y))

            c_r_buttons = [
                (
                    x.render(width, height, st, at),
                    (x.xpos, x.ypos)
                )
                for x in self.const_buttons
            ]

            for vis_b, xy in c_r_buttons:
                r.blit(vis_b, xy)
            
            cal_r_displayables = [
                (
                    x.render(width, height, st, at),
                    (x.xpos, x.ypos)
                )
                for x in self.day_buttons
            ]

            for button_text, button_pos in self.day_button_texts:
                text_r = button_text.render(width, height, st, at)
                cal_r_displayables.append((text_r, button_pos))
            
            for vis_d, xy in cal_r_displayables:
                r.blit(vis_d, xy)
            
            return r
        

        def event(self, ev, x, y, st):

            if ev.type in self.MOUSE_EVENTS:

                sel_action = self._buttonSelect(ev, x, y, st)

                if sel_action:

                    if sel_action == self.CALENDAR_CLOSE:

                        return ""
                    
                    if (
                            isinstance(sel_action, datetime.datetime)
                            and sel_action.year >= self.MIN_SELECTABE_YEAR
                        ):
                        
                        return sel_action
                    
                    if isinstance(sel_action, type(list())):
                        self._showScrollableEventList(sel_action)
                    
                    if sel_action == self.CALENDAR_YEAR_INCREASE:
                        self._changeYear()
                    
                    if sel_action == self.CALENDAR_YEAR_DECRESE:
                        self._changeYear(False)
                    
                    if sel_action == self.CALENDAR_MONTH_INCREASE:
                        self._changeMonth()
                    
                    if sel_action == self.CALENDAR_MONTH_DECREASE:
                        self._changeMonth(False)
                
                renpy.redraw(self, 0)
            
            elif ev.type == pygame.KEYDOWN and config.developer:

                curr_year = self.selected_year

                if ev.key == pygame.K_m:

                    self._changeYear(set_to=self.selected_year+1000)
                
                elif ev.key == pygame.K_n:
                    self._changeYear(set_to=self.selected_year+100)
                
                elif ev.key == pygame.K_b:
                    # incrementyera by 10
                    self._changeYear(set_to=self.selected_year+10)
                elif ev.key == pygame.K_v:
                    # decrement yera by 10
                    self._changeYear(set_to=self.selected_year-10)
                elif ev.key == pygame.K_c:
                    # decrement yera by 100
                    self._changeYear(set_to=self.selected_year-100)
                elif ev.key == pygame.K_x:
                    # decrement year by 1000
                    self._changeYear(set_to=self.selected_year-1000)
                
                if self.selected_year != curr_year:
                    renpy.redraw(self, 0)
                
            
            raise renpy.IgnoreEvent()

init -10 python in fae_calendar:

    CAL_TYPE_EV = 1
    CAL_TYPE_REP = 2

    enabled = True

init -1 python in fae_calendar:


    import datetime
    import json
    import bisect

    import renpy
    import store

    calendar_database = dict()

    for i in range(1,13):
        calendar_database[i] = dict()

        for j in range(1,32):
            calendar_database[i][j] = dict()
    
    NUM_DEFS = {
        1: "st",
        2: "nd",
        3: "rd",
        11: "th",
        12: "th",
        13: "th"
    }


    def getZodiacSign(date):

        zodiac_signs = [
            (1, 19, "capricorn"), (2, 18, "aquarius"), (3, 20, "pisces"), (4, 19, "aries"),
            (5, 20, "taurus"), (6 ,21, "gemini"), (7, 22, "cancer"), (8, 22, "leo"),
            (9, 22, "virgo"), (10, 22, "libra"), (11, 22, "scorpio"), (12, 21, "sagittarius"),
            (12, 31, "capricorn")
        ]
        index = bisect.bisect(zodiac_signs, (date.month, date.day))

        return zodiac_signs[index][-1]
    


    def _formatDay(day):

        if day in NUM_DEFS:
            suffix = NUM_DEFS[day]
        
        else:
            suffix = NUM_DEFS.get(day % 10, "th")
        
        return str(day) + suffix
    

    def _formatYears(years):

        if years <= 0:
            return ""
        
        if years == 1:
            return "last year"
        
        return str(years) + " years ago"

    
    def genFriendlyDispDate_d(_date):


        disp_month = _date.strftime("%B")

        disp_day = _formatDay(_date.day)

        _today = datetime.date.today()

        _day_diff = _today - _date

        _year_diff = _today.year - _date.year

        _cout = list()

        if _today.month == _date.month and _today.day == _date.day:

            if _year_diff == 0:

                _cout = [
                    "today"
                ]
            
            else:

                _cout = [
                    _formatYears(_year_diff),
                    "on this date"
                ]

        elif _day_diff.days <= 365:

            _cout = [disp_month, disp_day]
        
        elif _year_diff <= 10:

            _cout = [
                _formatYears(_year_diff),
                "on",
                disp_month,
                disp_day
            ]
        
        else:


            _cout = [
                disp_month,
                disp_day + ",",
                str(_date.year)
            ]

        return (" ".join(_cout), _day_diff)
    

    def genFormalDispDate(_date):


        return (
            " ".join([
                _date.strftime("%B"),
                _formatDay(_date.day) + ",",
                str(_date.year)
            ]),
            datetime.date.today() - _date
        )
    

    def saveCalendarDatabase(encoder):

        with open(renpy.config.savedir + '/db.mcal', 'w', encoding="utf-8") as fp:

            fp.write(unicode(json.dumps(calendar_database, cls=encoder, ensure_ascii=False)))
    

    def loadCalendarDatabase():


        try:
            with open(renpy.config.savedir + '/db.mcal', 'r') as fp:

                calendar_database = json.load(fp)
        except (IOError, ValueError):

            pass
        
    
    def __addEvent_md(chat_label, month, day):

        calendar_database[month][day][chat_label] = ((
            CAL_TYPE_EV,
        ))
    
    def _addRepeatable_md(identifier, display_label, month, day, year_param):

        calendar_database[month][day][identifier] = ((
            CAL_TYPE_REP,
            display_label,
            year_param
        ))


    def addEvent(ev):

        if ev.start_date is None:
            return
        
        if ev.end_date is None:
            addEvent_evdt(ev, ev.start_date)
        
        else:

            _delta = datetime.timedelta(days=1)
            curr_date = ev.start_date

            while curr_date < ev.end_date:
                addEvent_evdt(ev, curr_date)
                curr_date += _delta
    
    def addEvent_evd(ev, _date):

        __addEvent_md(
            ev.eventlabel,
            _date.month,
            _date.day
        )


    def addEvent_evdt(ev, _datetime):

        addEvent_evd(ev, _datetime.date())
    

    def addRepeatable(identifier, display_label, month, day, year_param):
        """
        Adds a repeatable to the calendar at a precise month / day
        Sanity checks are done for month / day

        IN:
            identifier - label of the event that it's unique
            display_label - label that will be displayed
            month - month to add to
            day - day to add to
            year_param - data to put in the year part of the tuple
        """
        if month in range(1,13) and day in range(1,32):
            _addRepeatable_md(identifier, display_label, month, day, year_param)


    def addRepeatable_d(identifier, display_label, _date, year_param):
        """
        Adds a repeatable to the calendar at precise datetime.date

        IN:
            identifier - identifier of the repeatable to add
            display_label - label that will be displayed
            _date - datetime.date to add to
            year_param - data to put in the year part of the tuple
        """
        _addRepeatable_md(
            identifier,
            display_label,
            _date.month,
            _date.day,
            year_param
        )


    def addRepeatable_dt(identifier, display_label, _datetime, year_param):
        """
        Adds a repeatable to the calendar at a precise datetime

        IN:
            identifier - identifier of the repeatable to add
            display_label - label that will be displayed
            _datetime - datetime to add to
            year_param - data to put in the year part of the tuple
        """
        addRepeatable_d(
            identifier,
            display_label,
            _datetime.date(),
            year_param
        )
    

    def _findEvent_md(chat_label, month, day):


        _events = calendar_database[month][day]

        if chat_label in _events:

            _ev = _events[chat_label]
            if _ev[0] == CAL_TYPE_EV:

                return _ev
            
        return None
    
    def _findRepeatable_md(identifier, month, day):
        """
        Finds the repeatable dtuple from the calendar at a precise month / day

        NOTE: no sanity checks are done for month / day

        IN:
            identifier - the id of the repeatable to find
            month - month we should look at for finding
            day - day we should look at for finding

        RETURNS:
            the repeatable tuple if itw as found, None otherwise
        """
        _events = calendar_database[month][day]

        if identifier in _events:
            _rp = _events[identifier]
            if _rp[0] == CAL_TYPE_REP:
                # NOTE: we still check for repetable type in the case that an
                #   event was added to the _events dict and was given a key
                #   that is also an identifier. We should avoid doing this,
                #   but it's certainly possible.
                return _rp

        return None
    

    def _removeEvent(chat_label, remove_all=False):

        for month in range(1,13):

            _removeEvent_m(chat_label, month, remove_all=remove_all)
        
    
    def _removeEvent_d(chat_label, day, remove_all=False):
        """
        Removes an event from the calendar on a particular day.

        NOTE:
            no sanity checks are done for day.

        IN:
            chat_label - eventlabel of the event to remove
            day - day we should look at for removal
            remove_all - SEE removeEvent_el
        """
        for month in range(1,13):
            if not remove_all and _removeEvent_md(chat_label, month, day):
                return


    def _removeEvent_m(chat_label, month, remove_all=False):
        """
        Removes an event from the calendar in a particular month.

        NOTE:
            no sanity checks are done for month

        IN:
            chat_label - eventlabel of the event to remove
            month - month we should look at for removal
            remove_all - SEE removeEvent_el
        """
        for day in range(1,32):
            if not remove_all and _removeEvent_md(chat_label, month, day):
                return


    def _removeEvent_md(chat_label, month, day):
        """
        Removes an event from the calendar at a precise month / day.

        NOTE: no sanity checks are done for month / day

        IN:
            chat_label - eventlabel of the event to remove
            month - month we should look at for removal
            day - day we should look at for removal

        RETURNS:
            True if we removed something, False otherwise
        """
        ev_tup = _findEvent_md(chat_label, month, day)

        if ev_tup is not None:
            calendar_database[month][day].pop(chat_label)
            return True

        return False


    def _removeRepeatable(identifier):
        """
        Removes a repeatable from teh calendar.

        NOTE: O(n^2) efficiency, please avoid using this.

        IN:
            identifier - identifier of the repeatable to remove
        """
        for month in range(1,13):
            _removeRepeatable_m(identifier, month)


    def _removeRepeatable_d(identifier, day):
        """
        Removes a repeatable from teh calendar in a particular month.

        NOTE: no sanity checks are done for day

        IN:
            identifier - identifier of the repeatable to remove
            day - day we should look at for removal
        """
        for month in range(1,13):
            if _removeRepeatable_md(identifier, month, day):
                return


    def _removeRepeatable_m(identifier, month):
        """
        Removes a repeatable from the calendar in a particular month.

        NOTE: no sanity checks are done for month

        IN:
            identifier - identifier of the repeatable to remove
            month - month we should look at for removal
        """
        for day in range(1,32):
            if _removeRepeatable_md(identifier, month, day):
                return


    def _removeRepeatable_md(identifier, month, day):
        """
        Removes a repeatable from teh calendar at a precise month / day.

        NOTE: no sanity checks are done for month / day

        IN:
            identifider - identifier of the repeatable to remove
            month - month we should look at for removal
            day - day we should look at for removal

        RETURNS:
            True if we removed somethign, False otherwise
        """
        rp_tup = _findRepeatable_md(identifier, month, day)

        if rp_tup is not None:
            calendar_database[month][day].pop(identifier)
            return True

        return False


    def removeEvent(ev):
        """
        Removes an event from the calendar using it's start_date and end_date
        properties.

        IN:
            ev - event to remove
        """
        if ev.start_date is None:
            return

        if ev.end_date is None:
            # no end date means we assume it's a single day to remove
            removeEvent_evdt(ev, ev.start_date)

        else:
            # otherwise we iterate over a range
            _delta = datetime.timedelta(days=1)
            curr_date = ev.start_date

            while curr_date < ev.end_date:
                removeEvent_evdt(ev, curr_date)
                curr_date += _delta


    def removeEvent_eld(chat_label, _date):
        """
        Removes an event from the calendar at a precise date.

        IN:
            chat_label - eventlabel of the event to remove
            _date - datetime.date we should look at for event removal
        """
        _removeEvent_md(chat_label, _date.month, _date.day)


    def removeEvent_evd(ev, _date):
        """
        Removes an event from the calendar at a precise date.

        IN:
            ev - event to remove
            _date - datetime.date we should look at for event removal
        """
        removeEvent_eld(ev.eventlabel, _date)


    def removeEvent_eldt(chat_label, _datetime):
        """
        Removes an event from the calendar at a precise datetime.

        IN:
            chat_label - eventlabel of the event to remove
            _datetime - datetime we should look at for event removal
        """
        removeEvent_eld(chat_label, _datetime.date())


    def removeEvent_evdt(ev, _datetime):
        """
        Removes and event from the calendar at a precise datetime.

        IN:
            ev - event to remove
            _datetime - datetime.date we should look at for removal
        """
        removeEvent_eldt(ev.eventlabel, _datetime)


    def removeEvent_el(chat_label, month=None, day=None, remove_all=False):
        """
        Removes an event from the calendar.

        NOTE: The default params will check EVERY SINGLE calendar spot for the
        event to remove. It is considered HIGHLY INEFFICIENT. Try to use the
        other removeEvent functions if possible, or narrow the search using
        month and day.

        NOTE:
            Using both month and day will do the same check as removeEvent_eld

        IN:
            chat_label - eventlabel of the event to remove
            month - If given (and a valid month), will only check the calendar
                in the given month.
                (Default: None)
            day - If given (and a valid day), will only check the calendar
                for the given day for each month
                (Default: None)
            remove_all - True means we remove every single occurence of the
                given eventlabel. False means we only remove the first one we
                find.
                (Default: False)
        """
        # inital sanity checks
        if month not in range(1,13):
            month = None

        if day not in range(1,32):
            day = None

        # now to see what operation we are doing
        if month is not None and day is not None:
            # ideally we want the user to pass in a month and day
            _removeEvent_md(chat_label, month, day)

        elif month is not None:
            # probably common to clean a month of an event
            _removeEvent_m(chat_label, month, remove_all=remove_all)

        elif day is not None:
            # less common to clean a particular day of each month
            _removeEvent_d(chat_label, day, remove_all=remove_all)

        else:
            # full scan. hopefully no one does this
            _removeEvent(chat_label, remove_all=remove_all)


    def removeEvent_ev(ev, month=None, day=None, remove_all=False):
        """
        Removes an event from the calendar.

        SEE removeEvent_el for important NOTES regarding this function.

        IN:
            ev - event to remove
            month - SEE removeEvent_el
            day - SEE removeEvent_el
            remove_all - SEE removeEvent_el
        """
        removeEvent_el(
            ev.eventlabel,
            month=month,
            day=day,
            remove_all=remove_all
        )


    def removeRepeatable(identifier, month=None, day=None):
        """
        Removes a repeatable from the calendar.

        NOTE: The default params will check EVERY SINGLE calendar spot for the
        repeatable to remove. It is considered HIGHLY INEFFICIENT. Try to use
        the other removeRepeatable functions if possible, or narrow the search
        using month and day.

        IN:
            identifier - identifier of the repeatable to remove
            month - If given (and a valid month), will only check the calendar
                in the given month.
                (Default: None)
            day - If given (and a valid day), will only check the calendar for
                the given day for reach month
                (Default: None)
        """
        # inital sanity checks
        if month not in range(1,13):
            month = None

        if day not in range(1,32):
            day = None

        # now to see which operation we are doing
        if month is not None and day is not None:
            # ideally we want the user to pass in a month and day
            _removeRepeatable_md(identifier, month, day)

        elif month is not None:
            # probably common to clean a month
            _removeRepeatable_m(identifier, month)

        elif day is not None:
            # less common to clean a particular day of a month
            _removeRepeatable_d(identifier, day)

        else:
            # full scan, hopefully no one does this
            _removeRepeatable(identifier)


    def removeRepeatable_d(identifier, _date):
        """
        Removes a repeatable from teh calendar at a precise datetime.date

        IN:
            identifier - identifier of the repeatable to remove
            _date - datetime.date we should look at for removal
        """
        _removeRepeatable_md(identifier, _date.month, _date.day)


    def removeRepeatable_dt(identifier, _datetime):
        """
        Removes a repeatable from teh calendar at aprecise datetime

        IN:
            identifier - identifier of the repeatable to remove
            _datetime - datetime we should look at for removal
        """
        removeRepeatable_d(identifier, _datetime.date())


init python:

    import store.fae_calendar as calendar
    import datetime

    calendar.addRepeatable("New years day",_("New Year's Day"),month=1,day=1,year_param=list())
    calendar.addRepeatable("Valentine",_("Valentine's Day"),month=2,day=14,year_param=list())
    #calendar.addRepeatable("White day","White Day",month=3,day=14,year_param=list())
    calendar.addRepeatable("Halloween",_("Halloween"),month=10,day=31,year_param=list())
    calendar.addRepeatable("Christmas eve",_("Christmas Eve"),month=12,day=24,year_param=list())
    calendar.addRepeatable("Christmas",_("Christmas"),month=12,day=25,year_param=list())
    calendar.addRepeatable("New year's eve",_("New Year's Eve"),month=12,day=31,year_param=list())

    if (
        persistent.sessions is not None
        and "first_session" in persistent.sessions
        and persistent.sessions["first_session"] is not None
    ):
        calendar.addRepeatable_dt(
            "first_session",
            _("<3"),
            persistent.sessions["first_session"],
            year_param=[persistent.sessions["first_session"].year]
        )
    
    player_bday = persistent._fae_player_bday

    if (
        player_bday is not None
        and type(player_bday) == datetime.date
        ):

        calendar.addRepeatable_d(
            "player-bday",
            _("Your Birthday"),
            player_bday,
            range(player_bday.year,FAECalendar.MAX_VIEWABLE_YEAR)
        )

init 2 python in fae_calendar:

    import store

    def addSeasonEvents():


        WINTER = _("Winter")
        SPRING = _("Spring")
        SUMMER = _("Summer")
        AUTUMN = _("Autumn")

        if renpy.game.persistent._fae_player_south_hemisphere:
            _season_names = [SUMMER,AUTUMN,WINTER,SPRING]
        else:
            _season_names = [WINTER,SPRING,SUMMER,AUTUMN]
        
        addRepeatable_d(
            WINTER,
            _season_names[0],
            store.fae_winter_solstice,
            []
        )

        addRepeatable_d(
            SPRING,
            _season_names[1],
            store.fae_spring_equinox,
            []
        )

        addRepeatable_d(
            SUMMER,
            _season_names[2],
            store.fae_summer_solstice,
            []
        )

        addRepeatable_d(
            AUTUMN,
            _season_names[3],
            store.fae_fall_equinox,
            []
        )

    addSeasonEvents()


label fae_show_calendar_detail(items,area,align,first_item,final_item):
    call screen fae_calendar_events_scrollable_list(items, area, align, first_item=first_item, final_item=final_item)
    return


style event_list_day_text is default

style event_list_night_text is default:
    color "#000000"
    outlines [(2, "#00000000", 0, 0)] # Otherwise text size will be different

style event_list_day_vscrollbar is classroom_vscrollbar

style event_list_night_vscrollbar is classroom_vscrollbar

style event_list_day_textbutton is generic_button_light:
    xysize (None, None)
    padding (0, 0, 0, 0)
    background Null()

style event_list_night_textbutton is generic_button_dark:
    xysize (None, None)
    padding (0, 0, 0, 0)
    background Null()

style event_list_day_textbutton_text is generic_button_text_light

style event_list_night_textbutton_text is generic_button_text_light
    
            


screen fae_calendar_events_scrollable_list(items, display_area, scroll_align, first_item=None, final_item=None, mask="#000000B2", frame=("mod_assets/calendar/calendar_bg.png" if mas_current_background.isFltDay() else "mod_assets/calendar/calendar_bg-n.png")):
    style_prefix ("event_list_day")

    zorder 51

    if mask:
        add Solid(mask)

    frame:
        area display_area

        if frame:
            background Frame(frame, 60, 60)

        # Header
        fixed:
            xpos 0
            ypos 0
            xfill True
            ysize 59

            if first_item:
                text _(first_item[0]):
                    xalign 0.5
                    yalign 0.5
                    if first_item[1]:
                        italic True
                    if first_item[2]:
                        bold True

        # Footer
        fixed:
            xpos 0
            ypos display_area[3] - 59
            xfill True
            ysize 59

            if final_item:
                textbutton _(final_item[0]):
                    style_suffix "textbutton"
                    xpos 20
                    yalign 0.5
                    if final_item[2]:
                        text_italic True
                    if final_item[3]:
                        text_bold True
                    action Return(final_item[1])

        # Item list
        viewport id "items":
            xpos 0
            ypos 69
            xfill True
            ysize display_area[3] - 128
            yadjustment prev_adj
            mousewheel True

            vbox:
                spacing 5

                for item_prompt,is_italic,is_bold in items:
                    text item_prompt:
                        xpos 20
                        if is_italic:
                            italic True
                        if is_bold:
                            bold True

        vbar:
            value YScrollValue("items")
            adjustment prev_adj
            xalign scroll_align
            ypos 69
            ysize display_area[3] - 128

label _fae_start_calendar(select_date=True):

    python:

        ui.add(FAECALENDAR(select_date))
        rv = ui.interact()

    
    return rv

label fae_start_calendar_read_only:

    call _fae_start_calendar(select_date=False) from _call__fae_start_calendar
    return _return

label fae_start_calendar_select_date:

    call _fae_start_calendar(select_date=True) from _call__fae_start_calendar_1
    return _return

screen calendar_overlay():
    zorder 6

    # vbox:
    #     xalign 0.305
    #     yalign 0.4
    #
    image "mod_assets/calendar/calendar_button_shadow.png" xpos 351 ypos 251

    if store.fae_calendar.enabled and not store._menu:
        imagebutton:
            idle ("mod_assets/calendar/calendar_button_normal.png")
            hover "mod_assets/calendar/calendar_button_hover.png"
            hover_sound gui.hover_sound
            activate_sound gui.activate_sound
            action Function(show_calendar)
            xpos 360
            ypos 260
    else:
        image ("mod_assets/calendar/calendar_button_normal.png") xpos 360 ypos 260

init python:

    def fae_isLeapYear(year):

        try:
            datetime.date(year, 2, 29)
            return True
        except ValueError:

            return False

