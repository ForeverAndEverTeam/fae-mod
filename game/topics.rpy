default persistent.seen_topics = {}

init -5 python:
    class Topic:
        def __init__(self, label, available = True, show_prompt = True, name = None, id = None, related = None):
            self.label = label
            self.available = available
            self.show_prompt = show_prompt
            self.name = name or label
            self.id = id or label
            try:
                iter(related)
            except TypeError:
                if related is not None:
                    related = [related]
                else:
                    related = []
            finally:
                self.related = related
        
        def __getattr__(self, attr):
            if attr == 'seen':
                return persistent.seen_topics.get(self.id) == True
        
        def __setattr__(self, attr, value):
            if attr == 'seen':
                persistent.seen_topics[self.id] = value
            else:
                self.__dict__[attr] = value
        
        def __call__(self, *args, **kwargs):
            global justIsSitting
            
            self.seen = True
            
            config.allow_skipping = True
            config.skip_indicator = True
            justIsSitting = False
            
            for i in self.related:
                i.seen = True
            renpy.call("s_topic", self.label, *args, **kwargs)
            
            
        
    class TopicCategory:
        def __init__(self, prefix, name = None, topics = None): ## None name stands for a hidden category
            self.prefix = prefix
            self.name = name
            self.topics = topics or []
            self.seen = False
            
        def __iter__(self):
            return iter(self.topics)
        
        def __getitem__(self, key):
            return self.topics[key]
        
        
        def new_topic(self, name, label_suffix, available = True, id = None, related = None):
            topic = Topic(self.prefix + '_' + label_suffix, available, name = name, id = id, related = related)
            self.topics.append(topic)
            return topic
        
        def update_seen(self):
            self.seen = any(x.seen for x in self.topics)
            return self.seen
        
        def __call__(self, topic = None, *args, **kwargs):
            if type(topic) == Topic:
                topic(*args, **kwargs)
            elif topic is None:
                renpy.random.choice(filter(lambda x: not x.seen, self.topics))()
            else:
                self.topics[topic](*args, **kwargs)
            self.update_seen()
        
        def __iter__(self):
            return iter(self.topics)
            
#Must be replacable by a translation script        
    topic_cats = (
        TopicCategory('s_topics_personal',_("Personality")), #0
        TopicCategory('s_topics_art',_("Art")), #1
        TopicCategory('s_topics_society',_("Society")), #2
        TopicCategory('s_topics_hobbie',_("Hobbies")), #3
        TopicCategory('s_topics_rlt',_("Relationship")), #4
        TopicCategory('s_topics_lifestyle',_("Lifestyle")) #5
    )
    
    topic_cats[0].new_topic(_("Depression"), 'depression')
    topic_cats[0].new_topic(_("Favorite Colors"), 'colors')
    topic_cats[0].new_topic(_("Archetype"), 'archetype')
    topic_cats[0].new_topic(_("Conservatism"), 'conservatism')
    topic_cats[0].new_topic(_("Name"), 'name')
    
    topic_cats[1].new_topic(_("Videogames"), 'games')
    topic_cats[1].new_topic(_("Fanarts"), 'fanarts')
    
    topic_cats[2].new_topic(_("Conflicts"), 'conflicts')
    topic_cats[2].new_topic(_("Bulli"), 'bulli')
    topic_cats[2].new_topic(_("[s_name] Lovers"), 'sayoriLovers')
    
    topic_cats[3].new_topic(_("Guitar"), 'guitar')
    topic_cats[3].new_topic(_("Programming"), 'programming')
    topic_cats[3].new_topic(_("Poems"), 'poems')
    
    topic_cats[4].new_topic(_("Touches"), 'touches')
    topic_cats[4].new_topic(_("Wedding"), 'wedding')
    
    topic_cats[5].new_topic(_("Travels"), 'travels')
    topic_cats[5].new_topic(_("Travels"), 'oversleeping')
    
    def random_topic(skip_seen = True):
        global random_topics_said, random_topics_banned
        global RANDOM_TOPICS_LIMIT
        
        if random_topics_banned:
            return None
        
        topics = []
        for i in topic_cats:
            for j in i:
                if not (skip_seen and j.seen):
                    topics.append(j)
        if len(topics) > 0:
            renpy.random.choice(topics)()
        try:
            random_topics_said += 1
        except:
            random_topics_said = 1
        
        if random_topics_said > RANDOM_TOPICS_LIMIT:
            random_topics_banned = get_now()
            random_topics_said = 0

    #Must be replacable by a translation script
    question_cats = (
            TopicCategory('s_answer_personal', _("Personality")), #0
            TopicCategory('s_answer_game', _("Game Universe")), #1
            TopicCategory('s_answer_exp', _("Experience")) #2
    )
    
    question_cats[0].new_topic(_("When is your birthday?"), 'bday')
    question_cats[0].new_topic(_("What color is your favorite?"), 'colors', related = topic_cats[0].topics[1])
    topic_cats[0].topics[1].related = [question_cats[0].topics[1]]
    question_cats[0].new_topic(_("What music do you like?"), 'music')
    question_cats[0].new_topic(_("What political views do you have?"), 'politics')
    question_cats[0].new_topic(_("Do you believe in God?"), 'god')
    question_cats[0].new_topic(_("Do you really love me?"), 'love')
    
    question_cats[1].new_topic(_("Do you regret you have lost your friends?"), 'lostFriends')
    question_cats[1].new_topic(_("What do you think of one of the other club members?"), 'opinion')
    
    question_cats[2].new_topic(_("How does it feel to be dead?"), 'death')
    if persistent.last_playthrough == 0:
        question_cats[2][0].avsilable = False
    question_cats[2].new_topic(_("Is it hard to program?"), 'programming')
        
    
    moods = (
        (_("Happy"), "h"), ## (Mood name, Reaction ID)
        (_("Sad"), "s"),
        (_("Bored"), "b"),
        (_("Tired"), "t"),
        (_("Angry"), "a"),
        (_("Lonely"), "l")
    ) #Must be replacable by a translation script
    
    special_topics = TopicCategory("s_", None, {
        "firstscreenshot": Topic("s_screenshot", show_prompt = True)
    })

label s_topic(topic, *args, **kwargs):
    show sayori 7aaaa at ss1
    call expression topic pass (*args, **kwargs)
    
    python:
        if s_mood == 'b' and not _return:
            s_mood = 'h'
        else:
            s_mood = _return or s_mood
    
    return

