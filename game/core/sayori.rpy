init 0 python:
    import store.fae_outfits as fae_outfits


    class Sayori(object):

        __pic = False

        __iig = False

        _outfit = None

        @staticmethod
        def findOutfitName():

            return Sayori._outfit.reference_name


        @staticmethod
        def setOutfit(outfit):

            Sayori._outfit = outfit
            store.persistent.fae_outfit_quit = Sayori._outfit.reference_name
        
        @staticmethod
        def isWearingOutfit(reference_name):

            return Sayori._outfit.reference_name == reference_name
        

        @staticmethod
        def isWearingClothes(reference_name):

            return Sayori._outfit.clothes.reference_name == reference_name
        

        @staticmethod
        def isWearingHairstyle(reference_name):

            return Sayori._outfit.hairstyle.reference_name == reference_name
        

        @staticmethod
        def isWearingAccessory(reference_name):

            return Sayori._outfit.accessory.reference_name == reference_name


        @staticmethod
        def isWearingEyewear(reference_name):
            
            return Sayori._outfit.eyewear.reference_name == reference_name
        

        @staticmethod
        def isWearingHeadgear(reference_name):

            return Sayori._outfit.headgear.reference_name == reference_name
        
        @staticmethod
        def setInChat(p_i_c):
            """
            Sets Sayori state as in action with player.
            Disables hotkeys
            FEED:
                p_i_c = boolean value set to True
            """

            if not isinstance(p_i_c, bool):
                raise TypeError("p_i_c must be boolean")
            
            Sayori.__pic = p_i_c
        
        @staticmethod
        def setInGame(i_i_g):
            """
            Same as setInChat, but with games instead

            FEED:
                i_i_g = boolean value set to True
            """

            if not isinstance(i_i_g, bool):
                raise TypeError("i_i_g must be boolean")
            
            Sayori.__iig = i_i_g
        
        @staticmethod
        def isInChat():
            """
            Checks whether Sayori is in a topic, or interaction
            Hotkeys disabled

            RESULT:
                If in action, True, else False
            """
            return Sayori.__pic

        @staticmethod
        def isInGame():
            """
            Same as isInChat, but for games

            RESULT:
                If in game: True, False if now
            """
            return Sayori.__iig

        @staticmethod
        def add_new_regret_awaiting(regret_type):

            if not isinstance(regret_type, int) and not isinstance(regret_type, fae_regrets.RegretTypes):
                raise TypeError("regret_type must be of types int of fae_regrets.RegretTypes")
            
            if not int(regret_type) in store.persistent._fae_player_awaiting_apologies:
                store.persistent._fae_player_awaiting_apologies.append(int(regret_type))
        
        @staticmethod
        def add_regret_quit(regret_type):

            if not isinstance(regret_type, int) and not isinstance(regret_type, fae_regrets.RegretTypes):
                raise TypeError("regret_type must be of types int or fae_regrets.RegretTypes")
            
            store.persistent._fae_player_apology_type_on_quit = int(regret_type)
        
        @staticmethod
        def deleteRegret(regret_type):

            if not isinstance(regret_type, int) and not isinstance(regret_type, fae_regrets.RegretTypes):
                raise TypeError("regret_type must be of types int or fae_regrets.RegretTypes")
            
            if int(regret_type) in store.persistent._fae_player_awaiting_apologies:
                store.persistent._fae_player_awaiting_apologies.remove(int(regret_type))
        
        
