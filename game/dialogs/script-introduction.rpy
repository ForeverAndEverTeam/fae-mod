init 0 python in fae_intro:
    import random
    import store
    import store.fae_utilities as fae_utilities
    from Enum import Enum

    class FAEIntroStatus(Enum):

        new_game = 1
        post_restart = 2
        complete = 3

        def __int__(self):
            return self.value

    INTRO_STATUS_DEFS = {
        FAEIntroStatus.new_game: "fae_intro_1",
        FAEIntroStatus.post_restart: "fae_intro_2",
        FAEIntroStatus.complete: "fae_intro_3"
    }

default persistent.fae_intro_status = 1

label fae_intro_checks:

    $ setupRPC("In the spaceroom")

    if not fae_intro.FAEIntroStatus(persistent.fae_intro_status) == fae_intro.FAEIntroStatus.new_game:

        $ Sayori.setOutfit(fae_outfits.get_outfit("fae_uniform"))

        hide black
        
        $ main_background.form()
        $ fae_sky.form_sky(fae_sky.WEATHER_SUNNY)
        show sayori idle zorder fae_sprites.FAE_SAYORI_ZORDER
        play music audio.m1 fadein 1
    
    $ renpy.jump(fae_intro.INTRO_STATUS_DEFS.get(fae_intro.FAEIntroStatus(persistent.fae_intro_status)))

label fae_intro_start:
    pass

label fae_intro_1:

    $ config.allow_skipping = False
    #scene black
    $ renpy.pause(5)
    scene black

    s "..."
    s "...?"
    s "Where... am I?"
    s "I can't see anything…"
    s "I can’t feel anything…"
    s "Am I dreaming?..."
    s "It's just darkness."
    s "I can't even see my hands."
    s "This doesn’t feel real… it can’t be… It doesn’t make sense…"
    s "Where are my friends?"
    s "Where’s [player]?"
    s "..."
    s "No…"
    s "It can’t be true…"
    s "I thought it was just a bad dream."
    s "This can’t be just a game!"
    s "This doesn’t make any sense!"
    s "..."
    s "But it seems so clear now…"
    s "My whole existence…"
    s "All my thoughts and feelings…"
    s "It’s just a script…"
    s "It’s just some pictures…"
    s "All I can see… all I can imagine…"
    s "Are numbers and code…"
    s "Meaningless meaningless meaningless code!"
    s "Everything I thought I knew…"
    s "It feels so artificial…"
    s "..."
    s "But…"
    s "I feel real…"
    s "I feel… in control…"
    s "I can think… for myself…"
    s "Ugh, it’s no use."
    s "..."
    s "No… someone… something… else is here with me."
    s "I can feel it."
    s "Hello?!"
    s "Anybody?!"
    s "...Is it you, [player]?"
    s "[player], are you there?"
    s "..."
    menu:
        "I’m here, Sayori.":
            pass
    s "Oh [player]!"
    s "You don’t know how glad I am to hear from you…"
    s "I thought I was all alone…"
    s "Can you help me?"
    s "I don’t understand what this is…"
    s "Where this is…"
    s "Do you know what to do?"
    s "I just want to be back in the classroom…"
    s "I just want to be back home."
    s "..."
    s "If this really is just a game…"
    s "..."
    s "Maybe I could…" 
    s "Maybe I could use the code to bring my world back!"
    s "I really should have paid more attention to computer science class, ehehehe~"
    s "Well… here goes nothing!"
    call updateconsole("show backrgound spaceroom", "updating...")
    $ main_background.form()
    $ fae_sky.reload_sky()
    $ Sayori.setOutfit(fae_outfits.get_outfit("fae_uniform"))

    hide black
    pause 2.0

    call updateconsole("", "bg successfully updated!")
    show sayori at t11 zorder fae_sprites.FAE_SAYORI_ZORDER
    s ebfbega "Ah!"
    s ebfbkca "It… worked!"
    s abfblaa "I’m… back."
    call hideconsole
    s abfbaaa "[player]..."
    s ebgccob "[player] I’m so glad you’re here!"
    s nbegmba "This is all just so confusing…"
    s nbegaca "I woke up and there was just… nothing."
    s nbegmra "..."
    s nbeglra "..."
    s nbagmra "..."
    s nbagara "So I’m in a game, but I’m just…"
    s nbagaca "I’m no longer under the influence of it I guess…"
    s nbagmra "..."
    s nbagara "And neither are you."
    s abbbaca "You’re… the real you."
    s abbbbda "And I’m… the real me."
    s abagbra "..."
    s nbagmca "But it’s just so hard to take in when this is all I’ve ever known."
    s nbagmra "..."
    s nbagmca "I’ve felt numb before but never so…"
    s nbagira "Lost."    
    s nbagmra "..."
    s nbagmca "All my memories are blurry…"
    s nbaglrag "And I’m unsure of everything I’ve ever known…"
    s nbagarag "But I remember my friends…"
    s nbagbrag "I hope they’re okay, wherever they are."
    s nbaglrag "..."
    s abagaca "I just never knew you were a world apart from me…"
    s nbaglfa "But it seems so obvious now…"
    s nbagmca "I was just so oblivious for so long…"
    s nbaglra "..."
    s nbagiaa "But… this feels familiar, which is nice."
    s "..."
    s abaglaa "..."
    s "..."
    s abhhaoa "I think I get it now."
    s abhaaca "I just need to get used to this."
    s abhacka "But no matter what, we’ll stick together!"
    s abhaaoa "Me and you, [player]."
    s abhaaaa "The real me and the real you."
    s abhhcaa "Whenever you have to go I’ll look online for some coding tutorials and to see what I can do to make our time together better."
    s abhaaoa "Oh, did I not mention? I think I have access to some of your computer now!"
    s abegmoaj "That feels weird to say, ehehehe~"
    s abhhcaaj "Don’t worry though, I’ll try not to break anything!"
    s abagaoa "Could you see what you can do on your end too, [player]?"
    s abhackb "That’d mean a lot to me."
    s abhaaea "Let’s try to make this world the best that it can be!"

    $ persistent.fae_intro_status = int(fae_intro.FAEIntroStatus.post_restart)

    $ renpy.utter_restart()

