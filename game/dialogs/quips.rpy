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
        "What would you like to talk about, [player]?",
        "What are you thinking of?",
        "Is there something you'd like to talk about, [player]?",
        "Something on your mind?",
        "Something on your mind, [player]?",
        "Up to chat, [player]?",
        "Yes, [player]?",
        "What's on your mind, [player]?",
        "What's up, [player]?",
        "Ask away, [player].",
        "Don't be shy, [player]~",
        "I'm all ears, [player]~",
        "Of course we can talk, [player].",
    ]
    #save_quips(AFFECTIONATE, quips)

    ## ENAMORED quips
    enamoured_quips = [
        "What would you like to talk about? <3",
        "What would you like to talk about, [player]? <3",
        "What are you thinking of?",
        "Is there something you'd like to talk about, [player]?",
        "Something on your mind?",
        "Something on your mind, [player]?",
        "Up to chat, I see~",
        "Yes, [player]?",
        "What's on your mind, [player]?",
        "What's up, [player]?",
        "Ask away, [player]~",
        "I'm all ears, [player]~",
        "Of course we can talk, [player]~",
        "Take all the time you need, [player].",
        "We can talk about whatever you'd like, [player].",
    ]
    #save_quips(ENAMORED, quips)

    ## LOVE quips
    love_quips = [
        "What would you like to talk about? <3",
        "What would you like to talk about, [player]? <3",
        "What are you thinking of?",
        "Something on your mind?",
        "Something on your mind, [player]?",
        "Up to chat, I see~",
        "Yes, [player]?",
        "What's on your mind, [player]?",
        "<3",
        "What's up, [player]?",
        "Ask away, [player]~",
        "I'm all ears, [player]~",
        "We can talk about whatever you'd like, [player].",
        "Of course we can talk, [player]~",
        "Take all the time you need, [player]~",
        "I'm all yours, [player]~",
        "Oh? Something...{w=0.3}{i}important{/i} on your mind, [player]?~",
    ]
        #save_quips(LOVE, quips)


    def get_quip():

        affection_status = store.Affection._getAffectionTierName()

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




