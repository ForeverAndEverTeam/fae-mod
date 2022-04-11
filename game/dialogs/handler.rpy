init python in chat_handler:
    import store

    standard_chat_defs = dict()

    CHAT_CODE_DEFS = {
        store.CHAT_GROUP_GREETING: store.greetings.GREETING_DEFS,
        store.CHAT_GROUP_FAREWELL: store.farewells.FAREWELL_DEFS,
        store.CHAT_GROUP_NORMAL: store.chats.CHAT_DEFS,
        store.CHAT_GROUP_EVENT: store.sayo_events.EVENT_DEFS
    }

init 6 python in chat_handler:

    ALL_CHAT_DEFS = dict()

    for chat_defs in CHAT_CODE_DEFS.itervalues():
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
    import re
    import store.sayo_utilities as sayo_utilities


    class Holidays():
        none = 1
        nyd = 2
        easter = 3
        halloween = 4
        ce = 5
        cd = 6
        nye = 7

        def __str__(self):
            return self.name
        


    #Constants for types. Add more here if we need more organizational areas
    CHAT_GROUP_FAREWELL = "FAREWELL"
    CHAT_GROUP_GREETING = "GREETING"
    CHAT_GROUP_NORMAL = "NORMAL"
    CHAT_GROUP_EVENT = "EVENT"

    #LOCKED BASE MAP
    clm = {
        #STUFF WHICH SHOULDN"T CHANGE
        "conditional": True,
        "unlocked": True,
        "seen_no": True,
        "latest_seen": True,
        
        #THINGS WHICH CAN CHANGE
        "label": False,
        "category": False,
        "prompt": False,
        "additional_properties": False
    }

    class Chat(object):
        """
        Chat class. Manages all topics
        PROPERTIES:
            - label: renpy label this topic corresponds to
            - prompt: prompt for this topic in menus
            - category: how to categorize this topic
            - unlocked: whether we show this topic to the user in menus or not
            - additional_properties: extra properties which don't directly affect the topic
        """

        def __init__(
            self,
            persistent_db,
            label,
            prompt="",
            conditional=None,
            category=None,
            unlocked=False,
            additional_properties=None
        ):
            """
            Topic constructor
            IN:
                persistent_db - persistent dict reference to store the topic data in
                label - renpy label (as string) this topic corresponds to
                prompt - string representing the prompt to use for this topic in menus
                    (Default: '')
                conditional - condition under which this topic should be allowed to be shown
                    (Default: None)
                category - list of strings representing categories to group this topic under. If None, an empty list is assigned
                    (Default: None)
                unlocked - whether or not this topic is displayed to the user in menus

                additional_properties - dictionary representing additional properties which don't directly affect the topic itself. If None, an empty dict is assigned
                    (Default: None)
            """
            if not isinstance(persistent_db, dict):
                raise Exception("Persistent database provided is not of type dict")
            
            self.__persistent_db = persistent_db

            if not renpy.has_label(label):
                raise Exception("Label {0} does not exist.".format(label))
            
            #STUFF WHICH SHOULDN'T CHANGE FROM PERSISTENT DATA
            self.label = label
            self.conditional = conditional
            self.unlocked = unlocked


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

            if additional_properties is None:
                additional_properties = list()

            self.additional_properties = additional_properties

            #ADD IT ALL BACK TO PERSISTENT DATA

            persistent_db[label] = dict()
            self.__save()

        def __eq__(self, other):
            """
            Equals override for the Chat class
            Checks if the labels are equivalent, as otherwise, loading data should be from the same persistent key
            IN:
                other - comparitor
            OUT:
                boolean:
                    - True if the dialogue labels are the same
                    - False otherwise
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
            Exports a dict representation of the data to be persisted
            OUT:
                dictionary representation of the topic object (excluding the persistent_db property)
            """
            return {
                key:value
                for key, value in self.__dict__.iteritems()
                if key != "_m1_handler__persistent_db"
            }

        def conditional_checker(self):
            """
            Checks a dialogue's conditionals
            """

            if self.conditional is not None:
                try:
                    return eval(self.condtional, globals=store.__dict__)
                
                except Exception as e:
                    return False
            
            return True
        
        def __load(self):
            """
            Load the chat stuff
            """
            
            for persistent_key, value in self.__persistent_db[self.label].iteritems():
                if clm[persistent_key]:
                    self.__dict__[persistent_key] = value
        
        def __save(self):
            """
            Save dialogue to persistent
            """
            for persistent_key, value in self.as_dict().iteritems():
                if clm[persistent_key]:
                    self.__persistent_db[self.label][persistent_key] = value
        
        @staticmethod
        def _std():
            """
            Saves all topics
            """
            for chat in store.chat_handler.ALL_CHAT_DEFS.itervalues():
                chat.__save()

        def hapwv(self, prop_key, prop_val):
            """
            Returns whether this topic has a given additional_attribute key with
            the supplied value
            IN:
                self - Reference to this topic
                property_key - The key under additional_properties to test against
                property_value - The value to test the value under the property_key
            OUT:
                True if the property exists and matches the given value, otherwise False, or raises an Exception if missing/undefined
            """

            if prop_key not in self.additional_properties:
                return False
            return self.additional_properties[prop_key] is prop_val

            

        def _chat_filt(
            self,
            unlocked=None,
            has_seen=None,
            seen_no=None,
            in_categories=list(),
            no_categories=list(),
            additional_properties=list()
        ):
            """
            Filters this topic accordng to conditions
            IN:
                unlocked - boolean: Whether or not this topic is unlocked
                is_seen - boolean: Whether or not this topic should be seen
                includes_categories - list: A list of categories, all of which this topic MUST have
                excludes_categories - list: A list of categories, none of which this topic should have
                additional_properties - list: A list of additional properties, can be either string or tuple
                    If tuple, the first item is the key, the second is the expected value. If just string, only presence is validated
                NOTE: If these values are None or empty, checks on them are not performed.
            OUT:
                boolean - True if all checks pass, False otherwise
            """
            if unlocked is not None and unlocked != self.unlocked:
                return False
            
            if has_seen is not None and renpy.seen_label(self.label) != has_seen:
                return False
            
            if not self.conditional_checker():
                return False
            
            if seen_no is not None and self.seen_no == seen_no:
                return False


            if in_categories and len(set(in_categories).intersection(set(self.category))) != len(in_categories):
                return False

            if no_categories and self.category and len(set(no_categories).intersection(set(self.category))) > 0:
                return False
            
            if additional_properties:
                for additional_prop in additional_properties:
                    #KEY VALUE CHECKER
                    if isinstance(additional_prop, tuple):
                        if not self.hapwv(*additional_prop):
                            return False
                    
                    #JUST KEY STUFF
                    else:
                        if additional_prop not in self.additional_properties:
                            return False
            
            
            #ALL CHECKS PASSED
            return True


        @staticmethod
        def chat_filt(
            chat_list,
            unlocked=None,
            has_seen=None,
            seen_no=None,
            in_categories=list(),
            no_categories=list(),
            additional_properties=list()
        ):
            """
            Filters this chat accordng to conditions
            IN:
                chat_list - List of topics to filter down
                See _chat_filt for the rest of the properties
                NOTE: If these values are None or empty, checks on them are not performed.
            OUT:
                List of topics matching the filter criteria
            """

            return [
                _chat
                for _chat in chat_list
                if _chat._chat_filt(
                    unlocked,
                    has_seen,
                    seen_no,
                    in_categories,
                    no_categories,
                    additional_properties
                )
            ]
    
    #MAIN FUNCTIONS THAT WE USE A FUCK-TON

    def Chatreg(Chat, chat_group=CHAT_GROUP_NORMAL):
        """
        Registers a topic to the defs to allow it to be picked from the topic "pool"
        IN:
            Chat - Topic object representing the topic to be added
            chat_group - group to map this topic to
                (Default: CHAT_GROUP_NORMAL (in other words, a standard topic, not greeting/farewell/special))
        NOTE: Should be used at init 5
        """
        local_defs = store.chat_handler.CHAT_CODE_DEFS.get(chat_group)

        if local_defs is None:
            raise Exception("Chat type '{0}' is not registered.")
        
        elif not isinstance(local_defs, dict):
            raise Exception("Chat defs for type '{0}' is not a dict.")
        
        local_defs[Chat.label] = Chat

    def ats(chat_label):
        """
        Adds a dialogue to the stack
        IN:
            chat_label - Chat.label of the dialogue you want to push
        """
        persistent._event_list.insert(0, chat_label)

    def atq(chat_label):
        """
        Adds a dialogue to the queue
        IN:
            chat_label - Chat.label of the dialogue you wish to queue
        """
        persistent._event_list.append(chat_label)

    def ciel(chat_label):
        """
        Returns whether or not a topic is in the event list
        IN:
            chat_label - Chat.label of the topic you wish to check
        OUT:
            boolean - True if the topic is in the event list, False otherwise
        """

        return chat_label in persistent._event_list

    
    def cielp(chat_pattern):
        """
        Returns whether or not a topic is in the event list
        IN:
            chat_pattern - Pattern to match against the topic labels
        OUT:
            boolean - True if the topic is in the event list, False otherwise
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

    def makelist(menu_chat, additional_chats):
        """
        Returns a list of items ready for a menu
        IN:
            chat_topics - List<Topic> of topics
            additional_chats - optional, array of tuples
                syntax: [("prompt1", "label2"), ("prompt2", "label2"), ...]
        OUT:
            array of tuples usable by menu()
        """

        menu_entries = []
        for chat in menu_chat:
            menu_entries.append((chat.prompt, chat.label))

        for chat in additional_chats:
            menu_entries.append(chat)
        return menu_entries.sort()

    def makedict(menu_chat):
        """
        Builds a dict of items ready for use in a categorized menu
        IN:
            menu_chat - A List<Topic> of topics to populate the menu
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
        for chat in menu_chat:
            for category in chat.category:
                omi[category].append(chat)
        
        return omi


init -999 python in sayo_utilities:
    import datetime
    import hashlib
    import os
    import store
    import pygame

    __KEY_HASH = "5420cfc14ddb171df60c55cfea8d5beb39543f0696a4fe34c396bfe0e23a5bc9"


init python in sayo_utilities:
    import re
    import store
    #import store.sayo_globals as sayo_globals
    # Key setup
    key_path = os.path.join(renpy.config.basedir, "game/dev/key.txt").replace("\\", "/")
    if not os.path.exists(key_path):
        __KEY_VALID = False

    else:
        with open(name=key_path, mode="r") as key_file:
            __KEY_VALID = hashlib.sha256(key_file.read().encode("utf-8")).hexdigest() == __KEY_HASH

    def get_key_valid():
        """
        Returns the validation state of the key.
        """
        return __KEY_VALID

    def save_game():
        """
        Saves all game data.
        """
        #Save topic data
        store.Chat._save_topic_data()