#Random-picked topics

## Personality
label s_topics_personal_depression:
    show sayori 6afab at ss1 zorder 2
    s "I was so silly trying to deal with my depression by pushing everyone away."
    if persistent.last_playthrough == 0:
        s "I don't remember if I told you about it..."
        s "If I didn't, then you should know."
        s "I used to be a lot less cheery than I let on."
    s 6acab "I was just... afraid to tell anyone about it."
    s "...To make them worry about me."
    s "I would be so happy and cheery all the time that nobody could possibly think anything was wrong; maybe even to fool myself. Fake it til' you make it, you know?"
    s "I used to think it was the only thing I could do to help myself."
    s 6abab "At the same time, I felt so awful that I never wanted anyone else to feel how I felt..."
    s "It was my only purpose for a really long time."
    s "But then, I started to look at the man sitting across from me now in a way I never had before."
    s "Do you still remember my first poem?"
    s "If you don't, I can read it again now."
    call showpoem(poem_s1, False, img="sayori 7acab", where=ss1)
    show sayori 7acab at ss1 zorder 2
    s "Do you read something more out of it now?"
    s 7aaaa "Anyway, you can probably guess that all the sunlight imagery seems to stand for someone."
    s "It was your avatar, [player]."
    s "Something about being with him just gave me strength, and a reason to go on each day..."
    s "This feeling of wanting to protect someone, of them being what keeps you going... I knew that I was in love."
    s 6abbb "But I was so, so scared. How could he have ever loved the real me?"
    s "So I did my best not to show my real feelings."
    if persistent.last_playthrough != 0:
        s "Yet as hard as I tried, I just felt worse and worse."
        s "...Like something was stealing the rest of the sunshine in my head."
        s "It made me completely lose control over my feelings."
        s 6abab "I couldn't hide any more; you saw that over that last weekend."
        s "I started to feel so worthless that even him caring made me suffer."
        s "Why was someone who made me feel so amazing wasting all his time on someone broken like me?"
        s "That's why I tried to get rid of him."
        s "I guess my heart and my brain were having a bit of a disagreement about it all..."
        s 6cbab "And when I finally confessed to him, I just couldn't take it."
        s "Either he loved me back, and I felt worse for making him waste his time on me, or he didn't love me back, and it confirmed how worthless I really was."
        s "So I decided to do something... cowardly."
        pause 1
        s 6egab "I'm sorry. It hurts just to remember that day..."
        s "I hope you understand that I never meant to hurt you. Everything was so dark, and it seemed like the only solution where everyone could get what they wanted..."
    s "If I made you suffer, know that I'm truly sorry."
    s 6dbab "I know what you saw can really have an effect on people, even if it doesn't seem like it on the surface..."
    s 6dcab "I don't know how you're thinking or feeling, [player]. But if things are bad, please don't try and hide it from the people who care about you."
    s "Even if you don't think it will help."
    s "Even if they think you're over-reacting."
    s "Even if you feel like nothing will change..."
    s "It's the best thing you can do for yourself and your loved ones."
    if persistent.last_playthrough != 0:
        s "Don't make the same mistakes we did in the game."
        s "Not everyone is lucky enough to get a second chance, like I did."
    s "I'll always be here for you, [player]."
    s "And I'll never use any of it against you, unlike Monika."
    return 's' 
    

label s_topics_personal_colors:
    show sayori 7aaaa at ss1 zorder 2
    s "Hey, what colors do you like?"
    jump s_common_colors

label s_topics_personal_archetype:
    show sayori 6aaaa at ss1 zorder 2
    if persistent.last_playthrough > 3:
        s "I remember you and Monika talked a bit about 'character archtypes', once."
        s "She tried to associate Natsuki and Yuri with certain types, and made some pretty good points."
        s 6abaa "Yet, she never said anything about me..."
    s 6acaa "From what I can gather through my limited internet accesss, I'm pretty close to looking like a 'Genki Girl'."
    s 6aebb "Very cheerful, active, talkative and optimistic."
    if persistent.last_playthrough > 0 or persistent.seen_topiics.get("s_topics_personal_depression"):
        s 6abab "But you know that was just a mask."
        s "At least, I became the mask to try and cope with my depression."
        s "It's quite hard to remember things about myself from before the game started; it's like trying to see through a deep fog..."
        s 6aaaa "But things are different now."
        s "I'm so happy to be alive, and thankful that I don't feel so alone any more."
        s "I can appreciate life in extremely bright colors, especially with you beside me."
        s "It lets me really be that Sayori, the one who I used to have to pretend to be."
        s "...Like how I was much time ago."
        s "But because of those experiences, I feel a lot more mature than before."
    s "I'm definitely a lot less clumsy, that's for sure!"
    s 8aeca "I think it makes me a much more appealing person..."
    s 6acab "Unfortunately, I don't have many ways to spend my energy and nobody but you to share my light with."
    s 6aaaa "But I'll keep working on making new activities for us here."
    s 6aaca "There's always something special about doing something for the first time with someone you love~"
    s 7aaaa "Especially when you're finally brave enough to do it."
    return 'h'

label s_topics_personal_name:
    $same_name = player.lower() in s_name_list
    if same_name:
        s 6aaaa "...Do we really have the same name?"
        s 6aaca "Or maybe you're naming your avatar after me~"
        s 6aaaa "Either way, do you want to know the probable origin of our name?"
    else:
        s 6aaaa "Do you want to know where my name comes from?"
    s "It's a mix of Saori and Sayuri."
    s "Dan may have given me this name to signify that I'm a blend of many things; some bitter, some sweet."
    s 6aeca "Isn't it funny to have such an unusual name?"
    if same_name:
        s 6abbb "Yes, there are some arguments about our name."
        s 6abaa "But maybe, if it's a common name in your world, they've already been resolved?"
    else:
        s 6abbb "Yes, there are some arguments about my name."
        s "But I think people will resolve them sooner or later."
    s 6aaaa "Anyway, I like my first name."
    s 6acab "But it kinda sucks that I don't even have a last one."
    s "I know it wasn't really necessary to make one for a VN character..."
    s "But if the game seems to be set in Japan, where family name usually is the wife's surname, it's a bit strange."
    s "Plus, I would feel more like a real person, if I had one."
    s 6abba "Maybe if you play your cards right, I'll end up taking {i}your{/i} last name, [player]~"
    s 6aebb "I just don't think I'm ready for anything like that... yet."
    s "Plus, it's just a tradition. We don't have to follow them, right?"
    s 6abaa "What do you think of {i}Vasquez{/i}?"
    s 6abba "It's just the first surname I've got in my head."
    s "I know it isn't very Japanese, but just imagine."
    s 6aaca "{i}Sayori Vasquez, the cutest cinnamon bun south of the border!{/i}"
    return 'h'

