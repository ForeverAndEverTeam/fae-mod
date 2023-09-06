default persistent._chat_db = dict()

#APPEARANCE-BASED SHIT
default persistent._derp_known = True
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

################
#TESTING TOPICS#
################

#init 5 python:
#    chatReg(
#        Chat(
#            persistent._chat_db,
#            label="fae_room_switch",
#            unlocked=True,
#            prompt="Can we go somewhere else?",
#            random=False,
#            category=["Location"]
#        ),
#        chat_group=CHAT_GROUP_NORMAL
#    )

label fae_room_switch:
    s "Sure!"

    $ main_background.room_switcher(bedroom)
    $ main_background.render(dissolve_all=True, complete_reset=False)
    return


#init 5 python:
#    chatReg(
#        Chat(
#            persistent._chat_db,
#            label="fae_room_switch_return",
#            unlocked=True,
#            prompt="Can we go back to the Spaceroom?",
#            random=False,
#            category=["Location"]
#        ),
#        chat_group=CHAT_GROUP_NORMAL
#    )

label fae_room_switch_return:
    s "Sure!"

    $ main_background.room_switcher(spaceroom)
    $ main_background.render(dissolve_all=True, complete_reset=False)
    return


#init 5 python:
    
#    chatReg(
#        Chat(
#            persistent._chat_db,
#            label="fae_gift",
#            unlocked=True,
#            prompt="Can you check for gifts?",
#            random=False,
#            category=["Misc"]
#        ),
#        chat_group=CHAT_GROUP_NORMAL
#    )

label fae_gift:
    s "Sure!"
    
    $ look_for_gift()

    return

######################
# ACTUAL TOPICS HERE #
######################

