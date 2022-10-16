# Start in the spaceroom (as usual)
default persistent._present_room = "spaceroom"

# Sunrise Sunset times
default persistent.fae_sunup = 6
default persistent.fae_sundown = 18
default persistent.fae_moonup = 21

init -1 python in fae_rooms:

    import store
    
    ROOM_DEFS = dict()

init -20 python:

    import os
    
    # The zorder of the room. Behind Sayori, in front of sky.
    FAE_ROOM_ZORDER = 1

    class Rooms(object):
    
        """
        Props:
            id
            image_directory
            when_enter
            when_leave
            decoration_permitted
        """

        # Room file suffixes (not including extentions)
        DAY = "-day"
        NIGHT = "-night"

        IMG_EXTENSION = ".png"

        def __init__(
            self,
            id,
            image_directory,
            image_failsafe=None,
            decoration_permitted=None,
            when_enter=None,
            when_leave=None,
        ):
            """
            Constructor
            
            Feed:
                id - a unique id for this background. Will raise exceptions if a Location with a duplicate initialized
                image_directory - Path to images
                image_failsafe - a dict of image tags with the following keys:
                    "DAY", "NIGHT", these will have image tags as their values, which should be used to display
                decoration_permitted - List of strings representing categories for decorations which are supported for this Location
                    If None, this is set to an empty list. Empty lists mean no decorations are supported
                    (Default: None)
                when_enter - Function to run when changing into this Location. If None, nothing is done.
                    (Default: None)
                when_leave - Function to run when leaving this Location. If None, nothing is done.
                    (Default: None)
            """

            if id in store.fae_rooms.ROOM_DEFS:
                raise Exception("[ERROR]: A room with id '{0}' already exists.".format(id))
            
            if not os.path.isdir(renpy.config.gamedir + "/mod_assets/rooms/{0}".format(image_directory)):
                raise Exception(
                    "[ERROR]: Image directory '{0}' is not a directory.".format(
                        os.path.join(renpy.config.gamedir, "mod_assets", "rooms", image_directory)
                    )
                )
            
            # Check it can be loaded.
            if id in store.fae_rooms.ROOM_DEFS:
                raise Exception("[ERROR]: A room with id '{0}' already exists.".format(id))
            
            if not os.path.isdir(renpy.config.gamedir + "/mod_assets/background/{0}".format(image_directory)):
                raise Exception(
                    "[ERROR]: Image dir '{0}' is not a directory.".format(
                        os.path.join(renpy.config.gamedir, "mod_assets", "backgrounds", image_directory)
                    )
                )
                    
            
            daytime_path = "mod_assets/rooms/{0}/{1}".format(image_directory, id + Rooms.DAY + Rooms.IMG_EXTENSION)
            night_path = "mod_assets/rooms/{0}/{1}".format(image_directory, id + Rooms.NIGHT + Rooms.IMG_EXTENSION)


            if not renpy.loadable(daytime_path):
                raise Exception("[ERROR]: Daytime image ('{0}') is not loadable.".format(daytime_path))
            
            if not renpy.loadable(night_path):
                raise Exception("[ERROR]: Nighttime image ('{0}') is not loadable.".format(night_path))

            
            self.id = id

            self.daytime_tag = "{0}_day".format(id)

            self.nighttime_tag = "{0}_night".format(id)

            renpy.display.image.images.update({
                (self.daytime_tag,): Image(daytime_path),
                (self.nighttime_tag,): Image(night_path)
            })

            if decoration_permitted is None:
                self.decoration_permitted = list()
            
            self.when_enter = when_enter
            self.when_leave = when_leave

        def find_room_now(self):


            if store.main_background.is_daytime():

                return self.daytime_tag
            return self.nighttime_tag
    
    class FAERooms(object):

        def __init__(self, fae_sunup, fae_sundown):

            self.room = None
            self.decoration = dict()

            self.fae_sunup = datetime.time(fae_sunup)
            self.fae_sundown = datetime.time(fae_sundown)

            self.__is_seeing_day = self.is_daytime()

            self.day_to_night_switch = FAEEvent()

            self.night_to_day_switch = FAEEvent()
        
        def select_room(self, new_room, **kwargs):


            if new_room.when_enter is not None:

                new_room.when_enter(self.room, **kwargs)

            self.room = new_room
        
        def room_switcher(self, new_room, **kwargs):

            if self.room.when_leave is not None:

                self.room.when_leave(new_room, **kwargs)
            
            self.select_room(new_room, **kwargs)
        

        def is_daytime(self):

            return self.fae_sunup <= datetime.datetime.now().time() < self.fae_sundown
        
        def render(self, dissolve_all=False, complete_reset=False):

            renpy.with_statement(None)

            if complete_reset:
                renpy.scene()
                renpy.show("black")
            
            room = None

            if dissolve_all or complete_reset:
                room = self.room.find_room_now()
            
            if room is not None:
                renpy.show(room, tag="main_bg", zorder=FAE_ROOM_ZORDER)
            
            else:
                fae_utilities.log("Unable to draw room: no room image was found.")
            
            if dissolve_all or complete_reset:
                renpy.hide("black")
                renpy.with_statement(Dissolve(1.0))
            
            return
        
        def form(self):

            room = self.room.find_room_now()
            if room is not None:
                renpy.show(room, tag="main_bg", zorder=FAE_ROOM_ZORDER)
            
            else:
                fae_utilities.log("Unable to show room: no room image was found.")
            
            return
        
        def is_seeing_day(self):

            return self.__is_seeing_day
        
        def reset_checker(self):

            if self.is_daytime() and self.__is_seeing_day is False:
                self.__is_seeing_day = True
                self.form(dissolve_all=True)

                self.night_to_day_switch()
            
            elif not self.is_daytime() and self.__is_seeing_day is True:
                self.__is_seeing_day = False
                self.form(dissolve_all=True)

                self.day_to_night_switch()
        
        def save(self):

            persistent._present_room = self.room.id

init 0 python:

    main_background = FAERooms(
        fae_sunup=int(store.persistent.fae_sunup),
        fae_sundown=int(store.persistent.fae_sundown)
    )

    spaceroom = Rooms(
        id="spaceroom",
        image_directory="spaceroom"
    )

    bedroom = Rooms(
        id="bedroom",
        image_directory="bedroom"
    )
    

    main_background.select_room(spaceroom)

    if main_background.is_daytime():
        main_background.night_to_day_switch()
    
    else:
        main_background.day_to_night_switch()
    
    if persistent._present_room in fae_rooms.ROOM_DEFS:
        main_background.room_switcher(persistent._present_room)
