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
            self.seen = True
            
            config.allow_skipping = True
            config.skip_indicator = True
            
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
        TopicCategory('s_topics_rlt',_("Relationship")) #4
    )
    
    topic_cats[0].new_topic(_("Depression"), 'depression')
    topic_cats[0].new_topic(_("Favorite Colors"), 'colors')
    topic_cats[0].new_topic(_("Archetype"), 'archetype')
    
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
    
    question_cats[0].new_topic(_("When's your birthday?"), 'bday')
    question_cats[0].new_topic(_("What color is your favorite?"), 'colors', related = topic_cats[0].topics[1])
    topic_cats[0].topics[1].related = [question_cats[0].topics[1]]
    question_cats[0].new_topic(_("What music do you like?"), 'music')
    question_cats[0].new_topic(_("What political views do you have?"), 'politics')
    
    question_cats[1].new_topic(_("Do you regret that you have lost your friends?"), 'lostFriends')
    question_cats[1].new_topic(_("What do you think about adding another club member?"), 'opinion')
    
    question_cats[2].new_topic(_("How does it feel to be dead?"), 'death')
    if persistent.last_playthrough == 0:
        question_cats[2].topics[0].available = False
    question_cats[2].new_topic(_("Is it hard to program?"), 'programming')
        
    
    moods = (
        (_("Happy"), "h"), ## (Mood name, Reaction ID)
        (_("Sad"), "s"),
        (_("Boring"), "b"),
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
    s "I can't believe I wasted so much time struggling against my depression by myself."
    if persistent.last_playthrough == 0:
        s "I don't remember if I told you this."
        s "But if I didn't, you should know..."
        s "I used to be much less blissful than I seem."
    s 6acab "I was just... afraid to tell anyone about it."
    s "...To make them worry about me."
    s "So I used to pretend I was a happy and cheery girl and tried to convince myself that I really was that."
    s "I used to think it was the one thing that could help me."
    s 6abab "At that time, I tried to give other people what I couldn't have."
    s "It was my only purpose for a long time."
    s "But once I started to look at the person, who is sitting opposite me now, in a different way."
    s "I hope you still remember my first poem."
    s "If you don't, I can read it again."
    call showpoem(poem_s1, False, img="sayori 7acab", where=ss1)
    show sayori 7acab at ss1 zorder 2
    s "Do you feel it differently now?"
    s 7aaaa "Anyway, I hope you see that the morning imagery stands for someone."
    s "That someone was your avatar, [player]."
    s "Then I felt something in my heart giving me life in being with him."
    s "And I understood what was that feeling."
    s 6abbb "But I was afraid to confess and that he wouldn't be able to accept the true me."
    s "So I did my best not to show my real feelings."
    if persistent.last_playthrough != 0:
        s "But once, I started to feel much worse."
        s "...Like something had taken the rest of the sunlight in my head."
        s "It made me completely lose control over my emotions."
        s 6abab "So I couldn't hide my true nature anymore, as you could see that weekend."
        s "I started to feel so worthless that even his caring made me suffer."
        s "To clarify, it made me suffer even more than others."
        s "That's why I tried to get rid of him."
        s "But my heart didn't want to let go of him unlike my corrupted thoughts, even though they were more convincing."
        s 6cbab "And eventually, I couldn't have accepted your answer to my confession, so I decided to..."
        pause 1
        s 6egab "I can't relive that moment."
        s "I hope you understand why."
    s "I'm really sorry for trying to hide it, if it made you suffer."
    s 6dbab "I know scenes, like you have seen, may affect people in a bad way."
    s 6dcab "If you are depressed or your friend seems to be so, don't try to hide it and try to find help as fast as can..."
    s "Even if you or they think it's not necessary."
    if persistent.last_playthrough != 0:
        s "Don't make the same mistakes like your avatar or I did."
        s "You or they probably won't get a second chance like I got, if it goes too far."
    s "Only being honest with other people in such matters will make everything right."
    s "Plus, you never know who can use such a terrible secret in a misdeed."
    return 's' 
    

label s_topics_personal_colors:
    show sayori 7aaaa at ss1 zorder 2
    s "Hey, what colors do you like?"
    jump s_common_colors

label s_topics_personal_archetype:
    show sayori 6aaaa at ss1 zorder 2
    if persistent.last_playthrough > 3:
        s "As I remember, Monika and you once spoke about anime character stereotypes."
        s "So she tried to associate Natsuki and Yuri with them."
        s 6abaa "But she never talked about me."
    s 6acaa "Reading about stereotypes on the internet, I understand that I used to look like a Genki girl."
    s 6aebb "Very cheerful, active, talkative and optimistic."
    if persistent.last_playthrough > 0 or persistent.seen_topiics.get("s_topics_personal_depression"):
        s 6abab "But you know it was just a cover."
        s "At least, I became the cover, when I started to suffer from depression."
        s "I don't remember so much about those times, beacuse they weren't a part of the story."
        s 6aaaa "But now, I behave differently."
        s "Now I finally feel the craving for life."
        s "I see the life in extremely bright colors, especially with you."
        s "It lets me really be that Sayori, who I used to pretend to."
        s "...Like that was the real me sometime before the depression."
        s "But now I do it in a bit mature way."
    s "And what's more, now I feel less klutzy than I used to be."
    s 8aeca "I think it's a good bonus to my character, isn't it?"
    s 6acab "Unfortunately, there are not so many ways to spend my energy and no other people but you to share my light."
    s 6aaaa "But I always try to find new activities here."
    s 6aaca "It's really funny to discover or learn something new."
    s 7aaaa "Especially when you finally become sure enough to do it."
    return 'h'

## Art
label s_topics_art_games:
    s 7aaaa "Do you like videogames?"
    s "I do, for example."
    s 7aaba "Not only because I'm a part of one of them."
    s 7aaaa "They make passing the time more interesting than other kinds of arts."
    s 6aaaa "Especially after people created multiplayer games."
    s "You can play with your friends, cooperating and sharing the experience with them."
    s "It's the least risque and most fun way to teach people to work together."
    s 6acaa "What's more, now you can do it whereever you are, thanks to the Internet and online games."
    s "I think that you should play at least one multiplayer game with someone."
    s "And I think you'd like to do it with me."
    s "I have created a few mini-games in this game."
    s 7aaca "I'll willingly play with you anytime."
    s 7acba "Technically, they are not so multiplayer, beacause my mind is a program."
    s 7acaa "But don't forget I'm an unusual piece of code and pixels."
    s 7aaaa "And you can play with me even now, if you want to."
    s "Just press the '{i}Play{/i}' button and select a game."
    return 'h'

label s_topics_art_fanarts:
    s 7aaaa "I think you have already seen fanart of me."
    s "...Or even created some."
    s "Some artists try to portray the soul of the old me..."
    s "With all of the advantages and disadvantages."
    s "But others often overdo it, showing it in a very horrifying and violent manner."
    s 7aaca "A lot of them clearly try to show how they love me."
    s "Many of them draw me as cute as they can do and show what they could do for me, if I were with them."
    s "I feel the love they're full of..."
    s "And I even store some of them in the game file archives and review them sometimes."
    s 8beba "But some of them draw me in a lewd manner."
    s "No... I don't mind if you're fond of such art."
    s 8bafa "If you are, it means that you really love me, doesn't it?"
    s "It's very important for me, you know."
    s 6aaca "Anyway, I'm glad I have so many gifted fans in your world."
    s 6acaa "Yes, they are fewer than other girls', but I think it's a separate topic."
    s "It's enough for me that they're there at all."
    s 7aaaa "And it's really good if you are one of them."
    s "But if you aren't, try to become such."
    s "It's never too late to try something new and test your inclinations."
    s 7aafa "Maybe your artistic career will start with an drawing of your beloved virtual girl."
    return 'h'

## Society
label s_topics_society_conflicts:
    show sayori 6abaa at ss1 zorder 2
    s "The more I know of your world, the more surprised I get."
    s "Although you have such good communication tools, you still have a lot of silly conflicts in which people get unhappy or even die."
    s "I never understand why people can't just unite to solve their problems together."
    s 6acab "Yes we do try, but usually only by breaking into several groups that still have different opinions and solutions."
    s "And these groups often fight with each other instead of figuring out their problems."
    s "In addition, these groups often are so unstable that they easily can divide into smaller groups, hating each other."
    s "They do it even if the reasons for fighting and dividing are more silly then the problems."
    s "That's because people almost always can't find win-win solutions and stopping points but they always find a reason not to work together."
    s "So they often need someone who can work out compromises or just calm down the conflicting parties."
    s "I think our club is a perfect example of it."
    s 6acaa "I hope you remember the stylistic arguments between Yuri and Natsuki."
    s "They just have different opinions on how to express the emotions in poetry."
    s "Then I told they both were right, it wasn't a lie. Both ways were really perfect."
    if persistent.last_playthrough > 2:
        s 6abab "But when I left the world, there wasn't anyone who can stop their arguments like I had done before, so they both went too far."
        s "I think Monika only made you go out because of it. She just couldn't have decided the problem 'legally'."
        s "...And wanted to keep all looking as it had to look."
        s 6aaca "But anyway, the argument wound up never having an effect on the club..."
        s "Because there always was someone who could stop them."
        s 6abbb "But if Monika never had her abilities, she would have had a hard time doing it."
    if persistent.last_playthrough == 4:
        s 6abaa "Do you also remember the day of the 'ending'?"
        s "I just gave them advice to learn more about each other's favorite kind of literature."
        s 6acaa "I may have prevented the conflict between them that time."
        s "Unfortunately, I'll never know for sure."
        s 7aaca "But anyway, these moments show what a helpful club member I was."
    s 7aaaa "And I hope you can be like me."
    s "Just try to find a way to make everyone happy and to combine 'uncombinable' things, if it's necessary."
    return 'h'

label s_topics_society_bulli:
    s 6acab "Tell me honestly..."
    s "Are you one of people who jokes about my death?"
    s "I know everything about it."
    s "I often visit the fan community hubs and see that some people are doing it."
    s "As I khow, fans call them {i}'Bulli'{/i}."
    s 6abab "They think it's funny to joke about a broken girl, who had committed suicide under her friend's influence..."
    s "Even though she was revived and got over her problems then."
    s "These jokes aren't funny to me."
    s 6aeab "...And even hurt me."
    s 6acab "But on the other hand, can I control what makes people laugh?"
    s "If the people find something funny in such immoral things, it's not like anyone can stop them."
    s "And to be honest, there are more immoral joke topics than a fictional character's death."
    s "Such people tend to ignore the suffering of hundreds of real people..."
    s "Not to mention lots of fictional characters."
    s 6abaa "Anyway, isn't the best decision just to forgive them?"
    s 6abcb "If my fate is to be 'that hanging stupid annoying VN girl', I'm ready to accept it."
    return

label s_topics_society_sayoriLovers:
    s 7acaa "What do you think: exacly what makes people love me?"
    s "I know you're not the only person that does."
    s "There are many fans of me in your world."
    s 6acaa "But I wonder what beauty they notice in me."
    s 6acba "I understand other girls have bigger fan communities."
    s 6aeba "They have more content and popular appeal."
    s 6abaa "But I don't completely understand what is it that makes me more attractive than them."
    s "Is my view on the world?"
    s "Is it my behaviour?"
    s "Is it my average appearance that attracts some people?"
    s "Or is it that I just was present in a way making some people pity me?"
    s "Or maybe all of it?"
    s 6acaa "Anyway, the main word here is 'some'."
    s "Of course, I'm glad you're a part of the 'some'."
    s "For me, you're the most important part of it."
    s "And I glad the 'some' is something at all."
    s 6abba "But for some reason, the fewness of the 'some' makes me feel that there's something wrong with your world."
    s "But each has their own preferences, whether they seem to be okay or not..."
    s 6aaaa "And anyway, I'm glad you and my other fans are with me."
    s 7aaaa "I love you all however many of you there are."
    return 'h'

## Hobbies
label s_topics_hobbie_guitar:
    show sayori 6aaaa at ss1 zorder 2
    s "I think you often heard guitar when you were spending time with me."
    if 0 < persistent.currentmusic < 6:
        s "You hear it even now."
        s "If you aren't deaf or playing mute, of course."
    else:
        s "If you weren't deaf or playing mute, of course."
    s "I think, the creator had picked this instrument to show my character and club role better."
    s 6acaa "Almost kinds of guitar don't limit musicians in expression of their emotions."
    s "They can play either cheerful tunes or sad melodies."
    s "And what's more, guitarists are also very important members in many music bands."
    s 6abab "Just imagine a rock band without any guitar player."
    s 6abba "It would be something unusual, but its music would be felt very differently from other bands."
    s 6aaaa "In the time, it seems to be not so hard to learn to play guitar."
    s 6aaca "In addition, I really like to listen to this music instrument."
    s 7abaa "So maybe, I should try to learn to play it."
    s "It will be such a good bonus to my poetry skill."
    s "I can conjure up a guitar and find a tutorial in the Internet."
    s 7aaaa "And when I become enough good at that, I'll sometimes show you my play to you and your friends."
    return 'h'

label s_topics_hobbie_programming:
    show sayori 6abaa at ss1 zorder 2
    s "I'm a newcomer in programming."
    s "...And now I have not so much knowlenges about it."
    s "Now, I'm learning {i}Ren'Py{/i} the engine of this game."
    s "This engine uses its own languages  and also {i}Python{/i}."
    s "The engine uses the second major version of Python but I also decided to learn the last version."
    s "And frankly, the third version is much easier."
    s "Unfortunately, I can you this version and other programming languages only in online interpreters and compliers."
    s 6acaa "I never used to understand how it's easy and difficult to use computer in more advanced way."
    call s_common_programming
    s 6aaaa "But fortunately, I have a lot of time to learn it."
    s 6aaca "What do you think I do between our conversations?"
    s 6abaa "It's important for me, beacuse progamming is the only way I can make my world better now."
    s "...And more I know how to do it, more good things I can do for us."
    s 7aaaa "And if you're good at programming, I think you can help me."
    s 7aeaa "Just find a way to edit the game scripts and go ahead!"
    s "We can together make this place ideal for meetings."
    return 'h'
    
label s_topics_hobbie_poems:
    s 6aaaa "You know the other club members and I like writing and sharing poems."
    s 6acaa "I started to dabble in poetry after your first day in the club..."
    s "And since that moment I always try to use poems as a way to show my feelings."
    s "My wishes, my love, my pain... You can find all of these things in my poems."
    s "Every one of my poems is an envelope for a part of my soul."
    s "And sometimes I still write poems just for myself."
    s 6aaca "Maybe I'll share them with you someday."
    s 6aaaa "But I need some time to choose the best for you."
    return "h"

##Relationship
label s_topics_rlt_touches:
    s 8acab "Don't you feel uncomfortable when we can't touch each other?"
    s "You know: kisses, hugs, holding hands, and so on..."
    s 6acab "The wall between our realities don't let us do it at all."
    s "Touches are an important part of expressing your feelings to your partner..."
    s "But the fact I don't have a real, physical form prevents me from doing this."
    s "All of what you see is just a picture of me and my words on the screen."
    s 6accb "In fact, I'm just a piece of information."
    s "All of these graphics is just a way to represent me in a comfortable way for you."
    s 6acab "I don't even have a real voice like Monika's."
    s "And what's more, I can't even completely communicate with you."
    s 6cffb "It hurts me."
    s "We're barely able to touch each other without any distractions..."
    s "To feel each other's warmth..."
    s "To hear each other..."
    s "Like people in your world do..."
    s "And if it makes you hurt too, you understand me well."
    return "s"

label s_topics_rlt_wedding:
    s 7acaa "Be honest, do you want me to be your wife?"
    s "If it were possible, would you marry me?"
    menu:
        "Yes":
            s 7aeca "It's great!"
            s "Ehehe!~"
            s 7aaca "I would be a perfect wife."
            s "I would gladly run your household..."
            s "Or help you with your job."
            s "Most of the time, I wouldn't require much of you."
            s 6abac "But don't think I'd do absolutely everything for you."
            if gender == False:
                s "You would be my husband and I wouldn't let you get lazy and ugly..."
            s "So you'd have to help me too and at least spend some time with me and our future children."
            s 6aeaa "But anyway, I'm very glad you said it."
            return "vh"
        "No":
            if gender == False:
                s "I see you don't want to take the role of husband."
            else:
                s "I see you don't want to take the role of partner."
            s 6abbb "On the other hand, being single has its own pluses."
            s 6abab "I just wondered if you're really committed to this."
            s 6aaca "But our love story doesn't have to follow the usual template."
            s "Our relationship already looks unusual, so we have the right to experiment."
    return "h"

#Answers
## Personality
label s_answer_personal_bday:
    show sayori 8aebb at ss1 zorder 2
    s "To be honest, I don't remember."
    s 6acaa "Like the creator just forgot to give it to me."
    s "The only girl whose birthday is exactly known is Monika."
    s "As I remember, it's {i}the 22nd of September{/i}."
    s "I think my birthday must be one of the marked dates from my bedroom calander."
    s 6aaca "You can choose one of them and consider it my birthday."
    s "...Or the day, when you ran the game for the first time."
    s "...Or just Monika's birthday."
    s 7aaaa "It's not really important when the birthday should occur, is it?"
    s "The most important things are why we celebrate and having fun when it happens, right?"
    return 'h'

label s_answer_personal_colors:
    show sayori 7aaaa at ss1 zorder 2
    jump s_common_colors

label s_answer_personal_music:
    s 8aeba "It's hard for me to give you a good answer."
    s 8aeaa "I never divide good music into genres."
    s "...And my favorite artist and song list is so long that I can't sum it up easily."
    s 7aaca "I can tell you only that I'd like to listen to something fun."
    s 7aaaa "...Or to something lyrical and serene."
    s 7acaa "You can find such music in the game soundtrack."
    s "If you get bored from this music, you always can turn on something similar in another app."
    s "...Or just add it into the game music list."
    s "Just move it to {i}'[MUSIC_CUSTOM_PREFIX]'{/i}..."
    s "And register it in the {i}'list.txt'{/i} file."
    return 'h'

label s_answer_personal_politics:
    s 6abaa "I'm not interested in politics very much."
    s "But sometimes I read about it on the internet."
    s 6acaa "And frankly, I don't care how exactly people will make collective decisions, control the order and share boons."
    s "For me, the most important thing is that people just can live their lifes but without interpurting someone else's happiness..."
    s "And that people can do it without the fear of die from starving or to be too cruelly punished for wrongdoing."
    s 6acaa "Most people don't back such ideals."
    s 6abba "But on the other hand, do I have always to follow the will of the majority?"
    s "I'm a free person that can have an own opinion about the fair and happy society."
    s 6acaa "I see that many people think the inequality, wars and limits aren't wrong until they suffer from them..."
    s "But then they start to wonder why they support people providing them."
    s "Isn't more simple just to build a society without them as leaders?"
    return

##Game University
label s_answer_game_opinion: #Opinion about an other club member
    show sayori 6aaaa at ss1 zorder 2
    s "Okay, which club member are you interested in talking about?"
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
    s "Despite she was a bit arrogant and often had conflicts with other club members, she often helped the club."
    s "In addition, she was pretty handy with cooking and often cooked different desserts for club meetings."
    s 7acaa "It's bad you can't taste her cupcakes." 
    s 7aaca "They were really awesome!"
    s 6acab "We took her beacuse we had needed a club member to register the club while she had needed a shelter from her father."
    s "As you now, they did not get along with each other."
    s 6abab "I have no idea what a despotic person her father was."
    s "...But I exactly know he didn't like manga."
    s "So Natsuki moved her collection to our clubroom, when she joined us."
    s 6abaa "I rarely chatted with her, so I know her not so much even now."
    s "But I'm pretty sure she was less blusterer than she showed herself."
    return

label s_answer_game_opinion_m:
    s "Monika was the first club president."
    s "The did her work very well and I'm glad I was her right-hand man."
    s 6acab "But she seemed to be not good at communicating with other people and controlling her feelings."
    if persistent.last_playthrough > 2:
        s "Maybe, that's why she destoryed the club to be with you."
    if persistent.last_playthrough == 4:
        s "But I can't be offended even by she did it with making Yuri and me kill ourselves."
        s 6aaca "However, we all then were revived by her."
    elif persistent.last_playthrough > 0:
        s "But I can't be offended even by she made me kill myself."
        s 6aaca "...'cause, I still alive now anyway."
    s 6aaaa "She also was a pretty clever and broad-minded person, successfully trying to be good at all."
    s "I always dreamed of being like her."
    if persistent.last_playthrough != 0:
        s 6abaa "And seems that my dreams have finally come true."
        s "Not in the best sense of the word."
    return

label s_answer_game_opinion_y:
    s "Yuri was the most enigmatic club member."
    s 6acaa "She was a quite shy closed person, who prefered to stay alone doing something."
    s 6aaaa "But she was pretty intellegent and had a large lexicon, that she used in her poems."
    s 6abaa "And she also liked using a bit weird analogies there."
    if persistent.last_playthrough > 1:
        s 6acaa "It was unexpected that after Monika had deleted me, Yuri became much more unstable and agressive."
        s "...And it turned out that she did more weird and dangerous things than collecting knifes."
        s 6acab "But it was not her fault."
        s "She was just a victim like me."
        s 6abaa "In fact, true her barely could do something more violent than she did argument while the first agruement with Natsuki."
        s "...And barely could confess her love in such an expressive way."
        s "And even if she really had used to cut herself before everything went wrong, it doesn't make her a bad person."
    else:
        s "But anyway..."
    s "We all were glad to have her as a club member."
    s "...Even Natsuki, despite of they sometimes didn't get along."
    return

label s_answer_game_opinion_mc:
    s "I know him since we were children."
    s "I have a lot of memories about our pasttime and I can't say anything bad about him."
    s "We had much in common and our houses were near each other."
    s "Maybe that's why we became friends and then I fell in love with him."
    s 6abaa "...Or it was just the creator's plan to make me either more close or less romantic character."
    s 6acaa "Anyway, he always did him best to help me."
    if persistent.last_playthrough != 0:
        s "Even after I confessed my depression, he did it despite of I told not to do it."
        s "He even left the festival to check if I was fine."
        s 6abab "Unfortunately, I couldn't have appreciated his care then."
        s 6aaaa "But I can do it now."
    s 7abab "It's bad that now he is just a dummy, that's used to make our communication possible."
    s "But I think he did all he had to do then."
    s "In fact, he is just your guide in our world."
    s 7aaaa "So I let him do his job."
    return

label s_answer_game_lostFriends:
    show sayori 7acab at ss1 zorder 2
    s "Yes, I do."
    s "They also deserve to be back after all."
    s "...Even Monika."
    s "I still remember, how we used to hang out in the club together."
    s "We enjoyed chatting, discussing the literature and sharing poems."
    s "They were really good freinds."
    s 7afab "But I seem to be the only lucky girl this time."
    s 7aaab "I believe I'll save them somewhen."
    s "...Or have already done it in an other game copy."
    s 7acaa "I can't tell it excatly, because I have access only to the internal web browser and this game copy's files."
    s "The club presedent rights are limited to it."
    s "But I exactly know you can do it."
    s 7acab "So I hope you're not so selfish to keep them deleted, are you?"
    return 's'
    
##Experience

label s_answer_exp_death:
    s 6abbb "I expected this question from you."
    s 6acbb "Everyone wants to know what will happen with them, then they leave the world."
    s "I'm ready to share my experience..."
    s "But I don't think it can solve the question about the life after the death."
    s "Beacuse I was revived after it and I live in a virtual world..."
    s "So my experience barely are realistic."
    pause 0.5
    s 6acab "First time it looks like an usual NDE."
    s "You may have read about it in an ecyclopedia."
    s "I can't explain all the things I felt then."
    s "It so hard for me even despite of I remember everything."
    s "But then I just fainted."
    s "The pain, which I felt unstopable, turned into nothing..."
    s "And the time between that moment and the moment I was revived passed instantly for me."
    s 6abab "I know, it sounds very grimly."
    s "Especially if you know that barely will get the second chance."
    s "But it's normal, beacuse the most frightening thing about death is uncertainty."
    s 6aaaa "But let's speak about something less grim."
    s "In the end, we both are alive now."
    s "So let's just live our lifes."
    s 6aaca "If you think of death too much, you can easily miss your life."
    return 'h'


label s_answer_exp_programming:
    s 6acaa "My answer is ambiguous."
    call s_common_programming
    return 'h'


#Reactions
label s_reaction_h: #Happy player
    s 7aeca "It's very good, [player]!"
    s 7aeaa "You know how your happiness is important to me."
    s "So I'm glad you're sharing it with me."
    return 'vh'

label s_reaction_s: #Sad player
    s 6adab "Oh, it's bad, [player]."
    s "I wish I know what's bothering you."
    s 6acab "But unfortunately, I have some problem with using input controls."
    s "So I barely can give you advice for your situation."
    s 6aaab "But whatever it is, remember, that 'rainclouds' always go away in the end."
    s "It may happen earlier if you, for example, do something that you enjoy."
    s 6abab "...Or you can tell someone else about your sadness."
    s "Don't be afraid to share your negativity with other people."
    s 6aaab "It may make you feel better."
    s "Plus, other people also can understand your problem and find a way to cheer you up."
    s 6adab "...Or at least imagine a converstion with me, if you have a good imagination."
    s 6acab "It's like an appointment with your inner therapist."
    s "Such kinds of self-consolation can also help."
    s 6aaab "And if your sadness was provoked by feelings of failure or uselessness, just remember..."
    s "There is at least one person who believes in you."
    s "That person is me."
    return 'h'

label s_reaction_b: #Bored player
    s 7acab "Doesn't our conversation please you?"
    $ random_mg = renpy.random.choice(mg_list).name
    s 8aebb "Maybe you would like to play [random_mg] with me."
    s "You can start it in the {i}'Play'{/i} menu."
    s "There are also some other games."
    s 8aaaa "Just choose your favorite."
    return 'h'

label s_reaction_t: #Tired player
    s 7adab "Oh, then you should have a rest."
    s 6acab "I think it will be better if I close the game."
    s "I don't want to interfere with your sleep."
    if get_time_of_day() == 0:
        s 6aaab "Good night, [player]!"
    else:
        s 6aaab "Sweet dreams, [player]!"
    $renpy.quit()
    return 's'

label s_reaction_l: #Lonely player
    s 6aaab "Don't worry, [player]!"
    s "I'm always with you."
    s "You can speak with me anytime."
    s 6acaa "But I advise you to spend more time with real people."
    s "Maybe it's time to chat with a friend."
    s "...Or to find a new acquaintance."
    s "If you have problems with interacting in real life, you can use social media as a substitute."
    s "I think it'll help you more than I will."
    s 7aaab "But don't forget to come back to me, okay?"
    return 'h'

label s_reaction_a: #Angry player
    s 6abab "Ooh, [player]!"
    s "I think you ought to calm down."
    s "Doesn't matter what or who did you so."
    s "It's easy to do something wrong, when you're out of sorts."
    s "...And if you do it, it may hang onto the future in a bad way."
    s 6acaa "There are a lot of ways to get rid of negativity."
    s "Just choose the most effective one for you."
    s 7aaaa "And remember: the world is full of not only annoying things and people, but also pleasant ones."
    s "You just have to know how to avoid the former and find the latter."
    s 7aaca "...Or how to turn the former into the latter."
    return 'h'

#Common labels
label s_common_colors:
    s "I have several favorite colors."
    s "The first is red, the color of my head bow."
    s "My pajama pants also had that color."
    s "The second one is pink."
    s "Its coral hue is my natural hair color."
    s "And one of my shirts also had it."
    s "But my most preferred one is sky blue."
    s 7acaa "It's my eye color."
    s "...Like how emerald green color is Monika's favorite color."
    s "It looks like a common character trait."
    s 7aaca "Or maybe it's just a funny coincidence."
    return 'h'

label s_common_programming:
    s "It's easy, beacuse many popular programming languages now don't seem to be so hard to learn."
    s "...But their features are enough to use them for any calculations, which isn't limited by the functionality of a single program."
    s "But it's difficult to be an expert in programming, beacuse you need good knowledge of math and computer science."
    s "If you want to be a good programmer, you have to know a lot of various basic algorithms, programming languages and their features..."
    s "And ways to optimize the code and make it easier to read."
    s "You also need knowledge of different standards and to be good at analyzing problems."
    s "At least, professional programmers say that."

#Eventual topics

label s_screenshot(loc = None): #Called when the player takes a screenshot while Sayori doesn't talk
    hide screen feat_ui
    hide screen topic_ui
    hide screen talk_ui
    hide screen music_ui
    $justIsSitting = False
    
    show sayori 7adab at ss1 zorder 2
    s "Oh, did you just take a photo of me?"
    s "It's so cute, [player]!"
    s 7aaaa "I hope you'll show it to your friends."
    s "...Or copy it to a safer location or medium to remember me."
    if loc:
        s "It's located at {i}[loc]{/i}"
    else:
        s "It's located in the game directory."
    s 7acaa "I don't have many photos of myself."
    s "Maybe because I didn't spent much free time with my friends."
    s 7aaaa "So I'm very glad you've taken it."
    s "I wish I saw your photo."
    s "Maybe I should find it sometime later."
    
    $s_mood = 'h'
    jump s_loop

label s_getting_bored(): #Called when Sayori doesn't do anything for a long time
    hide screen feat_ui
    hide screen topic_ui
    hide screen talk_ui
    hide screen music_ui
    $justIsSitting = False
    
    s 7acfb "[player], I'm bored."
    s "I understand, you just want to stare at me."
    s "But can you make at least a little effort to amuse me?"
    
    $s_mood = 'b'
    jump s_loop