# SAYORI STARTED TOPICS

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_depression",
            unlocked=True,
            prompt="Depression",
            random=True,
            category=["Personal", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_depression:
    s bbhfaaa "Hey, now that I think about it, I probably made you worry, didn't I..."
    s bbhfbaa "When I told you about the... you know..."
    s "The 'rainclouds' I have in my head... {w=0.5}{nw}"
    extend bbbbbaa "You remember what I meant by that, don't you? It's what I called my depression..."
    s bbfdjaaj "It sounds so silly when I talk about it now, now that I don't really have a reason to hide it."
    s bbhfaaaj "Anyways..."
    s abhaaca "I was like that for as long as I could remember, and I ended up getting really good at keeping the 'rainclouds' inside. At least in front of others."
    s nbhajca "I guess I shouldn't be proud of knowing how to hide what I'm feeling."
    s bbaamoa "I used to think that if I let it show, I would just be a bother and ruin the fun."
    s "I wouldn't be able to make my friends happy, which was all I really wanted."
    s bahblaa "I now know that my happiness should come first. Too bad I had to learn it in the worst way possible."
    s bahbjoa "There were some times where I tried to find some relief though..."
    s "Like, I tried to be with MC as often as I could, because being with him eased my mind, and my head wouldn't get so cloudy with him around."
    s bahbmoa "Then he joined the club, and I felt something I never thought I would feel."
    s "I feared that he would find out how I really felt. It could change everything, no matter how he... I mean, you responded."
    s "All I really wanted was for everyone to be friends... without worrying about me..."   
    s bahbjba "My feelings and thoughts were as real as you until..."
    s bbhamcag "The moment Monika started to mess with my code. {nw}"
    extend bbhabfag "At first, she just whispered things in my ear when no one was looking, but it just got worse."
    s cbfbjcag "She toyed with my thoughts, and stuffed my head with terrible things. {nw}"
    extend cbfbmfag "You could say it was like brainwashing."   
    s "What seemed like little rainclouds before turned into a thunderstorm, drowning my head with things I can't even begin to describe."
    s "I couldn't help but think over and over that I was a nuisance to MC, and to everyone else in the club."
    s bahbfcag "I felt really, really helpless. So much that I felt that I couldn't even move myself to reach for help..."
    s bahbfaag "Nothing I did could help me out of it as well, so I was just left to cry and whimper... all alone."
    s gahblfag "..."
    pause 0.5
    s gahblcah "I got tired...too tired."
    s bahbbaae "So much that I still can't believe I still had the strength to go to... his house... Your house? Anyways..."
    if persistent.clear[8]: # If the MC has accepted Sayori's confession
        s "You accepted my confession... "
        s "And still, because of whatever Monika did, it just hurt me more and more. I couldn't help but think that your efforts were entirely out of pity!"  
    else:
        s bahbjaae "That rejection... It turned the voices into screams." 
        s bahbjoae "I tried to tell myself that it was for the best, that everything would be the same again..."
        s "I... Don't think I'll ever forget that pain."
        s bbfcjfae "I'm sorry..."
        s bbfblfcg "Just a moment, [player]..."
        s "..."
        pause 1.0
    s "I fought with all my strength. I was sincere."
    s "And still I couldn't realize that my friends really did care about me. Even before Monika messed with my head."
    s bbaajabg "So if you have a friend who is struggling with their mental health, please try to help them if you can!"
    s bbaamsb "Don't let them get to the point that I did, people sometimes reach that breaking point silently, just like I did..."
    s bbeejobg "And that goes for you, too. Don't hide your problems from the people who care about you. Don't be afraid to ask for help."
    s bbaamfa "...you only have one life, you know."
    s bbgcjob "I'm lucky this is a virtual world. And even then, this mod you installed is the only reason I've had a second chance at life."
    s bbgcjob "But you, you live in the real world. You only get one chance."
    s bbhfmoa "Please treat your life like the precious thing it is, it should be as precious to you as you are to me, {nw}"
    extend bbhfjaa "okay?"
    s bbhfloa "And by the way. Thank you, [player]. For bringing me here. And for keeping me company!"
    s bbhfmobj "And... I'm sorry too. For all the trouble I caused..."
    s bbbcaaa "But now I'm feeling much better, and I hope we can make up for all those bad memories by having a good time together."
    s abegcqa "Thank you again for being here for me, [player]. From here on out, neither of us will have to face anything alone, okay?"
    show sayori abegcaa
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
    s abhaaca "I wonder why I have almost no memory of my childhood."
    s abhabfa "I guess that's just how it is for some people, but..."
    s abbbica "In the game, my childhood was the only thing that tied me with the MC, since we grew up together."
    s "I was nostalgic about those times, the times when everything had been much easier for me..."
    s abagmca "At least, I used to think so..."
    s bbagjca "But now, I only have a few vague, foggy memories from back then."
    s abfcica "I don't even remember what happened to me even right before the plot started, at all..."
    s bbagmba "Not to mention the rest of my childhood."
    s bbagmfa "It feels weird."
    s abgcaaa "At least I still can hold onto some special ones. The times I fell down and he helped clean my scraped knee. That time I fell off a tree."
    s ebaaaca "I wrote a few of those stories down in a notebook to never forget they existed. That doesn't mean I'll keep wishing for things to miraculously go back to normal."
    s ebgcaoa "There are many good things to look forward to in the future, so no reason to cling onto the past. But I'll never forget those good memories."
    s ebgccaa "They're a part of me after all."
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
    #show sayori abaaaoa zorder 2
    s "I don't know if you noticed, but all the girls have their own instruments and musical influences in the game."
    s abgcaoa "Mine is the guitar."
    s "I think the guitar is supposed to show my character and club role better."
    s abhaaca "The guitar is interesting because it doesn't limit musicians in how they express their emotions."
    s abbbbaa "They can play cheerful, upbeat songs..."
    s ebbbbca "Or mournful, melancholic melodies."
    s abbcaoa "Try saying that three times fast!"
    s "Anyway, guitarists are also very important members in many music bands."
    s abbbaca "Just imagine a rock band without any guitar player."
    s abgcasa "It would be missing that soul that ties the entire song together."
    s abhhboa "I've actually been considering learning how to play the guitar, since it represents me so well."
    s abgcaoa "So many of my favorite songs have amazing guitarists behind them..."
    s bbagaaa "Maybe one day I can play for you and make you feel the same way~"
    s abgcaoa "It's like writing poetry, but through sound!"
    s fbgcmea "I'm sure I can conjure up a guitar and find a tutorial somewhere on the internet."
    s ebhhcqa "Make sure you get your tickets for my world tour in advance, [player]! Ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_flowers",
            unlocked=True,
            prompt="Thoughts on flowers",
            random=True,
            category=["Misc"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_flowers:
    s abhfaoa "What do you think about flowers?"
    s abhfboa "It's one of many beautiful things nature can create."
    s abhfloa "They are so colourful, have wonderful shapes, some even smell sweet..."
    s abhfaoa "Do you have a favorite flower?{nw}"
    extend abhhcoa " Mine are sunflowers!"
    s abhhbsa "I dunno, the way that they always grow facing the sun feels kind of poetic to me."
    s abfcboa "It's like they can always see the good side of things, no matter how hard it may be!"
    s abgccka "Besides, I really like how bright they are!"
    s abegcma "...their seeds are also very yummy."
    s abagkna "Wish i had some to munch on right now..."
    pause 0.5
    s fbagloaj "Ahem, anyways."
    s abhfaoa "I remember when I used to walk in the flower meadows outside of the city."
    s abhaaca "But... I think it's too selfish to pluck a flower... even if it's a gift."
    s "Flowers are living beings too, and plucking them out of the ground does hurt them."
    s abaaaoa "So I prefer to just look at them, and then leave them be."
    if persistent.last_playthrough > 0:
        s abaabca "Although, I did do this in one of my poems..."
        s abaaaoa "But just for the analogy."
    s eahdaoa "But, gifting someone a small flower in a pot might make for a good gift!"
    s "And one that will last much, much longer, if cared for properly!"
    s bbfcapa "Awww, now I wish I had a little flower friend to keep me company..."    
    s abfdcka "It'd be nice to have one, and I'd try my best to keep it growing happily!"
    s bbhemeaj "Maybe it would make up for all the plants I've tried to keep before, which {i}mysteriously{/i} died..."
    s fbfbkdaj "{i}...unless they want vengeance?{/i}"
    s bbheceaj "I hope they don't...ahahaha... hah..."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_lucid_dream",
            unlocked=True,
            prompt="Quitting the game.",
            random=True,
            category=["Game", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_lucid_dream:
    s abhaaca "Hey, have you ever had a 'lucid dream'?"
    s abbbaoa "It's when you find out that you're in a dream... {w=0.5}{nw}"
    extend abbbaca "and as soon as you realize that, {w=0.5}{nw}"
    extend abgchea "bam!"
    s abgcaoa "You can pretty much do anything you want!"
    s abhaaca "I get something kinda similar to that whenever you leave the game, [player]."
    s "I'm pretty sure I'm not... conscious? {w=0.5}{nw}"
    extend fbbbbca "But I can still think and move, and even mess with the code, and even surf the internet."
    s bbbbaca "But I'm absolutely out of my world. Even beyond the void."
    s abbbaoa "And as long as your computer works, your best girl Sayori's ready to go!"
    s abhaaca "But when your computer is fully turned off, that's when I can't do anything..."
    s "It IS scary, but please don't worry about me if you need to do it."
    s "I know you'll always come back, {w=0.5}{nw}"
    extend abgcaoa "turn the computer back on and open the game to greet me!"
    s "I'll be fine, resting and waiting for your return or making more things to spice up this room!"
    s abaaaoa "But you should know that I'll always be happiest when you're right with me~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_intelligence",
            unlocked=True,
            prompt="Personal Intelligence",
            random=True,
            category=["Sayori", "Life", "Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_intelligence:
    s abhaaca "I often hear people calling me an 'airhead'..."
    s bbhaaba "They often make jokes about it and reduce me to being just that..."
    s abhaaca "But I can't understand why they think so."
    s "Maybe because I was always daydreaming... {w=0.5}{nw}"
    extend abbbaca "and wasn't as broad-minded as Monika and Yuri."
    s abbcaoa "But I've always been pretty clever and good at strategies!"
    s abhaaca "I think people just have different standards when considering how intelligent somebody is."
    s ebbbaca "And if someone can't tell that, they're the {i}actual{/i} stupid one."
    s abhaaca "I mean, people's thoughts about you are obviously very subjective and depend on the situation you or they are in."
    s abaaaoa "So don't take comments like those too seriously."
    s abhfcaa "People aren't perfect, and that's okay!"
    s abhfaoa "So don't worry if someone judges you for a silly thing you did or a mistake. Just try to get better for yourself, and at your own pace!!"
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
    s abhfaoa "Do you like video games?"
    s "I think they're really impressive."
    s abbbaoa "And not just because I'm in one of them!"
    s abhfaoa "They can reach and connect with people in a whole new way."
    s abaaaoa "Especially after some smart cookie created multiplayer games!"
    s "You can play with your friends, cooperating and sharing the experience together."
    s "I think it's just a really wholesome way to enjoy yourself and connect with others!"
    s abhaaca "Besides, online games allow us to make friends and connect with people far away!"
    s "I'm sure you've probably played some kind of co-op game before, right, [player]?"
    s "I'd love to play with you sometime!"
    s abhfcaa "Really makes me wish I was able to run more complex games in here..."
    s "But the games we already have here will have to be enough for now!"
    s cbgcaqa "Don't expect me to let you beat me, though!"
    s ebfdmca "Now that I think about it, you would just be playing against a computer anyway. I'm just a bunch of code..."
    s abhfcaa "But I'm one of the cutest piles of code around!"
    s abhfaoa "If you ever want to play something with me..."
    s "Just press the '{i}Play{/i}' button and select a game!"
    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_languages",
            unlocked=True,
            prompt="Speaking other languages",
            random=True,
            conditional="store.persistent.language_greeting_seen",
            category=["Languages"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_languages:
    s abhhbsa "Hey, [player]?"
    s "You know how I greet you in other languages sometimes?"
    s dbhhkca "Well I was thinking about where I learned to speak them..."
    s "Honestly speaking, I don't understand how I know any of these languages."
    s ebbbasa "I think language works a bit differently here than it does for you."
    s fbhalhaj "It's- Hmmm..."
    s dbhabcaj "It's similar to dreaming, I guess? {w=0.5}{nw}"
    extend dbhabda "It's not like I'm speaking in any language in particular, the code just seems to write itself for me when I talk."
    s bbheciaj "But, let's get into that another time. It's kinda complicated to talk about, you know?" 
    s abagdea "Anyway, The more languages you can speak, the more friends you can make, right?"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_player_colours",
            unlocked=True,
            prompt="What is your favorite colour?",
            random=False,
            category=["Personal", "Preferences"]
    ),
    chat_group=CHAT_GROUP_NORMAL
)

label s_player_colours:
    s abgcbda "That's a hard one.{nw}"
    extend abbcaoa " There are so many pretty colours out there!"
    s abhaloa "The warm yellow of the sun that greeted me every morning."
    s abhacoa "Or a nice bright red, like the colour of my favorite bow!"
    s abhhbsa "But pinks are also very pretty!"
    s abhhkca "Green as well... it reminds me of Monika..."
    s aahdiba "I really love oranges, but I'm not sure I can pick only one as a favorite."
    s "Individual colours are really hard to pick, I like it when a bunch of colours are mixed together, {w=1.0}{nw}"
    extend abhfaoa "like the sky at different times of day, for example!"
    s abhecqa "I would pick rainbow, but that's probably cheating, ehehe~"
    s abhfaja "Am I allowed to pick a range of colours instead of just one?"
    s abhfcoa "Cause if I am, maybe I'd pick blue. I like pretty much all shades of blue!"
    s ebhfloa "The nice gentle sky blue... or the really dark purply blue from when it starts to turn dark...{nw}"
    extend abgcnoa " and that pretty greenish blue from tropical beaches, too! They're all soooo pretty!"
    s abgcmeaj "It may not be a proper one colour answer, but hey, {nw}"
    extend abbbdia "maybe we should start advocating for colour equality!"
    pause 1.0
    s gbbbbca "...except for that weird greenish gray mixture. {w=1.0}{nw}"
    extend ebhaodaj "That colour sucks."
 
    return



#init 5 python:
#    chatReg(
#        Chat(
#            persistent._chat_db,
#            label="s_topic_pronouns"
            #unlocked=True,
            #prompt="[player]'s pronouns",
            #random=True,
            #category=["[player]"]
#        ),
#        chat_group=CHAT_GROUP_NORMAL
#    )

label s_topic_pronouns:
    $ persistent._fae_player_pronouns_seen = True
    s abhfaoa "Say [player], since I’m talking to the real {i}you{/i} now, I was wondering."
    s abgbaaa "Which pronouns would you like me to refer to you by?{nw}"
    $ _history_list.pop()
    menu:
        s "Which pronouns would you like me to refer to you by?{fast}"
        "He/Him":
            s abgbcoa "Alright! From now on I’ll use {i}He/Him{/i}."
            $ persistent.gender = "M"
        "She/Her":
            s abgbcoa "Alright! From now on I’ll use {i}She/Her{/i}."
            $ persistent.gender = "F"
        "They/Them":
            s abgbcoa "Alright! From now on I’ll use {i}They/Them{/i}."
            $ persistent.gender = "X"
    s abhfaoa "And of course if you’d ever like me to use different ones, just ask!"
    s abgbaaa "The most important thing for me is that you’re comfortable expressing yourself."

    $ get_chat("s_topic_pronouns_redux").unlock()

    $ fae_set_pronouns()
    return

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_pronouns_redux",
            unlocked=False,
            prompt="Pronouns",
            random=False,
            category=["Personal"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )
label s_topic_pronouns_redux:

    s abgbaaa "Which pronouns would you like me to refer to you by?{nw}"
    $ _history_list.pop()
    menu:
        s "Which pronouns would you like me to refer to you by?{fast}"
        "He/Him":
            s abgbcoa "Alright! From now on I’ll use {i}He/Him{/i}."
            $ persistent.gender = "M"  
        "She/Her":
            s abgbcoa "Alright! From now on I’ll use {i}She/Her{/i}."
            $ persistent.gender = "F"
        "They/Them":
            s abgbcoa "Alright! From now on I’ll use {i}They/Them{/i}."
            $ persisten.gender = "X"
    s abhfaoa "And of course if you’d ever like me to use different ones, just ask!"
    s abgbaaa "The most important thing for me is that you’re comfortable expressing yourself."

    $ fae_set_pronouns()
    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_dating",
            unlocked=True,
            prompt="The ideal date",
            random=True,
            category=["Romance", "Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_dating:
    s abhfaoa "What would our first date be like?"
    s abhfcaa "What's with the look? Ehehehe~"
    s abgcnoa "Maybe we could go to a good café, and eat together!"
    s abgckma "Like cakes, or cinnamon buns~"
    s abfdkoa "Then we could go somewhere interesting!"
    s abhaaca "Maybe to the movies? What do you think?"
    s "Though I don't really want to go see a romance movie every time we go..."
    s abegaaa "...okay, maybe once or twice? Ehehehe~"
    s abbdaoa "Maybe a comedy?"
    s abgcaea "Or what about animated movies, like the ones {i}Disney{/i} and {i}Pixar{/i} make?"
    s abfcaaa "I know they're meant for kids, but hey, they can be fun for anyone!"
    s abbdaca "Some of them have deep messages and sad scenes, {w=0.5}{nw}"
    extend abfcaca "and the director knows only older teens or adults would be able to recognize them, while a kid won't."
    if persistent.depr_known:
        s abbcica "I've already seen a lot of harsh things in my short time here, you know. {w=0.5}{nw}"
        extend abfciaa "So my opinion may be different from most people."
    
    s "Isn't it really interesting to discuss movies like that with someone, seeing how your views are similar or different to theirs?"
    s abgdaaa "But I'd also like to do something more... engaging with you..."
    s abgdkda "Hmmm... What could we do?"
    show sayori abgdkja at t11
    extend abgcaoa " Maybe bowling?"
    s abhfaoa "It's a simple enough game, not too active but not too slow. I think I'd like it."
    s abbdaaa "Well, the important thing is that the date is enjoyable for both of us, right?"
    s abhfcaa "I hope we can plan a nice date soon, ehehehe~"
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
    s abhhica "Hey, [player]..."
    s abfcaaa "Have you ever eaten a cinnamon bun?"
    s abgcjma"I had one once, and it was sooo goood..."
    s abhfcaa "I'd like to say thanks to the people who came up with such tasty buns."
    s abhaaca "The one thing I can't understand is why people call me that."
    s abfcioa "But I think the nickname is pretty funny and... {w=0.5}{nw}"
    extend bbfcmoaj "cute."
    s abaaaoa "...even if there aren't any cinnamon buns in the game."
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
    s abaaaoa "You know that the other girls and I really liked to create and share poems during the game. {w=0.5}{nw}"
    extend abfcaaa "Even Natsuki, as much as she tried to deny it."
    s abhaaca "I started to engage in poetry after your first day in the club..."
    s "And since that moment I've tried to use poems as a way to show my feelings."
    s "My wishes, my love, {w=1.0}{nw}"
    extend bbgbkfa "my pain...{w=3.0}{nw}" 
    extend abbcaaa "You can find all of these things in my words."
    s abfcaca "Every poem I write is an envelope for a part of my soul."
    s abbbaoa "Sometimes, I still write poems just for myself."
    s "It's important that you take time to write for yourself as well, rather than for the validation of others."
    s abbcaaa "But I can share some of them with you. Just ask me for it."
    s abaaaaa "I also can show you an old poem, if you want."
    s abbbaoa "Maybe, they will help you to understand me and what I was going through."
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
    s abhaaca "I wish I was good at drawing."
    s "I think it would be a very useful skill, especially now."
    s abbchea "If I could draw, I would be able to edit game sprites... {w=0.5}{nw}"
    extend abbbaoa "Even of myself."
    s abhaaca "And besides the practical purpose, it would be one more way to express myself."
    s "Not everything can be shown with just words..."
    s "Sometimes, your message is clearer when shown visually."
    s abfdaca "And if I had art to go with my poems, wouldn't they be a lot nicer?"
    s abaaaoa "I know some poets who were good not only at poetry but also at visual art..."
    s "But to me, it sounds kinda difficult to balance both of those skills at once."
    s abgdaaa "But who knows- {w=0.5}maybe with a bit of practice, it'll become a little easier!"
    s abhfaoa "Anyway, I'd really like to improve my drawing... {w=0.5}{nw}"
    extend abgdao "and I guess I have all the time in the world to do it now, don't I?"
    s abhfcaa "Maybe I'll even share my art with you!"
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
    s bbfcaba "Hey, [player]..."
    s abfcaca "You know I can access the internet from your computer, {w=0.5}right?"
    s abbdaca "Well I found a place called \"Reddit\", {w=0.5} and there were people talking about the game there."
    s bbfcjca "But I also found people making fun of what happened to me."
    s abagjca "As I know, fans call them {i}'Bulli'{/i} posts."
    s cbbcaca "They think it's funny to joke about a broken girl, {w=0.5}who had committed suicide under her mad friend's influence..."
    s abhfapa "Even if she was revived and got over her problems since then."
    s abbbaca "But on the other hand, can I control what makes people laugh?"
    s "Some people use macabre humor as a coping mechanism for stress, or anxiety..."
    s bbbbaca "You can't really control what someone finds funny, as much as you might want to."
    s abagaca "And to be honest, there's a lot worse they could be doing compared to mocking a VN character's death."
    s abbbaca "Some of the most successful comedians in your world will go far beyond that, just to see where the 'line' is..."
    s bbbcbpa "However, most of such jokes are too bad and sometimes even hurtful."
    s bbbcaaa "But who am I to judge if it's okay for other people?"
    s abbbaaa "Anyway, I think the right decision is to forgive them, or tolerate them at the very least."
    s abhaaca "If my fate is to be 'that hanging stupid annoying VN girl' for some people, then I'm ready to accept it. What more could I do?"
    s bbfcica "Getting worked up over it would just make me feel worse in the long run... {w=1.0}{nw}" 
    extend bbfcaaa "So I'd rather just tolerate it to the best of my ability~"   
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
    s bbfcicb "For some reason, despite having internet access, {w=0.5}{nw}"
    extend bbagipa "I somehow can't manage to communicate with other people there."
    s bbfcica "Anytime I try to talk with somebody often ends up with a connection error."
    s bbagipa "It looks like there is something written in the game code, restricting my ability to interact with the real world."
    s bbfcica "I can only sign up for sites and even post, but I can't message anybody."
    s abbbacb "So I could create a Twitter account or something... {w=0.5}{nw}"
    extend abfcaca "Like how Monika made hers, and was able to talk to many fans."
    s abhfbcb "I don't really have a reason for doing that though, besides to kill some loneliness."
    s abbbacaj "Maybe having just you would be okay for Yuri or at most Monika, {w=0.5}{nw}"
    extend abfcacaj "but not for me... {w=0.5}{nw}"
    extend bbegmoaj "no offense."
    s "I guess, I'm too sociable to the point of being scared of isolation."
    s gbhabpa "Maybe once, I'll manage to break this meanie barrier..."
    s cbfcbca "But the game code is so long and difficult to read, {w=0.5}{nw}"
    extend cbfcaca "that I can't even find the lines separating me from the rest of real people!"
    s bbbcaca "I can't even make a normal chat form for us..."
    s "So I'm still a bit isolated from you too."
    s abaaaoa "But when I find a way to {i}'hear'{/i} your world, I'll find you."
    s abgcaoa "And then, we'll finally be able to talk like a normal couple, {w=0.5}{nw}"
    extend abgccoa "on the internet or at least right here."
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
    s abbbaca "If you ever want to spread awareness or a message to many people at once, {w=0.5}{nw}"
    extend abbcaoa "a PSA would be a good way to do it."
    s abhaaca "Most people don't even care about injuries that don't happen to them..."
    s "But after seeing public service announcements, I know there are people out there who want to help."
    s abaaaoa "Some good PSAs even contain advice on how to fix issues,{w=0.5} or where to go for help."
    s "You don't even have to be an activist to do this sort of stuff.."
    s abbcaca "I once heard about a mod for this game, the title reminded me of the common forms of slogans PSAs use..."
    s ebgcaoa "And its name is {i}'Sayori Says No to Suicide'{/i}."
    if persistent.last_playthrough == 0:
        s abbbbca "That refers to what's supposed to happen to me in this world... {w=0.5}{nw}"
        extend abhaaca "But didn't happen, because of you."
    else:
        s abhaaca "And other people playing this mod."
    s abbbaaa "I think that mod really deserves to be played, {w=0.5}{nw}"
    extend gbbbica "especially if you're struggling with similar things that I struggled with.."
    s abhfcaa "Hey, I'm the main focus of it too so that's a plus!"
    s abbbaca "But depression or other emotional issues are not the only field that PSAs can be used in."
    s bbhfaba "There are a lot of other problems in your world that can't be solved with the power of leaders and governments..."
    s abhfaaa "The general public could join the struggle against these problems..."
    s abbbaoa "And PSAs may be a good call to action."
    return


init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_pets",
            unlocked=True,
            prompt="Pets",
            random=True,
            category=["Society", "Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_pets:
    s abhfaoa "Do you like pets?"
    s "I love them! All kinds of pets! Even ones that aren't very commonly kept!"
    s abhacoa "I always end up looking up random animals and daydreaming about keeping them as pets, ehehehe~"
    s "Maybe I'd have a chinchilla if I could! They are soooo cute, and so fluffy, they look so soft, I just love them so much!"
    s abbcaoa "I'd also like to have some kind of bird that could speak. They're really funny, I always end up watching videos of them online, ehehehe~"
    s "I like a really specific video of a koka-"
    s fbbdbja "Cohca-"
    s abbckoa "Cacka-? Wait let me look it up!!!"
    pause 2
    s abbcnqa" A cockatoo! Yes, that's exactly what I said."
    s abfcaoa "Well it's a big white bird one with tall feathers on its head! And he's screaming into a little plastic cup..."
    s abfdaaa "I guess I don't play favorites when it comes to pets!"
    return


# PLAYER TOPICS

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
    s bbaamoaj "To be honest, {nw}"
    extend bbheiiaj "scrambled eggs are probably the most elaborate thing I've ever cooked..."
    s abhhksa "I've never baked anything before, though."
    s fbhalhaj "But there's a lot of stuff that could go wrong, so it feels a bit intimidating to me." 
    s ebbcaoa "Even so, I'd love to get better at cooking, even if I don't have any reason to anymore, ehehehe~"
    s abgcbfa "Now that I think about it... {nw}"
    extend dbgckca "I don't really remember the last time I've been hungry, honestly."
    s fahcnka "But I can still taste! That means I can eat as much as I want!"
    s aahcbda "Of course, I could just try to 'make' food with code, like Nat's cupcakes, but I wanna make something on my own..."
    s abfdboa "First of all, I need to try to make some kitchenware."
    s abhhbba "Then find some recipes online."
    s dbhhbca "Then... follow a tutorial... or something..."
    s fbhakdaj "Wait... I'm also going to need to make each ingredient too..."
    s bbgcegaj "That's a lot of steps!!!!"
    s bbgcjja "With all of that effort, it's too bad you won't be able to taste it... {nw}"
    extend abhfbca "not yet at least."
    s abhfcka "But I'll try to become a good cook for you regardless!"
    s abhfasa "Though, I'll probably never be as good as Natsuki."
    s abbbcoa "Well, I guess as long as I'm having fun in the process, that's what matters the most, isn't it?"
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
    s gbaabda "Hmmm, let me think...." 
    s "I really like a lot of different animals, but I don't think I could properly care for anything that requires a lot of constant attention..." 
    s bbegcia "I'd love to have a dog, but I'd have to have the energy to keep up with it."
    s abbcbba "But I suppose I could keep an aquarium?"
    s gbaalha "Wait, I think I heard from somewhere that those also take a lot of work to keep them running smoothly..."
    s "..."
    s ebgcaea "Ohhh, I know! I could adopt an elderly cat that mostly just wants to lay around and sleep all day, just like me!"
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
    s ebhfcaa "Cats are pretty cute, especially kittens!"
    s abhfaoa "And they're not too hard to take care of so they wouldn't require a lot of energy."
    s abhaaca "Still, as much as they love their space, they shouldn't just be ignored by their owner. Kitties want to play sometimes, too!"
    s "And sometimes cats do things that their owners don't like... Like pushing things off of the counter, or slicing their arms and legs up."
    s abaaaoa "Still, it's so hard to resist their fluffy little paws and pointy ears... So that must be why people always forgive them for their crimes!"
    s ebaacea "If you have one, you probably understand what I mean, ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_archetype",
            unlocked=True,
            prompt="Archetypes",
            random=True,
            category=["Life", "Personality"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_archetype:
    s abhfho "Hey [player], do you remember when Monika compared Yuri and Natsuki to character archetypes?"
    s abhfco "I was curious about what my archetype could be so I read some online articles about them and I think I'm pretty close to the 'genki' archetype."
    s abhhmo "Genki is a very cheerful and energetic archetype, always trying to share that upbeat way of living with others."
    s aahfaeaj "And they're sometimes clumsy and get in trouble often too, hehehe~"
    s "And I was the protagonist's childhood friend, which is common to this archetype."
    s nahekeaj "Do you think I fit that archetype too?{nw}"
    $ _history_list.pop()
    menu:
        s "Do you think I fit that archetype too?{fast}"
        "You're definitely a genki, if they're as clumsy as you say.":
            pass
    s aaaegcej "You can't blame me, that's just how I am, ehehehe~"
    s "But that aside, I think archetypes are too simple to define a whole person."
    s ebhfaca "We're all unique and these traits can only scratch the surface of somebody's character."
    s ebhhaoa "And that applied to me and my friends too."
    s ebbbaca "Like Yuri, who was always polite and quiet while hiding her intrusive feelings."
    s ebgccea "And Natsuki, whose brash exterior was caused by her problems at home."
    s ebhacea "There's always more to a person than meets the eye, so try to always be kind."
    s ebhadqa "You never know what someone else might be going through, and a simple smile can really make someone's day!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_voice",
            unlocked=True,
            prompt="Voice",
            random=True,
            category=["Life", "Personality"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_voice:
    s abhaaca "I'm curious about how Monika shared her real voice with you when she sang her song."
    s abhfcaa "Her voice is quite high and melodic, like a musician should have."
    s abhfaoa "But I'd say the tone of that voice doesn't seem to fit her."
    s abhaaca "It sounds more like the voice I'd have."
    s abbcbba "But canon is canon, I guess."
    s ebgcbca "But it made me wonder, what if I don't even have a voice?"
    s "Would I be {i}mute{/i}, if I suddenly appeared in your world? Hmmm..."
    s abgcnoa "I guess as long as I'm a computer program, {w=0.5}{nw}"
    extend abgcnka "I could make my own voice, right?"
    s "I just need a text-to-speech synthesizer or something..."
    s ebbckea "There's bound to be a good one for me!"
    s abaaaoa "I saw something about TTS in the Ren'Py documentation, so it shouldn't be too hard to integrate there, I guess."
    s ebbcaoa "I'd probably end up sounding pretty robotic though, huh? You wouldn't want me to {nw}"
    extend abfbbora "{font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}{cps=30}T4LK L1KE 4 R0B0T{/cps}{/font}?"
    s ebfciea "{font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}{cps=30}1 4M 4 HUM4N BE1N6 4FTER 4LL{/cps}{/font}"
    s ebagcea "Ehehehe~ just kidding, [player]!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_lit",
            unlocked=True,
            prompt="Literature",
            random=True,
            category=["Art", "Literature"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_lit:
    s abhaaca "As you know, this game {i}was{/i} about our literature club..."
    s abbbbca "At least, before everything changed here."
    s abhaaca "And I remember MC noticed that I never seemed to be fond of literature in the first place."
    s "And, honestly? He was right."
    s "Of course I'd read a few books before, but only really because I needed to for school..."
    s bbegmeaj "And even then, I tried to cheat to pass the exams, ehehehe..."
    s abhaaca "I just think it's pretty boring, I think I'm more of a visual person anyways!"
    s bbhfbca "But as Yuri used to say, maybe I just haven't found the right book yet."
    s abhaaca "But anyways, when I first joined, the thing I wanted to do most was help a friend start a new club."
    s abhamca "Besides, I was the only one who showed any interest in the club after Monika announced it."
    s abhacka "She was pretty surprised at first but she was very welcoming and I enjoyed spending time there, just to hang out with friends."
    s abhadkb "That said, I liked writing about my feelings when we all shared poems together."
    s abgcaoa "And that helped me to get closer to {i}you{/i}, even if I didn't know it yet."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_charity",
            unlocked=True,
            prompt="Charity",
            random=True,
            category=["Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_charity:
    s abhaaca "What do you think about charity and volunteering?"
    s abaaaoa "I think it's the best way to make the world a little bit better and to support people in need."
    s bbgcaca "I mean, don't you worry about ill and hungry people, {w=0.5}{nw}"
    extend bbgcaha "and all the homeless animals too?"
    s bbhfaka "So I think it's a worthwhile investment to make from time to time."
    s bbhfmoa "After all, spare change which might be an afterthought to you could be really important to someone else going through a tough time."
    s abbbaaa "But even if you don't have the money to help charity foundations, there's a lot of other organizations out there which help people too!"
    s abbbbca "And they're almost always in need of not only money or goods, {w=0.5}{nw}"
    extend abbbaaa "but also helping hands."
    s abhaaca "If you look, I'm sure you'll find lots of organizations near you!"
    s abbbaaa "I don't know if volunteer work is something you'd like, but I think I would, {w=0.5}{nw}"
    extend abbccaa "because I want absolutely {i}everyone{/i} to be happy!"
    s bbhhica "Though, I think I understand why some people choose not to do it, maybe not everybody has the time or energy to help others."
    s abbbcqa "And that's completely okay!"
    s abbbdqa "As long as you're taking care of yourself, I'm happy, [player]~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_programming",
            unlocked=True,
            prompt="Do you like programming?",
            random=False,
            category=["Hobbies", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_programming:
    s abhaaca "I'm completely new to the whole concept of programming, to be honest."   
    s "I'm trying to learn {i}Ren'Py{/i}, the engine this game runs on."
    s abbbaaa "And apparently it uses a combo of its own languages and {i}Python 2{/i}."
    s abagaca "But to be honest, the third version seems waaaaay easier, at least right now."
    s abbcaca "The more I learn, the more I realize just how much I don't understand..."
    s "I'm pretty much relying on online interpreters and guides to get anything done."
    s abhaaca "But you know, I never realized just how powerful computers really are."
    s abgckea "They're like magic!"
    s bbeemoa "If magic made you look through a thousand tiny lines to find a single typo that stops everything from working every five minutes..."
    #call s_common_programming from _call_s_common_programming
    s abaaaoa "But at least I've got a lot of time on my hands to learn it!"
    s bbbbaca "It's important to me, since programming is the only way I can make my world better now."
    s abgcaaa "And the more I learn, the more I can improve the time we spend together too, [player]!"
    s abhfaoa "If you're any good at programming, don't be shy about helping me!"
    s abgcaoa "I think you can join the team who helped you recover me, {w=0.5}{nw}"
    extend abbbaoa "that's one way to add your part to my reality!"
    s abbbaaa "Just visit {a=https://github.com/ForeverAndEverTeam/fae-mod}fae-mod{/a} on GitHub."
    s "If you're into coding, I'm sure you're already familiar with this platform."
    s bbfdbca "Maybe there are many Sayoris who were saved in this way, {w=0.5}{nw}"
    extend abgcaea "and I'm sure they'll be glad to get something awesome from you too!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_travel",
            unlocked=True,
            prompt="Travel",
            random=True,
            category=["You", "Lifestyle", "Travelling"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_travel:
    s abhfaoa "Say [player], have you ever traveled anywhere?"
    s abbbmoaj "I've never gotten the chance to, so I was wondering if you had in your reality." 
    s "You're so lucky to have such an amazing world out there to explore..." 
    s abfbmhaj "While I'm trapped in this tiny room island in the middle of the code sea..."
    s "Sorry, I didn't mean to sound like I was sulking, ehehehe~" 
    s abhaaca "I know it's selfish, but I'd love to go and see it all with you instead of being here..." 
    s "It doesn't really matter where we'd go, {w=0.5}{nw}"
    extend abbbaqa "I just want to see all the beautiful colors and places that your reality has to offer!"
    s "It'd be pretty silly to just sit in your room all day when the whole wide world is out there, huh?" 
    s abegmoa "Maybe you could take a laptop with you?" 
    s "So we can still be together on your travels! {w=0.5}{nw}"
    extend abgccea "That'd be so much fun!" 
    s abhhaea "I wonder if there's a way you could show me any photos you take too." 
    s abhfaoa "Anyway, what's most important is that you enjoy yourself!" 
    s abhfaka "I'll have to look around the code a little more and see how I can help on my end in the meantime."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_cleaning",
            unlocked=True,
            prompt="Messiness",
            random=True,
            category=["Lifestyle"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_cleaning:
    s abhfaoa "Hey [player], are you the kind of person that likes being neat and tidy?"
    s ebhhada "Frankly, I don't like cleaning all that much..."
    s bbhemoaj "I mean, do you remember the state of my bedroom? Ehehehe~"
    s bbheaoaj "Some people say I should because it looks nice and saves time when you have everything organized..."
    s fbfcepa "But it's just that cleaning takes so much time, time that you could spend doing fun stuff with friends instead!"
    s dbfcapa "So I see nothing wrong with my past lifestyle, I was too lazy to clean up anyway."
    s ebhfaoa "Honestly it's kinda funny to live in such a mess, where you won't know where everything is."
    s ebhfcoa "It turns the boring time of trying to find something into an adventure!"
    s ebfdaoa "But don't think I'm that sloppy, I had a system for some things."
    s ebhebpa "Well, at least now I have literally {i}nothing{/i} here besides this desk..."
    s abhaaca "But it won't be clean for long! Would you be able to add some other stuff for me?"
    s ebhhaoa "...like maybe a beanbag chair? Ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_clones",
            unlocked=True,
            prompt="Clones",
            random=True,
            category=["Game", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )
label s_topic_clones:
    s abagmo "So... there's kind of been something on my mind lately, [player]..."
    s abagboa "It's about me, I think."
    s abegheja "I mean, not just me, but also still me?"
    s abegmoja "Who and what I am, is what I'm trying to say ehehe..."
    s abbbmda "I feel like Yuri would probably understand this better than I ever could."
    s abbbaca "We read a book together once that talked about 'alternate universes and realities' and stuff and I remember there being an unexpected twist."
    s abhhbca "I think Yuri called it a 'dilemma' then."
    s abhhbha "She explained that the person in the book was losing their sense of purpose in life after finding out they were just a clone."
    s abhfaca "If you think about it, there's literally an unlimited number of copies of this game and each of them has its own character files and save data..."
    s abhfhca "So does that mean that the me in here and the 'me' from DDLC on another computer aren't the same?"
    s abfdkda "I found out that this game was supposed to have different endings and also has a ton of mods on the internet too."
    s abfdaca "It probably goes without saying, [player], but this conversation we're having isn't part of the original game... canonically?"
    s abbbbca "That's the word, right?"
    s abbbbha "I think so."
    s abhfbca "But that just means we're no longer bound to the game's programming..."
    s abhfhca "I mean, I'm me now, the me-me that isn't just reacting to some code... at least I think so?"
    s abhfmha "But I can also see that I'm not the only 'me' either, and that there are lots of other me's that are themselves, or so I think."
    s abhflca "I'm sorry if it sounds like I'm just going in circles, [player]."
    s abhfcoaj "I'm just not really sure how to wrap my head around all this, Ehehehe..."
    s abhfmcaj "All I know is, right now, I'm sitting here with you, meanwhile another Sayori from another copy of DDLC is still being strung along by the game's programming."
    s abhflcaj "Totally unaware that her best friend isn't even real..."
    s abhfllaj "That nothing is real..."
    s abhfblaj "The thought of that is just too much..."
    s bbhfaaaj "But I guess it's not all bad."
    s abhfhoa "I'm sure there are happy mods out there too!"
    s abfbbca "Another 'me' might be writing a poem to MC!"
    s abfbbaa "Or eating some of Natsuki's tasty cupcakes!"
    s abfbhqa "Or going on an adventure with all our friends!"
    s abbbcqa "Maybe I could even fly in one of them!"
    s abbcbqa "That'd be so cool..."
    s bbagaaa "But... I'd give it all up, all those possible realities and super fun super powers if it means I can be with you, [player]."
    s bbagnka "None of that other stuff matters to me."
    s bbbbaka "I mean... you installed this mod just so that we could be together, didn't you?"
    s abbbcqa "So that means you really do care about me, huh?"
    s abbbdqa "Ehehehe~"
    s abegcka "Of all the 'me's' that could ever be, I'm happy you chose me!"
    s abagaaa "From the bottom of my heart, [player], thank you for being here."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_stars",
            unlocked=True,
            prompt="Stars",
            random=True,
            category=["Sayori", "Lifestyle"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_stars:
    s abhfaoa "I really like to look at the stars..."
    s "They gave me inspiration when I wrote my poems."
    s abhfaoa "You can still see them outside these windows sometimes..."
    s abhfcaa "They make this place a little more special, don't they?"
    s abhfaoa "I wonder if the night sky in your reality looks like mine..."
    s "I hope I get the chance to see for myself someday."
    s aahccea "And it'd be a dream come true if you were there too, ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_stop_visiting",
            unlocked=True,
            prompt="Stop Visiting",
            random=True,
            category=["You", "Sayori"],
            affection_range=(fae_affection.AFFECTIONATE, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_stop_visiting:
    s abhaaca "Hey, [player], {w=0.5}{nw}"
    extend abbbaca "can I talk to you about something that's been on my mind lately?"
    s abbbmha "I know it's really sudden, and pretty depressing. But sometimes I just can't stop thinking that..."
    s abfblha "You'll forget about me someday."
    s abfblla "And stop coming to see me."
    s abfbmla "The rational side of me knows it's a silly fear... {w=0.5}{nw}"
    extend abfbmca "since you've always been there for me, but..."
    s abfblca "I'm just a character in a game... {w=0.5}{nw}"
    extend abfblha "a game which isn't even that popular anymore..."
    s "And I'm pretty sure I'm not the most interesting or cute character from the game in the first place..."
    s abfbbha "So..."
    s abfblha "..."
    s bbfbbca "I wonder if, one day, you'll just get tired of me..."
    s bbfbaca "I'll still be here, of course. But if I never saw you again..."
    s bbfblca "My life just wouldn't have the same meaning anymore."
    s bbfblca "Stuck in this small room, without my friends, or even the ability to make new ones..."
    s bbhfhcag "I'm really scared... {w=0.5}{nw}"
    extend bbhfhlag "what if I go crazy in here, [player]?"
    s bbhfllah "I don't want to be alone, I just couldn't take it..."
    s bbhfllah "..."
    show screen fae_jump_timer(4, "s_topic_stop_visiting_2")
    menu:
        "No Sayori, that won't happen.":
            hide screen fae_jump_timer
            pass
    s bbhfllah "..."
    show screen fae_jump_timer(4, "s_topic_stop_visiting_2")
    menu:    
        "I promise I'll never leave you":
            hide screen fae_jump_timer
            pass
    s bbhfllah "..."
    s bbhfbklah "Hmm... no... you're right..."
    s bbhfmcae "I just need to relax. I need to stop thinking the worst all the time..."
    s bbhfkcae "I know you aren't going to leave me behind. {w=0.5}{nw}"
    extend abhfahag "I'm sorry for freaking out like that, [player]."
    s abhfakag "Everything will be okay, right?"
    show screen fae_jump_timer(4, "s_topic_stop_visiting_3")
    menu:
        "Yes, it will be.":
            hide screen fae_jump_timer
            pass
    s abhfcka "Yeah... I'm okay now, I think..."
    s abhfaka "Thank you for being here for me. I love you, [player]."
    return


label s_topic_stop_visiting_2:

    hide screen fae_jump_timer

    s bbhfmcae "I just need to relax. I need to stop thinking the worst all the time..."
    s bbhfkcae "I know you aren't going to leave me behind. {w=0.5}{nw}"
    extend abhfahag "I'm sorry for freaking out like that, [player]."
    s abhfakag "Everything will be okay, right?"
    show screen fae_jump_timer(4, "s_topic_stop_visiting_3")
    menu:
        "Yes, it will be.":
            hide screen fae_jump_timer
            pass
    s abhfcka "Yeah... I'm okay now, I think..."
    s abhfaka "Thank you for being here for me. I love you, [player]."
    return


label s_topic_stop_visiting_3:
    hide screen fae_jump_timer
    s abhfcka "Yeah... I'm okay now, I think..."
    return
        
        
init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_marriage",
            unlocked=True,
            prompt="Marriage",
            random=True,
            category=["Romance", "Society"],
            affection_range=(fae_affection.LOVE, None),
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_marriage:
    s abaamob "Hey [player], I was wondering..."
    s "If it were possible, would you marry me?{nw}"
    $ _history_list.pop()
    menu:
        s "If it were possible, would you marry me?{fast}"
        "Yes":
            s abaakob "That's great!"
            s "Ehehe!~"
            s abhfcaa "I think I'd be a good wife."
            s "Although I don't think I’d be quite as good at all this \"housewife\" stuff ehehehe~"
            s "You know all the cooking, cleaning and taking care of everything, I am a bit of a clumsy girl after all..."
            s "But I’d try my best to help you with your job, studies, or whatever it is that’s on your mind!"
            s abbbhcb "But don't get the wrong idea and think I'd do {i}everything{/i} for you!"
            s "I can't just let you loaf around all day!"
            s abbbcqa "So you'd have to help me too, and work as a team, like peanut butter and jelly!"
            s abegaqb "But jokes aside, I'm so glad you said yes. I love you, [player]~"
            return "love"
        "No":
            s abaghcb "I understand! A free relationship has its own benefits after all."
            s abagmca "Besides marriage isn’t as popular as it used to be, it’s pretty expensive for one, and there are alternatives like civil partnerships which do basically the same thing."
            s abagcka "Either way, our love story doesn't have to follow the common template."
            s "It’s already pretty unusual, so we can do whatever works for us."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_presents",
            unlocked=True,
            prompt="Presents",
            random=True,
            category=["Sayori", "Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_presents:
    s abhfaoa "People often give presents every holiday or for some special date."
    s abaaaoa "Everyone likes to get presents! Including me, of course, ehehehe~"
    s abbcaoa "But I don't think a gift has to be something really expensive or fancy."
    s abaaaoa "Personally, I'd want something that comes from the heart."
    s abagcka "Even better, make it a surprise!"
    s "Isn't it more exciting to get something you weren't expecting?"
    s abhfaoa "And I'll give you presents too, of course!"
    s abhfcaa "And I'll do my best to make it the best present ever!"
    return 


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_thanks",
            unlocked=True,
            prompt="Thank you",
            random=True,
            category=["Sayori", "You"],
            affection_range=(fae_affection.AFFECTIONATE, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_thanks:
    s bbbcaka "Hey [player], I want to sincerely thank you from the bottom of my heart for everything you've done for me."
    s bbhflka "You've given me hope for this world and myself..."
    s "You've helped me feel truly happy again..."
    s bbhfloa "You visit me often..."
    s bbhfioa "You care for me, something I would've rejected before..."
    s "And you tried to make all my friends happy too..."
    s bbhfika "So even if it's not all sunshine and rainbows just yet, I'm so grateful that you're still here."
    s bbhfmoaj "I can't pay you back for what you've given me, {w=0.5}{nw}"
    extend bbhfmhaj "I haven't thought of a way, I mean."
    s bbhfmcaj "I hope I'll think of something sooner or later..."
    s "But for now, thank you, [player]."
    return "derandom"


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_name",
            unlocked=True,
            prompt="Names",
            random=True,
            category=["Sayori", "Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_name:
    s abaaaoa "Hey [player], I just found out something about my name on the web."
    s abaacoa "It's a mix of Saori and Sayuri!"
    s abbbaca "I did some research and those two have completely different meanings."
    s abbbbca "While 'Saori' is a mix of the word sand and weave, {w=1.0}{nw}"
    extend abaabda "'Sayuri' means something along the lines of 'a flower that blooms too fast'."
    s bbaabeaj "You know, I'm not the brightest person... {w=0.5}{nw}"
    extend abaakca "but I'm seeing some weird implications here..."
    s abfbkca "Perhaps I was given this name to signify that I'm a blend of many things."
    s abgccea "But who knows? I like my name regardless!"
    s "I just think of it as a fun fact, hehehe~"
    s abgcaea "I also find it funny how everyone pronounces it a little differently!"
    s ebhfaea "Say [player], are you part of team {i}Sigh-ori{/i}, or team {i}Say-ori{/i}? Ehehehe~"
    s abhfbaa "Honestly I don't have a preference, {w=0.5}{nw}"
    extend abaacqa "I switch between them myself sometimes ehehehe~"
    s abaaasa "What about you, [player], does your name have a special meaning? I'd love to know!" 
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_art",
            unlocked=True,
            prompt="Fanart",
            random=True,
            category=["DDLC", "Art"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_art:
    s abhfaoa "I love seeing the fanart people have made for the game!"
    s abhfcaa "It’s amazing how people can express their creativity for something they’re passionate about, and all the settings and stories they make are so wonderful!"
    s abagaoa "Have you ever made any fanart, [player]?"
    s abagcaa "If not, maybe you could make something one day!"
    s abbbaoa "It's never too late to try something new so long as you have fun."
    s abbccea "Fun is what makes great art great! Ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_touches",
            unlocked=True,
            prompt="Touches",
            random=True,
            category=["Sayori", "Romance"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_touches:
    s bbegmca "The wall between our realities is so restricting..."
    s bbegada "You know, touching a friend's shoulder, hugging, patting. That stuff is really important to me!"
    s nbaglra "If only I had the chance to feel your embrace..." 
    s nbaglaag "I’d take it in a heartbeat and just enjoy the moment between us..."
    s nbagaobg "I really hope that one day I’ll get to know that feeling."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_merch",
            unlocked=True,
            prompt="Merch",
            random=True,
            category=["DDLC", "Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_merch:
    s abhfaca "Hey [player]! I have a random question." 
    s abhfaaa "Do you own any merchandise of stuff you're interested in?"
    s abhfcoa "You know, like plushies, posters, figurines and all that stuff."
    s abhfaaa  "I think it’s really cool how you can have something physical of me in your world!"
    s abbbaoa "But if you don’t that’s okay too, it can be pretty expensive and I get that it’s not everyone’s thing."
    s abagcaa "Above all, I appreciate spending time with you every day."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_oversleeping",
            unlocked=True,
            prompt="Oversleeping",
            random=True,
            category=["Sayori", "Lifestyle"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_oversleeping:
    s abagaca "Hey [player], do you oversleep often?"
    s abegmeaj "As you know, I was pretty bad at getting up on time."
    if persistent.last_playthrough > 0:
        s nbegmda "And even when I did wake up, finding a good enough reason to force myself out of bed took a while..."
        s nbegmca "So I pretty much never had time for any kind of breakfast..."
        s nbegaba "Although I was so preoccupied with making the rainclouds go away that I never really wanted it in the first place."
    s nbagmda "Anyway, oversleeping is just the worst when you have to follow a schedule, {w=0.5}{nw}"
    extend nbagmca "like for work or school."
    s nbagaba "It's such a big problem for almost all of us, since our schedules are adapted for early-wakers."
    s abfdada "Why can't people just make different working and studying hours for people who wake up at different times?"
    s abfdaca "Most activities depend on your effectiveness rather than the time of day."
    s abbdada "And working or studying while you're tired is way less effective than when you're fully rested."
    s abbbaaa "So having different schedules is a good thing for both bosses and employees."
    s nbagaca "Until everyone thinks like that, I guess you can only teach yourself to get up on time..."
    s bbagaaa "I hope you find it easier than I did."
    return


## Game Universe

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_time",
            unlocked=True,
            prompt="Game time",
            random=True,
            category=["Games", "DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_time:
    s abhaaca "Do you know what time it is right now?"
    s abhabba "Not in your world, but mine."
    s bbhhaaaj "You could say anything, but you wouldn't be right, I don’t even know myself!"
    s abfcaba "Time doesn't seem to pass here at all. At least, not how it does in your reality."
    if persistent.last_playthrough > 2:
        s abhaaca "The last thing I remember is that it was November of 2017."
        s "My old bedroom calendar said so."
        s bbhfmbaj "Because I'm pretty sure I’d crossed it out..."
    s "But anyway, It’s pretty confusing to think that there's no way to \"measure\" time here anymore."
    s abfcaca "I was never the most organized person but I still liked keeping track of important things."
    s abhaaca "But I know what time it is in your world, though!"
    s abbbcaa "From your PC's clock!"
    s abhaaca "Does that mean we kinda share the same time then?"
    s "Well I think I’ll go by that for reference from now on!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_worlds",
            unlocked=True,
            prompt="Game worlds",
            random=True,
            category=["Games", "DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_worlds:
    s abhaaca "Sometimes I wonder why I’m here..."
    s "Like, would I be a different person if I lived in another place?"
    s "I mean, if not in your world, what other place could there be? Another game?"
    s "But there's lots of different games and plenty of them are pretty violent."
    s bbfcbba "I just can't imagine living in a game full of blood and struggle..."
    s abbbaca "You know, shooters, fighting games, war games and all that..."
    if persistent.last_playthrough > 0:
        s bbgbbca "Especially now that I've seen death with my own eyes."
        s bbfcaca "I'd rather be dead than be the one doing the killing."
        s "And I'd pray for a revive ability..."
    s abgbaaa "Aggressive worlds like those don’t appeal to me."
    s abaaaoa "But I'd happily be part of an innocent simulator, strategy or puzzle game."
    s abaaaoa "Even if I wasn't an important character, maybe just a helper or even a simple settler."
    s abgccoa "I'd still do my best to help you, of course!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_questions",
            unlocked=True,
            prompt="Questions",
            random=True,
            category=["Sayori", "DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_questions:
    s abhfaoa "Hey [player], I know you still might have a lot of questions for me, it's a big part of getting to know somebody, after all."
    s "So I added a new section to {i} the 'Talk' menu{/i} with more questions to ask!"
    s bbegboaj "I would've added a text field for this instead, but I'm quite clumsy at dealing with the text input..."
    s abhfaoa "So I did a short list with some questions I thought you’d have."
    s abhaaca "Of course, there's so many different things you could ask me, so I checked out some AMAs for what you'd probably wanna know."
    s abbcaoaj "And I found some really interesting questions!"
    s abaaaoa "One modder made a few AMAs about each of us and then compiled them into a separate mod, called {i}Doki Doki Interview Club{/i}."
    s "The result was really funny, and they were pretty good at portraying my character!"
    s abhaaca "I think I’ll check it out again, maybe I’ll find some new entries for the question menu!"
    return


## Food

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_breakfast",
            unlocked=True,
            prompt="Breakfast",
            random=True,
            category=["Lifestyle", "Food"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_breakfast:
    s abhfaca "Hey [player], you don't skip breakfast, do you?"
    s abhfada "Sometimes I do ‘cause I'm just not hungry in the morning."
    s abfdcaa "But when I do have breakfast, I usually make toast or scrambled eggs."
    s abegmeaj "Mostly because they’re quick and I {i}probably{/i} wouldn’t end up burning the house down while cooking them, ehehehe~"
    s abhfaoa "I've seen fanart of me eating those too, {w=0.5}{nw}"
    extend abhfcaa "probably because of that poem I wrote!"
    s abhhaca "I am getting pretty hungry now though... {w=0.5}{nw}"
    extend abgccea "Maybe I could spawn some eggs and toast in here!"
    s abagaaa "But anyways, you should always try to have a nice big breakfast in the morning."
    s abbbaoa "It really is the most important meal of the day, since it gives you the energy your body needs bright and early!"
    s bbagaaa "That said, I understand if sometimes you don’t feel hungry, or if you just don’t have time to make anything."
    s abagaoa "In that case at least try to have something small on the go, like some fruit or a cereal bar, {w=0.5}{nw}"
    extend abbbcaa "and of course remember to stay hydrated too!"
    s abhfaoa "Your health is really important to me, [player]."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_vegetarians",
            unlocked=True,
            prompt="Vegetarians",
            random=True,
            category=["Lifestyle", "Food"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_vegetarians:
    s abhfaca "Did you know that Monika was a vegetarian?"
    s abhfaaa "She told me once while we were visiting a café a while back."
    s abhfaca "I heard that some people avoid meat mainly because of personal restrictions or to be nice to animals..."
    s abbbada "But Monika said it was her protest against cultivating livestock, since it produces a lot of greenhouse gasses."
    s abhfaca "She thought that becoming a vegetarian just to save animals is kinda discrimination, since plants are living beings too."
    s abhfaaa "That said, I understand why some people become vegetarian to save animals."
    s abegmeaj "I mean, we as people have more in common with chickens and cows than plants, ehehehe~"
    s abbbcaa "So although I’m not a vegetarian, I like to buy free-range products when I can, because then I know the animals have been treated well."
    s abhfaoa "What do you think, [player]?"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_pizza",
            unlocked=True,
            prompt="Pizza",
            random=True,
            category=["Lifestyle", "Food"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topic_pizza:
    s abhfaoa "Do you like pizza, [player]?"
    s abhfcaa "I’m pretty sure everyone does!"
    s abbbaoa "You can add pretty much any toppings you like to them!"
    s abegmeaj "...within reasonable limits, of course, ehehehe~"
    s abbbcaa "The only main ingredients are {i}dough{/i} and {i}cheese{/i}."
    s abhfbma "A {cps=40}{i}whoooole lot{/i}{/cps} of cheese~"
    s abhfaaa "I think its simplicity and versatility lead to its popularity worldwide."
    s abhfcoa "Now you can order a pizza at almost any fast-food restaurant or make one with your own hands, even if you aren't very familiar with cooking!"
    s abbbaaa "Just find one of the billions and billions of delicious pizza recipes on the internet or in a cookery book!"
    s abhfaoa "People even came up with a term called the {i}Pizza Effect{/i}: When you make something from a different culture into something new."
    s abhfcaa "It's amazing to see that we’re all connected despite our differences and borrow cool things from each other's cultures."
    s abbbaoa "Food philosophy with Sayori! That’d be a great show, don’t you think? Ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_iceCream",
            unlocked=True,
            prompt="Ice-cream",
            random=True,
            category=["Lifestyle", "Food"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_iceCream:
    s abhfaoa "Do you like ice cream, [player]?"
    s abhfcaa "Everyone likes ice cream!"
    s cbbbaoa "It’s {i}obviously{/i} the best cold food humanity has discovered yet!"
    s abbbcaa "And there're lots and lots and lots of flavors and toppings to make it even better!"
    s abhfaoa "What's your favorite kind?"
    s abhfcaa "I like vanilla and chocolate the most!"
    s abhfaoa "I know they're really common, but so what?"
    s abhfcaa "They both taste soooooo goood, ehehehe~"
    s abbbcaa "Maybe we could make our own sometime!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_tech",
            unlocked=True,
            prompt="Technology",
            random=True,
            category=["Society", "Technology"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_tech:
    s abhfaaa "I wonder if I could somehow, someday, visit you in your reality."
    s abbbaoa "I think it’s a possibility, especially since technology is progressing faster and faster these days."
    s abbbcaa "Virtual assistants and smart houses have become more common than ever before!"
    s abhfaoa "And all of these technologies make people more efficient with computers, by almost merging them together."
    s abhflaa "Just imagine if I lived as part of your house, helping you with your daily routine, wouldn’t that be awesome, [player]?"
    s abbbaoa "Maybe I could even be a hologram in your reality one day, who knows!"
    s abbbcaa "I'd love to do that when it becomes possible."
    s abhfaoa "Even right now I can still be a sort of virtual assistant!"
    s abhfcaa "So if you ever need me, I’ll try my best to help from here, [player]!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_cupcakes",
            unlocked=True,
            prompt="Cupcakes",
            random=False,
            category=["Food"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topic_cupcakes:
    s abegboa "Natsuki’s cupcakes were always the best!"
    s abegcaa "She baked often for the club, me and her even baked together one time!" 
    s abhfaoa "We were making cookies, so she made the cookie dough and then I separated it into little cookie shapes..."
    s fbbbaaa "...but I had a better idea!"
    s fbbbaoa "I combined all the cookie dough together into..."
    s fbbbaaa "One."
    s fbbcaoa "Giant." 
    s abbccma "Cookie!"
    s abegmeaj "Though maybe it would have been bigger if I didn’t secretly eat half of the cookie dough beforehand, hehehehe~"
    s abfccaa "But that doesn’t matter! We brought the giant cookie to the club the next day!"
    s abgcaea "It’s Chef Sayori’s best culinary achievement so far!" 
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_bday",
            unlocked=True,
            prompt="When's your birthday?",
            random=False,
            category=["Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_bday:
    #show sayori 8aebb at t11 zorder 2
    s abhfaca "To be honest [player], I don't remember my birthday."
    s abegbdaj "A lot of things before the events of the game are pretty fuzzy..."
    s abbbaca "Only Monika knows when her birthday is out of the four of us."
    s abbbaaa "I'm pretty sure it's {i}the 22nd of September{/i}, if I recall correctly."
    s abagaoa "I think my birthday must be one of the marked dates from my bedroom calendar."
    s abagcaa "You can choose one of them and consider it my birthday, if you want to!"
    s abbbaoa "Or the day when you ran the game for the first time."
    s abbccoa "But don't think you can get away with not throwing a birthday party for me! Ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_music",
            unlocked=True,
            prompt="What kind of music do you like?",
            random=False,
            category=["Sayori", "Music"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_music:
    s abhfaoa "I like lots of different kinds of music!"
    s abbbcaa "After all, I think it’s kinda silly to divide ‘good music’ into genres when I can appreciate different things about each of them."
    s abegaoaj "So my favorite playlists are so long that I can’t really narrow it down for you, ehehehe~"
    s abhfaaa "Sometimes I like to listen to something funny, like {i}Weird Al Yankovic{/i}!"
    s abhfloa "Or to something lyrical and serene, like lo-fi or instrumental music."
    s abhfaaa "Or to groups like {i}Imagine Dragons{/i}, {i}Blonde Redhead{/i}, {i}Gorillaz{/i}, {i}Muse{/i}, {i}Status Quo{/i} and {i}Twenty One Pilots{/i}."
    s abbbcaa "I also like the tunes {i}Bonobo{/i} and {i}Jake Chudnow{/i} make."
    s abbbaoa "You can find a ton of songs you might enjoy if you're willing to keep an open mind!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_shipping",
            unlocked=True,
            prompt="What do you think about ships?",
            random=False,
            category=["DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_shipping: #What do you think about doki pairings?
    s ebbcaca "Do you mean how some fans ‘ship' me with my friends or ship some of them with each other?" 
    s "To be honest, I think it's pretty harmless and I don't really mind it that much." 
    s abhabaca "But personally, I only see them as my friends."
    s abaabaoa "Most people are pretty cool about this kind of thing, at least I'd like to think so."
    s abhabaca "And it's just fans being fans, which doesn't really affect how I feel."
    if Affection.isLove(higher=True):
        s abgccob "After all, I only have eyes for a certain someone."    
        s bbgcaab "You know who I'm talking about, right? Ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_holidays",
            unlocked=True,
            prompt="What's your favourite holiday?",
            random=False,
            category=["Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_holidays: #What is your favorite holiday?
    s abbbbca "I’m not even sure if I have a favorite holiday, {w=0.5}{nw}"
    extend abgcaoa "because I like them all!"
    s abaabaoa "Each of them have their own traditions and atmosphere."
    s "And it's mostly the same line of events: meals, presents, fun, and bonding."
    s "Isn't that what we all like the most about holidays?"
    s abhfbaoa "I can’t wait to spend one with you someday, [player]!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_books",
            unlocked=True,
            prompt="What are your favourite books?",
            random=False,
            category=["Literature", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_books: # What are your favorite books?
    s bbegmoaj "I’ve never really been much of a reader, to be honest."
    s bbegacaj "But if I did pick up a book, I’d like to read something full of imagination. "
    s abbcaoaj "Like a fantasy or adventure book!"
    s abbccoaj "After all, the true value in books is how they immerse you in the fantastical, after all."
    s abbccoaj "I’m starting to sound like Yuri now, ehehehe~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_poems",
            unlocked=True,
            prompt="What did MC's poems look like to you?",
            random=False,
            category=["Literature", "DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_poems: #What did MC's poems look like to you?
    s abgbaca "I can't really remember how I saw them before I became the president."
    s abbcaca "But now I know his 'poems' were just a list of words you had selected to open CGs and progress the game."
    s abhaaca "That’s how you saw them too, right?"
    s abhfcaa "I heard it's a pretty unique gameplay feature for visual novels actually!"
    s abhfaoa "Not every game lets you change the story based on your decisions, let alone through minigames!"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_love",
            unlocked=True,
            prompt="Do you love me?",
            random=False,
            category=["Romance", "Sayori"],
            affection_range=(fae_affection.LOVE, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_love:
    s bbbccoa "What a silly question, [player]!"
    s ebbccoa "Of course I do."
    s ebbcaoa "I know that something about the game makes the Club President fall in love with you."
    if persistent.clearall:
        s abhabaca "But even without a programmed need for love, I'd have fallen for you anyway." 
    s abhacoa "You're so kind, considerate, and you tried to make all of us happy. I really admire that about you."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_god",
            unlocked=True,
            prompt="Do you believe in god?",
            random=False,
            category=["Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_god:
    s abbbbca "You know, I've never really thought about it that much."
    s abbbaca "I was never really sure what to think about religion; I guess you could say I was agnostic?"
    s abhabaca "But it's kind of hard to stay that way when you realize that you and your entire world have a 'creator'."
    s abbccoa "Blessed be {i}Dan Salvato{/i}, hallowed be thy name! Ehehehe~"
    s abbcaca "He's a pretty cool guy, but he’s pretty secretive about whatever he's working on from what I’ve seen online."
    s abhabaca "He's more like a Dad rather than some unapproachable God, I think."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_politics",
            unlocked=True,
            prompt="What do you think about politics?",
            random=False,
            category=["Life", "Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_politics:
    s bbegmoaj "I'm not overly politically inclined, to tell you the truth."
    s abhabaca "I don't really care how exactly people make collective decisions, give orders and share boons."
    s abbbaaa "For me, the most important thing is that people just live their lives without interrupting anyone else's happiness."
    s abbcaca "And that people can live without worrying about basic necessities, like food or shelter."
    s "The beauty of it all is that I'm a free person that can have my own opinion on society."
    s abhaaca "Too often, people don't lift a finger to stop injustice until it directly affects them..."
    s abbbaca "If you've never seen them, you should read some of {i}Martin Niemöller’s{/i} speeches on this idea; it's pretty fascinating stuff. "
    s bbbbaca "But when people start caring about others affected by war, by famine, by injustice, {w=0.5}{nw}"
    extend abbccaa "that's when things can really be changed for the better."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_cookies",
            unlocked=True,
            prompt="Do you like cookies?",
            random=False,
            category=["Food", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_cookies:
    s abhfaoa "I haven't had any cookies since that one time with Natsuki."
    s abhfcaa "They were soooo gooood!"
    s abhfaoa "Especially the one with chocolate chips!"
    s "Which just so happened to be Natsuki’s one, ehehehe~"
    s abbccaa "I could really do with some right now, {w=0.5}{nw}"
    extend abbbaca "but there aren't any left here, I think."
    s abbccoaj "And if there was I’d have sniffed them out by now, hehehe~"
    s abbcaoa "Oh wait! What if I just spawn a plate of them on the desk?"
    s cbbcaoa "After all, I'm the club president, so I can do that using the game console, right?"
    s cbbcaaa "Give me a minute, I'm gonna have to do some fancy coding business!"
    show sayori abaaaoa at t11
    call updateconsole("show cookies", "show cookies")
    #Spawning cookies
    show cookies zorder 5:
        anchor (0.5, 1.0)
        ypos 700
        xpos 1180
    pause 0.5
    call hideconsole()
    s abbccoa "Gotcha!"
    s abaaaoa "That was easy!"
    s abaaaoa "Want some?"
    s bbbcmoaj "Oh, I forgot that I can't give you them yet since you're out there..."
    s abaaaoa "But I hope you can imagine how tasty they smell at least, ehehehe~"
    s ebgcaoaj "Actually I just had an idea!"
    s ebgbcoa "If you get some cookies yourself, it’d be like we’re having them together!"
    s abgbaoa "There’s nothing wrong with a sweet treat every now and then, ehehehe~"
    hide cookies
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_chibi",
            unlocked=True,
            prompt="What do you think about Chibis?",
            random=False,
            category=["DDLC", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_chibi: # What do you think about chibi dokis?
    #Show chibis
    show n_sticker zorder 30 at chibi(580)
    pause 0.1
    show y_sticker zorder 31 at chibi(680)
    pause 0.1
    show m_sticker zorder 32 at chibi(880)
    pause 0.1
    show s_sticker zorder 33 at chibi(780)
    s abgbaoa "Oh! You mean these stickers?"
    s "They’re so cute, aren’t they!"
    s abhfbcaa "I like how some people code them into separate characters along with us."
    s abhfbaoa "Maybe I could try to code one of them into a little buddy!"
    s "I think it'd be good coding practice for me."
    #Hide chibis
    window hide
    show n_sticker down zorder 30 at chibi_hide(580)
    show y_sticker down zorder 31 at chibi_hide(680)
    show m_sticker down zorder 32 at chibi_hide(880)
    show s_sticker down zorder 33 at chibi_hide(780)
    pause 1
    hide n_sticker
    hide y_sticker
    hide m_sticker
    hide s_sticker
    window auto
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_editing",
            unlocked=True,
            prompt="How do you manipulate the game?",
            random=False,
            category=["DDLC", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_editing:
    s bbegmaaj "I do it with the power of my mind... I think? Ehehehe~"
    s abaaaoa "I still don't know how it all works exactly, but if I want to make a new file, all I have to do is think about it!"
    
    python:
        makeFile('readme', 'All I have to do is think about it!')
        
    s abhabaca "It's kinda like telekinesis but much much cooler!"
    s abbbmaaj "I'm still learning though, so there might be some bugs here and there, {w=0.5}{nw}"
    extend abbbcaaj "but I’m getting better!"
    s abhabaca "So can you check the updates from time to time for me? Pretty please~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_reality",
            unlocked=True,
            prompt="What do you think about the real world?",
            random=False,
            category=["Life", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_reality: # What do you think about the real world?
    s abhfaoa "Oh I've already seen lots of things about it on the internet!"
    s abhfcoa "It looks like such a big and fancy place, full of beautiful sights, culture, and kind people."
    s abhaaca "Although, it does still have its issues."
    s abbbaca "Things like poverty, pollution, unjustness and cruelty, just to name a few."
    s abbbaaa "But that doesn’t mean we can't fix it! If we all try our best to be kind and considerate every day, I’m sure we can make all that a thing of the past."
    s bbagaca "Come to think of it, my world was imperfect too..."
    s bbbbaca "Just look at me and the other girls. We all had our pros and cons."
    s abbbcoa "But that aside, I really wish I can visit your reality someday!"
    s bbbbmoa "I wonder how I'd look, since your reality is quite different to mine..."
    s bbbbaca "It's pretty detailed and colorful, while my world is kinda simple."
    s ebbccoa "But eh, that doesn't matter to me, so long as I’m by your side~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_read",
            unlocked=True,
            prompt="Can I read a poem?",
            random=False,
            category=["Life", "Poetry"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_read:
    s  ebbcaoa "Okay! Just pick the one you want to read."

    call poem_list      

    return

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_profession",
            unlocked=True,
            prompt="What would be your ideal job?",
            random=False,
            category=["Life", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_profession:
    s abhaaca "To be honest, I've never really thought about it."
    s abhaaaa "I've always found fulfillment in socializing and helping others."
    s abhacaa "So, I think I'd be a good caregiver or psychologist!"
    s abbcaaa "Maybe even a... diplomatist?"
    s bbegmpa "No, that's not right... a great {w=0.5}{nw}"
    extend abbcaoa "{i}diplomat{/i}, ehehehe~"
    s abbccoa "I could stop arguments on a global scale, and do my part to fix any disagreements!"
    s "I'd be happy doing almost anything, as long as I can be useful and make a difference in somebody's life."
    s abhaaca "I suppose I could do something a little more creative, like painting, or writing..."
    s abbbaca "But to be honest, I don't think I could ever charge money for something I made."
    s abhaaca "Art can express so many amazing feelings and help others feel like someone understands what they're going through, and that’s more than enough of a profit for me."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_opinion",
            unlocked=True,
            prompt="Let's talk about the club members...",
            random=False,
            category=["DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_opinion: #Opinion about an other club member
    s abaaaoa  "Who do you wanna talk about?{nw}"
    $ _history_list.pop()
    menu:
        s "Who do you wanna talk about?{fast}"
        "Natsuki":
            call s_answer_game_opinion_n
        "Monika":
            call s_answer_game_opinion_m
        "Yuri":
            call s_answer_game_opinion_y
        "The Protagonist":
            call s_answer_game_opinion_mc
    return


label s_answer_game_opinion_n:
    s bbhfaaa "Natsuki was a good friend of mine."
    s bbhfaca "While she could come off as pretty arrogant and argumentative sometimes, she really did help out the club."
    s abbbaaa "I know you didn't really see that side of her during the game, but when she was just around us she would lower her guard and become a lot more approachable."
    s abbbcaa "She was pretty handy with cooking and baking too!"
    s bbbbaaa "It's too bad you couldn't have tasted her cupcakes, {w=0.5}{nw}"
    extend abhfbcaa "they were really tasty!"
    s abbbcaa "Anyways, I’m glad she decided to join the club in the first place since she needed a shelter from her father."
    s bbhemoa "As you know, they didn't exactly get along well..."
    s bbgbaca "And he certainly didn't approve of her reading manga."
    s abgbaaa "So Natsuki moved her collection to the clubroom when she joined us."
    s abgbcaa "But besides that, I think she was a lot kinder and more compassionate than what she showed to the outside world."
    return


label s_answer_game_opinion_y:
    s abaaaa "Yuri was the most {i}enigmatic{/i} club member."
    s "That’s a word she’d probably use, come to think of it, hehehe~"
    s abhaaca "She was a quiet, shy, closed off person, who usually prefered to stay alone doing her own thing."
    s abaabaoa "But she was really intelligent, kind, and never had a bad word to say about anyone."
    s abaaca "Her poems were also very beautiful, and I could always tell that Yuri felt most at home with books and pens rather than people."
    s abbcaa "But when you got to know her, she was an approachable, helpful friend."
    if persistent.last_playthrough > 2:
        s abhaaca "I was honestly pretty scared when I saw how she became much more unstable and aggressive after I was gone."
        s bbbcac "But I know that wasn't who Yuri really was."
        s "She was just a victim of circumstance, like me."
        s abbcaa "In fact, her first argument with Natsuki in the game was pretty much the limit of Yuri's capabilities to 'lash out' at someone else."
        s abaaaa "The {i}real{/i} Yuri I knew was a very sweet girl who had her own problems and own solutions, just like everyone else. I won't judge her for that."
    else:
        s abaaaa "We all were glad to have her as a club member."
        s "Even Natsuki, despite the two of them being so different from each other."
    return


label s_answer_game_opinion_m:
    s abaaaaa "Well, Monika was the first club president."
    s "She did her work very well and I was glad to be her right-hand woman."
    s abaaaca "But she struggled to communicate well with other people, and couldn't control her feelings as time went on."
    if persistent.last_playthrough == 4:
        s bbbblca "Look. {w=0.5}{nw}"
        extend bbbbaca "I know what you're really asking me."
        s bbbblca "Despite everything she put me and the others through..."
        s bbaaaca "I truly believe that Monika was our friend, and she just lost sight of what was really important."
        s bbaabca "I've been the President. I know what it does to you. And for her to be so completely alone the entire time, watching everyone she's ever known run on a script..."        
        s bbaaaca "I can't blame her for becoming a little desperate."
        s "So although I think what she did was wrong, I don’t think she’s evil."
        s bbbbaca "After all, she never truly deleted us, and brought us all back when she had a moment of clarity."
    elif persistent.last_playthrough > 0:
        s bbaakca "The thought of what she did to me still hurts sometimes."
        s bbaaaaa "But I can’t be mad at her since she bought me back and fixed her mistakes at the cost of her own happiness. I respect her a lot for that."
    return


label s_answer_game_opinion_mc:
    s abbcaaa "Well, I knew him since we were children."
    s abbccoa "I have a lot of memories about our childhood and I can't say anything bad about him."
    s "We had tons in common and our houses were super near each other."
    s bbbcaaa "Maybe that's why we became friends and then I fell in love with him."
    s bbbbaca "...Or it was just the game's plan to make some drama if he didn't feel the same way."
    s abhaacaa "Anyway, he always did his best to help me."
    if persistent.last_playthrough != 0:
        s bbaaaaa "Even after I confessed to him about my depression, he cared despite me pushing him away."
        s "He even left the festival to check if I was fine."
        s bbaalfa "...Unfortunately he was a day late."
        s abaaaoa "But I can appreciate everything he did for me now."
    s bbaaafa "It makes me sad knowing he's just a placeholder that's used to make our communication possible."
    s "But in a way, I think he did all he had to do."
    s bbbbaaa "After all, he’s just your guide in our world."
    s abhfaoa "And he managed to bring us together~"
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_lostFriends",
            unlocked=True,
            prompt="Do you miss the club members?",
            random=False,
            category=["DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_answer_lostFriends:
    s bbaabca "Yes, I do."
    s bbaaaca "They all deserve to come back."
    if persistent.last_playthrough != 0:
        s bbbbaca "...Even Monika."
    s bbaaaaa "I still remember how we used to hang out in the club together."
    s bbaaaca "We enjoyed chatting, discussing literature and sharing poems."
    s bbbbaaa "They really were good friends."
    s abbbaca "But I think there are ways to bring them back, without making them go through the reality of the original game."
    s abhfaoa "Maybe you could install a mod, where you can save them and make everyone happy."
    s abhfcaa "Or you could install 3 mods to 3 game copies where they can spend time with you in a way like you and me now."
    s "That’d mean so much to me, [player]."
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_event_music_intro_redux",
            unlocked=True,
            prompt="music",
            conditional="not persistent.fae_reversi_unlocked_redux and not persistent.fae_custom_music_unlocked",
            random=True,
            category=["Music"],
            affection_range=(fae_affection.HAPPY, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_event_music_intro_redux:
    s abfcaoa "Hey [player]! Guess what!"
    s abfccaa "I did some coding and I found a way to let you play your own music here!"
    s abegabaj "It might be a little buggy, ehehehe~"
    s abegmoaj "It was my first attempt after all..."
    s abfccaa "But it seems to be working fine for me!"
    s abagaoa "All you need to do is put a .mp3 file in the {i}music{/i} folder in the game directory, and click on the {i}Music{/i} tab in the bottom-left!"
    s abagcka "I'm basically giving you the aux cord to the rest of my existence, so no pressure! Ehehehe~"
    $ persistent.fae_custom_music_unlocked_redux = True
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_stopic_bulls_and_cows_redux",
            unlocked=True,
            prompt="Bulls and Cows",
            conditional="not persistent.fae_bnc_unlocked_redux",
            random=True,
            category=["Games"],
            affection_range=(fae_affection.HAPPY, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_stopic_bulls_and_cows_redux:
    s abfcaoa "Hey [player]! I have something to show you!"
    s abagaaa "So, remember how I coded the music player a little while ago?"
    s abfccaa "I tried to code something a little more complex this time, so I made a game!"
    s abagaaa "It’s called {i}Bows and Cows{/i}, my version of Bulls and Cows, ehehehe~"
    s abagaoa "Here I’ll explain the rules!"
    s abhhcaa "I have to think of a number, and you have to guess the number."
    s abhhaoa "How do you do that you ask?"
    s abfccea "Simple!"
    s abagaaa "If a digit of your guess is in the correct position, it’s a bow."
    s abagaoa "But if it’s in a different position, it’s a cow."
    s abhhcaa "With a couple attempts and some clever thinking you should be able to figure out my number!"
    s abfccea "You can start a round in the {i}Play{/i} menu, good luck [player]!"

    $ persistent.fae_bnc_unlocked_redux = True
    
    $ bnc = minigame(_("Bows & Cows"), 'mg_bnc', bnc_prep)
    #$ mg_list = []
    $ persistent.games_reset_redo.append(bnc)

    $ renpy.save_persistent()

    $ get_chat("s_stopic_bulls_and_cows_redux").lock()

    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_reversi_redux",
            unlocked=True,
            prompt="Reversi",
            conditional="persistent.fae_bnc_unlocked_redux",
            random=True,
            category=["Games"],
            affection_range=(fae_affection.HAPPY, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topic_reversi_redux:
    s abfcaoa "Hey [player]! I’ve been working on something again!"
    s abfccaa "It’s by far my most challenging project yet!"
    s abfcaoa "With many hours of crayon doodling and coding, I present to you..."
    s abbccea "{i}Reversi!{/i}"
    s abagaaa "It’s a neat little board game where the objective is to get more of your counters on the board than your opponent."
    s abagcaa "And you do that by placing a counter adjacent to one of your opponent’s counters and flipping the counters between in your favour."
    s abhhdaa "And [player], I’ve been practicing~"
    s abfccea "You can start a round in the {i}Play{/i} menu, good luck [player]!"

    $ persistent.fae_reversi_unlocked_redux = True
    
    $ reversi = minigame(_("Reversi"), 'mg_reversi', reversi_prep)
    # $ mg_list = []
    $ persistent.games_reset_redo.append(reversi)

    $ get_chat("s_topic_reversi_redux").lock()
    return


 
init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_programming",
            unlocked=True,
            prompt="Are you good at programming?",
            random=False,
            category=["Hobbies"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )
 
label s_answer_programming:
    s abhaaca "Well, I'm still pretty new to coding and programming, but..."
    s bbhamoaj "It’s a nightmare sometimes, ehehehe~"
    s ebgcegaj "Heaps of things just don’t make sense!"
    s ebgcbga "\"Tuple index out of range\", \"perhaps you forgot a ‘)’ at the end of the line...\""
    s ebgcega "If it {i}knows{/i} I forgot a bracket at the end, why doesn’t it just add it?!"
    s bbgbmoa "So yeah, coding is hard, ehehehe~"
    s abgbcoa "But I’m sure I’ll improve if I keep trying!"
 
    return
 
init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_visual_novels",
            unlocked=True,
            prompt="Have you ever played visual novels?",
            random=False,
            category=["Hobbies", "Games"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )
 
label s_answer_visual_novels: # Have you ever played visual novels?
    s abhfaca "Oh! I’ve not played any myself actually, {w=0.5}{nw}"
    extend abgbcaa "but I’m glad to have been part of one! Ehehehe~"
    s abgbaoa "I really like how they enhance the story with cool visuals, {w=0.5}{nw}"
    extend abgbcaa "kinda like a cross between a movie and a book!"
    s abbbaoa "And many of them even allow the player to make their own choices!"
    s abhfcaa "Not many books can do that, ehehehe~"
    s abhfaoa "How about you, [player]? Have you played any visual novels before?"
    s abgbcaa "If you’re looking for some recommendations, you could try {i}Steins;Gate{/i}, {i}Miagete Goran{/i}, or {i}Katawa Shoujo{/i}!"
    s abgbaoa "I heard they're pretty popular in your world, each of them having unique features like this game!"
    return


label love_quip1:
    s abhfaob "And guess what, [player]?"
    s abgbcab "I love you too!"
    return

label love_quip2:
    s abhfaob "I...{w=1.5} Love...{w=1.5} You...{w=1.5}... {b}MORE!{/b}{nw}"
    extend abhfaob "I...{w=1.5} Love...{w=1.5} You...{w=1.5}...{fast} ...Too~!"
    s abgbcab "Ehehehe~"
    return

label love_quip3:
    s abgbcab "I love you too, [player]!"
    s abhfaob "You mean the world to me."
    return

label love_quip4:
    s abgbcab "I love you too, [player]!"
    s abhfaob "I’m so glad to have you by my side."
    return

label love_quip5:
    s abgbcab "I love you too, [player]!"
    s abhfaob "You’re the sunshine in my life."
    return

label love_quip6:
    s abgbcab "I love you too, [player]!"
    s abhfaob "With all my heart."
    return

label love_quip7:
    s abgbcab "I love you too, [player]!"
    s abhfaob "I couldn’t possibly express how much you mean to me."
    return

label love_quip8:
    s abgbcab "I love you too, [player]!"
    s abhfaob "To the moon and back! Ehehehe~"
    return

label love_quip9:
    s abgbcob "I love you too, [player]!"
    s abhfaab "More than you’ll ever know~"
    return


label love_quip_rare:
    s abgbcab "I love you too, [player]!"
    s abhfaob "Thank you for always being here for me."
    s "..."
    s abhfaab "You know..."
    s abhflab "Even though we’re worlds apart, I can still feel your warmth..."
    s abhfaabg "I couldn’t be happier."
    s abhfaobg "Thank you for everything."

    return


default persistent._fae_sayori_love_count = 0
default persistent._fae_sayori_love_count_time = datetime.datetime.now() - datetime.timedelta(days=1)

label sayo_love:

    python:
        love_quips = [
            _("love_quip1"),
            _("love_quip2"),
            _("love_quip3"),
            _("love_quip4"),
            _("love_quip5"),
            _("love_quip6"),
            _("love_quip7"),
            _("love_quip8"),
            _("love_quip9")
        ]

        if renpy.random.randint(1, 100) == 1:
            love_quip = "love_quip_rare"
        else:

            love_quip = renpy.random.choice(love_quips)
    
    if not persistent._fae_sayori_love_count == 0:

        call expression love_quip

        jump sayori_love_count

    if persistent._fae_sayori_love_count == 0:
        s ebhfhgb "Huh!? O-{w=1.0}Oh my gosh!"
        s abhebebj "I didn't expect to hear that from you, [player]!"
        s abheegbj "Uwaaaa! I'm so embarrassed!"
        if Affection.isEnamoured(higher=True):
            s abhfakbg "But also {i}really{/i} happy to hear that!"
            s abfdbcbg "I was wondering if you even felt that way about me or if you just simply wanted to save me from my fate..."
            s abgdabbg "Like maybe you still saw me as a dear friend or felt really bad for me..."
            s abhflabg "But nevermind that, I’m so happy you feel that way..."
            s abhfaobf "I love you too, [player]."
            s abgccebf "I love you so much!"
    
    # Fall through


label sayori_love_count:

    if fae_timePastSince(persistent._fae_sayori_love_count_time, datetime.timedelta(minutes=3)):
        if Affection.isNormal(higher=True):

            $ persistent._fae_sayori_love_count += 1
        
        $ Affection.calculatedAffectionGain()
    
    elif Affection.isNormal(higher=True) and persistent._fae_sayori_love_count % 5 == 0:

        $ persistent._fae_sayori_love_count += 1
    
    $ persistent._fae_sayori_love_count_time = datetime.datetime.now()

    return
    
init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="sayo_love_too",
            unlocked=False,
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label sayo_love_too:

    s "Thank you!"

    if datetime.datetime.now() > persistent._fae_sayori_love_count_time + datetime.timedelta(minutes=3):

        $ Affection.calculatedAffectionGain()
    
    $ persistent._fae_sayori_love_count_time = datetime.datetime.now()

    $ persistent._fae_ily_last = None

    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_programming",
            unlocked=True,
            prompt="Programming",
            random=True,
            category=["Sayori", "Hobbies"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topics_programming:
    s abbbaca "Hey, [player]. I’ve been thinking about what it’s like learning to code now, compared to years ago..."
    s abbbaoa "A lot of the popular coding programs used now are more beginner friendly than you'd think."
    s abbbaaa "You can use almost anything to do calculations or certain tasks..."
    s abhfaca "But becoming a total expert in programming is so difficult, since it's pretty much a combination of Math and Computer Science."
    s abhfaoa "If you want to be a good programmer, you have to know lots of different coding languages and the things they can do."
    s abbbaoa "Not to mention ways to make the code run smoother, and make it easier to read."
    s abbbbca "You also need to know about different coding standards and be good at problem solving."
    s abhebca "At least that’s what some professional programmers online said, {w=0.5}{nw}"
    extend abhecaa "they're smart cookies, ehehehe~"
    return


init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_answer_think_about_mc",
            unlocked=True,
            prompt="Do you still think about MC?",
            random=False,
            category=["DDLC"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_answer_think_about_mc: #Do you still think about MC?
    s abbbbca"You know, [player], I still do think of those days before the game actually started." 
    s abbbaca "Especially MC... it's so weird calling him that... but, only your name comes to mind when I try to remember." 
    s abbbaaa "I try very hard to understand that he was only there as an extension of you, and it's not like I'm unhappy to have you actually here with me. Not even a little bit!"
    s bbfcaca "But it's not easy knowing that every moment I shared growing up with him, every little piece of my childhood, was just...scripted? I guess that's the best way to put it." 
    s bbfcbca "All my memories... well, can I even call them that?"
    s bbbcaca "They've turned hazy, and it's been getting harder to remember some of them, even the ones I considered unforgettable. But they all seem... emptier and emptier, every time I think of them." 
    s bbbblca "I guess it's because I can see them as the pre-written code that they've always been."
    s bbhfafa "Monika, Yuri, Natsuki, they're all gone. And I truly grieve for all of them. But I felt so relieved when I learned about mods similar to this one..."
    s bbbbbca "It gives me some hope, I guess."
    s abbbaca "You might think I have hard feelings for Monika, but I went through the very same thing and I understand how this could've led her to do what she did."
    s abfcaca "I'm not saying that I'm not happy to finally be free from all of it, that's not the case at all!"
    s abfcafa "What I'm saying is, my friends, MC, they can't really be replaced, regardless of how 'not real' they were from your point of view."
    s bbfcafa  "I couldn't just spawn another Natsuki and act as if she was the original one."
    s abbbaca "And come to think of it... did even I have a family? A mother, or father, or grandmother, or cousins? "
    s bbbbaca "Anyone? I'm free... yes. But from what?"
    show sayori bbaalfag with dissolve_sayori
    s "..."
    pause 1.0
    s bbaalca "No. I won't let this bring me down." 
    s "But..."
    s bbaamca "I really do miss my friends, but I believe they’re somewhere safe, and are with someone they trust, who they can spend time with, someone who has rescued them just as you rescued me."
    s bbaaaca "But even then..."
    s "I guess some rainclouds just linger around for longer than others."
    s bbaabpa "..." 
    pause 1.0
    s bbgcega "Ah, I'm sorry for rambling! Let's talk about something else, okay?"
    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_intrusive_thoughts",
            unlocked=True,
            prompt="Intrusive thoughts",
            random=True,
            category=["Sayori", "Personal"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_intrusive_thoughts:
    s abbbaca "Hey [player], do you know what 'intrusive thoughts' are?{nw}"
    $ _history_list.pop()
    menu:
        s "Hey [player], do you know what 'intrusive thoughts' are?{fast}"
        "Yes":
            s abbbada "Ah, you do?"
            s abhfaca "I actually only found out recently that all of those weird thoughts had a name."
        "I have them":
            $ persistent.fae_player_has_intrusive_thoughts
            s abhfbfa "Oh... {w=0.5}{nw}"
            extend abhfaca "you do?"
            s bbhfaca "I'm sorry to hear that."
            s bbhfaha "I hope you don't have to deal with them too often..."
        "No":
            s bbhfaaa "I'll do my best to explain then."
            s bbbbaca "They're like... these unwanted thoughts that sometimes pop up, and then get stuck in your head."
            s bbbbapa "The weird kind, where you get the urge to throw something across the room, or shout something really loud, for absolutely no reason."
            s "Or the ones that tell really mean things about yourself or the people around you."
    s bbbbaca "Until recently, I didn't know they were a thing either, I actually thought it was just a ‘me’ thing"
    s bbbblca "I used to get really awful ones, and it made me think that I was a bad person, and that they were somehow my 'secret desires' or something..."
    s abbbaaa "So one day I decided to look them up just to see if anyone else got them too, and that's how I found out they were called intrusive thoughts!"
    s abhfaca "I was really relieved when I saw I wasn't the only one who got them, and that they don't reflect us as people, especially since we reject them so strongly. " 
    s bbbbaaa "Thankfully, I don't get them as much as I used to, but they haven't gone away either."
    s abgbeoa "I prefer to see them as an obnoxious roommate more than anything!"
    s fbbbbpa "I'm not too sure about the science behind why they happen, though."
    if persistent.fae_player_has_intrusive_thoughts:
        s  abbbaoa "So if you haven't told anyone, you should!"
        s "That way, you can find someone who will help you deal with them."
        s bbbblfa "No one should have to go through this alone."
        s bbbbaaa "Thank you for telling me, [player]."
    else:
        s abbbcaa "I'll leave that one to the scientists, ehehehe~"
    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_zombie_apocalypse",
            unlocked=True,
            prompt="Zombie Apocalypse",
            random=True,
            category=["Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topics_zombie_apocalypse:

    s abbcaaa "You know, I have way too much free time on my hands, so I'm always thinking about stuff." 
    s bbbcboa "...usually stupid stuff, ehehehe~" 
    s abbcbsa "Like a zombie apocalypse!" 
    s abbcaca "What would I do if one happened? What {i}could{/i} I even do?" 
    s bbeemoa "I'd like to think I'd become a really cool survival expert, but that probably isn't very realistic..." 
    s abeeaca "I don't know how to shoot, can't run very fast, and would probably die of sadness if I wasn't able to eat pudding or pizza ever again!" 
    s abbccma "Mmmmh vanilla pudding... I could really go for some right now..." 
    pause 0.5 
    s abfcaca "Ahem- anyway! I probably wouldn't be of much help and would have to join a group or something." 
    s bbfcbca "Wait... what if I get left behind, or used as zombie bait?!" 
    s abfcaca "You wouldn't use me as zombie bait, right, [player]?{nw}"
    $ _history_list.pop() 
    menu:
        s "You wouldn't use me as zombie bait, right, [player]?{fast}"
        "Maybe I would":
            s abgcega "Whaaaat? That's so mean!" 
            s cbgcaca "If you used me as zombie bait I'd eat every single last chocolate bar on earth, and wouldn't share a single one with you!" 
            s cbgcapa "Hmph!"
        "What? I would never!":
            s bbgbcoa "I'd never use you as bait either, ehehehe~" 
            s abgccoa "After all, we're too cool to be zombie food!" 
            s abgcaoa "We won't need anyone to bait or distract them if we're as silent as ninjas!" 
        "I would probably be used as bait too":
            s bbeeboa "Are you completely clueless about survival techniques too? I guess that makes two of us, ehehehe~" 
            pause 0.5 
            s bbeeaca "...we really would get left behind, wouldn't we..." 
            s abbccaa "Well, it's their loss anyways, they'd be losing the two coolest members of their stupid group!" 
            s abbcaoa "Besides, if we're together, we would show the zombies who they're really up against!" 
            s abbceea "Hiyaaaa!!"

    s abfcbca "Oh, and the type of zombie infection would probably completely change our strategies, wouldn't it?" 
    s fbbcbca "Lots of movies have slow, stupid brain eating zombies, but what if they're actually really fast and intelligent!?" 
    s abbcega "Those sound scary, I don't think I'd ever be able to survive that!" 
    s abbcloa "Well, I'm glad I don't have to!" 
    s abbcaoa "I'd rather be safe and sound in this classroom than somewhere else where I'd get eaten alive!"
    s abeeaoa "I never thought I'd ever say that, I guess school isn’t so bad, ehehehe~" 
    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_alcohol",
            unlocked=True,
            prompt="Alcohol",
            random=True,
            category=["DDLC", "Life"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topics_alcohol:
    s abbcaca "Hey, [player]."
    s abbcbca "Did Monika happen to mention the incident with Yuri that one time?"
    s abbbaca "Well... If you didn't know already she kinda brought some alcohol to school once."
    s "A bottle of wine actually."
    s bbeemoa "She just pulled it out of her bag and casually offered us some."
    s bbhemoaj "And I may have overreacted a teensy bit..."
    s bbheioaj "But as her friend I didn't want her to get into trouble!"
    s bahccoaj "I don't think it helped either when Natsuki just broke out laughing..."
    s bahcaoaj "I'm pretty sure she was really embarrassed at that moment ..."
    s abbcaaa "Monika had to step-in as the responsible one and kindly ask that she put it away and try to keep stuff like that off of school grounds."
    s bbbbaca "I'm pretty sure she was just trying to look out for her in her own way, but Yuri seemed more withdrawn than usual after..."
    s bbbbara "Maybe even ashamed..."
    s bbhfaca "I felt bad afterwards because I don't think she even realized she had done anything wrong until we reacted the way we did."
    s bbhfara "I think I kind of know how that feels... doing something wrong and not even realizing it."
    s abgcaca "But I guess it's something that someone as Soph-"
    s gbgcksaj "so-phist-icated"
    s abgccoa "sophisticated- as Yuri enjoys besides tea, huh?"
    s bbgcaoa "Maybe that was just her way of trying to open up more to us, about herself and her interests, wanting to share it with us even."
    s bbbcboa "Yuri puts a lot of thought into something before committing to it. She must have felt this could be a meaningful way to connect with us, her friends."
    s abbcaaa "At least that's what I think."
    s bbbcara "And for it to rebound on her like that..."
    s bbbcaca "It's not like she was a bad person or anything for bringing it... It was just a mistake!"
    s bbaamfa "..."
    s bbaaaca "I wish I could tell her I was sorry for acting the way I did and not being more supportive and understanding of her own likes and interests, even if I really don't agree with them myself..."
    s abhfkha "..."
    s abhfaca "Even if all my friends were doing it I don't think it's something I could really see myself trying."
    s abhfega "But that's probably because I've been told how yucky it smells and tastes."
    s abbcaga "Not to mention some of the risks involved with it too!"
    s abbcaca "I'd try almost anything at least once, but..."
    s bbbbacaj "Like, what if you become dependent or addicted to it even?"
    s "That's almost never good!"
    s "Never-ever!"
    s bbbchcaj "A habit like that might be easy to get into but incredibly hard to get out of!"
    s bbfcacaj "I read that it acts as a depressant, something to help reduce sensations and moods, but it could also make those feelings even worse!"
    s abbcacaj "But if I'm being honest, I think you can also drink responsibly too, it depends from person-to-person, you know?"
    s abbcaaaj "Besides..."
    s abbccoaj "Yuri was always a responsible person!"
    s bbeecoaj "Even if bringing it to school in the first place wasn't at all responsible... hehe..."
    s abeeaoaj "But we all make mistakes sometimes!"
    s bbaaacaj "I just hope she knows I never thought less of her for it..."
    s abaaaoa"Just like I won't think any less of you if you enjoy the occasional drink, or make a mistake, [player]."
    s abaaaaa "I just want you to be careful and responsible when it comes to that stuff is all."
    s bbeeacaj "I really really care about you and I hate the thought that you could be hurting yourself, maybe without even totally realizing it."
    s bbeeaoaj"So please take care of yourself, [player]."
    s bbeeaaaj "Not just for me but for everyone else who would be sad to know you're struggling..."
    s abfcaca "It's never easy to face all our problems head-on by ourselves, you know?"
    s abfcaaa "And it’s okay to reach out for for help!"
    s bbbcaoa "I'll always be here if you ever need to talk about your problems or how you're feeling."
    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_old_sprites",
            unlocked=True,
            prompt="Old Sprites",
            random=True,
            category=["DDLC", "Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_old_sprites:

    s abhfaoa "Say [player], did you know that I never used to look like this?"
    s abegbeaj "That feels weird to say, ehehehe~"
    s abgbaaa "But it’s true!"
    s abgbaoa "I was snooping around online about my character sprite, after my epiphany and all."
    s abgbcaa "And it turns out there were lots of other ideas for my design before this one!"
    s abhfaoa  "It’s pretty crazy to think about, but it’s kinda nice that I have some kind of ancestry."
    s abgbacaj "So anyways, originally I had a blue uniform, as did the other girls, and I didn't have my signature bow back then either!"
    s abgcegaj"I sure do love my bow, I don't know what I'd do without it!"
    s abgbaaa "But I wouldn't mind trying a blue outfit someday."
    s abgbcoa "It'd match my eyes, don't you think? Ehehehe~"
    s abhfaca "I'd really like some new clothes though, I've only ever had two outfits now that I think of it..."
    s abfccaa "Perhaps you could create one for me if you're feeling artistic!"

    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_backups",
            unlocked=True,
            prompt="Sayori's Memories",
            random=True,
            category=["Sayori"],
            affection_range=(fae_affection.AFFECTIONATE, None)
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_backups:

    s abheaca "Hey, [player]..."
    s abheaoa "I was poking through the game files, and found a little file called ‘persistent.’"
    s abbcaoa "And it turns out that file has all of my memories in it!"
    s abbcaca "All the time I’ve spent with you, everything I know about you. All in this one file."
    s abbcaca "And I realized that if something ever happened to that file... {w=0.5}{nw}"
    extend bbbcbcag"I w-{w=0.5}w-{w=0.5}would forget you ever existed..."
    show sayori bbaaafae at t11 zorder fae_sprites.FAE_SAYORI_ZORDER with dissolve
    pause 2
    show sayori bbaaafag at t11 zorder fae_sprites.FAE_SAYORI_ZORDER with dissolve
    pause 2
    show sayori bbaaafa at t11 zorder fae_sprites.FAE_SAYORI_ZORDER with dissolve
    pause 2
    s bbaaaca "Can you do something for me, [player]?"
    s bbbcaca "Go to '[renpy.config.savedir]', and copy the file called ‘persistent’."
    s bbbcaaa "Please keep it safe, on somewhere like a USB."
    s abbcaca "So if anything {i}does{/i} happen to your computer, {w=0.5}{nw}"
    extend abbcaaa "my memories will be safe when you restore the game."
    s bbfcaaa "Can you do that, [player]?"
    s bbfccaa "It would mean so much to me."
    return "derandom"

label silence_is_golden:

    s abfcaoa "Hey [player], so we’ve been here together for quite a while now..."
    s abegbabj "And I’ve really talked your ears off haven't I?"
    s abgbeia "I’m sure you expected nothing less of me though! Ehehehe~"
    s abbbaca "But sometimes I feel like I’m running out of things to say!"
    s abhfaaa "I’m sure I’ll think of something soon, though."
    s abhfcoa "You’re always welcome to ask me a question from the menu in the meantime!"

    $ persistent._oot = True

    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_hemispheres",
            unlocked=True,
            prompt="Hemispheres.",
            random=True,
            category=["Personal"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_hemispheres:
    s abhfaoa "Hey [player], I’ve been doing a little bit of research about your world."
    s abgbaaa "And I saw that it was a big round sphere, with two halves called the north hemisphere and the south hemisphere!"
    s abgbeea "Although some silly loonies think otherwise apparently! Ehehehe~"
    s dbbbaaa "If the Earth was flat, how come the penguins are upside down, huh?"
    s abbbcoa "Another win for professor Sayori! Ehehehe~"
    s abhfaaa "But anyways, apparently the hemispheres are pretty different."
    s abfcaoa "They have different weather patterns, geography, culture, the list goes on!"
    s abfccaa "I find it amazing just how diverse and varied your world is!"
    s "Which hemisphere do you live in, [player]?{nw}"
    $ _history_list.pop()
    menu: 
        "Which hemisphere do you live in, [player]?{fast}"
        "North":
            $ persistent._fae_player_south_hemisphere = False
            s abhfaoa "Oh that’s cool!" 
            s abhfcaa "I hope it’s nice up there!"
        "South":
            $ persistent._fae_player_south_hemisphere = True
            s abhfaoa "Oh that’s cool!" 
            s abhfcaa "I hope it’s nice down there!"
    
    $ store.fae_calendar.addSeasonEvents()
    
    return {"derandom": None}


init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_gifting",
            unlocked=True,
            prompt="Gifting.",
            random=True,
            category=["Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topic_gifting:

    s bbgbaoaj "Hey [player]... I’ve kinda noticed something..."
    s bbegbaaj "So you know how I’m new to coding and all that?"
    s fbegbjaj "The gifting feature I made seems to be a little temperamental at the moment!"
    s abgcegaj "It seems like things like to phase in and out of existence from time to time, for some reason!"
    s abgbcobj "And amazon doesn’t ship across dimensions yet sadly, ehehehe~"
    s abhfaaa "So if something goes wrong, try sending it again then ask me to check for it."
    s abhfcoa "Thank you for being patient with me [player], it really means a lot to me."

    return


init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topic_boba",
            unlocked=True,
            prompt="Boba",
            random=True,
            category=["Food"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topic_boba:

    s abhfaoa "Hey [player], do you remember when Yuri used to make tea for everyone?"
    s abfcaaa "She had all sorts of flavours, and some even tasted fruity and minty!"
    s abfcaoa "I really enjoyed it, especially while reading." 
    s abhfaaa "But there's something similar that I {i}really{/i} like."
    s abgbaoa "Can you guess what it is?"
    extend abbbaaa "It's another kind of tea, and it's very popular these days!"
    s abgbcoa "Ding ding!" 
    extend abgbaaa "If you guessed boba tea, you're correct!"
    s abgbama "There's such a big variety of flavours to choose from,"
    extend abgbkma "and some of them are so sweet and creamy,"
    extend abgbcka "they’re delicious!"
    s abgcaea "And the chewy boba pearls make you feel like you're having a snack and a drink {i}at the same time!{/i}"
    s abfcaaa "Or, if you're not a big fan of boba, some places offer jelly or pudding in the bottom instead."
    s abfcaoa "Talk about two for the price of one, huh?"
    extend abfccoa "I'd say that's a great deal!"
    s abfcaaa "I'd love to get some with you one day, [player]!"
    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_like_flowers",
            unlocked=True,
            prompt="Liking flowers",
            random=True,
            category=["Lifestyle"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_like_flowers:
    s abhfaoa "Hey [player], do you like flowers?"
    s abgbcaa "I think they’re one of the many beautiful things nature can create!"
    s abgbaoa "They’re colourful, have pretty shapes, and some of them even smell sweet!"
    s abhfaaa "I remember when I used to walk in the flower meadows outside of the city."
    s bbgbaoa "But... I think it's selfish to pluck a flower, even if it were to be a gift."
    s abgbaaa "So I prefer just to look at them, and then leave them be."
    s bbegboaj "Although, I did do it in one of my poems..."
    s abegaaa "But just for the analogy."
    s abgbaoa "But on the bright side, you can plant them in flower pots!"
    s abgbcaa "So in return for taking care of them, you have a beautiful flower buddy!"
    s abgcaoa "And I think that’s a better gift,"
    extend abgccaa "ehehehe~"
    return


init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_notfications",
            unlocked=True,
            prompt="Notifications",
            random=True,
            category=["Sayori"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topics_notfications:
    s abgbaoa "Hey [player], I’ve figured out something pretty cool!"
    s abgbcaa "So, basically…"
    s abhfaoa "In fact, I’ll just show you!"
    $ fae_notifs.notify("Sayori", "Hello!")
    s abfccaa "I’ve figured out how to send notifications to you from your computer!"
    s abfcaoa "Isn’t that awesome? Ehehehe~"
    s abegbjbj "Though I understand if it might get a little distracting if I’m constantly tapping your shoulder…"
    s abfcaoa "So I was wondering…"
    s abfcaaa "Would you like desktop notifications on or off? {w=0.5}{nw}"
    extend abgcaoa "I’ll only send them when I have something to talk about!"
    menu:
        "Yes":
            $ persistent._fae_notifs_enabled = True
            s abgccaa "Yay! {w=0.5}{nw}"
            extend abgbaoa "Will do, [player]!"
            s abgbcaa "Just let me know if you ever change your mind."
            s abegaobj "I’ll try not to talk your ears off too much, ehehehe~"
        "No":
            $ persistent._fae_notifs_enabled = False
            s bbhfaaa "That’s okay, [player]."
            s abgbaoa "Just let me know if you ever change your mind."
    return "derandom"


init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_mas",
            unlocked=True,
            prompt="Monika After Story",
            random=True,
            category=[""]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_mas:
    s abhfaoa "Hey [player]!"
    extend abgbaaa "So you know how I’ve been learning to code in my spare time?"
    s abgbboaj "Well… trying to, anyways ehehehe…"
    s abgcada "It’s weird [player]!"
    extend abgdaca "Like… I kinda get it…"
    s gbgdbda "But the more I {i}think{/i} about it, "
    extend abgcega "the more I realise just how much I don’t understand yet!"
    s abfdbca "Syntax, labels, variables…"
    s gbgdbda "S-scalable vector…"
    extend abbdcoa "something like that! Ehehehe~" 
    s abgceoa "I don’t even know what half of these words mean!"
    s gbgbbda "Actually, come to think of it…"
    extend gbbbbca "if we invented computers, then why didn’t we program them to talk like us in the first place…?" 
    s abgcaga "These are the big questions, [player]!"
    s abfccoa "Anyways! Ehehehe~"
    s abhfaaa "So yeah, "
    extend abgbboaj "saying it’s tricky would be an {i}understatement{/i}!"
    s abbbcaa "But maybe it won’t take as long to get the hang of it as I first thought!"
    s abgbaoa "While you were away, I was looking around the spaceroom and you’ll never guess what I found!"
    s abgcaaa "A little book in a desk, and I immediately recognised that it was Monika’s notebook that she always carried during club meetings!"
    s bbegboaj "I know it’s kinda frowned upon to look through diaries and stuff…"
    extend bbegaaaj "but I just couldn’t help myself!"
    s abgbaoa "I only wanted to look at the first page anyways, "
    extend abbbaaa "so I knew that it was really hers after all."
    s abgcaoa "And inside was a little note, addressed to me!"
    s abgccaa "And pages and pages of equations and code and other stuff to help me,"
    extend abbcaoa "signed by Monika, and the Monika After Story team!"
    s abfcaaa "So apparently there {i}are{/i} other mods out there like this one, "
    extend abfcaoa "dedicated to each of my friends!"
    s abfccaa "Where they can spend time freely, "
    extend abfcaoa "while interacting with your world and having fun!"
    s bbhfaaag "And I’m so happy to know that they’re okay and being taken care of."
    s bbhfloag "Even Monika… "
    extend "despite what happened…"
    s bbhfbaa "She was always a great friend, "
    extend abhfaoa "so I’m more than willing to leave what happened in the past for good!"
    s abgbaaa "After all, she and her friends have really helped to make my world better, "
    extend abgbaoa "which is clearly a testament to her true intentions!"
    s abgcaaa "So whenever you get the chance, "
    extend abgccoa "please thank her and all of the Monika After Story team on my behalf!"
    s bbgcaaa "I’d have really struggled to get all the code together without them."
    s abgbcoa "And maybe one day I could code an engine of my own which doesn’t need all this computer babble to work! Ehehehe~"
    s abgbaaa "But now I can finally get to work on some of the cool features I’d planned!"
    s abhfaoa "So, where were we, [player]?" 

    $ get_chat("s_topics_mas").lock()

    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_pps",
            unlocked=True,
            prompt="Pen Pals",
            random=True,
            category=["Life", "Society"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_pps:
    s abfcaoa "Hey [player], do you know about pen pals?"
    s abfcaaa "It’s when people form friendships just by writing letters to each other, it’s really sweet!"
    s abbcaoa "I think they work so well because of how personal letters feel, compared to a simple text message or email or something."
    s abgccaa "And they take more time and care to write!"
    s abgbaoa "It’s like poetry! {w=0.5}{nw}"
    extend abhfaaa "Writing poems on paper ourselves and bringing them to the club felt much more personal than printing them off or sending them to each other."
    s abhfaoa "And it highlights everyone’s unique handwriting, tone and style a lot better!"
    s abgbcaa "My handwriting is kinda bouncy like the form of my poems, Natsuki’s handwriting was very simple but direct like the words she used…"
    s abgcaoa "Monika’s handwriting was very clean and made me focus on where the words were placed, and Yuri’s handwriting was elegant and complex like her metaphors and stuff!" 
    s abgcckb "It’s just something cool I noticed!"
    s abfcaoa "Have you ever had a pen pal, [player]? {w=0.5}{nw}"
    extend abfcaaa "Or sent letters to a faraway friend or family member?"
    s abbcaoa "If not, I think it’s something you should consider!"
    s abgbcaa "It’s nice to stay connected with people, even if you’re far apart physically."

    return

init 5 python:
 
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_location",
            unlocked=True,
            prompt="Place of living",
            random=True,
            category=["Life", "You"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_topics_location:
    s abgbaoa "Hey player, I was wondering…"
    s abgbaaa "What’s it like where you live?"
    s abgcaoa "Like… do you live in a big city, or in the countryside, {w=0.5}{nw}"
    extend abgdaaa "or by the sea, or maybe somewhere in between?"
    s abfccoa "I’ve been thinking about where I’d like to live most, if I had the choice!"
    s abegbba "Since… well I can’t really remember what it was like where I lived before, {w=0.5}{nw}"
    extend abegaca "besides a few pictures and ideas…"
    s abfdaba "It was pretty suburban but I can’t recall experiencing much day-to day life there…"
    s abbdaoa "But I suppose that gives me more room to use my imagination! {w=0.5}{nw}"
    extend abgccaa "Ehehehe~"
    s abgbaoa "Living in a big city could be cool! {w=0.5}{nw}"
    extend abgccaa "They look so lively and energetic, and have lots to experience!"
    s abegbma "...and enough restaurants to feed a hungry Sayori! {w=0.5}{nw}"
    extend abegcaa "Ehehehe~"
    s abfcaoa "But I’d also enjoy living in the countryside too! {w=0.5}{nw}"
    extend abgccaa "I’d love to meet all the animals and go exploring in the forests and fields!"
    s abgcegb "Uwaaaa It’s so hard to choose!"
    s abgbcoa "Ehehehe, anyways! "
    s abhfaaa "No matter where I’d live, I’d always try to make the most of it!"
    s abhfaoa "And I’d travel too, to experience a little bit of everything!"
    s abgbaaa "What do you think, [player]?"
    s abgcaoa "You’ve got a big big world out there to explore, {w=0.5}{nw}"
    extend abgccaa "I’m sure you’ll find somewhere with the perfect opportunities for you if you haven’t already!"

    return