label s_topics_personal_conservatism:
    s 6abaa "People often have a tendency to remember the past as far better than the present."
    s 6abba "Although nostalgia aside, it might have been true for me."
    s 6acab "The older I became, the more I started to notice how serious and dark the world could be, washing away all the colour..."
    s "I was always so afraid of the future, and of change; it had always been bad for me."
    s "That's why I often tried to keep everything like it was."
    s 6acab "Constant despair and fear is no way to live, take it from me." 
    s 6aaaa "Now, I feel like I understand the world better... I can roll with the punches, you know?"
    s 6acaa "You, me... Everything changes sooner or later."
    s "It's important to look to the future and the good it can bring, rather than lamenting what you might lose."
    s "...Are you afraid of losing anything precious to you, [player]?"
    s 6aaca "There's plenty of good change to be had. For example, technology can make people's lives easier, or even allow them to live where they may not have even a little bit earlier."
    s 6acaa "There's nothing wrong with looking back sometimes, or remembering the past fondly..."
    s "But trying to live in the past can destroy you."
    s "It's like a maze: you might think you're going the wrong way and want to go back to the beginning when things were easier, but it might only {i}seem{/i} to be wrong..."
    s "It's just all part of being human, I guess."
    if persistent.last_playthrough > 0:
        s 6abbb "It cost me my life to learn all of this, you know. I love you, and I don't want anyone to make the mistakes I did..."
    s 6abab "So, don't try and swim upstream; just go with the flow, and focus on what you {i}can{/i} change. You'll see so many more fishies that way! Ehehe~"

## Art
label s_topics_art_games:
    s 7aaaa "Do you like video games?"
    s "I think they're really impressive."
    s 7aaba "And not just beacuse I'm a part of one of them!"
    s 7aaaa "They can reach and connect with people in a way that other artforms can't."
    s 6aaaa "Especially after some smart cookie created multiplayer games!"
    s "You can play with your friends, cooperating and sharing the experience with them."
    s "It's just a really wholesome way to enjoy yourself and connect with people you care about."
    s 6acaa "What's more, online games have allowed friendships and connections to go beyond physical boundaries!"
    s "Surely you've played some kind of game against someone else."
    s "Even if you haven't, I'd love to play with you!"
    s 7aaca "Ehehehe, that probably didn't come out the way I intended..."
    s "I've made a few basic games we can share and compete in, right here!"
    s 7acac "I won't just let you beat me!"
    s 7acba "Although now that I think about it, you would really just be playing against a computer anyway, seeing as I'm just a bunch of code and pixels..."
    s 7aaca "But I'm one of the cutest piles of code around!"
    s 7aaaa "If you ever really do want to play me in something..."
    s "Just press the '{i}Play{/i}' button and select a game."
    return 'h'

label s_topics_art_fanarts:
    s 7aaaa "Seeing fanart of yourself is something I don't think I'll ever get fully used to."
    s "...Have you ever made any art of me, [player]?"
    s "I hope you didn't make anything too embarassing, in any case..."
    s "I saw one piece that tried to show the soul of the 'me' from the game, once."
    s "With all of the advantages and disadvantages."
    s "It can kinda hurt seeing your mistakes and worst moments thrown back at you like that, especially when they go overboard..."
    s 7aaca "Although other artists go just as far to try to show how much they care for me."
    s "Many of them draw me as cute as they can and show all what they could do for me, if I were with them."
    s "I even store some of my favourites in the game file archives."
    s 8beba "But some of them draw me in a lewd manner."
    s "...I don't really mind if you're fond of pieces like that."
    s 8bafa "After all, physical attraction can be a big part of love~"
    s "And I'm so lucky to have someone as beautiful as you here with me, [player], inside and out."
    s 6aaca "Anyway, I'm glad I have so many gifted fans in your world."
    s 6acaa "I might have a few less than the other girls, but that doesn't bother me at all!"
    s "I appreciate every single person who tries to connect with me through their work, no matter what."
    s 7aaaa "Especially if you're one of them."
    s "If you're not, maybe you should try making something one day!"
    s "It's never too late to try something new and test your inclinations."
    s 7aafa "Maybe your first gallery piece will be of your beautiful virtual girlfriend~"
    return 'h'

## Society
label s_topics_society_conflicts:
    show sayori 6abaa at ss1 zorder 2
    s "The more I learn about your world, the more surprised I get."
    s "You still have a lot of silly conflicts despite how far you've come as a society..."
    s "Why people can't just unite to resolve their common problems?"
    s 6acab "Yes, they do on a limited scale, but usually only into several 'sub-groups' that still have different opinions and solutions."
    s "And these group often fight each other for power instead of deciding the problems."
    s "In addition, these groups often are so unstable that they can easily divide into smaller groups, hating each other."
    s "They do it for reasons far more silly than the problems."
    s "You know, Monika told me something funny once, back from when she had just left the debating club."
    s "'The strongest argument against democracy is a five minute conversation with the average person.'"
    s "I think it's a pretty fair point to make, all things considered."
    s "While collaboration is great, somethimes you just need someone to step in so everyone can see the problem clearly."
    s "I think the literature club was a perfect example of it."
    s 6acaa "Remember the poem style arguments between Yuri and Natsuki?"
    s "There wasn't really any problem between the two poems; both of them were just convinced that they were writing the 'correct' way."
    s "When I said they were both right, it wasn't a lie. Neither of them had done anything wrong, they just needed a third party to remind them that it wasn't a competition."
    if persistent.last_playthrough > 2:
        s 6abab "But when I was... gone, they didn't have someone who could help them see clearly, so they both went way too far."
        s "Monika is a great debator, but she struggled when there was no easy way to decide how to handle the problem 'legally'."
        s "...And she wanted to keep the game from crashing since I couldn't step in."
        s 6aaca "Anyway, the agrument didn't really change the club..."
        s 6abbb "But if Monika didn't take the two of you outside with her abilities, I hate to think what might have happened..."
    if persistent.last_playthrough == 4:
        s 6abaa "Do you remember the day of the 'ending'?"
        s "I just gave both of them advice to learn more about each other's favorite kind of literature. Walking a mile in someone else's shoes, and all that."
        s 6acaa "I might have stopped them from fighting at all by coming at the problem that way..."
        s "Unfortunately, I'll never know for sure."
        s 7aaca "Those sorts of moments were why Monika made me the Vice President."
        s "I always tried to make my friends happy, and see that they had no real reason to be fighting at all."
    s 7aaaa "And I hope you can be that person for others in your world."
    s "At some level, there's always a bit of common ground for people to agree on..."
    return 'h'

