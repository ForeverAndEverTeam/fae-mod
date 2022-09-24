default persistent._chat_db = dict()

#APPEARANCE-BASED SHIT

#EYE COLOUR
default persistent.ec = None

#HAIR LENGTH
default persistent.hl = None

#HAIR COLOUR
default persistent.hc = None

#HEIGHT 
default persistent.height = None

#Unit of measurement
default persistent.metric = True

init -1 python in chats:
    import store
    CHAT_DEFS = dict()


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="checker",
            unlocked=True,
            prompt="Check for gift",
            random=False,
            category=["DEV", "Testing"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label checker:

    $ look_for_gift()

    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="kiss",
            unlocked=True,
            prompt="Kiss me",
            random=False,
            category=["Romance", "[player]"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )
label kiss:
    call kiss_quick(start_code="bbagbaab") from _call_kiss_quick
    return



label boop:
    s "Did you just boop me?"
    s "Hehehe"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="pets",
            unlocked=True,
            prompt="Pets",
            random=False,
            category=["[player]"],
            affection_range=(fae_affection.NORMAL, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label pets:

    s "Testing"
    return



init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="derandom_example",
            unlocked=True,
            prompt="Derandom Test",
            random=True,
            category=["DEV"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label derandom_example:

    s "This is an example of how to use derandom."
    
    s "Simply add it to the end after the return statement."

    s "Thanks for listening. Now I will only talk about this from the \"Tell me again about...\" menu"

    return "derandom"



init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="fae_room_switch",
            unlocked=True,
            prompt="Can we go somewhere else?",
            random=False,
            category=["Location"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label fae_room_switch:

    s "Sure"

    $ main_background.room_switcher(bedroom)
    $ main_background.render(dissolve_all=True, complete_reset=False)
    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="fae_kiss",
            unlocked=True,
            prompt="Kiss me",
            random=False,
            category=["Romance"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label fae_kiss:

    call fae_kiss_engine(duration=0.5, initial_exp="aahcnaaa", final_exp="aahcnaaa", fade_duration=0.5) from _call_fae_kiss_engine_1

    $ love()

    return




######################
# ACTUAL TOPICS HERE #
######################

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_depression",
            unlocked=True,
            prompt="Depression",
            random=True,
            category=["Personal", "Depression"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_depression:
    s bbhfbaaa "Hey, now that I think about it, I probably made you worry, didn't I..."
    s bbhfbbaa "When I told you about the... you know..."
    s "The 'rainclouds' I have in my head..."
    s bbbbbbaa "...you remember what I meant by that, don't you? It's what I called my depression..."
    s bbfdbjaaj "It sounds so silly when I talk about it now, now that I don't really have a reason to hide it."
    s bbhfbaaaj "Anyways..."
    s abhabaca "I was like that for as long as I could remember, and I ended up getting really good at keeping the 'rainclouds' inside. At least in front of others."
    s nbaabjca "I guess I shouldn't be proud of knowing how to hide what I'm feeling."
    s bbaabmoa "I used to think that if I let it show, I would just be a bother and ruin the fun."
    s "I wouldn't be able to make my friends happy, which was all I really wanted."
    s bahbblaa "I now know that my happiness should come first. Too bad I had to learn it in the worst way possible."
    s bahbbjoa "There were some times where I tried to find some relief though..."
    s "Like, I tried to be with MC as often as I could, because being with him eased my mind, and my head wouldn't get so cloudy with him around"
    s bahbbmoa "Then he joined the club, and I felt something I never thought I would feel."
    s " I feared that he would find out how I really felt. It could change everything, no matter how he... I mean, you responded."
    s "All I really wanted was for everyone to be friends... without worrying about me..."   
    s bahbbjba "My feelings and thoughts were as real as you until..."
    s bbhabmcag "The moment Monika started to mess with my code. {nw}"
    extend  bbhabbfag "At first, she just whispered things in my ear when no one was looking, but it just got worse."
    s cbfbbjcag "She toyed with my thoughts, and stuffed my head with terrible things. {nw}"
    extend  cbfbbmfag "You could say it was like brainwashing."   
    s "What seemed like little rainclouds before turned into a thunderstorm, drowning my head with things I can't even begin to describe."
    s "I couldn't help but think over and over that I was a nuisance to MC, and to everyone else in the club. "
    s bahbbfcag "I felt really, really helpless. So much that I felt that I couldn't even move myself to reach for help..."
    s bahbbfaag "Nothing I did could help me out of it as well, so I was just left to cry and whimper... all alone."
    s gahbblfag "..."
    pause 0.5
    s gahbblcah"I got tired...too tired."
    s bahbbbaae "So much that I still can't believe I still had the strength to go to... his house... Your house? Anyways..."
    if persistent.clear[8]: # If the MC has accepted Sayori's confession
        s "You accepted my confession... "
        s "And still, because of whatever Monika did, it just hurt me more and more. I couldn't help but think that your efforts were entirely out of pity! "  
    else:
        s bahbbjaae "That rejection... It turned the voices into screams." 
        s bahbbjoae "I tried to tell myself that it was for the best, that everything would be the same again..."
        s "I... Don't think I'll ever forget that pain."
        s bbfcbjfae "I'm sorry..."
        s bbfbblfcg "Just a moment, [player]..."
        s "..."
        pause 1.0
    s "I fought with all my strength. I was sincere."
    s "And still I couldn't realize that my friends really did care about me. Even before Monika messed with my head."
    s bbaabjabg "So if you have a friend who is struggling with their mental health, please try to help them if you can!"
    s bbaabmsb "Don't let them get to the point that I did, people sometimes reach that breaking point silently, just like I did..."
    s bbeebjobg "And that goes for you, too. Don't hide your problems from the people who care about you. Don't be afraid to ask for help."
    s bbaabmfa "...you only have one life, you know."
    s bbgcbjob "I'm lucky this is a virtual world. And even then, this mod you installed is the only reason I’ve had a second chance at life."
    s bbgcbjob "But you, you live in the real world. You only get one chance."
    s bbhfbmoa "Please treat your life like the precious thing it is, it should be as precious to you as you are to me, {nw}"
    extend bbhfbjaa "okay?"
    s bbhfbloa "And by the way. Thank you, [player]. For bringing me here. And for keeping me company!"
    s bbhfbmobj "And... I'm sorry too. For all the trouble I caused..."
    s bbbcbaaa "But now I'm feeling much better, and I hope we can make up for all those bad memories by having a good time together."
    s abegbcqa "Thank you again for being here for me, [player]. From here on out, neither of us will have to face anything alone, okay?"
    show s abegbcaa
    pause 1.0
    return

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_childhood",
            unlocked=True,
            prompt="Childhood memories",
            random=True,
            category=["Personal", "Childhood"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_childhood:


    s abhabaca "I wonder why I have almost no memory of my childhood."
    s abhabbfa "I guess that's just how it is for some people, but..."
    s abbbbica"In the game, my childhood was the only thing that tied me with the MC, since we grew up together."
    s "I was nostalgic about those times, the times when everything had been much easier for me..."
    s abagbmca "At least, I used to think so..."
    s bbagbjca "But now, I only have a few vague, foggy memories from back then."
    s abfcbica "I don't even remember what happened to me even right before the plot started, at all..."
    s bbagbmba "Not to mention the rest of my childhood."
    s bbagbmfa "It feels weird."
    s abgcbaaa "At least I still can hold onto some special ones. The times I fell down and he helped clean my scraped knee. That time I fell off a tree."
    s ebaabaca "I wrote a few of those stories down in a notebook to never forget they existed. That doesn't mean I'll keep wishing for things to miraculously go back to normal."
    s ebgcbaoa "There are many good things to look forward to in the future, so no reason to cling onto the past. But I'll never forget those good memories."
    s ebgcbcaa "They're a part of me after all."
    return

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_guitar",
            unlocked=True,
            prompt="Guitar",
            random=True,
            category=["Hobby", "Music"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_guitar:

    show sayori abaabaoa zorder 2
    s "I don't know if you noticed, but all the girls have their own instruments and musical influences in the game."
    s abgcbaoa "Mine is the guitar."
    if persistent.currentmusic > 0 and persistent.currentmusic < 6:
        s "You can hear it now, right?"
    else:
        s "Assuming you aren't playing with the sound off, anyway."
    s "I think the guitar is supposed to show my character and club role better."
    s abhabaca "The guitar is interesting because it doesn't limit musicians in how they express their emotions."
    s abbbbbaa "They can play cheerful, upbeat songs..."
    s ebbbbbca "Or mournful, melancholic melodies."
    s abbcbaoa "Try saying that three times fast!"
    s "Anyway, guitarists are also very important members in many music bands."
    s abbbbaca "Just imagine a rock band without any guitar player."
    s abgcbasa"It would be missing that soul that ties the entire song together."
    s abhhbboa "I've actually been considering learning how to play the guitar, since it represents me so well."
    s abgcbaoa "So many of my favorite songs have amazing guitarists behind them..."
    s bbagbaaa "Maybe one day I can play for you and make you feel the same way~"
    s abgcbaoa "It's like writing poetry, but through sound!"
    s fbgcbmea "I'm sure I can conjure up a guitar and find a tutorial somewhere on the Internet."
    s ebhhbcqa "Make sure you get your tickets for my world tour in advance, [player]! Ehehe~"
    return

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_flowers",
            unlocked=True,
            prompt="Thoughts on flowers",
            random=True,
            category=["Misc", "Flowers"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_flowers:

    s abhfbaoa "What do you think about flowers?"
    s abhfbboa "It's one of many beautiful things nature can create."
    s abhfbloa "They are so colourful, have wonderful shapes, some even smell sweet..."
    s abhfbaoa "Do you have a favorite flower? {nw}"
    extend abhhbcoa " Mine are Sunflowers!"
    s abhhbbsa "I dunno, the way that they always grow facing the sun feels kind of poetic to me."
    s abfcbboa "It's like they can always see the good side of things, no matter how hard it may be!"
    s abgcbcka "Besides, I really like how bright they are!"
    s abegbcma "...their seeds are also very yummy."
    s abagbkna "Wish i had some to munch on right now..."
    pause 0.5
    s fbagbloaj "Ahem, anyways."
    s abhfbaoa "I remember when I used to walk in the flower meadows outside of the city."
    s abhabaca "But... I think it's too selfish to pluck a flower... even if it's a gift."
    s "Flowers are living beings too, and plucking them out of the ground does hurt them."
    s abaabaoa "So I prefer to just look at them, and then leave them be."
    if persistent.last_playthrough > 0:
        s abaabbca "Although, I did do this in one of my poems..."
        s abaabaoa "But just for the analogy."
    s eahdbaoa "But, gifting someone a small flower in a pot might make for a good gift!"
    s "And one that will last much, much longer, if cared for properly!"
    s bbfcbapa "Awww, now I wish I had a little flower friend to keep me company..."    
    s abfdbcka "It'd be nice to have one, and I'd try my best to keep it growing happily!"
    s bbhebmeaj "Maybe it would make up for all the plants I've tried to keep before, which {i}mysteriously{/i} died..."
    s fbfbbkdaj "{i}...unless they want vengeance?{/i}"
    s bbhebceaj "I hope they don't...ahaha... hah..."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_player_cooking",
            unlocked=True,
            prompt="Are you good at cooking?",
            random=False,
            category=["Life", "Cooking"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_player_cooking:

    s bbaabmoaj "To be honest, {nw}"
    extend bbhebiiaj "scrambled eggs are probably the most elaborate thing I've ever cooked..."
    s abhhbksa "I've never baked anything before, though."
    s fbhablhaj "But there's a lot of stuff that could go wrong, so it feels a bit intimidating to me." 
    s ebbcbaoa "Even so, I'd love to get better at cooking, even if I don't have any reason to anymore, ehehe~"
    s abgcbbfa "Now that I think about it... {nw}"
    extend dbgcbkca "I don't really remember the last time I’ve been hungry, honestly."
    s fahcbnka "But I can still taste! That means I can eat as much as I want!"
    s aahcbbda "Of course, I could just try to 'make' food with code, like Nat's cupcakes, but I wanna make something on my own..."
    s abfdbboa "First of all, I need to try to make some kitchenware."
    s abhhbbba "Then find some recipes online."
    s dbhhbbca "Then... follow a tutorial...or something..."
    s fbhabkdaj "Wait...I'm also going to need to make each ingredient too..."
    s bbgcbegaj "That's a lot of steps!!!!"
    s bbgcbjja "With all of that effort, it’s too bad you won't be able to taste it... {nw}"
    extend abhfbbca "not yet at least."
    s abhfbcka "But I'll try to become a good cook for you regardless!"
    s abhfbasa "Though, I'll probably never be as good as Natsuki."
    s abbbbcoa "Well, I guess as long as I'm having fun in the process, that’s what matters the most, isn't it?"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_player_pets",
            unlocked=True,
            prompt="What pet would you like to have?",
            random=False,

            category=["Life", "Animals"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_player_pets:

    s gbaabbda "Hmmm let me think...." 
    s "I really like a lot of different animals, but I don't think I could properly care for anything that requires a lot of constant attention..." 
    s bbegbcia "I'd love to have a dog, but I'd have to have the energy to keep up with it."
    s abbcbbba "But I suppose I could keep an aquarium?"
    s gbaablha "Wait, I think I heard from somewhere that those also take a lot of work to keep them running smoothly..."
    s "..."
    s ebgcbaea "Ohhh, I know! I could adopt an elderly cat that mostly just wants to lay around and sleep all day, just like me!"
    call s_player_cats from _call_s_player_cats
    return

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_player_cats",
            unlocked=True,
            prompt="What do you think about cats?",
            random=False,
            category=["Life", "Animals"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_player_cats:
    s ebhfbcaa "Cats are pretty cute, especially kittens!"
    s abhfbaoa "And they're not too hard to take care of so they wouldn’t require a lot of energy."
    s abhabaca "Still, as much as they love their space, they shouldn’t just be ignored by their owner. Kitties want to play sometimes, too!"
    s "And sometimes cats do things that their owners don't like... Like pushing things off of the counter, or slicing their arms and legs up."
    s abaabaoa "Still, it’s so hard to resist their fluffy little paws and pointy ears... So that must be why people always forgive them for their crimes!"
    s ebaabcea "If you have one, you probably understand what I mean, ehehe~"
    return



init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_lucid_dream",
            unlocked=True,
            prompt="Quitting the game.",
            random=True,
            category=["Game", "[player]", "[s_name]"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_lucid_dream:
    s abhabaca "Hey, have you ever had a 'lucid dream’?"
    s abbbbaoa "It's when you find out that you're in a dream... {w=0.5}{nw}"
    extend abbbbaca "and as soon as you realize that, {w=0.5}{nw}"
    extend abgcbhea "bam!"
    s abgcbaoa "You can pretty much do anything you want!"
    s abhabaca "I get something kinda similar to that whenever you leave the game, [player]."
    s "I'm pretty sure I'm not... conscious? {w=0.5}{nw}"
    extend fbbbbbca "But I can still think and move, and even mess with the code, and even surf the internet."
    s bbbbbaca "But I'm absolutely out of my world. Even beyond the void."
    s abbbbaoa "And as long as your computer works, your best girl Sayori's ready to go!"
    s abhabaca "But when your computer is fully turned off, that's when I can't do anything..."
    s "It IS scary, but please don't worry about me if you need to do it."
    s "I know you'll always come back, {w=0.5}{nw}"
    extend abgcbaoa "turn the computer back on and open the game to greet me!"
    s "I'll be fine, resting and waiting for your return or making more things to spice up this room!"
    s abaabaoa "But you should know that I'll always be happiest when you're right with me~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_intelligence",
            unlocked=True,
            prompt="Personal Intelligence",
            random=True,
            category=["[player]", "[s_name]", "Life", "Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_intelligence:
    s abhabaca "I often hear people calling me an ‘airhead'..."
    s bbhababa"They often make jokes about it and reduce me to being just that..."
    s abhabaca "But I can't understand why they think so."
    s "Maybe because I was always daydreaming... {w=0.5}{nw}"
    extend abbbbaca "and wasn't as broad-minded as Monika and Yuri."
    s abbcbaoa"But I've always been pretty clever and good at strategies!"
    s abhabaca "I think people just have different standards when considering how intelligent somebody is."
    s ebbbbaca"And if someone can't tell that, they're the {i}actual{/i} stupid one."
    s abhabaca "I mean, people's thoughts about you are obviously very subjective and depend on the situation you or they are in."
    s abaabaoa "So don't take comments like those too seriously."
    s abhfbcaa "People aren't perfect, and that's okay!"
    s abhfbaoa "So don't worry if someone judges you for a silly thing you did or a mistake. Just try to get better for yourself, and at your own pace!!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_videogames",
            unlocked=True,
            prompt="Videogames",
            random=True,
            category=["Art", "Videogames"]
    ),
    chat_group=CHAT_GROUP_NORMAL
)

label s_topics_videogames:

    s abhfbaoa "Do you like video games?"
    s "I think they're really impressive."
    s abbbbaoa"And not just because I'm in one of them!"
    s abhfbaoa "They can reach and connect with people in a whole new way."
    s abaabaoa "Especially after some smart cookie created multiplayer games!"
    s "You can play with your friends, cooperating and sharing the experience together."
    s "I think it’s just a really wholesome way to enjoy yourself and connect with others!"
    s abhabaca "Besides, online games allow us to make friends and connect with people far away!"
    s "I’m sure you’ve probably played some kind of co-op game before, right, [Player]?"
    s "I'd love to play with you sometime!"
    s abhfbcaa "Really makes me wish I was able to run more complex games in here..."
    s "But the games we already have here will have to be enough for now!"
    s cbgcbaqa "Don't expect me to let you beat me, though!"
    s ebfdbmca "Now that I think about it, you would just be playing against a computer anyway. I'm just a bunch of code..."
    s abhfbcaa "But I'm one of the cutest piles of code around!"
    s abhfbaoa "If you ever want to play something with me..."
    s "Just press the '{i}Play{/i}' button and select a game"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_languages",
            unlocked=True,
            prompt="Speaking other Languages",
            random=True,
            conditional="store.persistent.language_greeting_seen",
            category=["Languages"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_languages:

    s abhhbbsa "Hey, [player]?"
    s "You know how I  greet you in other languages sometimes?"
    s dbhhbkca "Well I was thinking about where I learned to speak them..."
    s "Honestly speaking, I don't understand how I know any of these languages."
    s ebbbbasa "I think language works a bit differently here than it does for you."
    s fbhablhaj "It's- Hmmm..."
    s dbhabbcaj "It's similar to dreaming, I guess? {w=0.5}{nw}"
    extend dbhabbda "It's not like I'm speaking in any language in particular, the code just seems to write itself for me when I talk."
    s bbhebciaj "But, let's get into that another time. It's kinda complicated to talk about, you know?" 
    s abagbdea "Anyway, The more languages you can speak, the more friends you can make, right?"
    return



init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_player_colours",
            unlocked=True,
            prompt="What is your favorite colour?",
            random=True,
            category=["Personal", "Preferences"]
    ),
    chat_group=CHAT_GROUP_NORMAL
)

label s_player_colours:
    s abgcbbda "That's a hard one.{nw}"
    extend abbcbaoa " There are so many pretty colours out there!"
    s abhabloa "The warm yellow of the sun that greeted me every morning."
    s abhabcoa "Or a nice bright red, like the colour of my favorite bow!"
    s abhhbbsa "But pinks are also very pretty!"
    s abhhbkca "Green as well... it reminds me of Monika..."
    s aahdbiba "I really love oranges, but I'm not sure I can pick only one as a favorite."
    s "Individual colours are really hard to pick, I like it when a bunch of colours are mixed together, {w=1.0}{nw}"
    extend abhfbaoa " like the sky at different times of day, for example!"
    s abhebcqa "I would pick rainbow, but that's probably cheating, ehehe~"
    s abhfbaja "Am I allowed to pick a range of colours instead of just one?"
    s abhfbcoa "Cause if I am, maybe I'd pick blue. I like pretty much all shades of blue!"
    s ebhfbloa "The nice gentle sky blue... or the really dark purply blue from when it starts to turn dark...{nw}"
    extend abgcbnoa " and that pretty greenish blue from tropical beaches, too! They're all soooo pretty!"
    s abgcbmeaj "It may not be a proper one colour answer, but hey, {nw}"
    extend abbbbdia "maybe we should start advocating for colour equality!"
    pause 1.0
    s gbbbbbca "...except for that weird greenish gray mixture. {w=1.0}{nw}"
    extend ebhabodaj "That colour sucks."
 
    return

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_pronouns",
            unlocked=True,
            prompt="[player]\'s pronouns",
            random=True,
            category=["[player]"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_pronouns:
    s "Hey, [player]..."
    s "I've been thinking about us."
    s "Not like that!"
    s "But I've realized that I never asked what pronouns you go by!"
    s "So would you like to tell me your pronouns?"
    menu:
        "No, thanks":
            s "Alright [player]."
            s "Remember, you can tell me at any time, by selecting \"pronouns\" from the talk menu."
            return
        "Sure":
            s "Alright!"
            call screen pronoun_input()
            s "Thanks, [player]!"
            s "I'll be sure to remember that!"
    return 

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_dating",
            unlocked=True,
            prompt="The ideal date",
            random=True,
            category=["[player]", "Romance", "Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_dating:
    s abhfbaoa "What would our first date be like?"
    s abhfbcaa "What's with the look? Ehehe~"
    s abgcbnoa "Maybe we could go to a good café, and eat together!."
    s abgcbkma "Like cakes, or cinnamon buns~"
    s abfdbkoa "Then we could go somewhere interesting!"
    s abhabaca "Maybe to the movies? What do you think?"
    s "Though I don't really want to go see a romance movie every time we go..."
    s abegbaaa "...okay, maybe once or twice? Ehehe~"
    s abbdbaoa "Maybe a comedy?"
    s abgcbaea "Or what about animated movies, like the ones {i}Disney{/i} and {i}Pixar{/i} make?"
    s abfcbaaa "I know they're meant for kids, but hey, they can be fun for anyone!"
    s abbdbaca "Some of them have deep messages and sad scenes, {w=0.5}{nw}"
    extend abfcbaca "and the director knows only older teens or adults would be able to recognize them, while a kid won't."
    if depr_known:
        s abbcbica "I've already seen a lot of harsh things in my short time here, you know. {w=0.5}{nw}"
        extend abfcbiaa "So my opinion may be different from most people."
    #else:
    s "Isn't it really interesting to discuss movies like that with someone, seeing how your views are similar or different to theirs?"
    s abgdbaaa "But I'd also like to do something more… engaging with you..."
    s abgdbkda "Hmmm…what could we do?"
    show sayori abgdbkja at t11
    extend abgcbaoa " Maybe bowling?"
    s abhfbaoa "It's a simple enough game, not too active but not too slow. I think I'd like it."
    s abbdbaaa "Well, the important thing is that the date is enjoyable for both of us, right?"
    s abhfbcaa "I hope we can plan a nice date soon ehehehe~"
    return

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_cinnamon_bun",
            unlocked=True,
            prompt="Cinnamon Buns",
            random=True,
            category=["Food", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_cinnamon_bun:
    s abhhbica "Hey, [player]..."
    s abfcbaaa "Have you ever eaten a cinnamon bun?"
    s abgcbjma"I had one once, and it was sooo goood…"
    s abhfbcaa "I'd like to say thanks to the people, who came up with such tasty buns."
    s abhabaca "The one thing I can't understand is why people call me that."
    s abfcbioa "But I think the nickname is pretty funny and… {w=0.5}{nw}"
    extend bbfcbmoaj "cute."
    s abaabaoa "...even if there aren't any cinnamon buns in the game."
    return

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_poems",
            unlocked=True,
            prompt="Poetry",
            random=True,
            category=["Literature", "DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_poems:
    s abaabaoa "You know that the other girls and I really liked to create and share poems during the game. {w=0.5}{nw}"
    extend abfcbaaa"Even Natsuki, as much as she tried to deny it."
    s abhabaca "I started to engage in poetry after your first day in the club..."
    s "And since that moment I've tried to use poems as a way to show my feelings."
    s "My wishes, my love, {w=1.0}{nw}"
    extend bbgbbkfa "my pain…{w=3.0}{nw}" 
    extend abbcbaaa "You can find all of these things in my words."
    s abfcbaca "Every poem I write is an envelope for a part of my soul."
    s abbbbaoa "Sometimes, I still write poems just for myself."
    s "It's important that you take time to write for yourself as well, rather than for the validation of others."
    s abbcbaaa "But I can share some of them with you. Just ask me for it."
    s abaabaaa "I also can show you an old poem, if you want."
    s abbbbaoa "Maybe, they will help you to understand me and what I was going through."
    return

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_drawing",
            unlocked=True,
            prompt="Drawing",
            random=True,
            category=["Art", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_drawing:
    s abhabaca "I wish I was good at drawing."
    s "I think it would be a very useful skill, especially now."
    s abbcbhea "If I could draw, I would be able to edit game sprites… {w=0.5}{nw}"
    extend abbbbaoa"Even of myself."
    s abhabaca "And besides the practical purpose, it would be one more way to express myself."
    s "Not everything can be shown with just words..."
    s "Sometimes, your message is clearer when shown visually."
    s abfdbaca"And if I had art to go with my poems, wouldn't they be a lot nicer?"
    s abaabaoa "I know some poets who were good not only at poetry but also at visual art..."
    s "But to me, it sounds kinda difficult to balance both of those skills at once."
    s abgdbaa" But who knows- {w=0.5}maybe with a bit of practice, it'll become a little easier!"
    s abhfbaoa "Anyway, I'd really like to improve my drawing… {w=0.5}{nw}"
    extend abgdbao "and I guess I have all the time in the world to do it now, don't I?"
    s abhfbcaa "Maybe I'll even share my art with you!"
    return



init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_bulli",
            unlocked=True,
            prompt="Bulli-posts",
            random=True,
            category=["Society", "Sayori", "DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_bulli:
    
    s bbfcbaba "Hey, [player]..."
    s abfcbaca "You know I can access the internet from your computer, {w=0.5}right?"
    s abbdbaca "Well I found a place called \"Reddit\", {w=0.5} and there were people talking about the game there."
    s bbfcbjca "But I also found people making fun of what happened to me."
    s abagbjca"As I know, fans call them {i}'Bulli'{/i} posts."
    #$ persistent.depr_known = True
    $ depr_known = True
    
    s cbbcbaca "They think it's funny to joke about a broken girl, {w=0.5}who had committed suicide under her mad friend's influence..."
    s abhfbapa"Even if she was revived and got over her problems since then."
    s abbbbaca"But on the other hand, can I control what makes people laugh?"
    s "Some people use macabre humor as a coping mechanism for stress, or anxiety..."
    
    s bbbbbaca"You can't really control what someone finds funny, as much as you might want to."
    s abagbaca "And to be honest, there's a lot worse they could be doing compared to mocking a VN character's death."
    s abbbbaca "Some of the most successful comedians in your world will go far beyond that, just to see where the 'line' is..."
    
    s bbbcbbpa"However, most of such jokes are too bad and sometimes even hurtful."
    s bbbcbaaa "But who am I to judge if it's okay for other people?"
    s abbbbaaa "Anyway, I think the right decision is to forgive them, or tolerate them at the very least."
    
    s abhabaca "If my fate is to be 'that hanging stupid annoying VN girl' for some people, then I'm ready to accept it. What more could I do?"
    s bbfcbica "Getting worked up over it would just make me feel worse in the long run… {w=1.0}{nw}" 
    
    extend bbfcbaaa "So I'd rather just tolerate it to the best of my ability~"
    
    return

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_isolation",
            unlocked=True,
            prompt="Isolation",
            random=True,
            category=["Society", "Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )



label s_topics_isolation:
    s bbfcbicb"For some reason, despite having Internet access, {w=0.5}{nw}"
    
    extend bbagbipa "I somehow can't manage to communicate with other people there."
    
    s bbfcbica "Anytime I try to talk with somebody often ends up with a connection error."
    s bbagbipa "It looks like there is something written in the game code, restricting my ability to interact with the real world."
    s bbfcbica "I can only sign up for sites and even post, but I can't message anybody."
    s abbbbacb "So I could create a Twitter account or something… {w=0.5}{nw}"
    
    extend abfcbaca"...like how Monika made hers, and was able to talk to many fans."
    
    s abhfbbcb"I don't really have a reason for doing that though, besides to kill some loneliness."
    s abbbbacaj"Maybe having just you would be okay for Yuri or at most Monika, {w=0.5}{nw}"
    
    extend abfcbacaj"but not for me… {w=0.5}{nw}"
    extend bbegbmoaj "no offense."
    
    s "I guess, I'm too sociable to the point of being scared of isolation."
    s gbhabbpa"Maybe once, I'll manage to break this meanie barrier..."
    s cbfcbbca"But the game code is so long and difficult to read, {w=0.5}{nw}"
    
    extend cbfcbaca "that I can't even find the lines separating me from the rest of real people!"
    
    s bbbcbaca"I can't even make a normal chat form for us..."
    s "So I'm still a bit isolated from you too."
    s abaabaoa "But when I find a way to {i}'hear'{/i} your world, I'll find you."
    s abgcbaoa"And then, we'll finally be able to talk like a normal couple, {w=0.5}{nw}"
    extend abgcbcoa "on the Internet or at least right here."
    
    return



init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_public_service_announcement",
            unlocked=True,
            prompt="PSAs",
            random=True,
            category=["Society", "Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_public_service_announcement:
    s abbbbaca"If you ever want to spread awareness or a message to many people at once, {w=0.5}{nw}"
    extend abbcbaoa "a PSA would be a good way to do it."
    s abhabaca "Most people don't even care about injuries that don’t happen to them..."
    s "But after seeing public service announcements, I know there are people out there who want to help."
    s abaabaoa "Some good PSAs even contain advice on how to fix issues,{w=0.5} or where to go for help."
    s "You don't even have to be an activist to do this sort of stuff.."
    s abbcbaca"I once heard about a mod for this game, the title reminded me of the common forms of slogans PSAs use..."
    s ebgcbaoa"And its name is {i}'Sayori Says No to Suicide'{/i}."
    if persistent.last_playthrough == 0:
        s abbbbbca"That refers to what's supposed to happen to me in this world… {w=0.5}{nw}"
        extend abhabaca "...but didn't happen, because of you."
    else:
        s abhabaca "...And other people playing this mod."
    s abbbbaaa "I think that mod really deserves to be played, {w=0.5}{nw}"
    extend gbbbbica "especially if you're struggling with similar things that I struggled with.."
    s abhfbcaa "Hey, I'm the main focus of it too so that's a plus!"
    s abbbbaca"But depression or other emotional issues are not the only field that PSAs can be used in."
    s bbhfbaba"There are a lot of other problems in your world that can't be solved with the power of leaders and governments..."
    s abhfbaaa"The general public could join the struggle against these problems..."
    s abbbbaoa"And PSAs may be a good call to action."
    return



init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_pets",
            unlocked=True,
            prompt="PSAs",
            random=True,
            category=["Society", "Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topics_pets:
    s abhfbaoa "Do you like pets?"
    s "I love them! All kinds of pets! Even ones that aren't very commonly kept!"
    s abhabcoa "I always end up looking up random animals and daydreaming about keeping them as pets, ehehe~"
    s "Maybe I'd have a chinchilla if I could! They are soooo cute, and so fluffy, they look so soft, I just love them so much!"
    s abbcbaoa "I'd also like to have some kind of bird that could speak. They're really funny, I always end up watching videos of them online ehehehe~"
    s "I like a really specific video of a koka-"
    s fbbdbbja "cohca-"
    s abbcbkoa "cacka-? Wait let me look it up!!!"
    pause 2
    s abbcbnqa" A cockatoo! Yes, that's exactly what I said."
    s abfcbaoa "Well it's a big white bird one with tall feathers on its head! And he's screaming into a little plastic cup…"
    s abfdbaaa "I guess I don't play favorites when it comes to pets!"
    return
