init -1 python:
    
    class Affection(object):


        @staticmethod
        def getAffectionGain(default=5, bypass=False):

            add = default
            if bypass:

                persistent.affection += add
            
            elif persistent.affection_day_gain > 0:

                persistent.affection_day_gain -= add
            
                persistent.affection += add
            
                if persistent.affection_day_gain < 0:
                    persistent.affection_day_gain = 0
                
            else:
                fae_utilities.log("Daily affection cap hath been reachethed!")
        
        @staticmethod
        def getAffectionLoss(default=5):

            persistent.affection -= default
        
        @staticmethod
        def AffectionGainPercetile(percentile_gain):

            persistent.affection += persistent.affection * (float(percentile_gain) / 100)
        
        @staticmethod
        def AffectionLossPercentile(percentile_loss):

            persistent.affection -= persistent.affection * (float(percentile_loss) / 100)
        

        @staticmethod
        def DayAffectionGainChecker():

            curr_date = datetime.datetime.now()

            if not persistent.affection_reset_date:
                persistent.affection_reset_date = curr_date
            
            elif curr_date.day is not persistent.affection_reset_date.day:
                persistent.affection_day_gain = 5
            
                persistent.affection_reset_date = curr_date
                fae_utilities.log("Daily affection cap has been reset to {0}".format(persistent.affection_day_gain))
            
        
        @staticmethod
        def __StatusMore(affection_status):

            return fae_affection._AffectionStateInRange(
                Affection._getAffectionStatus(),
                (None, affection_status)
            )
        

        @staticmethod
        def __StatusLess(affection_status):

            return fae_affection._AffectionStateInRange(
                Affection._getAffectionStatus(),
                (None, affection_status)
            )
        

        @staticmethod
        def __isAffection(affection_status, higher=False, lower=False):

            if higher and lower:
                return True
            

            if higher:
                return Affection.__StatusMore(affection_status)
            
            elif lower:
                return Affection.__StatusLess(affection_status)
            
            return Affection._getAffectionStatus() == affection_status
        

        @staticmethod
        def isNormal(higher=False, lower=False):

            return Affection.__isAffection(fae_affection.NORMAL, higher, lower)
        

        @staticmethod
        def isHappy(higher=False, lower=False):

            return Affection.__isAffection(fae_affection.HAPPY, higher, lower)
        

        @staticmethod
        def isAffectionate(higher=False, lower=False):

            return Affection.__isAffection(fae_affection.AFFECTIONATE, higher, lower)
        

        @staticmethod
        def isEnamoured(higher=False, lower=False):

            return Affection.__isAffection(fae_affection.ENAMOURED, higher, lower)
        
        
        @staticmethod
        def isLove(higher=False, lower=False):

            return Affection.__isAffection(fae_affection.LOVE, higher, lower)
        

        @staticmethod
        def _getAffectionStatus():

            
            i = 1
            for border in [
                fae_affection.AFFECTION_LOVE_BORDER,
                fae_affection.AFFECTION_ENAMOURED_BORDER,
                fae_affection.AFFECTION_AFFECTIONATE_BORDER,
                fae_affection.AFFECTION_HAPPY_BORDER
            ]:

                if fae_affection._AffectionBorderCompare(persistent.affection, border) >= 0:
                    return fae_affection._AFFECTION_STATUS_ORDER[-i]
                
                i += 1
        

        def _findAffectionLevel():

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
                    message="Unable to get level name for affection {0}. affection_status was {1}".format(
                        store.persistent.affection,
                        Affection._getAffectionStatus()
                    ),
                    logseverity=store.fae_utilities.SEVERITY_WARN
                )

                return "UNKNOWN"


init 10 python in fae_globals:

    curr_affection_status = store.fae_affection.NORMAL

default persistent.affection = 0.0

default persistent.affection_day_gain = 10
default persistent.affection_reset_date = None


init -2 python in fae_affection:

    import store
    import store.fae_utilities as fae_utilities
    import random

    AFFECTION_LOVE_BORDER = 1000
    AFFECTION_ENAMOURED_BORDER = 500
    AFFECTION_AFFECTIONATE_BORDER = 250
    AFFECTION_HAPPY_BORDER = 100
    AFFECTION_NORMAL_BORDER = 0


    NORMAL = 1
    HAPPY = 2
    AFFECTIONATE = 3
    ENAMOURED = 4
    LOVE = 5

    _AFFECTION_STATUS_ORDER = [
        NORMAL,
        HAPPY,
        AFFECTIONATE,
        ENAMOURED,
        LOVE
    ]


    def _checkAffectionStatus(status):

        return (
            status in _AFFECTION_STATUS_ORDER
            or status is None
        )
    
    def _AffectionBorderCompare(value, border):

        return value - border
    

    def _AffectionStatusCompare(status_1, status_2):


        if status_1 == status_2:
            return 0
        
        if not _checkAffectionStatus(status_1) or not _checkAffectionStatus(status_2):
            return 0
        

        if _AFFECTION_STATUS_ORDER.index(status_1) < _AFFECTION_STATUS_ORDER.index(status_2):
            return -1
        

        return 1
    

    def _checkAffectionRange(affection_range):

        if affection_range is None:
            return True
        
        low_sect, high_sect = affection_range

        if low_sect is None and high_sect is None:
            return True
        

        if (
            not _checkAffectionStatus(low_sect)
            or not _checkAffectionStatus(high_sect)
        ):
            return False
        
        if low_sect is None or high_sect is None:
            return True
        

        return _AffectionStatusCompare(low_sect, high_sect) <= 0
    
    def _AffectionStateInRange(affection_status, affection_range):

        if affection_status is None or not _checkAffectionStatus(affection_status):
            return False
        
        if affection_range is None:
            return True
        

        low_sect, high_sect = affection_range
    
        if low_sect is None and high_sect is None:
            return True
        

        if low_sect is None:

            return _AffectionStatusCompare(affection_status, high_sect) <= 0
        
        if high_sect is None:

            return _AffectionStatusCompare(aff_status, low_sect) >= 0
        
        if low_sect == high_sect:
            return affection_status == low_sect
        
        return (
            _AffectionStatusCompare(affection_status, low_sect) >= 0
            and _AffectionStatusCompare(affection_status, high_sect) <= 0
        )