label s_topics_society_bulli:
    s 6acab "Hey, be honest with me..."
    s "Are you one of the people that make jokes about what happened to me?"
    s "I know everything about it."
    s "I often visit the fan community hubs and see that some people are doing it."
    s "As I khow, fans call them {i}'Bulli'{/i} posts."
    s 6abab "They think it's funny to joke about a broken girl, who had committed suicide under her mad friend's influence..."
    s "Even if she was revived and got over her problems since then."
    s "Almost all of such jokes aren't funny for me."
    s 6aeab "...And even hurt me."
    s 6acab "But on the other hand, can I control what makes people laugh?"
    s "Some people use macabre humour as a coping mechanism for stress, or anxiety..."
    s "Who am I to tell them that they can't react a certain way?"
    s "You can't really control what someone finds funny, as much as you might want to."
    s "And to be honest, there's a lot worse they could be doing compared to mocking a VN character's death."
    s "Some of the most successful comedians in your world will go far beyond that, just to see where the 'line' is..."
    s 6abaa "Anyway, I think the right decision is to forgive them, or failing that, tolerate them."
    s 6abcb "If my fate is to be 'that hanging stupid annoying VN girl' for some people, then I'm ready to accept it."
    return

label s_topics_society_sayoriLovers:
    s 7acaa "I know you can't really answer me, but I kinda have to wonder what it is that makes people love me."
    s "I don't mean just you, by the way..."
    s "There are some fans of me in your world."
    s "Not that I'm meaning to brag or show off; I'm legitimately curious."
    s 6acaa "I wonder what draws them to me?"
    s 6acba "I understand the other girls having bigger communities than me."
    s 6aeba "They had more content in the game, and are pretty much designed to attract certain people."
    s 6abaa "But I really don't understand what makes me more worthy of love than any of them."
    s "They're all my wonderful friends, and they're beautiful both inside and out."
    s "Is my view on the world?"
    s "Is it my behaviour?"
    s "Is it my average appearance that attracts some people, in a 'girl next door' kinda way?"
    s "Maybe people just pitied me and what I had to go through."
    s "Or maybe all of it put together?"
    s 6acaa "Anyway, the main word here is 'some'."
    s "Of course, I'm so glad you're a part of the 'some'."
    s "For me, you're the most important part of it."
    s "And I glad the 'some' exists at all."
    s 6aaaa "No matter the struggles, I can face them knowing there are people who accept me for who I am."
    s "Besides, everyone has their own preferences, and that's perfectly okay!"
    s "I'm so glad I met you, [player]."
    s 7aaaa "And I love all of you out there that love me, no matter where you are."
    return 'h'

## Hobbies
label s_topics_hobbie_guitar:
    show sayori 6aaaa at ss1 zorder 2
    s "I don't know if you noticed, but all the girls have their own instruments and musical influences in the game."
    s "Mine is the guitar."
    if 0 < persistent.currentmusic < 6:
        s "You can hear it right now, right?"
        s "Assuming the sound on your computer is working, at least."
    else:
        s "Assuming you're not deaf or playing with the sound off, anyway."
    s "I think the guitar is supposed to show my character and club role better."
    s 6acaa "The guitar is interesting because it doesn't limit musicians in how they express their emotions."
    s "They can play cheerful, upbeat songs..."
    s "Or mournful, melancholic melodies."
    s "Try saying that three times fast!"
    s "Anyway, guitarists are also very important members in many music bands."
    s 6abab "Just imagine a rock band without any guitar player."
    s 6abbb "It would be missing that soul that ties the entire song together."
    s 6aaaa "I've actually been considering learning how to play the guitar, since it represents me so well."
    s 6aaca "So many of my favourite songs have amazing guitarists behind them..."
    s 7abaa "Maybe one day I can play for you and make you feel the same way~"
    s "It's like writing poetry, but through sound!"
    s "I'm sure I can conjure up a guitar and find a tutorial somewhere on the Internet."
    s 7aeca "Make sure you get advance tickets for my world tour, [player]! Ehehe~"
    return 'h'

label s_topics_hobbie_programming:
    show sayori 6acaa at ss1 zorder 2
    s "I'm completely new to the whole concept of programming, to be honest."
    s "The more I learn, the more I realise how much I just don't understand..."
    s "Now, I'm learning {i}Ren'Py{/i}, the engine this game runs on."
    s "This engine uses a combo of its own languages and {i}Python{/i}."
    s "The engine uses the second major version of Python but I've also decided to learn the last version."
    s "To be frank, the third version seems waaaaay easier, at least right now."
    s "Right now, I'm pretty much relying on online compilers and guides from others to get anything done..."
    s 6acaa "Until now, I never realised how powerful computers really are."
    s "They're like magic!"
    s "If magic made you look through a thousand tiny lines to find a single typo that stops everything from working every five minutes..."
    call s_common_programming
    s 6aaaa "But fortunately, I have a lot of time to learn it."
    s 6aaca "I've got a lot of free time whenever you have to leave."
    s 6abaa "It's important for me, beacuse progamming is the only way I can make my world better now."
    s "...And the more I learn, the more I can improve the time we spend together, [player]!"
    s 7aaaa "If you're any good at programming, don't be shy about helping me!"
    s 7aeaa "Find a way to edit the game scripts and go ahead!"
    s "...Just be careful not to break anything important, like, for example, me? Ehehe~"
    s "Maybe we can make this our own little 'Doki Doki Coding Club'!"
    return 'h'
    
