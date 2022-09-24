default persistent._fae_holiday_list = list()
default persistent._fae_holiday_completion_status = dict()


init -1 python in fae_holidays:
    
    import datetime
    from Enum import Enum
    import random
    import store
    import store.fae_affection as fae_affection
    import store.fae_globals as fae_globals
    import store.fae_outfits as fae_outfits
    import store.fae_utilities as fae_utilities

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
        natsuki_birthday = 7
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
            natsuki_sprite_code,
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
            self.natsuki_sprite_code = natsuki_sprite_code
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
                "natsuki_sprite_code": self.natsuki_sprite_code
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

        if holiday.label in __ALL_HOLIDAYS:
            fae_utilities.log("Cannot register holiday name: {0}, as a holiday with that name already exists.".format(holiday.reference_name))

        else:
            __ALL_HOLIDAYS[holiday.label] = holiday
            if holiday.label not in store.persistent._fae_holiday_list:
                holiday.__save()

            else:
                holiday.__load()

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

    def isPlayerBirthday(input_date=None)
    
