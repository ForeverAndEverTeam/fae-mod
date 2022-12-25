default persistent.affection_day_gain = 5
default persistent.affection_reset_date = None
default persistent.affection = 0
default persistent._affection_daily_bypasses = 5
init -2 python:
    def _fae_AffStart():

        if persistent.fae_last_visit_date is not None:
            persistent._fae_absence_time = (
                    datetime.datetime.now() -
                    persistent.fae_last_visit_date
            )
        else:
            persistent._fae_absence_time = datetime.timedelta(days=0)

init -2 python in fae_affection:


    import store
    import store.fae_utilities as fae_utilities
    import random

    AFF_BORDER_LOVE = 1000
    AFF_BORDER_ENAMORED = 500
    AFF_BORDER_AFFECTIONATE = 250
    AFF_BORDER_HAPPY = 100
    AFF_BORDER_NORMAL = 0

    NORMAL = 1
    HAPPY = 2
    AFFECTIONATE = 3
    ENAMOURED = 4
    LOVE = 5

    _AFF_STATUS_ORDER = [
        NORMAL,
        HAPPY,
        AFFECTIONATE,
        ENAMOURED,
        LOVE
    ]


    def get_relationship_length_multiplier():

        relationship_length_multiplier = 1 + (fae_utilities.get_total_gameplay_months() / 10)
        if relationship_length_multiplier > 1.5:
            relationship_length_multiplier = 1.5
        
        return relationship_length_multiplier


    def _isAffStatusValid(status):

        return (
            status in _AFF_STATUS_ORDER
            or status is None
        )
    
    def _compareAffBorders(value, border):

        return value - border

    def _compareAffectionStatuses(status_1, status_2):

        if status_1 == status_2:
            return 0

        if not _isAffStatusValid(status_1) or not _isAffStatusValid(status_2):
            return 0

        #If state 1 is less than state 2, return -1
        if _AFF_STATUS_ORDER.index(status_1) < _AFF_STATUS_ORDER.index(status_2):
            return -1

        #Else return 1
        return 1

    def _isAffRangeValid(affection_range):

        if affection_range is None:
            return True

        #deconstruct the tuple
        low_bound, high_bound = affection_range

        #No low bound and no high bound is equivalent to just no range
        if low_bound is None and high_bound is None:
            return True

        #Now test to see if the individual parts are valid
        if (
            not _isAffStatusValid(low_bound)
            or not _isAffStatusValid(high_bound)
        ):
            return False

        #Now if one side is None, and we know the other is valid, this is also valid
        if low_bound is None or high_bound is None:
            return True

        #Finally compare this to make sure we don't have an inversion
        return _compareAffectionStatuses(low_bound, high_bound) <= 0

    def _isAffStatusWithinRange(affection_status, affection_range):


        if affection_status is None or not _isAffStatusValid(affection_status):
            return False

        #No affection_range is a full range, so this is always True
        if affection_range is None:
            return True

        #Now, deconstruct the tuple
        low_bound, high_bound = affection_range

        #If low and high are none, it's also a full range, always True
        if low_bound is None and high_bound is None:
            return True

        #Now we run compareTo checks
        #Firstly, single-bounded checks (one side None)
        if low_bound is None:
            #We only care about the high bound
            return _compareAffectionStatuses(affection_status, high_bound) <= 0

        if high_bound is None:
            #Only the low bound matters
            return _compareAffectionStatuses(affection_status, low_bound) >= 0

        #If the range is only for the single level, so they should just be equal
        if low_bound == high_bound:
            return affection_status == low_bound

        #With the outlier cases done, simply check if we're within the range
        return (
            _compareAffectionStatuses(affection_status, low_bound) >= 0
            and _compareAffectionStatuses(affection_status, high_bound) <= 0
        )
    