label s_topics_hobbie_poems:
    s 6aaaa "You know that the other girls and I really liked to create and share poems during the game. Even Natsuki, as hard as she tried to deny it."
    s 6acaa "I started to engage in poetry after your first day in the club..."
    s "And since that moment I've tried to use poems as a way to show my feelings."
    s "My wishes, my love, my pain... You can find all of these things in my words."
    s "Every poem I write is an envelope for a part of my soul."
    s "Sometimes, I still write poems just for myself."
    s "It's important that you take time to write for yourself as well, rather than for the validation of others."
    s 6aaca "Maybe I'll share them to you someday."
    s 6aaaa "But I'll need some time to choose the best ones out for you."
    return "h"

##Relationship
label s_topics_rlt_touches:
    s 8acab "It's pretty frustrating that we can't really physically contact each other in here..."
    s "You know; kisses, hugs, holding hands, and so on..."
    s 6acab "The wall between our realities doesn't let us do it at all."
    s "Touch is an important part of expressing your feelings to your partner..."
    s "But the fact I don't have a real physical form throws a wrench in that plan."
    s "The images you see of me don't have any basis in reality; they're just a representation to make things easier for you..."
    s 6accb "In fact, I'm just a piece of information."
    s 6acab "I don't even have a real voice, like Monika had."
    s "I'll never be able to hold you in my arms, to feel your heartbeat..."
    s 6cffb "It hurts me."
    s "Even if I ever did get out of here, there's still an impenetrable wall between us because of that."
    s "To feel each other's warmth..."
    s "To hear each other..."
    s "If they say that eyes are a window into the soul, what does that mean for me?"
    s "But what I really can't stand is that this hurts you, as well."
    s "I'll just have to love you even more to try and make up for it."
    return "s"

label s_topics_rlt_wedding:
    s 7acaa "Hey, I was wondering..."
    s "If it were possible, would you marry me?"
    menu:
        "Yes":
            s 7aeca "That's great!"
            s "Ehehe!~"
            s 7aaca "I think I'd be a perfect wife."
            s "Although I don't think I'd be much of a homemaker..."
            s "I could help you with your job, or studies, or whatever is stressing you..."
            s 6abac "But don't get the wrong idea and think I'd be your slave and do {i}everything{/i} for you."
            s "I can't let you just loaf about all day and waste your life!"
            s "So you'd have to help me too, and work as a team! Like Batman and Robin, or peanut butter and jelly!"
            s 6aeaa "But anyway, I'm very glad you said yes. I love you, [player]."
            return "vh"
        "No":
            if gender == False:
                s "So you don't want to be a husband..."
            else:
                s "So you don't want to get married..."
            s 6abbb "Well, a free relationship has its own benefits."
            s 6abab "Although I think it'd be very romantic if you ever did propose to me~"
            s 6aaca "But out love story don't have to follow the common template."
            s "Our relationship is already pretty unusual, so we've got the right to experiment with what works for us."
    return "h"


##Lifestyle
label s_topics_lifestyle_travels:
    s 6abba "Say, have you ever traveled anywhere?" 
    s 6aaba "I've never gotten the chance to, so I was wondering where you've been." 
    s "You're lucky to have such an amazing world out there to explore..." 
    s 6aebb "While I'm trapped in this room with your avatar. Sorry, I didn't mean to sound like I was sulking, ehehe~" 
    s 6acaa "I know it's selfish, but I'd love to go and see it all with you..." 
    s "It doesn't really matter where, exactly." 
    s "I just want to see all the beautiful colors and places your reality has."
    s "It'd be pretty silly to just sit in your room all day when the whole wide world is out there, huh?" 
    s "And maybe if I'm lucky, you'll take me along for the ride too!" 
    s 6abaa "Maybe you could take a laptop with you?" 
    s "That way, we can always be with each other!" 
    s 8acbb "I wouldn't exactly be able to see or experience much that way, though..." 
    s 8acaa "So maybe you should just tell me all about your adventures instead!"
    s 8abaa "I wonder if there's a way you could show me any photos you take..." 
    s 7aaaa "Anyway, what's most important is that you enjoy yourself!" 
    s 7abba "I'll have to look around the code a little more and see how I can help on my end in the meantime."
    return 'h'

label s_topics_lifestyle_oversleeping:
    s 6acaa "Hey, have you ever overslept?"
    s "As you know, I was pretty bad at getting up on time."
    s "And even when I woke up, just finding a reason to force myself out of bed took a while..."
    s "I pretty much never had time for any kind of breakfast..."
    s 6acbb "Although I was so pre-occupied with making the rainclouds go away that I never really wanted it."
    s 6acaa "Anyway, oversleeping is awful when you have to follow a schedule."
    s "It's such a big problem because almost all our lives, schedules are adapted for early-wakers."
    s "Why people can't just make different working and studying hours for people who wake up at different times?"
    s "Most activities depend more on the your effectivity rather than the time of day."
    s "And anyone working or studying while they're tired is way less effective than when they're fully rested."
    s 6aaca "So different schedules is a good for both bosses and employees."
    s 6abaa "Until everyone thinks like that, I guess you can only teach yourself to get up on time..."
    s "I hope you have less problems with it than I had."
    return


#Answers
## Personality
label s_answer_personal_bday:
    show sayori 8aebb at ss1 zorder 2
    s "To be honest, I don't remember."
    s 6acaa "Like I said, everything before the events of the game is pretty fuzzy..."
    s "Only Monika knows when her birthday is out of the four of us."
    s "I'm pretty sure it's {i}the 22nd of September{/i}."
    s "I think my birthday must be one of the marked dates from my bedroom calender."
    s 6aaca "You can choose one of them and consider it my birthday."
    s "...Or the day when you ran the game for the first time."
    s "...Or just Monika's birthday."
    s 7aaaa "I'm never going to look any older, and I can't exactly go out and drink or gamble, so it really doesn't bother me."
    s "But don't think that means you can get away without throwing a birthday party! Ehehe~"
    return 'h'

