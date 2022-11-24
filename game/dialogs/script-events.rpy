default persistent._event_db = dict()
default persistent._fae_holiday_list = list()
default persistent._fae_holiday_completion_status = dict()

default persistent._fae_player_anniversary = None
#default persistent._fae_holiday_list = dict()
#default persistent._fae_holiday_completion_states = dict()

image asset mr_cow = "mod_assets/images/EVENT/mr_cow.png"
image asset spe1 = "mod_assets/images/EVENT/spe1.png"
image asset spe2 = Image("mod_assets/images/EVENT/spe2.png", yoffset=-100)
image asset desk = "mod_assets/sayori/table/desk.png"
image asset chair = "mod_assets/sayori/table/chair.png"
image asset desk_shadow = "mod_assets/sayori/table/desk_sh.png"
image asset note = "mod_assets/sayori/table/note.png"
image asset knife = Image("mod_assets/images/EVENT/pointy_stick.png", yoffset=1)



image asset mr_cow_desk = Composite(
    (1280, 720),
    (0, 0), "mod_assets/sayori/table/chair.png",
    (0, 0), "mod_assets/images/EVENT/mr_cow.png",
    (0, 0), "mod_assets/sayori/table/desk.png",
    (0, 0), "mod_assets/sayori/table/desk_sh.png"
)