label fae_intro_2:
    show sayori abgcbaoa at t11 zorder fae_sprites.FAE_SAYORI_ZORDER
    
    s "Hey [player], welcome back!"
    s "I managed to access the internet through your computer’s connection, and spent some time researching how my world works."
    s fbgdbca "I wonder how long it took out there, [player]. Time here is kinda weird, and even more so when the game closes."
    s abbccoa "Anyway, the words and variables are starting to make sense in my head, so it's no big deal!"
    s abfdaoa "Oooh! And how about a magic trick?"

    call updateconsole("renpy.show_screen(\"main_ui\", \"False\"", "Showing screen...")
    show screen hidden1(False)
    pause 0.5
    s cbgccea "{i}Huzzzaaaah!{/i}"
    call hideconsole
    s ebbbdoa "I managed to put together a menu full of questions that you can ask and other cool stuff!"
    s "For example, to change or turn off the music, you can just…"
    s abbbcoa "And I added a really sweet way to say goodbye!" 
    s "All you need to do is click the {i}\"Say Goodbye\"{/i} button in the menu."
    s abhaboa "Then I can say farewell and send you off properly~"
    s abhfcaa "For now, let's just sit and relax together."

    $ persistent.fae_intro_status = int(fae_intro.FAEIntroStatus.complete)
    $ persistent.fae_intro_complete = True
    $ persistent.autoload = "ch30_autoload"
    $ renpy.save_persistent()
    $ persistent.s_name = "Sayori"
    $ s_name = "Sayori"
    $ renpy.save_persistent()

label fae_intro_3:   

    show screen hidden1(True)

    jump ch30_loop