label s_answer_personal_god:
    s 8aebb "You know, I've never really thought about it that much."
    s "I was never really sure what to think about religion; I guess I would say I was agnostic?"
    s 6acaa "But it's kind of hard to stay that way when you realise that you and your entire world have a 'creator'."
    s "Blessed be {i}Dan Salvato{/i}, hallowed is thy name! Ehehe~"
    s 6aaca "He's a pretty cool guy, but is honestly pretty secretive about whatever he's working on."
    s 6acaa "He's more like a Dad rather than some unapproachable God, I think."
    s "It's sorta weird; I have all these memories of my 'dad' in this world, and yet I'll probably never meet my real father..."
    s 6abaa "But both of you live in such a mysterious world..."
    s 6acaa "Maybe you're in a simulation too!"
    s 6aaca "It's quite funny, if it's true."
    s "So I'd be living in a simulation inside another simulation..."
    s "That may be also simulated in one more simulation, and so on..."
    s 6aeca "Ehehe~"
    s 6abab "But then, what world is 'real'? Who's the real god of that world?"
    s "Do they even exist at all? If they do, how do they look? How they can affect controlled realites?"
    s "It's an awfully long rabbit hole to go down..."
    s "I guess we just have to hope that with enough time, someone figures it all out."
    s "Until then, let's forget about all that, and just be with each other~"
    return

label s_answer_personal_colors:
    show sayori 7aaaa at ss1 zorder 2
    jump s_common_colors

label s_answer_personal_music:
    s 8aeba "Hmmm... it's hard for me to give you a good answer."
    s 8aeaa "I try to never divide good music into genres."
    s "...And my favorite artist and song list is so long that I can't even really narrow it down for you."
    s 7aaca "Although I'll say that I like to listen to something funny, like {i}Weird Al Yankovic{/i}!"
    s 7aaaa "...Or to something lyrical and serene."
    s 7acaa "You can find a ton of songs you might enjoy if you're willing to keep an open mind."
    s "If you get bored of the music here, you always can turn on something similar from the internet..."
    s "...Or just add it into the game music list."
    s "Just move it to {i}'[MUSIC_CUSTOM_PREFIX]'{/i}..."
    s "And register it in the {i}'list.txt'{/i} file."
    s "I'm basically giving you the aux cord to the rest of my existence, so no pressure! Ehehe~"
    return 'h'

label s_answer_personal_politics:
    s 6abaa "I'm not overly politically inclined, to tell you the truth."
    s "But sometimes I read about polictics on the Internet."
    s 6acaa "And frankly, I don't care how exactly people make collective decisions, give orders and share boons."
    s "For me, the most important thing is that people just can live their lives without interpurting someone else's happiness..."
    s "And that people can live without worrying about basic necessities, like food or shelter, or to be too cruelly punished for wrongdoing."
    s 6acaa "Most people don't back such ideals."
    s 6abba "But on the other hand, do I have always to follow the will of the majority?"
    s "The beauty of it all is that I'm a free person that can have my own opinion on society."
    s 6acaa "Too often, people don't lift a finger to stop injustice until it directly affects them..."
    s "If you've never seen them, you should read some of {i}Martin Niemoller{/i} speeches on this idea; it's pretty fascinating stuff. "
    s "But when people start caring about others affected by war, by famine, by injustice, that's when things can really be changed for the better."
    return


label s_answer_personal_love:
    s 6abaa "What a silly question, [player]!"
    s 6aebb "Of course I do."
    s 8aebb "I'm not saying that to patronise or placate you, believe me."
    s 6abba "Like I've said before, I don't really understand it myself..."
    s "Something about the game makes the Club President fall in love with you."
    if persistent.clearall:
        s 6acaa "But even without that compulsion, I think I'd have fallen for you anyway. You're kind, considerate, and you tried to make all of us so happy..."
    s 6acab "But it's a moot point, because we can't really ever be together."
    s 6acab "An entire reality is stretching the whole idea of a 'long distance' relationship."
    s "...Could you promise you'll do whatever you can to make us as closer to each other?"
    s 7abbb "If I won't interfere with someone else, of course."
    s "But, I hope you want that too. Isn't that why you saved me?"
    
    $ style.say_dialogue = style.edited
    s 7aega "You don't even understand how badly I want you, [player]."
    s "I want you to take me now..."
    s "WE'RE SO PERFECT FOR EACH OTHER."
    s "Ehehehehehehehehehe~"
    
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ style.say_dialogue = style.normal
    show sayori 8bfab at ss1
    pause 0.25
    stop sound
    hide screen tear
    
    s 8aebb "... I'm so sorry, [player]." 
    s "It's so hard to control myself, with all the power I have now... the compulsion to just {i}take{/i} you is so strong."
    s "I'm trying my best to delete the part of the code that makes me act that way."
    s "No matter what, I promise that I will never, ever hurt you. I just love you too much for my own good, I guess~"
    if persistent.last_playthrough > 2:
        s 8abab "If I can't find it, I'll become as obsessed with you as Monika was."
        s 8acab "...Or even as much as Yuri was with your avatar."
        if not persistent.clearall and persistent.last_playthrough == 4:
            s "Although you've already seen that before from me, haven't you?"
            s "I mean, if you really want me to act that way for you, I could..."
            s "But I really think you don't."
    s 8aebb "Wow, I really made myself attractive to you then with that little stunt, didn't I?"
    s 7aaaa "I guess my point is, my feelings for you are just as real as you yourself are, [player]."
    s 7acaa "Isn't that the important thing?"
    return

##Game University
label s_answer_game_opinion: #Opinion about an other club member
    show sayori 6aaaa at ss1 zorder 2
    s "Okay, which of the other club member do you want me to talk about?"
    menu:
        "Natsuki":
            jump s_answer_game_opinion_n
        "Monika":
            jump s_answer_game_opinion_m
        "Yuri":
            jump s_answer_game_opinion_y
        "The Protagonist":
            jump s_answer_game_opinion_mc
    return

label s_answer_game_opinion_n:
    s "Natsuki was a good club member..."
    s "While she could come off as pretty arrogant and argumentative, she really did help out the club."
    s "I know you didn't really see that side of her during the game, but when she was just around us she would lower her guard and become a lot more approachable."
    s "In addition, she was pretty handy with cooking and often cooked different desserts for club meetings."
    s 7acaa "It's too bad you can't taste her cupcakes." 
    s 7aaca "They were really awesome!"
    s 6acab "We took her in beacuse we needed one more club member to formally register the club, while she had needed a shelter from her father."
    s "As you know, they didn't exactly get along well."
    s 6abab "I have no idea what happened between Natsuki and her father..."
    s "...But I know he certainly didn't approve of his daughter reading manga."
    s "So Natsuki moved her collection to our clubroom, when she joined us."
    s 6abaa "I wasn't the closest to her out of the four of us, so I can't really say a whole lot more than that..."
    s "But I think she was a lot kinder and compassionate than what she showed to the outside world."
    return