init -1 python in fae_events:
    import random
    import store
    #import store
    import datetime
    from Enum import Enum
    import store.fae_music as fae_music
    import store.fae_sky as fae_sky
    import store.fae_affection as fae_affection
    import store.fae_globals as fae_globals
    import store.fae_outfits as fae_outfits
    import store.fae_utilities as fae_utilities

    
    EVENT_DEFS = dict()
    EVENT_RETURN_OUTFIT = None

    
    FAE_EVENT_DECOR_ZORDER = 2
    FAE_EVENT_ASSET_ZORDER = 4

    HOLIDAY_DEFS = dict()

    HOLIDAY_RETURN_OUTFIT = None

    __ALL_HOLIDAYS = {}

    class FAEHolidayTypes(Enum):
        new_years_day = 1
        easter = 2
        halloween = 3
        christmas_eve = 4
        christmas_day = 5
        new_years_eve = 6
        sayori_birthday = 7
        player_birthday = 8
        anniversary = 9
        valentines_day = 10

        def __str__(self):
            return self.name
    
    class FAEHoliday():

        def __init__(
            self,
            label,
            holiday_type,
            conditional,
            affection_range,
            sayori_sprite_code,
            bgm=None,
            decor_list=[],
            prop_list=[],
            priority=0
        ):

            self.label = label
            self.is_seen = False
            self.holiday_type = holiday_type
            self.conditional = conditional
            self.affection_range = affection_range
            self.sayori_sprite_code = sayori_sprite_code
            self.bgm = bgm
            self.decor_list = decor_list
            self.prop_list = prop_list
            self.priority = priority

        
        @staticmethod
        def loadAll():
            global __ALL_HOLIDAYS
            for holiday in __ALL_HOLIDAYS.values():
                holiday.__load()
        
        @staticmethod
        def filterHolidays(
            holiday_list,
            holiday_types=None,
            affection=None,
            holiday_completion_status=None
        ):

            return [
                _holiday
                for _holiday in holiday_list
                if _holiday.__filterHoliday(
                    holiday_types,
                    affection,
                    holiday_completion_status
                )
            ]
        
        def asDict(self):

            return {
                "is_seen": self.is_seen
            }
        
        def currAffectionInAffectionRange(self, affection_status=None):

            if not affection_status:
                affection_status = fae_affection._getAffectionStatus()
            
            return fae_affection._AffectionStateInRange(affection_status, self.affection_range)

        def __load(self):

            if store.persistent._fae_holiday_list[self.label]:
                self.is_seen = store.persistent._fae_holiday_list[self.label]["is_seen"]
        
        def __save(self):

            store.persistent._fae_holiday_list[self.label] = self.asDict()
        

        def __filterHoliday(
            self,
            holiday_types=None,
            affection=None,
            holiday_completion_state=None
        ):
            if self.is_seen:
                return False

            elif holiday_types and not self.holiday_type in holiday_types:
                return False

            elif affection and not self.currAffectionInAffectionRange(affection):
                return False

            elif (
                holiday_completion_status
                and store.persistent._fae_holiday_completion_status[str(self.holiday_type)]
            ):
                return False

            elif not eval(self.conditional):
                return False

            return True

        def run(self):

            for prop in self.prop_list:
                renpy.show(name="prop {0}".format(prop), zorder=FAE_EVENT_PROP_ZORDER)

            for decor in self.decor_list:
                renpy.show(name="decor {0}".format(decor), zorder=FAE_EVENT_DECO_ZORDER)

            kwargs = {
                "sayori_sprite_code": self.sayori_sprite_code
            }
            if self.bgm:
                kwargs.update({"bgm": self.bgm})

            fae_globals.force_quit_enabled = True
            displayVisuals(**kwargs)

        
        def complete(self):

            self.is_seen = True
            self.__save()
            store.persistent._fae_holiday_completion_status[str(self.holiday_type)]

    def __regHoliday(holiday):

        #if holiday.label in __ALL_HOLIDAYS:
        #    fae_utilities.log("Cannot register holiday name: {0}, as a holiday with that name already exists.".format(holiday.reference_name))

        #else:
        #    __ALL_HOLIDAYS[holiday.label] = holiday
            #if holiday.label not in store.persistent._fae_holiday_list:
            #    holiday.__save()

        #    else:
        #        holiday.__load()
        return None

    def getHoliday(holiday_name):

        if holiday_name in __ALL_HOLIDAYS:
            return __ALL_HOLIDAYS[holiday_name]

        return None

    def isNewYearsDay(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_NEW_YEARS_DAY

    def isValentinesDay(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_VALENTINES_DAY

    def isEaster(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_EASTER

    def isHalloween(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_HALLOWEEN

    def isChristmasEve(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_CHRISTMAS_EVE

    def isChristmasDay(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_CHRISTMAS_DAY

    def isNewYearsEve(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_NEW_YEARS_EVE

    def isSayoriBirthday(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        return input_date == store.FAE_SAYORI_BIRTHDAY

    

    def isPlayerBirthday(input_date=None):

        if not store.persistent._fae_player_bday:
            return False

        if input_date is None:
            input_date = datetime.datetime.today()

        player_bday = datetime.date(
            #2020,
            store.persistent._fae_player_bday
        )

        return (input_date == player_bday)

    def isAnniversary(input_date=None):

        if not store.persistent._fae_player_anniversary:
            return False

        if input_date is None:
            input_date = datetime.datetime.today()

        anniversary_date = datetime.date(
            2020,
            store.persistent._fae_player_anniversary[1],
            store.persistent._fae_player_anniversary[0]
        )

        return (input_date.month == anniversary_date.month and input_date.day == anniversary_date.day)

    def getHolidaysForDate(input_date=None):

        if input_date is None:
            input_date = datetime.datetime.today()

        elif not isinstance(input_date, datetime.date):
            raise TypeError("input_date for holiday check must be of type date; type given was {0}".format(type(input_date)))

        holidays = []

        if isNewYearsDay(input_date):
            holidays.append(FAEHolidayTypes.new_years_day)

        if isValentinesDay(input_date):
            holidays.append(FAEHolidayTypes.valentines_day)

        if isEaster(input_date):
            holidays.append(FAEHolidayTypes.easter)

        if isHalloween(input_date):
            holidays.append(FAEHolidayTypes.halloween)

        if isChristmasEve(input_date):
            holidays.append(FAEHolidayTypes.christmas_eve)

        if isChristmasDay(input_date):
            holidays.append(FAEHolidayTypes.christmas_day)

        if isChristmasEve(input_date):
            holidays.append(FAEHolidayTypes.new_years_eve)

        if isSayoriBirthday(input_date):
            holidays.append(FAEHolidayTypes.sayori_birthday)

        if isPlayerBirthday(input_date):
            holidays.append(FAEHolidayTypes.player_birthday)

        if isAnniversary(input_date):
            holidays.append(FAEHolidayTypes.anniversary)

        return holidays

    def getAllHolidays():
        
        #Returns a list of all holidays.
        
        return __ALL_HOLIDAYS.values()
    
    def selectHolidays():
        
        #Returns a list of all holidays with a corresponding incomplete persistent entry that apply for the current date, or None if no holidays apply
        
        holiday_list = FAEHoliday.filterHolidays(
            holiday_list=getAllHolidays(),
            holiday_types=getHolidaysForDate(),
            affection=store.Affection._getAffectionStatus(),
            holiday_completion_status=False
        )

        if len(holiday_list) > 0:
            return holiday_list

        else:
            return None

    def resetHolidays():
        
        #Resets the is_seen state and corresponding completion state for all holidays.
        
        for holiday in getAllHolidays():
            holiday.is_seen = False

        for holiday_type in FAEHolidayTypes:
            if str(holiday_type) in store.persistent._fae_holiday_completion_status:
                store.persistent._fae_holiday_completion_status[str(holiday_type)] = False
    
    def displayVisuals(
        sayori_sprite_code,
        bgm=None
    ):

        renpy.show("sayori {0}".format(sayori_sprite_code), at_list=[store.fae_center], zorder=store.fae_sprites.FAE_SAYORI_ZORDER)
        renpy.hide("black")
        #renpy.show_screen("hkb_overlay")
        #renpy.play(filename=audio.light_switch, channel="audio")
        #renpy.play(filename=bgm, channel="music")

        # Reveal
        renpy.hide("black")

    #for holiday_type in FAEHolidayTypes:
    #    if not str(holiday_type) in store.persistent._fae_holiday_completion_states:
    #        store.persistent._fae_holiday_completion_states[str(holiday_type)] = False

    # Holiday registration

    # New year's eve
    __regHoliday(FAEHoliday(
        label="event_new_years_eve",
        holiday_type=FAEHolidayTypes.new_years_day,
        conditional="store.fae_holidays.isNewYearsEve()",
        affection_range=(fae_affection.HAPPY, None),
        sayori_sprite_code="aaabaa",
        priority=10
    ))

    # New year's day
    __regHoliday(FAEHoliday(
        label="event_new_years_day",
        holiday_type=FAEHolidayTypes.new_years_day,
        conditional="store.fae_holidays.isNewYearsDay()",
        affection_range=(fae_affection.HAPPY, None),
        sayori_sprite_code="aaabaa",
        #deco_list=["balloons"],
        priority=10
    ))

    # Player's birthday
    __regHoliday(FAEHoliday(
        label="event_player_birthday",
        holiday_type=FAEHolidayTypes.player_birthday,
        conditional="store.fae_holidays.isPlayerBirthday()",
        affection_range=(fae_affection.AFFECTIONATE, None),
        sayori_sprite_code="aaabaa",
        #bgm=audio.happy_birthday_bgm,
        #deco_list=["balloons"],
        #prop_list=["cake unlit"],
        priority=99
    ))



    def event_selector():

        kwargs = dict()

        event_list = store.Chat.chat_filt(
            EVENT_DEFS.values(),
            unlocked=True,
            affection=store.Affection._getAffectionStatus(),
            has_seen=False,
            **kwargs
        )

        if len(event_list) > 0:
            return random.choice(event_list).label
        
        else:
            return None
    

    
    
    
    def show_visuals(
        sayori_sprite_code,
        bgm="mod_assets/bgm/s1_ac.ogg"
    ):


        renpy.show("sayori {0}".format(sayori_sprite_code), at_list=[store.fae_center], zorder=store.fae_sprites.FAE_SAYORI_ZORDER)
        renpy.hide("black")

        renpy.play(filename=bgm, channel="music")

        renpy.hide("black")
    
label event_interlude:
    s "..."

    return



    
    
 

label event_new_years_eve:
    $ fae_events.getHoliday("event_new_years_eve").run()
    s "[player]!{w=1}{nw}"
    s "[player]!{w=0.5} [player]!"
    s "Look at the date!{w=0.5}{nw}"
    extend " Do you even know what day it is?!{w=1}{nw}"
    extend " It's almost the new year!"
    s "Man...{w=1}{nw}"
    extend " and about time too,{w=0.1} huh?"
    s "I don't know about you,{w=0.1} [player]...{w=1}{nw}"
    $ current_year = datetime.date.today().year
    extend " but I can't {i}WAIT{/i} to tell [current_year] where to stick it!"
    s "And what better way to do that...{w=0.75}{nw}" 
    extend " than a crap ton of explosions and snacks?"
    s "Ehehe.{w=0.5}{nw}"
    extend " It's gonna be great!"

    

    $ fae_events.getHoliday("event_new_years_eve").complete()

    return




init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_mr_cow_transform",
            unlocked=False,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_mr_cow_transform:

    hide black

    $ fae_globals.allow_force_quit = False

    show asset mr_cow_desk as mr_cow_desk zorder fae_sprites.FAE_SAYORI_ZORDER
   
    s "[player] heeeeeeelp!!!"
    s "I was messing with the code and accidentally turned myself into Mr. Cow!"
    s "Noooooooo!!!!"
    
    pause 1.5
    
    s "Pffffftt-"
    
    show asset spe1 zorder 2

    
    s "Bwahahahahah- I'm sorry, [player]!"
    s "I'm fine- I just couldn't resist that one!"
    s "I'll go put him away now, I'll be back in a sec!"

    hide asset spe1

    hide mr_cow_desk

    show emptydesk

    pause 2.0
    
    #ause 2.0

    $ fae_events.show_visuals("abhfcqa")

    #show sayori idle at t11 zorder fae_sprites.SAYO_ZORDER
    
    s abhfcqa "There we go, ehehe~"
    s abhfcoa "Welcome back, [player]!" 
    s abhabsa "I was just kinda starting to miss you so…"
    s abhacea "I dug in the code until I could rescue Mr. Cow!"
    s abbbloa "It was hard work, buuuuut!"
    s abgcdoa "Now I'll always have someone to cuddle with, and it'll never get {i}too{/i} lonely in here!"
    s abhfcaa "Anyways, I'm glad you're here now!" 
    return
    
init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_pointy_stick_stabber_girl",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_pointy_stick_stabber_girl:

    #$ fae_events.show_visuals("abbcckc")

    hide black

    #$ fae_events.show_visuals("idle")

    show sayori idle at fae_center zorder fae_sprites.FAE_SAYORI_ZORDER


    show asset knife as knife at fae_center zorder fae_sprites.FAE_SAYORI_ZORDER

    

    s abbcckc "Hi, [player]! Ready to chop up some bitches?"
    s "Does this look like the face of mercy, [player]?"
    s bbfceea "AHAHAHA…{nw}"
    extend bbfcdia"Just kidding!"
    s abbciia "Sorry about that!"
    
    menu:
        "Where did you even get that???":
            pass
    
    s eahcbsa "Great question!{w=1.0} {nw}"
    extend eahcada "I've been doing some more digging into the code to recover as much stuff as possible!"
    
    s ebbccqa "I managed to get this knife back today!"
    s fbfckdaj "Not really sure if I'll ever need it for anything, but I figured I might as well have it."
    s bbfcmoaj "But maybe it's better if I put this away now."
    s bbbcciaj "I wouldn't want anything bad to happen, ehehe~"
    
    hide knife 
    
    s abhaaoa "Hope you're doing good today, [player]~" 
    s abhaiia "Did I make you nervous?"
    s ebhhcoa "Sorry for scaring you, ehehe~"
    
    return

init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_sayori_desk_hide",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_sayori_desk_hide:
    hide sayori
    window hide
    hide black
    show asset spe2 at s11 zorder fae_sprites.FAE_SAYORI_ZORDER
    show emptydesk at t11 zorder 4
    pause 0.5
    $ style.say_dialogue = style.whisper
    s "Hehehe, [player] will never see this coming, Mr. Cow!"
    s "Oh! I think they're here! Shhh, get down!" 
    s "Ready? 3... 2... 1..."
    hide spe2
    hide emptydesk
    $ style.say_dialogue = style.normal
    show sayori at t11 zorder fae_sprites.FAE_SAYORI_ZORDER
    s ebbccoa "Boo!"
    s bbbcaoa "Hehehehehe! Did I scare you [player]?"
    s abgbaoa "I wish I could have seen the look on your face, ehehehe~"
    s cbgbaoa "You better always be on your toes around me!"
    s abaacoa "Anyways! Hehehehe~"
    return

init 5 python:
    chatReg(
        Chat(
            persistent._event_db,
            label="fae_event_door_open",
            unlocked=True,
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_EVENT
    )

label fae_event_door_open:
    scene black
    menu:
        "...":
            jump event_door_open
        "Gently open the door":
            hide black
            $ main_background.form()
            $ fae_sky.reload_sky()
            s bbegmoajj "Whoops! Sorry about that!"
            s abegaoaj "Welcome back, [player]! {w=0.5}{nw}"
            extend gbaamoj "Sorry if I scared you!"
            s abfccoaj "I've been learning how to use menus, and thought I'd give it a go.{w=0.5}{nw}"
            extend abfcaoaj " But never mind that."
            s abegcoaj "I'm so glad you're back!"
    return
