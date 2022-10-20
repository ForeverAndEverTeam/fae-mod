#Credit to the JN team who wrote the original code this was based off


init python in chat_handler:
    import store

    standard_chat_defs = dict()

    CHAT_CODE_DEFS = {
        store.CHAT_GROUP_GREETING: store.fae_greetings.GREETING_DEFS,
        store.CHAT_GROUP_FAREWELL: store.fae_farewells.FAREWELL_DEFS,
        store.CHAT_GROUP_NORMAL: store.chats.CHAT_DEFS,
        store.CHAT_GROUP_EVENT: store.fae_events.EVENT_DEFS,
        store.CHAT_GROUP_REGRET: store.fae_regrets.REGRET_DEFS,
        store.CHAT_GROUP_FLATTER: store.fae_flatter.FLATTERY_DEFS,
        store.CHAT_GROUP_MOOD: store.fae_moods.MOOD_DEFS,
        #store.CHAT_GROUP_DEV: store.fae_dev_tools.DEV_DEFS
    }

init 6 python in chat_handler:

    ALL_CHAT_DEFS = dict()

    for chat_defs in CHAT_CODE_DEFS.values():
        ALL_CHAT_DEFS.update(chat_defs)

init 6 python:
    import random

    def get_chat(chat_label):
        """
        Gets dialogue by it's label
        
        chat_label - chat.label meaning the label of the dialogue we want

        RETURNS:
            Dialogue if a dialogue with the label exists
        
        """
        return store.chat_handler.ALL_CHAT_DEFS.get(chat_label, None)

#####################################
# DEFINING CLASSES AND FUNCTIONS HERE
#####################################

#SOME PERSISTENT STUFF FIRST

default persistent._event_list = list()