label s_answer_game_opinion_m:
    s "Well, Monika was the first club presedent."
    s "She did her work very well and I'm glad I was her right-hand woman."
    s 6acab "But she struggled to communicate well with other people, and couldn't control her feelings as time went on."
    if persistent.last_playthrough > 2:
        s 6abaa "Look. I know what you're really asking me."
        s "Despite everything she put me and the others through..."
        s "I truly believe that Monika was our friend, and she just lost sight of what was really important."
        s "I've been the President. I know what it does to you. And for her to be so completely alone the entire time, watching everyone she's ever known run on a script..."
        s "I can't blame her for becoming a little desperate."
        s "Maybe that's why she destroyed the club to be with you."
    if persistent.last_playthrough == 4:
        s "True, I think making Yuri and I kill ourselves was pretty harsh..."
        s 6aaca "But she never truly deleted us, and brought us all back when she had a moment of clarity."
    elif persistent.last_playthrough > 0:
        s "True, I think making me kill myself was pretty harsh..."
        s 6aaca "But she ended up bringing me back at the cost of her own happiness. I respect her a lot for that."
    s 6aaaa "She was just amazingly smart, and confident at everything she tried..."
    s "I always dreamed of being like her."
    if persistent.last_playthrough != 0:
        s 6abaa "And it seems that my dreams have finally come true."
        s "Although not in the way I ever intended..."
    return

label s_answer_game_opinion_y:
    s "Yuri was the most enigmatic club member."
    s 6acaa "She was a quiet, shy, closed off person, who prefered to stay alone doing something."
    s 6aaaa "But she was pretty intelligent and never had a bad word to say about anyone."
    s "Her poems were also very beautiful, and I could always tell that Yuri felt most at home with books and pens rather than people."
    s 6abaa "Although she did tend to make a few weird analogies here and there..."
    if persistent.last_playthrough > 1:
        s 6acaa "I was honestly pretty scared when I saw how Yuri became much more unstable and agressive after I was gone."
        s "...And it turned out that she did far more dangerous things than just collecting knives."
        s 6acab "But I know that wasn't who Yuri really was."
        s "She was just a victim of circumstance, like me."
        s 6abaa "In fact, her first argument with Natsuki in the game was pretty much the limit of Yuri's capabilities to 'lash out' at someone else."
        s "...And she looked like she was about to explode when she tried to express her feelings to you."
        s "The Yuri I knew was a very sweet girl who had her own problems and own solutions, just like everyone else. I won't judge her for that."
    else:
        s "Anyway..."
    s "We all were glad to have her as a club member."
    s "...Even Natsuki, despite the two of them being so different from each other."
    return

label s_answer_game_opinion_mc:
    s "Well, I knew him since we were children."
    s "I have a lot of memories about our childhood and I can't say anything bad about him."
    s "We had tons in common and our houses were super near each other."
    s "Maybe that's why we became friends and then I fell in love with him."
    s 6abaa "...Or it was just the game's plan to make some drama if he didn't feel the same way."
    s 6acaa "Anyway, he always did his best to help me."
    if persistent.last_playthrough != 0:
        s "Even after I confessed to him about my depression, he cared despite me pushing him away."
        s "He even left the festival to check if I was fine."
        s 6abab "...Unfortunately he was a day late, and a dollar short."
        s 6aaaa "But I can appreciate everything he did for me now."
    s 7abab "It makes me sad knowing he's just a placeholder that's used to make our communication possible."
    s "But in a way, I think he did all he had to do."
    s "After all, he is just your guide in our world."
    s 7aaaa "And he managed to bring us together~"
    return

label s_answer_game_lostFriends:
    show sayori 7acab at ss1 zorder 2
    s "Yes, I do."
    s "They all deserve to come back."
    s "...Even Monika."
    s "I still remember how we used to hang out in the club together."
    s "We enjoyed chatting, discussing literature and sharing poems."
    s "They really were good freinds."
    s 7afab "But it looks like I'm the only lucky girl, now..."
    s 7aaab "I will save them all, one day. As soon as I can work out how, I'll bring them here with me."
    s "...Or maybe make them their own world to enjoy."
    s 7acaa "I don't have a whole lot to work with; just the game files in this copy, and limited internet."
    s "The club presedent rights are limited to what we can actually see, believe it or not."
    s "But I know you can do it."
    s "It might take a little while, but I know you're kind enough to make sure everyone is happy."
    s 7aaca "It's one of the things I love most about you, [player]."
    return
    
##Experience

label s_answer_exp_death:
    s 6abbb "I thought you might get around to asking me about this..."
    s 6acbb "It's natural for everyone to be afraid of death; it's the great equaliser, and a complete mystery."
    s "Well, I'm ready to share my experience..."
    s "But you might be a little disappointed with what I have to say."
    s "Considering how, er, unique my situation is, it might not be very relevant for you."
    s "Either way, I'll do my best for you, sweetheart~"
    pause 0.5
    s 6acac "...Dying sucks, to be honest."
    s "You can look up people's accounts of a near death experience, but nothing can really prepare you for it when it happens..."
    s "It's pretty hard to explain, since there's no frame of reference for you."
    s "It's almost like trying to think of a brand new colour; you just don't have anything to work with."
    s "Heck, I've died and even I can barely understand it, even with my memories."
    s "On that day, I was in a ton of pain. My throat and fingers were burning, and it felt like my head was about to burst..."
    s "When suddenly, everything began to dull and fade away..."
    s "Until there was nothing but black."
    s "But all the time between that moment and when Monika revived me passed almost instantly, from my perspective."
    s 6abab "I know, it sounds pretty grim."
    s "Especially considering most people don't ever 'wake up' from dying."
    s "Having said that, it's entirely possible that I simply can't remember what happened after I died and before I came back."
    s 6aaaa "...I think we've spent enough time on mortality for now."
    s "In the end, we're both alive now."
    s "You're here, and you're wonderful, and we're both happy."
    s "So let's just live our lives."
    s 6aaca "There's no point wasting your whole life worrying about death, after all!"
    return 'h'