init -2 python:
    
    class Affection(object):

        __capped_aff_dates = list()


        @staticmethod
        def calculatedAffectionGain(base=1, bypass=False):

            to_add = base * fae_affection.get_relationship_length_multiplier()

            if (
                not persistent._fae_player_confession_accepted
                and (persistent.affection + to_add) > (fae_affection.AFF_BORDER_LOVE -1)
            ):

                persistent.affection = fae_affection.AFF_BORDER_LOVE -1
                fae_utilities.log("Affection blocked - CN!")
                return

            if bypass and persistent._affection_daily_bypasses > 0:

                persistent.affection += to_add
                persistent._affection_daily_bypasses -= 1
                fae_utilities.log("Affection increased! (B)")
            
            elif persistent.affection_day_gain > 0:
                persistent.affection_day_gain -= to_add
                persistent.affection += to_add

                if persistent.affection_day_gain < 0:
                    persistent.affection_day_gain = 0
                
                fae_utilities.log("Affection increased!")
            
            else:
                Affection.writeCap()
        
        @staticmethod
        def calculatedAffectionLoss(base=1):

            persistent.affection -= base * fae_affection.get_relationship_length_multiplier()
            fae_utilities.log("Affection decreased")
        
        @staticmethod
        def percentageAffectionGain(percentage_gain):

            to_add = persistent.affection * (float(percentage_gain) / 100)
            if (not persistent._fae_player_confession_accepted and (persistent.affection + to_add) > (fae_affection.AFF_BORDER_LOVE -1)):
                
                persistent.affection = fae_affection.AFF_BORDER_LOVE -1
                fae_utilities.log("Affection blocked - CN!")

            else:
                persistent.affection += to_add
                fae_utilities.log("Affection increased!")

        @staticmethod
        def percentageAffectionLoss(percentage_loss):

            if persistent.affection == 0:
                persistent.affection -= (float(percentage_loss) / 10)

            else:
                persistent.affection -= abs(persistent.affection * (float(percentage_loss) / 100))
            
            fae_utilities.log("Affection decreased")

        @staticmethod
        def checkResetDailyAffectionGain():

            current_date = datetime.datetime.now()
            if current_date in Affection.__capped_aff_dates:
                return

            if not persistent.affection_reset_date:
                persistent.affection_reset_date = current_date

            elif current_date.day is not persistent.affection_reset_date.day:
                persistent.affection_day_gain = 5 * fae_affection.get_relationship_length_multiplier()
                persistent.affection_reset_date = current_date
                persistent._affection_daily_bypasses = 5
                fae_utilities.log("Daily affection cap reset; new cap is: {0}".format(persistent.affection_day_gain))
        
        @staticmethod
        def writeCap():
            fae_utilities.log("Daily affection cap reached!")
            if not datetime.datetime.today().isoformat() in Affection.__capped_aff_dates:
                Affection.__capped_aff_dates.append(datetime.datetime.today().isoformat())


        
        @staticmethod
        def __isStatusGreaterThan(aff_status):

            return fae_affection._isAffStatusWithinRange(
                Affection._getAffectionStatus(),
                (aff_status, None)
            )


        @staticmethod
        def __isStateLessThan(aff_status):
            return fae_affection._isAffStatusWithinRange(
                Affection._getAffectionStatus(),
                (None, aff_status)
            )

        
        @staticmethod
        def __isAff(aff_status, higher=False, lower=False):

            if higher and lower:
                return True

            if higher:
                return Affection.__isStatusGreaterThan(aff_status)

            elif lower:
                return Affection.__isStatusLessThan(aff_status)

            return Affection._getAffectionStatus() == aff_status


        @staticmethod
        def isNormal(higher=False, lower=False):

            return Affection.__isAff(fae_affection.NORMAL, higher, lower)


        @staticmethod
        def isHappy(higher=False, lower=False):

            return Affection.__isAff(fae_affection.HAPPY, higher, lower)

        @staticmethod
        def isAffectionate(higher=False, lower=False):

            return Affection.__isAff(fae_affection.AFFECTIONATE, higher, lower)


        @staticmethod
        def isEnamoured(higher=False, lower=False):

            return Affection.__isAff(fae_affection.ENAMOURED, higher, lower)


        @staticmethod
        def isLove(higher=False, lower=False):

            return Affection.__isAff(fae_affection.LOVE, higher, lower)

        @staticmethod
        def _getAffectionStatus():

            i = 1
            for border in [
                fae_affection.AFF_BORDER_LOVE,
                fae_affection.AFF_BORDER_ENAMORED,
                fae_affection.AFF_BORDER_AFFECTIONATE,
                fae_affection.AFF_BORDER_HAPPY,
                fae_affection.AFF_BORDER_NORMAL
            ]:


                if fae_affection._compareAffBorders(persistent.affection, border) >= 0:
                    return fae_affection._AFF_STATUS_ORDER[-i]

                # We can't go any further beyond happy; return it
                if border == fae_affection.AFF_BORDER_HAPPY:
                    return fae_affection._AFF_STATUS_ORDER[0]

                i += 1

        def _getAffectionTierName():
            affection_status = Affection._getAffectionStatus()
            if affection_status == fae_affection.ENAMOURED:
                return "LOVE"

            elif affection_status == fae_affection.ENAMOURED:
                return "ENAMOURED"

            elif affection_status == fae_affection.AFFECTIONATE:
                return "AFFECTIONATE"

            elif affection_status == fae_affection.HAPPY:
                return "HAPPY"

            elif affection_status == fae_affection.NORMAL:
                return "NORMAL"

            else:
                store.fae_utilities.log(
                    message="Unable to get tier name for affection {0}; affection_state was {1}".format(
                        store.persistent.affection,
                        Affection._getAffectionStatus()
                    ),
                    logseverity=store.fae_utilities.SEVERITY_WARN
                )
                return "UNKNOWN"
















