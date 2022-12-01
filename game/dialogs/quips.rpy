init 15 python in fae_quips:

    import store
    import random

    persistent = renpy.game.persistent
    layout = store.layout

    quips = [
        "What would you like to talk about?",
        "What are you thinking of?",
        "Is there something you'd like to talk about?",
        "Something on your mind?",
        "Yes, [player]?",
    ]
    #save_quips(NORMAL, quips)

    ## HAPPY quips
    happy_quips = [
        "What would you like to talk about?",
        "What are you thinking of?",
        "Is there something you'd like to talk about?",
        "Something on your mind?",
        "Up to chat, [player]?",
        "Yes, [player]?",
        "What's on your mind, [player]?",
        "What's up, [player]?",
        "Ask away, [player].",
        "Don't be shy, [player].",
    ]
    #save_quips(HAPPY, quips)

    ## AFFECTIONATE quips
    aff_quips = [
        "What would you like to talk about?",
        "What would you like to talk about, [fae_get_player_nickname()]?",
        "What are you thinking of?",
        "Is there something you'd like to talk about, [fae_get_player_nickname()]?",
        "Something on your mind?",
        "Something on your mind, [fae_get_player_nickname()]?",
        "Up to chat, [fae_get_player_nickname()]?",
        "Yes, [fae_get_player_nickname()]?",
        "What's on your mind, [fae_get_player_nickname()]?",
        "What's up, [fae_get_player_nickname()]?",
        "Ask away, [fae_get_player_nickname()].",
        "Don't be shy, [fae_get_player_nickname()]~",
        "I'm all ears, [fae_get_player_nickname()]~",
        "Of course we can talk, [fae_get_player_nickname()].",
    ]
    #save_quips(AFFECTIONATE, quips)

    ## ENAMORED quips
    enamoured_quips = [
        "What would you like to talk about? <3",
        "What would you like to talk about, [fae_get_player_nickname()]? <3",
        "What are you thinking of?",
        "Is there something you'd like to talk about, [fae_get_player_nickname()]?",
        "Something on your mind?",
        "Something on your mind, [fae_get_player_nickname()]?",
        "Up to chat, I see~",
        "Yes, [fae_get_player_nickname()]?",
        "What's on your mind, [fae_get_player_nickname()]?",
        "What's up, [player]?",
        "Ask away, [fae_get_player_nickname()]~",
        "I'm all ears, [fae_get_player_nickname()]~",
        "Of course we can talk, [fae_get_player_nickname()]~",
        "Take all the time you need, [player].",
        "We can talk about whatever you'd like, [fae_get_player_nickname()].",
    ]
    #save_quips(ENAMORED, quips)

    ## LOVE quips
    love_quips = [
        "What would you like to talk about? <3",
        "What would you like to talk about, [fae_get_player_nickname()]? <3",
        "What are you thinking of?",
        "Something on your mind?",
        "Something on your mind, [fae_get_player_nickname()]?",
        "Up to chat, I see~",
        "Yes, [fae_get_player_nickname()]?",
        "What's on your mind, [fae_get_player_nickname()]?",
        "<3",
        "What's up, [fae_get_player_nickname()]?",
        "Ask away, [fae_get_player_nickname()]~",
        "I'm all ears, [fae_get_player_nickname()]~",
        "We can talk about whatever you'd like, [fae_get_player_nickname()].",
        "Of course we can talk, [fae_get_player_nickname()]~",
        "Take all the time you need, [fae_get_player_nickname()]~",
        "I'm all yours, [fae_get_player_nickname()]~",
        "Oh? Something...{w=0.3}{i}important{/i} on your mind, [fae_get_player_nickname()]?~",
    ]
        #save_quips(LOVE, quips)


    def get_quip():

        affection_status = store.Affection._getAffinityTierName()

        if affection_status == "NORMAL":
            return random.choice(quips)

        elif affection_status == "HAPPY":
            return random.choice(happy_quips)
        
        elif affection_status == "AFFECTIONATE":
            return random.choice(aff_quips)
        
        elif affection_status == "ENAMORED":
            return random.choice(enamoured_quips)

        elif affection_status == "LOVE":
            return random.choice(love_quips)

        else:
            return random.choice(quips)