init -3 python:

    from collections import OrderedDict
    import datetime
    from Enum import Enum
    import re
    import store.fae_affection as fae_affection
    import store.fae_utilities as fae_utilities
    import webbrowser



    #Constants for types. Add more here if we need more organizational areas
    CHAT_GROUP_FAREWELL = "FAREWELL"
    CHAT_GROUP_GREETING = "GREETING"
    CHAT_GROUP_NORMAL = "NORMAL"
    CHAT_GROUP_EVENT = "EVENT"
    CHAT_GROUP_REGRET = "REGRET"
    CHAT_GROUP_FLATTER = "FLATTER"
    CHAT_GROUP_MOOD = "MOOD"
    #CHAT_GROUP_DEV = "DEV"

    #LOCKED BASE MAP
    clm = {
        #STUFF WHICH SHOULDN"T CHANGE
        "conditional": True,
        "unlocked": True,
        "random": True,
        "seen_no": True,
        "latest_seen": True,
        
        #THINGS WHICH CAN CHANGE
        "label": False,
        "category": False,
        "prompt": False,
        "affection_range": False,
        "extra_props": False
    }

    class Chat(object):
        """
        Chat manager
        
        persistent_db - since we save topics seen to the persistent_db
        
        label - the label used
        
        prompt - for the "repeat topics" thingy
        
        contional - yes (insert requirements here)
        
        random - whether it's random (duh)
        """

        def __init__(
            self,
            persistent_db,
            label,
            prompt="",
            conditional=None,
            category=None,
            unlocked=False,
            random=False,
            affection_range=None,
            extra_props=None
        ):
            """
            Chat Handler
            
                persistent_db: Persistent dictionary.
                label - renpy label (as string) this topic corresponds to
                prompt - The text show in the "Tell me again about, or Hey, Sayori..." menus (Defaults to empty)
                conditional - condition under which this topic should be allowed to be shown
                    (Default: None)
                category - list of strings representing categories to group this topic under. If None, an empty list is assigned
                    (Default: None)
                unlocked - whether or not this topic is displayed to the user in menus

                affection_range - Specify the range of affection Sayori needs to be at before the topic can be seen.
                    No value(False) results in the topic being seen at all affection stages.
                
                random - do I really need to explain this?

                extra_props - dictionary representing additional properties which don't directly affect the topic itself. If None, an empty dict is assigned
                    (Default: None)
            """
            if not isinstance(persistent_db, dict):
                raise Exception("Persistent database provided is not of type dict")
            
            self.__persistent_db = persistent_db

            if not renpy.has_label(label):
                raise Exception("Label {0} does not exist.".format(label))
            

            if not fae_affection._checkAffectionRange(affection_range):
                raise Exception("Affection range: {0} is invalid.".format(affection_range))
            
            #STUFF WHICH SHOULDN'T CHANGE FROM PERSISTENT DATA
            self.label = label
            self.conditional = conditional
            self.unlocked = unlocked
            self.random = random
            self.affection_range = affection_range
            #SOME EXTRA PROPERTIES
            self.seen_no = 0
            self.latest_seen = None
            
            #IF IT'S THERE, WE LOAD IT
            if label in persistent_db:
                self.__load()

            if category is None:
                category = list()
            
            self.category = category

            self.prompt = prompt

            if extra_props is None:
                extra_props = list()

            self.extra_props = extra_props

            #ADD IT ALL BACK TO PERSISTENT DATA
            
            persistent_db[label] = dict()
            self.__save()

        def __eq__(self, other):
            """
            Equals override for the Chat class
            Checks if the labels are equivalent, as otherwise, loading data should be from the same persistent key
            other: Thing to compare
            
            True if the labels haven't changed, otherwise False
            """

            if isinstance(other, Chat):
                return self.label == other.label
            return False

        def __repr__(self):
            """
            repr override
            """
            return "<Chat object (label '{0}' at {1})>".format(self.label, hex(id(self)))
        
        def as_dict(self):
            """
            Dictionary rep of the chat class without the database thing
            """
            return {
                key:value
                for key, value in self.__dict__.items()
                if key != "_m1_handler__persistent_db"
            }

        def conditional_checker(self):
            """
            Checks a dialogue's conditionals
            """

            if self.conditional is not None:
                try:
                    return eval(self.conditional, globals=store.__dict__)
                
                except Exception as e:
                    store.fae_utilities.log("Error evaluating conditional on topic '{0}'. {1}".format(self.label, e.message), fae_utilities.SEVERITY_ERR)
                    return False
            
            return True
        
        def now_affection_in_affection_range(self, affection_status=None):

            if not affection_status:
                affection_status = fae_affection._getAffectionStatus()
            
            return fae_affection._AffectionStateInRange(affection_status, self.affection_range)
        
        def __load(self):
            """
            Load the chat stuff
            """
            
            for persist_key, value in self.__persistent_db[self.label].items():
                if clm[persist_key]:
                    self.__dict__[persist_key] = value
        
        def __save(self):
            """
            Save dialogue to persistent
            """
            for persist_key, value in self.as_dict().items():
                if clm[persist_key]:
                    self.__persistent_db[self.label][persist_key] = value
        
        @staticmethod
        def _save_chat_data():
            """
            Saves all topics
            """
            for chat in store.chat_handler.ALL_CHAT_DEFS.values():
                chat.__save()

        def hapwv(self, prop_key, prop_val):
            """
            Returns whether this topic has a given additional_attribute key with
            the supplied value
            True if the property exists and matches the given value, otherwise False, raises an Exception if missing/undefined
            """

            if prop_key not in self.extra_props:
                return False
            return self.extra_props[prop_key] is prop_val

        def derandom(self):
            """
            Makes a topic unable to be brought up randomly.
            Makes it available through talk menu
            """

            self.random = False

        def _chat_filt(
            self,
            unlocked=None,
            random=None,
            has_seen=None,
            affection=None,
            seen_no=None,
            in_categories=list(),
            no_categories=list(),
            extra_props=list()
        ):
            """
            Filters this chat accordng to specificatiosn
            Should this topic be unlocked?
            Should this topic be seen?
            in_categories: A list of cats, all of which this topic MUST have
            no_categories: A list of cats, none of which this topic should have
            extra_props: A list of additional properties
                If tuple, the first item is the key, the second is the expected value. If just string, only presence is validated
            Returns a boolean - True if all valid, False otherwise
            """
            if unlocked is not None and unlocked != self.unlocked:
                return False

            if random is not None and random != self.random:
                return False
            
            if has_seen is not None and renpy.seen_label(self.label) != has_seen:
                return False
            
            if affection and not self.now_affection_in_affection_range(affection):
                return False
            
            if not self.conditional_checker():
                return False
            
            if seen_no is not None and self.seen_no == seen_no:
                return False


            if in_categories and len(set(in_categories).intersection(set(self.category))) != len(in_categories):
                return False

            if no_categories and self.category and len(set(no_categories).intersection(set(self.category))) > 0:
                return False
            
            if extra_props:
                for extra_prop in extra_props:
                    #KEY VALUE CHECKER
                    if isinstance(extra_prop, tuple):
                        if not self.hapwv(*extra_prop):
                            return False
                    
                    #JUST KEY STUFF
                    else:
                        if extra_prop not in self.extra_props:
                            return False
            
            
            #ALL CHECKS PASSED
            return True


        @staticmethod
        def chat_filt(
            chat_list,
            unlocked=None,
            random=None,
            has_seen=None,
            affection=None,
            seen_no=None,
            in_categories=list(),
            no_categories=list(),
            extra_props=list()
        ):
            """
            Filters this chat accordng to conditions
            chat_list - List of topics to filter down
            See _chat_filt for the rest of the properties
            Returns a list of topics matching the filter criteria
            """

            return [
                _chat
                for _chat in chat_list
                if _chat._chat_filt(
                    unlocked,
                    random,
                    has_seen,
                    affection,
                    seen_no,
                    in_categories,
                    no_categories,
                    extra_props
                )
            ]
    
    #MAIN FUNCTIONS THAT WE USE A FUCK-TON

    def chatReg(Chat, chat_group=CHAT_GROUP_NORMAL):
        """
        Registers a topic to the defs to allow it to be picked from the topic "pool"
        IN:
            Chat - Chat class representing the topic to be added
            chat_group - group to map this topic to
                (Defaults to CHAT_GROUP_NORMAL (not an event/greeting/farewell etc)
        NOTE: Must be used at init 5
        """
        local_defs = store.chat_handler.CHAT_CODE_DEFS.get(chat_group)

        if local_defs is None:
            raise Exception("Chat type '{0}' is not registered.")
        
        elif not isinstance(local_defs, dict):
            raise Exception("Chat defs for type '{0}' is not a dict.")
        
        local_defs[Chat.label] = Chat

    def ats(chat_label):
        """
        Adds a dialogue to the queue at position 1
        
        chat_label - topic label you want to force push
        """
        persistent._event_list.insert(0, chat_label)

    def atq(chat_label):
        """
        Adds a dialogue to the queue
        chat_label - topic label of the dialogue you wish to queue
        """
        persistent._event_list.append(chat_label)

    def ciel(chat_label):
        """
        Returns whether or not a topic is in the event list
        chat_label - Chat label of the topic you wish to check
        Returns boolean - True if the topic is in the event list, False otherwise
        """

        return chat_label in persistent._event_list

    
    def cielp(chat_pattern):
        """
        Returns whether or not a topic is in the event list
        
        chat_pattern - Pattern to match against the topic labels
        
        Returns boolean - True if the topic is in the event list, False otherwise
        """

        return any(
            re.match(chat_pattern, chat_label)
            for chat_label in persistent._event_list
        )



    def rcofel(chat_label):
        """
        Removes a single occurrence of a topic from the event list
        IN:
            chat_label - label of the topic you wish to remove
        """
        if chat_label in persistent._event_list:
            persistent._event_list.remove(chat_label)

    def rcfel(chat_label):
        """
        Removes all occurrences of a topic from the event list
        IN:
            chat_label - label of the topic you wish to remove
        """

        persistent._event_list = [
            _chat_label
            for _chat_label in persistent._event_list
            if _chat_label != chat_label
        ]
    def rcfelp(chat_label_pattern):
        """
        Removes all occurrences of a topic from the event list
        IN:
            chat_label_pattern - regex identifier of the topic you wish to remove
        """
        persistent._event_list = [
            _chat_label
            for _chat_label in persistent._event_list
            if not re.match(chat_label_pattern, _chat_label)
        ]

    def makelist(menu_entries, additional_chats):
        """
        Returns a list of items ready for a menu
        IN:
            menu_entries - List<Topic> of topics
            additional_chats - optional, array of tuples
                syntax: [("prompt1", "label2"), ("prompt2", "label2"), ...]
        OUT:
            array of tuples usable by menu()
        """

        menu_parts = []
        for chat in menu_entries:
            menu_parts.append((chat.prompt, chat.label))

        for chat in additional_chats:
            menu_parts.append(chat)
        return menu_parts.sort()

    def makedict(menu_entries):
        """
        Builds a dict of items ready for use in a categorized menu
        IN:
            menu_entries - A List<Topic> of topics to populate the menu
        OUT:
            Dictionary<string, List<string>> representing a dict of category: [ ...prompts ]
        """
        
        # Get the topic categories that the given topics share, and order them

        chat_categories = []

        for chat in menu_entries:
            for category in chat.category:
                if category not in chat_categories:
                    chat_categories.append(category)
        chat_categories.sort()

        # Make an ordered dictionary, this will retain the order of what we return for the menu items
        omi = OrderedDict()
        for chat_category in chat_categories:
            omi[chat_category] = []

        #Send the dialogues into the ordered dictionary.
        #NOTE: EACH DIALOGUE CAN HAVE MULTIPLE CATEGORIES
        for chat in menu_entries:
            for category in chat.category:
                omi[category].append(chat)
        
        return omi




