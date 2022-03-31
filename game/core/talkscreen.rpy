
label talk_menu:
    hide screen overlay
    menu:
        s "Let's talk!"

        "Let's talk about...":
            call pinit
        "Tell me again about...":
            call pinitrep
        "I love you, Sayori!":
            if persistent.ily == 0:
                call first_love
            else:
                call ily_response
        "I have to go":
            call fae_quit
        "Never mind.":
            
            show screen overlay
        
label pinit:
    #TODO: ADD TOPIC PASSING
    call screen talk

screen talk():

    style_prefix "choice"

    vbox:
        xpos 1.0
#        xalign 0.05
        yanchor 1.0
        ypos 715
#        yalign 0.95

        #textbutton _("Nevermind") action Return(None)

        