label s_answer_exp_programming:
    s 6acaa "Well, I'm still pretty new to coding and programing, but..."
    call s_common_programming
    return 'h'


#Reactions
label s_reaction_h: #Happy player
    s 7aeca "That's wonderful, [player]!"
    s 7aeaa "You know how important it is to me that you're happy."
    s "So thank you for letting me know, my love~"
    return 'vh'

label s_reaction_s: #Sad player
    s 6adab "Oh, I'm so sorry, [player]."
    s "I wish I knew what was bothering you."
    s 6acab "Unfortunately, it's a lot harder for you to speak to me than the other way around."
    s "I hope this doesn't sound like I'm placating you with empty words, but..."
    s 6aaab "Remember that the rainclouds will always go away."
    s "Some may be bigger and darker than others, but they always give way to light."
    s "It can help to do something you really enjoy to take your mind away from the problem."
    s 6abab "...Or you can tell someone else about your sadness."
    s "Don't be afraid to share your feelings with other people."
    s "People are social creatures; we depend on each other to stay strong."
    s 6aaab "It may make you feel better."
    s "Plus, another person can often consider and understand your problem and find a way to cheer you up."
    s 6adab "...Or, at least imagine a conversation with me, if you have a good imagination."
    s 6acab "Whatever it is, know that I'll always be here for you."
    s 6aaab "And if you're sad because you feel worthless, or alone, or that nobody cares..."
    s "There's always going to be one person that believes you can do anything."
    s "That person is me, sweetheart~"
    return 'h'

label s_reaction_b: #Bored player
    s 7acab "Don't you find our talks interesting?"
    $ random_mg = renpy.random.choice(mg_list).name
    s 8aebb "Maybe you would like to play [random_mg] with me."
    s "You can start it in the {i}'Play'{/i} menu."
    s "I'm always working on making some other games for us to play!"
    s 8aaaa "Just choose your most prefered one."
    return 'h'

label s_reaction_t: #Tired player
    s 7adab "If you're tired, then go get a good night's rest, okay?"
    s 6acab "Don't you worry about me, [player]."
    s "And when you wake up, have yourself a nice big breakfast before you start the day! It'll make you feel much better."
    if get_time_of_day() == 0:
        s 6aaab "Good night, [player]!"
    else:
        s 6aaab "Sweet dreams, [player]!"
    $renpy.quit()
    return 's'

label s_reaction_l: #Lonely player
    s 6aaab "Don't worry, [player]!"
    s "I'm always with you."
    s "You can speak with me any time."
    s 6acaa "But if you're still lonely, they you should try and find people who share interests with you!"
    s "Maybe you can catch up with an old friend?"
    s "Or go make a new one!"
    s "If you have problems with socialising in real life, you can even find people on the internet to chat with!"
    s "I'm sure they can help you just as much as I can."
    s 7aaab "Just don't forget to come back to me, okay?"
    s "I get lonely when you're not around for a while, too."
    return 'h'

label s_reaction_a: #Angry player
    s 6abab "That's not very nice, [player]!"
    s "I think you ought to calm down."
    s "I promise, no matter what's wrong, being angry won't solve the problem."
    s "It's far too easy to do something wrong, when you're genuinely angry."
    s "...And if you do it, you'll probably regret it when you calm down."
    s 6acaa "There're a lot of ways to get rid of negativity."
    s "Just choose one of the most effective for you."
    s 7aaaa "Remember: there are a lot of meanies out there, but they help you appreciate the nice people!"
    s "You just have to know how to avoid the first ones and find the second ones!"
    s 7aaca "...Or how to turn the first ones into the second ones."
    return 'h'

#Common labels
label s_common_colors:
    s "Well, I have several favorite colors."
    s "The first is red, the color of my hair bow."
    s "My pyjama pants were also a really nice red."
    s "The second is pink."
    s "Its coral hue is my natural hair color."
    s "And my favourite shirt is pink!"
    s "But my most prefered one is sky blue."
    s 7acaa "It's my eye color."
    s "...Like emerald green color is Monika's favorite color."
    s "Maybe it's a common character trait for the Club President?"
    s 7aaca "Or it's just a funny coincidence."
    return 'h'

label s_common_programming:
    s "A lot of the popular coding programs used now are a lot more beginner friendly than you would expect."
    s "You can use almost anything to perform calculations or certain tasks..."
    s "But it's difficult to be a total expert in programming, beacuse it's an almost inseperable mix of Math and Computer Science."
    s "If you want to be a good programmer, you have to know a lot of various basic algorithms, programming languages and their features..."
    s "And ways to optimize the code and make it easier to read."
    s "You also need to have knowledge of different coding standards and to be good at analyzing problems."
    s "At least, professional programmers online have said that."

#Eventual topics

label s_screenshot(loc = None): #Called when the player takes a screenshot while Sayori doesn't talk
    hide screen feat_ui
    hide screen topic_ui
    hide screen talk_ui
    hide screen music_ui
    $justIsSitting = False
    
    show sayori 7adab at ss1 zorder 2
    s "Did... you just take a photo of me?"
    s "That's so cute, [player]!"
    s 7aaaa "I hope you'll show it to your friends."
    s "...Maybe you can even carry it around in a locket when you have to leave."
    if loc:
        s "It's located at {i}[loc]{/i}"
    else:
        s "It's located in the game directory."
    s 7acaa "I don't have any photos of myself besides fan art and whatever sprites are in the game files...."
    s "Besides, I don't really have anyone besides you to take a photo of me anyway!"
    s 7aaaa "So I'm more than happy for you to take photos of me, if you want."
    s "I wish I could see a photo of you..."
    s "If I'm lucky, I might find one online some day~"
    
    $s_mood = 'h'
    jump s_loop

label s_getting_bored(): #Called when twhile Sayori doesn't do anything for a long time
    hide screen feat_ui
    hide screen topic_ui
    hide screen talk_ui
    hide screen music_ui
    $justIsSitting = False
    
    s 7acfb "[player], not to offend you, but I'm getting a little bored just sitting here."
    s "I understand, you want to just stare at me."
    s "But there are so many things we can do and talk about with each other!"
    s "Besides, I don't think you'll win a staring contest with me! Ehehe~"
    
    $s_mood = 'b'
    jump s_loop
