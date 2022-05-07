
init python:
    # This class defines the poems for the poem sharing mini-game.
    # Syntax:
    #   author - This variable contains the characters' name.
    #   title - This variable contains the title of the poem.
    #   text - This variable contains the poem lines for the poem.
    userplayer = renpy.substitute(persistent.playername)
    class Poem:
        def __init__(self, author="", title="", text="", d_day_poem=False):
            self.author = author.lower()
            self.title = title
            self.text = text
            self.d_day_poem = d_day_poem
        

    poem_d_day = Poem(
        author = "sayori",
        d_day_poem=True,
        title = "The Life of a Hopeless Romantic",
        text = """\

Every second, and everyday, no matter what I do, 
You cross my mind like the rays of the sun, when I'm down and blue. 
When I'm sad I think of you. 
And when you're sad you do too. 

It's clear that we both care for each other. 
But then you tore my heart unlike any other. 
I know you'll never look at me, the way I look at you, 
But why tear my heart like it meant nothing to you? 

I know I should I should stop running towards the sun, hoping to get closer. 
I know I should stop reaching for the stars, thinking I would be noticed. 
And I know should stop chasing you, and start anew. 
But why would I ever want to lose you? 

You tear my heart like paper, bound to break. 
But also put me back together, even when it seems so bleak. 
I don't know why I choose to love you. 
But I also don't know why I shouldn't. 

For you are my sun, but I am merely just the moon chasing you. 
But never growing near. The way I feel about you will never become clear, 
And its unhealthy to chase something that wont ever grow near. 
But that's when one thing becomes clear. 

If I love you so much, I need let you go. 
And let you love another even if you mean so much to me. 
Until our stars ever align, there will always be a place in my heart, 
Waiting until you'd think of me as anything more."""
    )


    poem_v_day = Poem(
        author = "sayori",
        title = "Hope",
        text = """\
A poem for you. 
A poem for me. 
The world is quiet, 
Even the noise from the sea. 


A friend, becomes a lover. 
A lover becomes a bride. 
Prevents each from drowning. 
From being pulled by the tide. 


When the world is dark, 
The light is gone 
Everything is fear. 
I will forever always have hope. 

Whenever you are near."""
    )

image d_day_paper = "mod_assets/poem/d_day.png"



image paper = "images/bg/poem.jpg"

transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="d_day_paper"):
    style_prefix "poem"

    vbox:
        add paper

    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True

        has vbox
        null height 40
    
        if currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        null height 100

    vbar value YScrollValue(viewport="vp") style "poem_vbar"

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style poem_vbox:
    xalign 0.5

# This style controls the viewport of the poem lines to add scrolling for
# larger poems.
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280

# This style controls the position of the poem vertical box.
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return

    play sound page_turn

    if music:
        # This variable grabs the current position of the music playing.
        #$ currentpos = get_pos()
        # This if/else statement declares a variable that plays the given characters'
        # version of Okay Everyone.
        #if track:
        #    $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
        #else:
        #    $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"

        # These variables stop the normal Okay Everyone track and plays the characters'
        # version of the track instead.
        stop music fadeout 2.0
        #$ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)

    # These variables hide the textbox and stops auto-forward.
    window hide
    $ renpy.game.preferences.afm_enable = False

    # This if/else statement determines whether to show a alternative poem paper
    # if it is declared in the label statement.
    if paper:
        if d_day_poem:
            show screen poem(poem, paper=d_day_paper)
        else:
            show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)

    # This statement determines if this is the player's first poem to show a
    # tutorial to dismiss the poem.
    if not persistent.first_poem:
        $ persistent.first_poem = True
        $ renpy.save_persistent()
        show expression "gui/poem_dismiss.png" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)

    $ pause()

    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto

    # This if statement reverts the music back to normal if declared.
    #if music and revert_music:
    #    $ currentpos = get_pos(channel="music_poem")
    #    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    #    stop music_poem fadeout 2.0
    #    $ renpy.music.play(audio.t5c, fadein=2.0)
    return
