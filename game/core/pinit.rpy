label prompts:
    hide screen overlay

    menu:
        s "Let's talk about..."

        "Let's talk about...":
            call screen pinit

        "Tell me again about...":
            call screen topic_rep

        "I love you, Sayori!":
            if persistent.ily == 0:
                call first_love
            else:
                call ily_response
        "Never mind.":
            jump main_idle
        
#screen pinit():
    #LIST OF ALL PLAYER-INITIATED TOPICS
    # SIMILAR TO THE "ASK A QUESTION" OF OLD
#    return



#screen topic_rep():
    #TODO: DISPLAY A LIST OF ALL SEEN AND REPEATABLE TOPICS HERE
#    return