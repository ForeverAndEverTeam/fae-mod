init -2:
    default persistent.fae_sayori_auto_outfit_change_enabled = True
    default persistent.fae_custom_outfits = False
    default persistent.fae_outfit_quit = "fae_uniform"
    default persistent.fae_outfit_list = {}
    default persistent.fae_wearable_list = {}

init -1 python in fae_outfits:
    from Enum import Enum
    import json
    import os
    import random
    import re
    import store
    import store.fae_affection as fae_affection
    import store.fae_utilities as fae_utilities
    import store.fae_sprites as fae_sprites
    import time


    __CUSTOM_WEARABLES_DIRECTORY = os.path.join(renpy.config.basedir, "game/mod_assets/sayori/sitting/jsons/").replace("\\", "/")
    __CUSTOM_OUTFITS_DIRECTORY = os.path.join(renpy.config.basedir, "game/mod_assets/sayori/sitting/jsons/").replace("\\", "/")
    __WEARABLE_BASE_PATH = os.path.join(renpy.config.basedir, "game/mod_assets/sayori/sitting/")

    __RESTRICTED_CHARACTERS_REGEX = "((\.)|(\[)|(\])|(\})|(\{)|(,)|(\!))"

    __ALL_WEARABLES = {}
    __ALL_OUTFITS = {}

    _PREVIEW_OUTFIT = None
    _LAST_OUTFIT = None


    _SESSION_NEW_UNLOCKS = list()

    _changes_made = False

    WEARABLE_CATEGORIES = [
        "hairstyle",
        "eyewear",
        "accessory",
        "clothes",
        "headgear",
        "necklace"
    ]


    class FAEWearable():

        def __init__(
            self,
            reference_name,
            display_name,
            unlocked,
            is_fae_wearable
        ):

            self.reference_name = reference_name
            self.display_name = display_name
            self.unlocked = unlocked
            self.is_fae_wearable = is_fae_wearable

        
        @staticmethod
        def load_all():

            global __ALL_WEARABLES
            for wearable in __ALL_WEARABLES.values():
                wearable.__load()
        

        @staticmethod
        def save_all():
            global __ALL_WEARABLES
            for wearable in __ALL_WEARABLES.values():
                wearable.__save()
        

        @staticmethod
        def filter_wearables(
            wearable_list,
            unlocked=None,
            is_fae_wearable=None,
            reference_name=None,
            not_reference_name=None,
            wearable_type=None
        ):

            return [
                _wearable
                for _wearable in wearable_list
                if _wearable.__filter_wearable(
                    unlocked,
                    is_fae_wearable,
                    reference_name,
                    not_reference_name,
                    wearable_type
                )
            ]
        

        def as_dict(self):

            return {
                "unlocked": self.unlocked
            }
        

        def unlock(self):

            self.unlocked = True
            self.__save()
        

        def lock(self):

            self.unlocked = False
            self.__save()
        

        def __load(self):

            if store.persistent.fae_wearable_list[self.reference_name]:
                self.unlocked = store.persistent.fae_wearable_list[self.reference_name]["unlocked"]
        

        def __save(self):

            store.persistent.fae_wearable_list[self.reference_name] = self.as_dict()
        


        def __filter_wearable(
            self,
            unlocked = None,
            is_fae_wearable = None,
            reference_name = None,
            not_reference_name = None,
            wearable_type = None
        ):


            if unlocked is not None and self.unlocked != unlocked:
                return False

            elif is_fae_wearable is not None and self.is_fae_wearable != is_fae_wearable:
                return False

            elif reference_name is not None and not self.reference_name in reference_name:
                return False

            elif not_reference_name is not None and self.reference_name in not_reference_name:
                return False

            elif wearable_type is not None and not isinstance(self, wearable_type):
                return False

            return True


    class FAEHairstyle(FAEWearable):

        def getFolderName(self):
            return "hair"
    

    class FAEEyewear(FAEWearable):

        def getFolderName(self):
            return "eyewear"
        
    
    class FAEAccessory(FAEWearable):

        def getFolderName(self):
            return "accessory"
    

    class FAEClothes(FAEWearable):

        def getFolderName(self):
            return "clothes"
    

    class FAEHeadgear(FAEWearable):

        def getFolderName(self):
            return "headgear"
    
    class FAENecklace(FAEWearable):

        def getFolderName(self):
            return "necklace"
    

    class FAEOutfit():

        def __init__(
            self,
            reference_name,
            display_name,
            unlocked,
            is_fae_outfit,
            clothes,
            hairstyle,
            accessory=None,
            eyewear=None,
            headgear=None,
            necklace=None,
        ):

            if clothes is None:
                raise TypeError("Outfit clothing cannot be None")
                return

            if hairstyle is None:
                raise TypeError("Outfit hairstyle cannot be None")
                return

            self.reference_name = reference_name
            self.display_name = display_name
            self.unlocked = unlocked
            self.is_fae_outfit = is_fae_outfit
            self.clothes = clothes
            self.hairstyle = hairstyle
            self.accessory = accessory
            self.eyewear = eyewear
            self.headgear = headgear
            self.necklace = necklace



        @staticmethod
        def load_all():

            global __ALL_OUTFITS
            for outfit in __ALL_OUTFITS.values():
                outfit.__load()
        

        @staticmethod
        def save_all():

            global __ALL_OUTFITS
            for outfit in __ALL_OUTFITS.values():
                outfit.__save()
        

        @staticmethod
        def filter_outfits(
            outfit_list,
            unlocked=None,
            is_fae_outfit=None,
            not_reference_name=None,
            has_accessory=None,
            has_eyewear=None,
            has_headgear=None,
            has_necklace=None
        ):

            return [
                _outfit
                for _outfit in outfit_list
                if _outfit.__filter_outfit(
                    unlocked,
                    is_fae_outfit,
                    not_reference_name,
                    has_accessory,
                    has_eyewear,
                    has_headgear,
                    has_necklace
                )
            ]


        def as_dict(self):

            return {
                "unlocked": self.unlocked
            }
        

        def unlock(self):

            self.unlocked = True
            self.__save()

            # Unlock outfit components
            if not self.clothes.unlocked:
                self.clothes.unlock()

            if not self.hairstyle.unlocked:
                self.hairstyle.unlock()

            if self.accessory and not self.accessory.unlocked:
                self.accessory.unlock()

            if self.eyewear and not self.eyewear.unlocked:
                self.eyewear.unlock()

            if self.headgear and not self.headgear.unlocked:
                self.headgear.unlock()

            if self.necklace and not self.necklace.unlocked:
                self.necklace.unlock()
        


        def lock(self):

            self.unlocked = False
            self.__save()

        
        def to_json_string(self):


            outfit_dict = {
                    "reference_name": self.reference_name,
                    "display_name": self.display_name,
                    "unlocked": True,
                    "clothes": self.clothes.reference_name,
                    "hairstyle": self.hairstyle.reference_name
                }

            if self.headgear and isinstance(self.headgear, FAEHeadgear):
                outfit_dict["headgear"] = self.headgear.reference_name

            if self.eyewear and isinstance(self.eyewear, FAEEyewear):
                outfit_dict["eyewear"] = self.eyewear.reference_name

            if self.accessory and isinstance(self.accessory, FAEAccessory):
                outfit_dict["accessory"] = self.accessory.reference_name

            if self.necklace and isinstance(self.necklace, FAENecklace):
                outfit_dict["necklace"] = self.necklace.reference_name
        

            return json.dumps(outfit_dict)
        

        def __load(self):

            if store.persistent.fae_outfit_list[self.reference_name]:
                self.unlocked = store.persistent.fae_outfit_list[self.reference_name]["unlocked"]
        

        def __save(self):

            store.persistent.fae_outfit_list[self.reference_name] = self.as_dict()


        def __delete_save(self):

            if store.persistent.fae_outfit_list[self.reference_name]:
                del store.persistent.fae_outfit_list[self.reference_name]
        

        def __filter_outfit(
            self,
            unlocked=None,
            is_fae_outfit=None,
            not_reference_name=None,
            has_accessory=None,
            has_eyewear=None,
            has_headgear=None,
            has_necklace=None
        ):

            if unlocked is not None and self.unlocked != unlocked:
                return False

            elif is_fae_outfit is not None and self.is_fae_outfit != is_fae_outfit:
                return False

            elif not_reference_name is not None and self.reference_name in not_reference_name:
                return False

            elif has_accessory is not None and bool(self.has_accessory) != has_accessory:
                return False

            elif has_eyewear is not None and bool(self.has_eyewear) != has_eyewear:
                return False

            elif has_headgear is not None and bool(self.has_headgear) != has_headgear:
                return False

            elif has_necklace is not None and bool(self.has_necklace) != has_necklace:
                return False
            
            return True
        

    def __register_outfit(outfit, player_created=False):

        if outfit.reference_name in __ALL_OUTFITS:
            fae_utilities.log("Cannot register outfit name: {0}, as an outfit with that name already exists.".format(outfit.reference_name))

        else:
            if not outfit.accessory:
                outfit.accessory = get_wearable("fae_none")

            if not outfit.eyewear:
                outfit.eyewear = get_wearable("fae_none")

            if not outfit.headgear:
                outfit.headgear = get_wearable("fae_none")

            if not outfit.necklace:
                outfit.necklace = get_wearable("fae_none")
            

            __ALL_OUTFITS[outfit.reference_name] = outfit
            if outfit.reference_name not in store.persistent.fae_outfit_list:
                outfit.__save()

                # If this is the first time adding it to the list, and it isn't FAE or created by this player in the session, it's a new unlock
                if not "fae_" in outfit.reference_name and not player_created:
                    _SESSION_NEW_UNLOCKS.append(outfit)
    

    def __register_wearable(wearable):

        if wearable.reference_name in __ALL_WEARABLES:
            fae_utilities.log("Cannot register wearable name: {0}, as a wearable with that name already exists.".format(wearable.reference_name))

        else:
            __ALL_WEARABLES[wearable.reference_name] = wearable
            if wearable.reference_name not in store.persistent.fae_wearable_list:
                wearable.__save()

                if not "fae_" in wearable.reference_name:
                    _SESSION_NEW_UNLOCKS.append(wearable)

            else:
                wearable.__load()
    

    def __delete_outfit(outfit):

        outfit.__delete_save()
        del __ALL_OUTFITS[outfit.reference_name]

    def _check_wearable_sprites(wearable):

        WEARABLE_COMMON_PATH = os.path.join(__WEARABLE_BASE_PATH, wearable.getFolderName())


        if isinstance(wearable, FAEClothes):

            sleeves_path = os.path.join(__WEARABLE_BASE_PATH, "arms", wearable.reference_name, "{0}.png".format(pose.name))
            clothes_path = os.path.join(__WEARABLE_BASE_PATH, "body", wearable.reference_name, "{0}.png".format(pose.name))

            if not fae_utilities.doesExist(sleeves_path) or not fae_utilities.doesExist(clothes_path):
                fae_utilities.log("Missing body/arms sprite(s) for {0}".format(wearable.reference_name))
                return False

        elif isinstance(wearable, FAEHairstyle):
            hair_path = os.path.join(WEARABLE_COMMON_PATH, "hair", wearable.reference_name, "a.png")

            if not fae_utilities.doesExist(hair_path) or not fae_utilities.doesExist(hair_path):
                fae_utilities.log("Missing hair sprite(s) for {0}".format(wearable.reference_name))
                return False

        else:
            resource_path = os.path.join(WEARABLE_COMMON_PATH, wearable.reference_name, "sitting.png")

            if not fae_utilities.doesExist(resource_path):
                fae_utilities.log("Missing sprite(s) for {0}: check {1}".format(wearable.reference_name, resource_path))
                return False

        return True

    def _load_wearable_from_json(json):

        if (
            "reference_name" not in json
            or "display_name" not in json
            or "unlocked" not in json
            or "category" not in json
        ):
            fae_utilities.log("Cannot load wearable as one or more key attributes do not exist.")
            return False
        
        elif(
            not isinstance(json["reference_name"], basestring)
            or not isinstance(json["display_name"], basestring)
            or not isinstance(json["unlocked"], bool)
            or not isinstance(json["category"], basestring)
            or not json["category"] in WEARABLE_CATEGORIES
        ):
            fae_utilities.log("Cannot load wearable {0} as one or more attributes are the wrong data type.".format(json["reference_name"]))
            return False
    
        elif re.search("^fae_.", json["reference_name"].lower()):
            fae_utilities.log("Cannot load wearable {0} as the reference name contains a reserved namespace.".format(json["reference_name"]))
            return False

        elif re.search(__RESTRICTED_CHARACTERS_REGEX, json["reference_name"]):
            fae_utilities.log("Cannot load wearable {0} as the reference name contains one or more restricted characters.".format(json["reference_name"]))
            return False

        else:
            # Register based on category
            kwargs = {
                "reference_name": json["reference_name"],
                "display_name": json["display_name"],
                "unlocked": json["unlocked"],
                "is_fae_wearable": False
            }

            if json["category"] == "hairstyle":
                wearable = FAEHairstyle(**kwargs)

            elif json["category"] == "eyewear":
                wearable = FAEEyewear(**kwargs)

            elif json["category"] == "accessory":
                wearable = FAEAccessory(**kwargs)

            elif json["category"] == "clothes":
                wearable = FAEClothes(**kwargs)

            elif json["category"] == "headgear":
                wearable = FAEHeadgear(**kwargs)

            elif json["category"] == "necklace":
                wearable = FAENecklace(**kwargs)
            

            if not _check_wearable_sprites(wearable):
                fae_utilities.log("Cannot load wearable {0} as one or more sprites are missing.".format(wearable.reference_name))
                return False

            __register_wearable(wearable)
            return True
    
    def _load_outfit_from_json(json):

        if (
            "reference_name" not in json
            or "display_name" not in json
            or "unlocked" not in json
            or "clothes" not in json
            or "hairstyle" not in json
        ):
            fae_utilities.log("Cannot load outfit as one or more key attributes do not exist.")
            return False

        elif (
            not isinstance(json["reference_name"], basestring)
            or not isinstance(json["display_name"], basestring)
            or not isinstance(json["unlocked"], bool)
            or not isinstance(json["clothes"], basestring)
            or not isinstance(json["hairstyle"], basestring)
            or "eyewear" in json and not isinstance(json["eyewear"], basestring)
            or "headgear" in json and not isinstance(json["headgear"], basestring)
            or "necklace" in json and not isinstance(json["necklace"], basestring)
        ):

            fae_utilities.log("Cannot load outfit as one or more attributes are the wrong data type.")
            return False
        

        elif re.search("^fae_.", json["reference_name"].lower()):
            fae_utilities.log("Cannot load outfit {0} as the reference name contains a reserved namespace.".format(json["reference_name"]))
            return False

        elif re.search(__RESTRICTED_CHARACTERS_REGEX, json["reference_name"]):
            fae_utilities.log("Cannot load outfit {0} as the reference name contains one or more restricted characters.".format(json["reference_name"]))
            return False

        if not json["clothes"] in __ALL_WEARABLES:
            fae_utilities.log("Cannot load outfit {0} as specified clothes do not exist.".format(json["reference_name"]))
            return False

        elif not json["hairstyle"] in __ALL_WEARABLES:
            fae_utilities.log("Cannot load outfit {0} as specified hairstyle does not exist.".format(json["reference_name"]))
            return False

        elif "accessory" in json and not json["accessory"] in __ALL_WEARABLES:
            fae_utilities.log("Cannot load outfit {0} as specified accessory does not exist.".format(json["reference_name"]))
            return False

        elif "eyewear" in json and not json["eyewear"] in __ALL_WEARABLES:
            fae_utilities.log("Cannot load outfit {0} as specified eyewear does not exist.".format(json["reference_name"]))
            return False

        elif "headgear" in json and not json["headgear"] in __ALL_WEARABLES:
            fae_utilities.log("Cannot load outfit {0} as specified headgear does not exist.".format(json["reference_name"]))
            return False

        elif "necklace" in json and not json["necklace"] in __ALL_WEARABLES:
            fae_utilities.log("Cannot load outfit {0} as specified necklace does not exist.".format(json["reference_name"]))
            return False
        
        else:
            outfit = FAEOutfit(
                reference_name=json["reference_name"],
                display_name=json["display_name"],
                unlocked=json["unlocked"],
                is_fae_outfit=False,
                clothes=__ALL_WEARABLES[json["clothes"]],
                hairstyle=__ALL_WEARABLES[json["hairstyle"]],
                accessory=__ALL_WEARABLES[json["accessory"]] if "accessory" in json else None,
                eyewear=__ALL_WEARABLES[json["eyewear"]] if "eyewear" in json else None,
                headgear=__ALL_WEARABLES[json["headgear"]] if "headgear" in json else None,
                necklace=__ALL_WEARABLES[json["necklace"]]  if "necklace" in json else None
            )

            if not isinstance(outfit.clothes, FAEClothes):
                fae_utilities.log("Cannot load outfit {0} as specified clothes are not valid clothing.".format(outfit.reference_name))
                return False

            elif not isinstance(outfit.hairstyle, FAEHairstyle):
                fae_utilities.log("Cannot load outfit {0} as specified hairstyle is not a valid hairstyle.".format(outfit.reference_name))
                return False

            elif outfit.accessory and not isinstance(outfit.accessory, FAEAccessory):
                fae_utilities.log("Cannot load outfit {0} as specified accessory is not a valid accessory.".format(outfit.reference_name))
                return False

            elif outfit.eyewear and not isinstance(outfit.eyewear, FAEEyewear):
                fae_utilities.log("Cannot load outfit {0} as specified eyewear is not valid eyewear.".format(outfit.reference_name))
                return False

            elif outfit.headgear and not isinstance(outfit.headgear, FAEHeadgear):
                fae_utilities.log("Cannot load outfit {0} as specified headgear is not valid headgear.".format(outfit.reference_name))
                return False

            elif outfit.necklace and not isinstance(outfit.necklace, FAENecklace):
                fae_utilities.log("Cannot load outfit {0} as specified necklace is not a valid necklace.".format(outfit.reference_name))
                return Fals

            if outfit.unlocked:
                if (
                    not outfit.clothes.unlocked
                    or not outfit.hairstyle.unlocked
                    or outfit.accessory and not outfit.accessory.unlocked
                    or outfit.eyewear and not outfit.eyewear.unlocked
                    or outfit.headgear and not outfit.headgear.unlocked
                    or outfit.necklace and not outfit.necklace.unlocked
                ):
                    fae_utilities.log("Outfit {0} contains one or more locked components; locking outfit.".format(outfit.reference_name))
                    outfit.unlocked = False

            __register_outfit(outfit)
            return True

    def _clear_outfit_list():

        __ALL_WEARABLES = {}

    def _clear_wearable_list():
        
        __ALL_WEARABLES = {}     
    

    def load_custom_outfits():

        if fae_utilities.makedirifnot(__CUSTOM_OUTFITS_DIRECTORY):
            fae_utilities.log("Unable to load custom outfits as the directory does not exist, and had to be created.")
            return

        outfit_files = fae_utilities.getDirFile(__CUSTOM_OUTFITS_DIRECTORY, ["json"])
        success_count = 0

        for file_name, file_path in outfit_files:
            try:
                with open(file_path) as outfit_data:
                    if _load_outfit_from_json(json.loads(outfit_data.read())):
                        success_count += 1

            except OSError:
                fae_utilities.log("Unable to read file {0}; file could not be found.".format(file_name))

            except:
                raise

        if success_count != len(outfit_files):
            pass#renpy.notify("One or more outfits failed to load; please check log for more information.")
    

    def load_custom_wearables():

        if fae_utilities.makedirifnot(__CUSTOM_WEARABLES_DIRECTORY):
            fae_utilities.log("Unable to load custom wearables as the directory does not exist, and had to be created.")
            return

        wearable_files = fae_utilities.getDirFile(__CUSTOM_WEARABLES_DIRECTORY, ["json"])
        success_count = 0

        for file_name, file_path in wearable_files:
            try:
                with open(file_path) as wearable_data:
                    if _load_wearable_from_json(json.loads(wearable_data.read())):
                        success_count += 1

            except OSError:
                fae_utilities.log("Unable to read file {0}; file could not be found.".format(file_name))

            except:
                raise

        if success_count != len(wearable_files):
            renpy.notify("One or more wearables failed to load; please check log for more information.")
    

    def unload_custom_outfits():

        __ALL_OUTFITS = FAEOutfit.filter_outfits(
            outfit_list=get_all_outfits(),
            is_fae_outfit=True
        )

    
    def unload_custom_wearables():

        __ALL_WEARABLES = FAEWearable.filter_wearables(
            wearable_list=get_all_wearables(),
            is_fae_wearable=True
        )

        return
    

    def outfit_exists(outfit_name):

        return outfit_name in __ALL_OUTFITS
    
    def wearable_exists(wearable_name):

        return wearable_name in __ALL_WEARABLES
    
    def get_outfit(outfit_name):

        if outfit_exists(outfit_name):
            return __ALL_OUTFITS[outfit_name]
        
        return None
    

    def get_wearable(wearable_name):

        if wearable_exists(wearable_name):
            return __ALL_WEARABLES[wearable_name]
        
        return None
    

    def get_all_outfits():

        return __ALL_OUTFITS.values()
    

    def get_all_wearables():

        return __ALL_WEARABLES.values()

    
    def save_temporary_outfit(outfit):


        temporary_outfit = get_outfit("fae_temporary_outfit")
        temporary_outfit.clothes = outfit.clothes
        temporary_outfit.hairstyle = outfit.hairstyle
        temporary_outfit.accessory = get_wearable("fae_none") if not outfit.accessory else outfit.accessory
        temporary_outfit.eyewear = get_wearable("fae_none") if not outfit.eyewear else outfit.eyewear
        temporary_outfit.headgear = get_wearable("fae_none") if not outfit.headgear else outfit.headgear
        temporary_outfit.necklace = get_wearable("fae_none") if not outfit.necklace else outfit.necklace

        store.Sayori.setOutfit(temporary_outfit, persist=False)

        return True
    

    def save_custom_outfit(outfit):

        new_custom_outfit = FAEOutfit(
            reference_name="{0}_{1}_{2}".format(
                store.persistent.playername,
                outfit.display_name.replace(" ", "_"),
                int(time.time())
            ).lower(),
            display_name=outfit.display_name,
            unlocked=True,
            is_fae_outfit=False,
            clothes=outfit.clothes,
            hairstyle=outfit.hairstyle,
            accessory=outfit.accessory,
            eyewear=outfit.eyewear,
            headgear=outfit.headgear,
            necklace=outfit.necklace
        )


        if fae_utilities.makedirifnot(__CUSTOM_OUTFITS_DIRECTORY):
            fae_utilities.log("custom_outfits directory was not found and had to be created.")

        try:
            
            with open(os.path.join(__CUSTOM_OUTFITS_DIRECTORY, "{0}.json".format(new_custom_outfit.reference_name)), "w") as file:
                file.write(new_custom_outfit.to_json_string())

            __register_outfit(outfit=new_custom_outfit, player_created=True)
            store.Sayori.setOutfit(new_custom_outfit)
            renpy.notify("Outfit saved!")
            return True

        except Exception as exception:
            renpy.notify("Save failed; please check log for more information.")
            fae_utilities.log("Failed to save outfit {0}, as a write operation was not possible.".format(new_custom_outfit.display_name))
            return False
    

    def delete_custom_outfit(outfit):

        if fae_utilities.makedirifnot(__CUSTOM_OUTFITS_DIRECTORY):
            fae_utilities.log("custom_outfits directory was not found and had to be created.")

        elif not fae_utilities.removeFileDir(
            path=os.path.join(__CUSTOM_OUTFITS_DIRECTORY, "{0}.json".format(outfit.reference_name))
        ):
            renpy.notify("Delete failed; please check log for more information.")
            fae_utilities.log("Failed to delete outfit {0}, as a remove operation was not possible.".format(outfit.display_name))
            return False

        else:

            __delete_outfit(outfit)
            renpy.notify("Outfit deleted!")
            return True
    

    def get_realtime_outfit():


        if store.Sayori.isAffectionate(higher=True):
            if store.fae_is_weekday():
                return _OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY.get(store.fae_get_current_time_block())

            else:
                return _OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY.get(store.fae_get_current_time_block())

    

    __register_wearable(FAEWearable(
        reference_name="fae_none",
        display_name="None",
        unlocked=False,
        is_fae_wearable=True
    )
    )

    __register_wearable(FAEHairstyle(
        reference_name="fae_bow",
        display_name="Bow",
        unlocked=True,
        is_fae_wearable=True
    ))

    __register_wearable(FAEHairstyle(
        reference_name="fae_bowless",
        display_name="Bowless",
        unlocked=True,
        is_fae_wearable=True
    ))

    __register_wearable(FAEClothes(
        reference_name="fae_uniform",
        display_name="School Uniform",
        unlocked=True,
        is_fae_wearable=True
    ))

    __register_wearable(FAEClothes(
        reference_name="base",
        display_name="Base",
        unlocked=True,
        is_fae_wearable=True
    ))

    # Thanks, DJ
    __register_wearable(FAEClothes(
        reference_name="fae_hoodie",
        display_name="Black Hoodie",
        unlocked=True,
        is_fae_wearable = True
    ))

    __register_wearable(FAEClothes(
        reference_name="casual",
        display_name="Tank Top",
        unlocked=True,
        is_fae_wearable=True
    ))

    __register_wearable(FAENecklace(
        reference_name="fae_scarf",
        display_name="Scarf",
        unlocked=False,
        is_fae_wearable=True
    ))

    __register_outfit(FAEOutfit(
        reference_name="fae_uniform",
        display_name="School Uniform",
        unlocked=True,
        is_fae_outfit=True,
        clothes=get_wearable("fae_uniform"),
        hairstyle=get_wearable("fae_bow")
    ))

    # Thanks, DJ
    __register_outfit(FAEOutfit(
        reference_name="fae_hoodie",
        display_name="Black Hoodie",
        unlocked=True,
        is_fae_outfit=True,
        clothes=get_wearable("fae_hoodie"),
        hairstyle=get_wearable("fae_bow")
    ))

    __register_outfit(FAEOutfit(
        reference_name="fae_christmas",
        display_name="Christmas Outfit",
        unlocked=False,
        is_fae_outfit=True,
        clothes=get_wearable("fae_hoodie"),
        hairstyle=get_wearable("fae_bow"),
        necklace=get_wearable("fae_scarf")
    ))



