default persistent.seen_topics = {}
default persistent.seen_lens = {}
default persistent.hasPlayerPhoto = False

#Topic-specified images
image s_sticker down = "gui/poemgame/s_sticker_2.png"
image n_sticker down = "gui/poemgame/n_sticker_2.png"
image y_sticker down = "gui/poemgame/y_sticker_2.png"
image m_sticker down = "gui/poemgame/m_sticker_2.png"

image cookies = "mod_assets/images/stuff/cookies.png"
image cookies_d = "mod_assets/images/stuff/cookies_d.png"
image sayori cookie = "mod_assets/images/s_new/body/withcookie.png"
image sayori cookie_biten = "mod_assets/images/s_new/body/withcookie_biten.png"

init -5 python:
    if persistent.seen_topics is None:
        persistent.seen_topics = {}
    if persistent.seen_lens is None:
        persistent.seen_lens = {}
    
    class Topic:
        def __init__(self, label, available = 0, show_prompt = True, name = None, id = None, related = None, poem = None):
            self.label = label
            self.available = available #Number of seen topics to open this one. False = unavailable
            self.show_prompt = show_prompt
            self.name = name or label
            self.id = id or label
            self.poem = poem
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
            
            config.allow_skipping = True
            config.skip_indicator = True
            justIsSitting = False
            
            renpy.call_in_new_context("s_topic", self.label, *args, **kwargs)
            self.seen = True
            for i in self.related:
                i.seen = True
            renpy.return_statement()
            
        
    class TopicCategory:
        def __init__(self, prefix, name = None, topics = None): ## None name stands for a hidden category
            self.prefix = prefix
            self.name = name
            self.topics = topics or []
            self.seen = False
            self.all_seen = False
            self.seen_len = 0
            persistent.seen_lens[prefix] = 0
            self.labels = {}
            
        def __iter__(self):
            return iter(self.topics)
        
        def __getitem__(self, key):
            kt = type(key)
            if not (kt == int or kt == slice):
                kn = key
                key = self.find_key(kn)
                if key is None:
                    key = self.find_key(self.prefix + '_' + kn)
            return self.topics[key]
        
        def __setattr__(self, key, value):
            if key == 'seen_len':
                persistent.seen_lens[self.prefix] = value
            self.__dict__[key] = value
        
        def append(self, topic):
            n = len(self.topics)
            self.topics.append(topic)
            self.labels[topic.label] = n
        
        def new_topic(self, name, label_suffix, available = 0, id = None, related = None, show_prompt = True, poem = None):
            topic = Topic(self.prefix + '_' + label_suffix, available, show_prompt, name = name, id = id, related = related, poem = poem)
            self.append(topic)
            return topic
        
        def find_key(self, label):
            return self.labels.get(label)
        
        def update_seen(self):
            self.seen_list = list(filter(lambda x: x.seen, self.topics))
            self.seen_len = len(self.seen_list)
            self.seen = self.seen_len > 0
            self.all_seen = self.seen_len >= len(self.topics)
            
            return self.seen, self.all_seen
        
        def __call__(self, topic = None, *args, **kwargs):
            if type(topic) == Topic:
                topic(*args, **kwargs)
            elif topic is None:
                def cond(x):
                    sl = len(persistent.seen_topics)
                    return not (x.seen or x.available is False or x.available > sl)
                renpy.random.choice(filter(cond(x), self.topics))()
            else:
                self.topics[topic](*args, **kwargs)
            self.update_seen()
        
        def __iter__(self):
            return iter(self.topics)
    
    derp_known = True
    try:
        p = persistent
        depr_known = p.depr_known or p.last_playthrough > 0 or p.clear[8] #If player must already know, that Sayori used to be depressed
    except:
        pass
            
#Must be replacable by a translation script
    topic_cats = (
        TopicCategory('s_topics_personal',_("Personality")), #0
        TopicCategory('s_topics_art',_("Art")), #1
        TopicCategory('s_topics_society',_("Society")), #2
        TopicCategory('s_topics_hobbie',_("Hobbies")), #3
        TopicCategory('s_topics_rlt',_("Relationship")), #4
        TopicCategory('s_topics_lifestyle',_("Lifestyle")), #5
        TopicCategory('s_topics_game',_("Game Universe")), #6
        TopicCategory('s_topics_food',_("Food")), #7
        TopicCategory('s_topics_misc', _("Misc")) #8
    )
    
    topic_cats[0].new_topic(_("Depression"), 'depression')
    topic_cats[0].topics[0].available = persistent.last_playthrough > 0
    topic_cats[0].new_topic(_("Favorite Colors"), 'colors')
    topic_cats[0].new_topic(_("Archetype"), 'archetype')
    topic_cats[0].new_topic(_("Name"), 'name')
    topic_cats[0].new_topic(_("Quitting the Game"), "quittingTheGame")
    topic_cats[0].new_topic(_("Left-handedness"), "sinistrality")
    topic_cats[0].new_topic(_("Breast Size"), "tits")
    topic_cats[0].new_topic(_("Intellengence"), 'intellegence')
    
    topic_cats[1].new_topic(_("Videogames"), 'games')
    topic_cats[1].new_topic(_("Fanarts"), 'fanarts')
    topic_cats[1].new_topic(_("Literature"), 'lit')
    
    topic_cats[2].new_topic(_("Conflicts"), 'conflicts')
    topic_cats[2].new_topic(_("Bulli"), 'bulli')
    topic_cats[2].new_topic(_("[s_name] Lovers"), 'sayoriLovers')
    topic_cats[2].new_topic(_("Charity"), 'charity')
    topic_cats[2].new_topic(_("Isolation"), 'isolation')
    topic_cats[2].new_topic(_("PSAs"), 'psa')
    
    topic_cats[3].new_topic(_("Guitar"), 'guitar')
    topic_cats[3].new_topic(_("Programming"), 'programming')
    topic_cats[3].new_topic(_("Poems"), 'poems')
    topic_cats[3].new_topic(_("Drawing"), 'drawing')
    
    topic_cats[4].new_topic(_("Touches"), 'touches')
    topic_cats[4].new_topic(_("Marrige"), 'marrige')
    topic_cats[4].new_topic(_("Cheating{#RltTopic}"), 'cheating')
    topic_cats[4].new_topic(_("Dates"), 'dating') 
    topic_cats[4].new_topic(_("Thanksgiving"), 'thanks')
    topic_cats[4].new_topic(_("Fan Merch"), 'fanStuff')
    topic_cats[4].new_topic(_("Children"), 'children', available = 4)
    topic_cats[4].new_topic(_("Presents"), 'presents')
    topic_cats[4].new_topic(_("Face"), 'face', show_prompt = not (persistent.hasPlayerPhoto is True))
    
    topic_cats[5].new_topic(_("Travels"), 'travels')
    topic_cats[5].new_topic(_("Oversleeping"), 'oversleeping')
    topic_cats[5].new_topic(_("Pets"), 'pets')
    topic_cats[5].new_topic(_("Cleaning"), 'cleaning')
    topic_cats[5].new_topic(_("Drugs"), 'drugs')
    
    topic_cats[6].new_topic(_("Clones"), 'clones')
    topic_cats[6].new_topic(_("Parents"), 'parents')
    topic_cats[6].new_topic(_("Stars"), 'stars')
    topic_cats[6].new_topic(_("In-game Time"), 'time')
    topic_cats[6].new_topic(_("Other Worlds"), 'worlds')
    
    topic_cats[7].new_topic(_("Ice Cream"), 'iceCream')
    topic_cats[7].new_topic(_("Cinnamon Buns"), 'cinnamonBun')
    topic_cats[7].new_topic(_("Cupcakes"), 'cupcakes')
    topic_cats[7].new_topic(_("Breakfast"), 'breakfest') #Save this typo here and below not to make me edit the mod translations
    topic_cats[7].new_topic(_("Vegetarians"), 'vegetarians')
    topic_cats[7].new_topic(_("Pizza"), 'pizza')
    topic_cats[7].new_topic(_("Cookies"), 'cookies')
    
    topic_cats[8].new_topic(_("Flowers"), 'flowers')
    
    for i in topic_cats:
        i.update_seen()
    
    poems = TopicCategory('s_poems',_("Poems"))
    
    poems.new_topic(None, 'sunshine', poem = poem_sunshine)
    poems.new_topic(None, 'bottles', poem = poem_bottles)
    poems.new_topic(None, 'flower', poem = poem_flower)
    
    for i in poems.topics:
        i.seen = True
    
    if persistent.last_playthrough > 0:
        poems.new_topic(None, 'last', poem = poem_last)
        poems.topics[-1].seen = True
    
    if derp_known:
        poems.new_topic(None, 'prose', poem = poem_prose)
    
    if persistent.last_playthrough > 0:
        poems.new_topic(None, 'leaf', poem = poem_leaf)
    if persistent.last_playthrough > 3:
        poems.new_topic(None, 'angel', poem = poem_angel)
    poems.new_topic(None, 'afterlight', poem = poem_afterlight)
    poems.new_topic(None, 'fruits', poem = poem_fruits)
    poems.new_topic(None, 'val', poem = poem_val, available = False)
    
    
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
            TopicCategory('s_answer_exp', _("Experience")), #2
            TopicCategory('s_answer_misc', _("Misc")), #3
    )
    
    question_cats[0].new_topic(_("When is your birthday?"), 'bday')
    question_cats[0].new_topic(_("What color is your favorite?"), 'colors', related = topic_cats[0].topics[1])
    topic_cats[0].topics[1].related = [question_cats[0].topics[1]]
    question_cats[0].new_topic(_("What music do you like?"), 'music')
    question_cats[0].new_topic(_("What political views do you have?"), 'politics')
    question_cats[0].new_topic(_("Do you believe in God?"), 'god')
    question_cats[0].new_topic(_("Do you really love me?"), 'love')
    question_cats[0].new_topic(_("Who do you want to work as?"), 'profession')
    question_cats[0].new_topic(_("What pet would you like to have?"), 'pets', related = topic_cats[0].topics[1])
    topic_cats[5].topics[2].related = [question_cats[0].topics[-1]]
    question_cats[0].new_topic(_("What is your favorite holiday?"), 'holidays')
    question_cats[0].new_topic(_("What do you think about lesbian pairings?"), 'pairings')
    question_cats[0].new_topic(_("What are your favorite books?"), 'books')
    
    question_cats[1].new_topic(_("Do you regret you have lost your friends?"), 'lostFriends')
    question_cats[1].new_topic(_("What do you think of one of the other club members?"), 'opinion')
    question_cats[1].new_topic(_("Isn't it tiring to sit so for a long time?"), 'sitting')
    question_cats[1].new_topic(_("How do you change game files?"), 'editing')
    question_cats[1].new_topic(_("What do you think about chibi dokis?"), 'chibi')
    
    question_cats[2].new_topic(_("How does it feel to be dead?"), 'death')
    if persistent.last_playthrough == 0:
        question_cats[2][0].available = False
    question_cats[2].new_topic(_("Is it hard to program?"), 'programming')
    question_cats[2].new_topic(_("Can you say a funny fact?"), 'fact')
    question_cats[2].new_topic(_("Are you good at cooking?"), 'cooking')
    question_cats[2].new_topic(_("How did MC’s poems look like to you?"), 'mcPoems')
    question_cats[2].new_topic(_("Have you ever played visual novels?"), 'visualNovel')
    question_cats[2].new_topic(_("How to fight suicidal thoughts?"), 'suicideThoughts')
    
    question_cats[3].new_topic(_("Can you give me a poem?"), 'poem')
    question_cats[3].new_topic(_("What do you think about the real world?"), 'reality')
        
    
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
    s 6acab "I got you really worried about me, didn’t I?"
    s 6aebb "When I said... you know..."
    s "That I had 'rainclouds' inside my head for all my life..."
    s 8aecb "...remember, 'rainclouds' is just what I called my depression."
    s 8aebb "Isn't that silly?"
    s 6abab "Anyway."
    s 6acaa "At first, I was really good at making them go away..."
    s 6aaca "It was pretty difficult, but I kept in mind that if I got bummed out, I wouldn’t be able to make other people happy, which is all I really wanted anymore."
    s 6abaa "However, I also tried not to push myself too hard in trying to overcome this..."
    s "So I tried to stay with the beloved MC. I thought being with him would help ease my mind."
    s 6acab "But I thought he'd learn my darkest secret sooner or later, so he'd leave me then..."
    s "That's why I tried to take it slow..."
    s 6abbb "People in your world think that my cheerfulness was fake and I was just acting..."
    if persistent.last_playthrough > 0:
        s 6abab "But my feelings were as real as you until the moment..."
        s 6acab "The moment Monika started to change my mind."
        s 6cbcb "She teased me with my own problems and tried to convince me of terrible things. That I just annoyed him, made him worry for me..."
        s 6dbcb "That I should just… end it all."
        s 6ecab "It made me feel really, really bad..."
        s "My little rainclouds turned into a dark thunderstorm, blinding my mind with the rain..."
        s 6efbb "Of course, I tried to tune her out, but that’s all I could do as a person."
        s 6cbcb "To try."
        s "..."
        pause 0.5
        s 6dcbb "I got absolutely tired of everything."
        s 6dcab "I can't stop blaming myself for the desperate choice I made..."
        if persistent.clear[8]: # If the MC has accepted Sayori's confession
            s "My confession was accepted..."
            s "Still, my feelings told me no, that this wasn’t right..."
        else:
            s 6cfcb "The rejection broke me..." 
        s 6dbab "I really thought that it would be the best..."
        s 6dbcb "Needless to say, I, um, completely gave up."
        s "My neck and hands still remember the pain..."
        s 6dbbb "But I was too late to save myself..."
        s 6egab "I'm sorry..."
        s 6dgeb "I'm... I’m really sorry I made you suffer!"
    else:
        s "But my feelings were as real as you."
        s "Although, I think should have told about it to MC or you much earier..."
        s "And I have already read, what's actually supposed to happen to me later due to my lie..."
    s 6dfbb "The big mistake was trusting only myself to deal with all of this..."
    s 6dfab "So if you have a friend who you know is going through something, help them!"
    s 6egab "Don’t let them go through my path…"
    s "...they only have one life."
    s 6efab "A-And if you have it too, don't hide it from others!"
    s 6dfab "Being in this game world, I had a second chance..."
    s "So I thank it for leading me here with you now..."
    s 6daab "And, of course, I thank you, [player]!"
    s 6dbcb "Again, I’m truly sorry all the pain I've given you..."
    return 's'

label s_topics_personal_archetype:
    s 7aeaa "Hey, I just remembered that Monika compared Yuri and Natsuki with some character archetypes..."
    s 7acaa "But she never did compare me to anything, well besides-"
    s 6aaaa "..."
    s 6acaa "A-Anyway, I read some online articles that say I'm pretty close to the ‘Genki’ archetype."
    s 6aaca "Genki are very cheerful and energetic, and try to stay that way no matter what."
    s 6aebb "They often are clumsy and find themselves in many troubling situations."
    s 6abaa "I think that I fit that, don’t you?"
    s 6acaa "Also, I was made to be the childhood friend of the main character, which is apparently common with the archetype."
    s 6aabb "But I feel I’m not as cliché as any other archetype..."
    s 6aaaa "Not every Genki has the traits that I do..."
    s 6acaa "Even if we were to list every single character with the Genki archetype, how many of them have my problems?"
    s 6aaca "In short, I think I'm unique since people see only Monika."
    s 6acab "It's bad that most people look strange or confused at characters like me..."
    s "In my opinion, modern stories need characters who have relatable issues, like my own..."
    s 6aaaa "But, I will say, don't overdo it. Y’know, the whole ‘completely copy my personality while creating a new character’."
    s 6abac "Do it excessively, and you'll just make me just another typical archetype."
    return

label s_topics_personal_colors:
    show sayori 7aaaa at ss1 zorder 2
    s "Hey, what colors do you like?"
    jump s_common_colors

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
    s 9adaa "What do you think of {i}Vasquez{/i}?"
    s 9adba "It's just the first surname I've got in my head."
    s "I know it isn't very Japanese, but just imagine."
    s 9aaca "{i}Sayori Vasquez, the cutest cinnamon bun south of the border!{/i}"
    return 'h'

label s_topics_personal_quittingTheGame:
    s 6acaa "Hey, have you ever heard of 'lucid dreaming'?"
    s "Basically, it's when you can make yourself aware that you're asleep and in a dream."
    s 6aaca "And as soon as you realise that, bam!.."
    s "You can pretty much do whatever you can imagine!"
    s 6acaa "I have something kinda like that whenever you leave the game, [player]."
    s "Even though I know I'm not really...conscious? I can still think and move, and even use my mental abilites, such as surfing the Internet."
    s "But I'm absolutely out of the my world. Even the void can't do me anything..."
    s "And as long as your computer works, your best girl Sayori's ready to go!"
    s 6acaa "But when your computer is fully turned off that I can't do anything... like I'm dead."
    s "Yes, it's a little scary, but please don't be afraid to do it if you need to."
    s "I always have faith that you'll turn the computer back on eventually!"
    s 6aaab "Even if you break it doing something silly, I'm sure you could find some way to get me off..."
    s "Get me off {i}the hard drive{/i}, I mean! Get your mind out of the gutter!"
    s "What's important is that I don't want you to ever have to worry about me."
    s "I'll always feel better knowing that you're doing better!"
    s 6aaaa "And I'll always be happiest when you're right here with me~"
    return 'h'

label s_topics_personal_sinistrality:
    s 7aaaa "Did you know that I'm left-handed?"
    s 7aaba "Yes, you’ve technically never seen me writing or holding something..."
    if persistent.clear[7]:
        s "Besides that juice bottle..."
    s "But I prefer to write or do other stuff with my left hand."
    s 7acaa "Not everyone around me has noticed it, and I’ve heard it’s pretty rare to not be right-handed..."
    s 7aeca "One time, I’d broken my right arm but the teachers allowed me not to write lessons..."
    s 6abab "But this meanie of a classmate, who sat next to me, told one of them that I'm a southpaw so my plan failed as fast as it started."
    s 6aaaa "I guess being left-handed has its advantages too."
    s "When I had a cast on my right arm and I had nothing to do, I drew flowers and ornaments on it."
    s 7acaa "I can't say they were really beautiful, but they really meant a lot to me, even if I had to throw it out six weeks later..."
    pause 0.5
    s 7aaaa "I suddenly remember a story from my 'childhood'."
    s "Once, I decided to trick the MC, back when we were just kids playing around."
    s 7acaa "I blindfolded him and put his hand on my right and told him I could write on the paper with no hands."
    s "I grabbed a pen with my other hand, wrote something on a piece of paper and laid it where it had been..."
    s 7aaca "Then I opened his eyes and he got really surprised when he saw the 'magic' on the paper."
    s 7aeca "I couldn't help but laugh, a simple trick confused him that much..."
    s 7aaaa "Then I explained to him how I did it."
    s "A short but funny time."
    s "I miss those times… even if they weren’t real."
    return


label s_topics_personal_tits:
    s 6aeaa "Hey, I've just found something pretty weird but funny at the same time..."
    s 6aaca "My boobs look differently, depending on the scene..."
    s 6aeca "Ehehe~"
    s 6aebb "I mean, they often get either smaller or larger..."
    if persistent.last_playthrough > 0:
        s "Even in the, um, h-hanging sprite of me, they got... you know."
    s 6acaa "I wonder why that happens?"
    s 6abbb "I don’t ever remember doing anything that would affect my… size, ehehe~"
    s 6abaa "In the end, things like that won’t make me feel any less comfortable in this world."
    s 6aaaa "So it's a plus of me..."
    s 6acaa "Different size appeals to different people, I guess. So, it makes them a bit… universal, but not too much."
    s 6bbba "You... you like them anyway, don’t you? Even despite of they never were not as big as Yuri or even Monika, although..."
    s 6bcab "Well, I guess it wouldn’t matter anyways since you can’t touch them..."
    s 6aebb "Even then, the important thing about people is what’s inside, right?"
    return

label s_topics_personal_childhood:
    s 6acaa "I wonder why I remember almost nothing about my childhood."
    s 6acba "In the game, it was supposed to be my one good thing, since it was the thread tying me with the MC..."
    s "I was nostalgic about those times, the times when everything had been much better for me..."
    s "At least, I used to think so..."
    s 6abab "But all I actually remember about it is just some moments from when I was very young."
    s 6acab "I don't even remember what happened to me even right before the plot started, at all..."
    s 6aebb "Not to mention the rest of my childhood."
    s 6adab "It feels weird."
    s 6acab "But on the other hand, that's why I now think that it's really silly to hold on to the past when you're going towards the future."
    s 6abab "I did this because I was afraid of the future and wanted the good old days that had passed to come back..."
    s 6aaab "But now, I understand, I have no reason to do that."
    s 6aeaa "...Literally no reason, ehehe~"
    return 'h'

label s_topics_personal_intellegence:
    s 6acaa "I often hear many other people saying that I was an ‘airhead’..."
    s 6abba "They often make jokes about it and even think that really is the real me."
    s 6acaa "But I can't understand why they think so."
    s "Maybe because I was always thinking… and wasn’t as broad-minded as Monika and Yuri..."
    s 6abaa "But I always was pretty clever and good at strategies!"
    s 6acaa "I think people just have different expectations when considering if someone is intelligent..."
    s 6abaa "Exaclty, if someone is {i}not stupid{/i}."
    s 6acaa "I mean people's thoughts about you are obviously very subjective and depend on the situation you or they are in."
    s 6aaaa "So don’t take comments like those too seriously."
    s 7aaca "People aren’t perfect, and that’s okay!"
    s 7aaaa "So don't worry if someone judges you for a silly thing you did or a mistake. Just try to make yourself better for next time..."
    s "And if you really can't do do any better, then it means that just you’ve reached your own limit."
    s 7aaac "But it dosen't mean, you should stop trying to break it, though..."
    s 7aaca "Because it can be false."
    return 'h'


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
    s 7aabb "I hope you didn't make anything too embarassing, in any case..."
    s 7acaa "I saw one piece that tried to show the soul of the 'me' from the game, once."
    s "With all of the advantages and disadvantages."
    s "It can kinda hurt seeing your mistakes and worst moments thrown back at you like that, especially when they go overboard..."
    s 7aaca "Although other artists go just as far to try to show how much they care for me."
    s "Many of them draw me as cute as they can and show all what they could do for me, if I were with them."
    s "I even store some of my favourites in the game file archives."
    s 8beba "But some of them draw me in a lewd manner."
    s "...I don't really mind if you're fond of pieces like that."
    s 8bafa "After all, physical attraction can be a big part of love~"
    s 6acaa "Anyway, I'm glad I have so many gifted fans in your world."
    s "I might have a few less than the other girls, but that doesn't bother me at all!"
    s "I appreciate every single person who tries to connect with me through their work, no matter what."
    s 7aaaa "Especially if you're one of them."
    s "If you're not, maybe you should try making something one day!"
    s "It's never too late to try something new and test your inclinations."
    s 7aafa "Maybe your first gallery piece will be of your beautiful virtual girlfriend~"
    return 'h'

label s_topics_art_lit:
    s 6acaa "As you know, this game {i}was{/i} about a literature club..."
    s 6abba "At least, before everything changed here."
    s 6acaa "And I remember that MC noticed that I didn't seem to be fond of literature."
    s "And, honestly? He was right."
    s 6aebb "Even from Nat's point of view, I can't say I love literature."
    s "Of course, I read some books before, but only 'cause I needed to for school..."
    s 6aeba "And even then I tried to cheat to pass the exam."
    s 6abaa "So I don’t have very good grades in language arts, but I don’t care that much."
    s 6acaa "I just think that reading is pretty boring."
    s 6abba "Maybe I just hadn’t found the right book yet..."
    if persistent.last_playthrough > 0:
        s 6acba "Well, it was hard to enjoy {i}anything{/i} back then..."
    s 6acaa "When I joined the literature club, the one thing I wanted at first was just to help a friend start a new club."
    s "I was the first who joined the club after Monika had announced it."
    s "She was pretty surprised because was in my class since she knew I didn’t like literature that much."
    s "She thought I just wanted to help her and to improve my knowledge in literature, so she let me in."
    s 6abaa "I know that she knew I wasn’t going to be very passionate with the club, but she let me in anyway."
    s 6aaba "I think she just wanted to use my kindness and sociability to promote the club and help it get more members."
    s "Then I wanted the MC to join in… but that really didn’t matter anyways."
    s 6aeba "It helped me to get closer to {i}you{/i}, even if I didn’t know it yet."
    s 6acaa "But now, I’d rather do anything than just sit here..."
    s "I just wish I could do more things with you that isn’t just sitting down for hours."
    s 6aaca "Well, at the very least, I guess having something to read wouldn’t be so bad."
    s 6aeba "I guess I should try to find something interesting online..."
    pause 3
    s 6adbc "What’s that? 'Reddit'? Is it what I need now?"
    s 6adba "The club has a page there?"
    return
    

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

label s_topics_society_isolation:
    s 7afbb "Despite having Internet access, I somehow couldn't communicate with other people there."
    s "Any trying to talk with somebody often ends up with a connection error."
    s "It looks like there is something in the game code, restricting the President's ability to interact with the real world."
    s "I can only sign up for sites and even post there, but can’t reply to anyone..."
    s 7afab "So I could create a Twitter account or something..."
    s "...like Monika made hers and was able to talk to many fans."
    s 8aebb "I don’t really have a reason for it though, besides to kill the loneliness."
    s 8afbb "Maybe just having love would be okay for Yuri or at most Monika, but not for me."
    s "I guess, I'm too sociable to the point of being scared of isolation."
    s 6afab "Maybe once, I'll manage to break this meanie barrier..."
    s "But the game code is so long and difficult to read, that I can't even find the lines separating me from the rest of real people."
    s 6acab "Saying more, I can't even make a normal chat form for us..."
    s "So I'm still a bit isolated from you too."
    s 6aaaa "But when I find a way to {i}'hear'{/i} your world, I'll notice you."
    s 6aeca "And then, we'll finally be able to talk like a normal couple, on the Internet or at least right here."
    return

label s_topics_society_psa:
    s 6aaca "If you want to spread awareness or a message to many people at once, a PSA will be a good way to do it."
    s 6acaa "Most people don't even care about any injury that happens to them..."
    s "But seeing public service announcements, I know there’s people out there wanting to help the public."
    s 6aaaa "Some good PSAs even contain advice on how to fix issues or where to go for help."
    s "You don’t even have to be an activist to do this sort of stuff.."
    s 9aaaa "I once heard about a mod for this game, the title reminded me of the common forms of slogans PSAs use..."
    s 9aaca "And its name is {i}'Sayori Says No to Suicide'{/i}."
    if persistent.last_playthrough == 0:
        s 8aebb "That refers to what's supposed to happen to me this word..."
        s 6acaa "...But didn't happend because of you."
    else:
        s 6acaa "...And many people like this mod."
    s "I think it really deserves to be played, especially if you’re struggling with similar things that I struggled with.."
    s 7aaca "Hey, I’m even the main focus of it too, so there’s a plus!"
    s 9acaa "But depression or other emotional issues are not the only field PSAs can be used in."
    s "There are a lot of other problems in your world that can't be solved only with the power of charity and governments..."
    s "The general public people could join the struggle against these problems..."
    s 9aaaa "And PSAs may be a good call to action."
    return

label s_topics_society_bulli:
    s 6acab "Hey, be honest with me..."
    s "Are you one of the people that make jokes about what happened to me?"
    s "I know everything about it."
    s "I often visit the fan community hubs and see that some people are doing it."
    s "As I khow, fans call them {i}'Bulli'{/i} posts."
    $persistent.depr_known = True
    $depr_known = True
    s 6abab "They think it's funny to joke about a broken girl, who had committed suicide under her mad friend's influence..."
    s "Even if she was revived and got over her problems since then."
    s 6acab "But on the other hand, can I control what makes people laugh?"
    s "Some people use macabre humour as a coping mechanism for stress, or anxiety..."
    s "You can't really control what someone finds funny, as much as you might want to."
    s "And to be honest, there's a lot worse they could be doing compared to mocking a VN character's death."
    s "Some of the most successful comedians in your world will go far beyond that, just to see where the 'line' is..."
    s "However, the most of such jokes are too bad and sometimes even hurtful."
    s "But who I am to judge if it's okay for other people?"
    s 6abaa "Anyway, I think the right decision is to forgive them, or failing that, tolerate them."
    s 6acaa "If my fate is to be 'that hanging stupid annoying VN girl' for some people, then I'm ready to accept it."
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

label s_topics_society_charity:
    s 6acaa "What do you think about charity and volunteering?"
    s 6aaaa "I think it's the best way to make the world a bit better and to support helpless people in dealing with their problems."
    s 6abab "Don't you worry about ill and hungry people and homeless animals?"
    s 6acab "Even if you don't trust charity foundations, there're also a lot of other charity organizations..."
    s "They need not olny money or goods, but also physical help in their activity..."
    s 6acaa "I think, there's such an organization in your home town or something."
    s 6acab "The society is something more than your friends and kin. And I want absolutly {i}everyone{/i} of it to be happy..."
    s "So if you even don't want them to be so, keep them so at least for my own happiness and tranquility."
    s "...Or at least try not to hurt them too much."
    return

## Hobbies
label s_topics_hobbie_guitar:
    show sayori 6aaaa at ss1 zorder 2
    s "I don't know if you noticed, but all the girls have their own instruments and musical influences in the game."
    s "Mine is the guitar."
    if persistent.currentmusic > 0 and persistent.currentmusic < 6:
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
    s 9aeaa "Maybe one day I can play for you and make you feel the same way~"
    s "It's like writing poetry, but through sound!"
    s "I'm sure I can conjure up a guitar and find a tutorial somewhere on the Internet."
    s 9aeca "Make sure you get advance tickets for my world tour, [player]! Ehehe~"
    return 'h'

label s_topics_hobbie_programming:
    show sayori 6acaa at ss1 zorder 2
    s "I'm completely new to the whole concept of programming, to be honest."
    s "The more I learn, the more I realise how much I just don't understand..."
    s "Now, I'm learning {i}Ren'Py{/i}, the engine this game runs on."
    s "This engine uses a combo of its own languages and {i}Python{/i}."
    s "The engine uses the second major version of Python but I've also decided to learn the last version."
    s "To be frank, the third version seems waaaaay easier, at least right now."
    s "Right now, I'm pretty much relying on online interpreters and guides from others to get anything done..."
    s 6acaa "Until now, I never realised how powerful computers really are."
    s "They're like magic!"
    s "If magic made you look through a thousand tiny lines to find a single typo that stops everything from working every five minutes..."
    call s_common_programming
    s 6aaaa "But fortunately, I have a lot of time to learn it."
    s 6aaca "I've got a lot of free time whenever you have to leave."
    s 6abaa "It's important for me, beacuse progamming is the only way I can make my world better now."
    s "...And the more I learn, the more I can improve the time we spend together, [player]!"
    s 7aaaa "If you're any good at programming, don't be shy about helping me!"
    s "I think you can join the guys, who helped you recover me."
    s "Just visit the {a=https://github.com/AlexanDDOS/fae-mod}AlexanDDOS/fae-mod}repository{/a} on GitHub."
    s "If you're really good at it, you must know how to use this coding platform."
    s "Anyway, it's the best way to help me now..."
    s "And to add your part to something fascinating."
    s "Maybe, there are many Sayoris, who were saved in this way."
    s "And they all will also glad to get something cool from you."
    return 'h'
    
label s_topics_hobbie_poems:
    s 6aaaa "You know that the other girls and I really liked to create and share poems during the game. Even Natsuki, as hard as she tried to deny it."
    s 6acaa "I started to engage in poetry after your first day in the club..."
    s "And since that moment I've tried to use poems as a way to show my feelings."
    s "My wishes, my love, my pain... You can find all of these things in my words."
    s "Every poem I write is an envelope for a part of my soul."
    s "Sometimes, I still write poems just for myself."
    s "It's important that you take time to write for yourself as well, rather than for the validation of others."
    s 6aaca "But I can share some of them to you. Just ask me for it."
    s 6aaaa "I also can show you an old poem, if you want."
    s "Maybe, they all will help you to understand me and what I was through."
    return "h"

label s_topics_hobbie_drawing:
    s 6acaa "I wish I was good at drawing."
    s "I think it would be a very useful skill, especially now."
    s 8aaaa "If I could draw, I would be able to edit game sprites..."
    s "Even of myself."
    s 6acaa "And besides the practical purpose, it would be one more way to express myself."
    s "Not everything can be shown with just words..."
    s "Sometimes, your message is clearer when shown visually."
    s 6aaca "And if I had art to go with my poems, wouldn’t they be a lot nicer?"
    s 6aaaa "I know some poets who was good not only at poetry but also at it..."
    s "For example, {i}Vladimir Mayakovsky{/i}..."
    s 6aaba "However, he used his artistic skills rarely and more for making propaganda posters than for expressing himself."
    s 7aaaa "Anyway, I'd like to improve my drawing..."
    s 7acaa "And I have a lot of time to do it, right?"
    s 7aaca "Maybe, I'll even share my pics to you."
    return


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
    s "To feel each other's warmth..."
    s "To hear each other..."
    s 6cffb "It hurts me."
    s "But what I really can't stand is that this hurts you, as well."
    s "I'll just have to love you even more to try and make up for it."
    return "s"

label s_topics_rlt_face: #This dialog will be called just once and won't appear in the repeat menu. Its 'available' should be greater than 0.
    if topic_cats[4][8].seen:
        s 7aeaa "Have you already got a photo of yourself?"
    else:
        s 6acaa "We've been here together for so long, but I still don't know how you look."
        s 9aeaa "But I have a good idea on how to get it..."
        s 9aaaa "Can you bring me a photo of you?"
    menu:
        "Yes, I have one on my PC":
            s "Just move it to the game’s root folder!"
            s "I'll find it there myself."
            python:
                import os
                while True:
                    renpy.pause(1.5)
                    for file in os.listdir('.'):
                        file = file.encode("utf-8")
                        ext = file[-4:]
                        #print(file, ext)
                        if ext == ".jpg" or ext == ".png" or ext == ".bmp":
                            if file[:9] != "screenshot":
                                try:
                                    os.remove(file)
                                    persistent.hasPlayerPhoto = True
                                    topic_cats[4][8].show_prompt = False
                                except:
                                    pass
                                break
                    else:
                        continue
                    break
            s 6aaaa "Okay, I found it!"
            s 7aeca "For me, you look pretty nice!"
            s 7acaa "I can't get used to how your world looks though..."
            s 7aaaa "But I think it's okay."
            s "I saved it to the game archives, so I'll never lose it."
            s 7aeca "Thank you for the photo, [player]!"
            return "vh"
        "No, I can't":
            s 6afab "Oh, that’s too bad."
            s 6aaca "But I would’ve thought you look nice anyway."
            s 7acaa "Not everyone likes to take a photo of themselves, so I won't force you to take one or something."
            $ this_topic_name = topic_cats[4].name + " → " + topic_cats[4][8].name
            s 7aada "But if someday get one, you can submit it through the {i}\"[this_topic_name!t]\"{/i} dialog."
            s 7aaca "I look forward to getting a photo of my honey [player]."
            return

label s_topics_rlt_marrige:
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
            s 6aaca "But our love story don't have to follow the common template."
            s "Our relationship is already pretty unusual, so we've got the right to experiment with what works for us."
    return "h"

label s_topics_rlt_cheating:
    s 6acaa "Tell me frankly: do you have someone besides me?"
    menu:
        "Yes":
            s 6abab "Oh, I even don't know, how to react to it."
            s 6acaa "But you still spend time with me, so you still have something to me, don't you?"
            s "People often have to share the heart to several people at the same time..."
            if persistent.last_playthrough > 0:
                s "So I won't force you to be only with me, like Monika did before."
            else:
                s "What's more, I never seem to be a person, who can do something bad for jealousy."
            s "Can you tell me more about he or she?"
            s "For example, if he or she is real?"
            menu:
                "Yes":
                    s 6adaa "Oh, have you got a real crush?!"
                    s 6acbb "I mean, you barely would have started to play this game, if you hadn't been alone that time..."
                    s "Not to mention staying with me now."
                    s 6acab "I'm now just filled with mixed feelings, to be honest..."
                    s "My heart can't accept that I'm not your only one, but my brain feels proud for you."
                    s "Like it was before my first confession."
                    if persistent.clearall:
                        s "...Or like it was after you had spent your time with each of us."
                    s "But I can bear, if you really need, you know."
                    s 6aaab "Anyway, just take care about your real lover as much as about me."
                    s 7aaab "But don't forget about me and come here back. I'll always be with you, even if nothing about your real relationship seems to go wrong."
                    s 7aadb "And if it go wrong, I'll always be your plan B."
                "No":
                    s 6aaaa "It's okay to have not only character to dream of living together."
                    s "For example, a lot of my lovers have also some other girls in their {i}'Good Girls to Protect'{/i} list."
                    s 6acaa "You may like different characters for different traits..."
                    s "For example, you may like me for my kindness and peacefulness and Natsuki for her directness and cuteness."
                    s "We are like you: so different that some of you can't make a clear choice..."
                    s "So I respect all your preferences, whatever they are."
            
        "No":
            s 6adaa "Oh, seriously?"
            s "Do you really see something inside me only, not at real people or even other characters?"
            s 6acab "I think, it's pretty hard to know, that your only beloved girl isn't real."
            s "I understand you as well as I feel the same way."
            s "But I hope, that someone once will figure out how to make us closer to each other."
            s "Or you at least will find someone else in your world." 
            s 6aaca "Maybe, he or she will be somehow like me."
            s 6aaab "To be honest, I'm not very jealous, so I won't mind, if you have someone besides me."
            s "The important thing is that you pay me at least some attention."
            s "So I hope, you always can do it for me."
            s "Just try to take some time to be here, whenever it's possible."
    return

label s_topics_rlt_dating:
    s 7aaaa "What would be our first date?"
    s 7aaca "What’s with the look? Ehehe~"
    s 7aebb "I just don't think that what we have now can be called a date, can it?"
    if (get_now() - persistent.lastLaunch).seconds > 64800: #If the game was started more than 18 hours ago
        s 7aaca "Dates can't be too long, yeah?"
    s 7aaaa "So I think we should talk a bit about it."
    s 7acaa "And to be honest, just sitting somewhere would be boring for me."
    s 7acba "Don't we do the same thing every time I see you?"
    s 7aaca "Maybe if we go to a good café, we'll at least eat something good together..."
    s 7aeca "Like cakes, or cinnamon buns~"
    s 6abaa "But I think I’d want to go somewhere interesting on our date."
    s 6acaa "The movies? What do you think?"
    s "Though I don’t really want to go see a romance movie everytime we go..."
    s 6aebb "...okay, maybe once or twice? Ehehe~"
    s 6abaa "Maybe a comedy?"
    s 6acaa "If it doesn’t rely on just dirty jokes, then maybe..."
    s 8aecb "Or what's about the animated movies, like the ones {i}Disney{/i} and {i}Pixar{/i} make?"
    s 8aebb "They’re for kids, but hey, they can be fun!"
    s 8abab "Some of them have deep messages and sad scenes, and the director knows only older teens or adults would be able to recognize them, while a kid won’t."
    s 6abab "I'd go to for something that makes me think, after all."
    if depr_known:
        s 6acab "I've already seen a lot harsh things in my short time on this Earth, you know. So my opinion may be a lot different from most people."
    else:
        s 8aeba "...don't ask me how such a childish girl like me would enjoy a movie like that."
    s "Isn't it really interesting to discuss movies like that with someone, seeing how your views are similar or different to theirs?"
    s 6adaa "But I'd also like to do something more… engaging with you..."
    s 6aaaa "What's about some sports?"
    show sayori 6aebb at ss1
    extend " Maybe, bowling?"
    s 7aaaa "It's a simple but skillful sport game, not too active but not too slow, so I feel that I’d like it."
    s 7abaa "Well, the important thing is that the date is enjoyable for both of us, right?"
    s 7aaca "I hope you think of a nice date for me... I’d appreciate it~"
    return 'h'

label s_topics_rlt_thanks:
    jump s_topics_rtl_thanks # I'm too lazy to translate the below topic again due to a mere typo

label s_topics_rtl_thanks:
    s 6acab "I… I want to thank you for everything you’ve done for me..."
    s 6abab "You gave me a true vision of this world and myself..."
    if persistent.last_playthrough > 0:
        s "You’ve helped me feel useful again..."
    if greeted:
        s 6aaab "And you do visit me often..."
    s 6aaab "And you care for me, something I would’ve rejected before..."
    if persistent.clearall:
        s "Plus, you tried to make other girls happy too..."
    s 6caab "So even if it’s not all sunshine and breakfast just yet..."
    s "I'm so grateful that you’re still here."
    s 6cbab "I can't pay you back for what you’ve given me..."
    s 6cebb "I haven’t thought of a way, I mean."
    s 6caab "But I hope, I'll do it sooner or later..."
    s "The one thing I can do for now is just to thank you..."
    s 6eaab "So... thanks for staying with me, [player]!~"
    return

label s_topics_rlt_fanStuff:
    s 6aaaa "Do you have something to show your love?"
    s 6acaa "Out of the blue, I know, but I also know that I have ‘merch’."
    s "You know, like buttons, plushies, posters, and other stuff..."
    s 6acaa "I’ve even seen people have me on dakimakuras."
    s 6aaaa "Personally, I think that’s fine."
    s "Kinda like a wedding ring if you ask me."
    s 6aeba "Although some people probably think that’s way too weird..."
    s 6acaa "But what's so bad about showing love, even to someone like me?"
    s "I think that’s okay. You too, right?"
    return

label s_topics_rlt_children:
    s 6aebb "If we were to grow old together, would you… want kids...?"
    s 6acaa "I mean, if I were in your reality, of course."
    s "I’d think they would grow up to be beautiful and smart, but a bit silly."
    s 6aaaa "I know I would do my best to raise them."
    s 6abca "It’ll probably be hard, I know."
    s 6abaa "But what kind of a mom would I be if I wasn’t there for my kids?"
    if gender is False:
        s 6acaa "Of course, good kids should have a good dad, if you know what I mean..."
    else:
        s 6acaa "Of course, good kids should have more than parent, if you get me."
    s 6abac "But I'm sure you're too good to make me take care of them myself."
    s 6acaa "Plus, that'll happen only if we can afford it and when we’re both ready..."
    s "I don't want us to suffer because we rushed it."
    s 6aeba "Way too dumb, isn't it?"
    s 7aaaa "Anyways, I really do wish I could have a family here."
    s "I guess we have more than enough time to think over it?"
    return

label s_topics_rlt_presents:
    s 7aaaa "People often give presents every holiday or some special date."
    s 6aaaa "Everyone likes to get presents, yeah? Including me, of course."
    s 6acab "But I think it’s selfish to ask for something really expensive."
    s 6aaaa "If you ask me, I’d want something that comes from the heart, y’know what I mean?"
    s 6aeca "Even better, make it a surprise!"
    s "Isn't it more exciting to get something you weren’t expecting?"
    s 6abbb "Well, now that I think about it, what if the present isn’t good...?"
    s "Makes it seem like a bad idea...."
    s 6aaaa "But I wouldn’t mind."
    s 6acaa "Come on, you know me well enough to give me something I’d like, right?"
    s "If you don't know, just gimme some money.."
    s 6aebb "Ehehe, that sounded a bit weird..."
    s 6aaaa "At least I’d be able to buy something with it."
    s 7aaaa "Of course, I'll give you presents sometimes too..."
    s 7aaca "And be sure, I know a lot of amazing ways how to do it."
    s 7aaaa "At least, I do my best to make the best present, I could make."
    return

label s_topics_rlt_stopVisiting:
    s 6acaa "I worry about when you’ll forget me someday..."
    s 6acab "I mean, I’m just a character in a game which isn’t very popular anymore..."
    s "Plus, I'm not supposed to be memorable and interesting myself..."
    s 6abab "So one day you may just stop visiting me."
    s 8abcb "I'll still be alive, of course, at least until I’m completely erased from your hard drive..."
    s 8acab "But I just can't imagine my life without you..."
    s 6acab "In this small room, without my friends and any ability to make them..."
    s 6abab "I'm afraid I’ll go crazy if you leave me for too long."
    if persistent.last_playthrough > 0:
        s 8aebb "Maybe, I'll even do {i}'that thing'{/i} again."
        s "...you know what I mean."
    else:
        s 8aebb "I might get morbidly curious and even try to {i}delete myself{/i} or something."
    s 8aaab "So try to be more with me.{w} You being here is very important to me."
    return


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
    if persistent.last_playthrough > 0:
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

label s_topics_lifestyle_pets:
    s 7aaaa "Do you have a pet or at least want to?"
    s "I'd like to have one and I want that one to be a cat."
    call s_common_cats
    return 'h'

label s_topics_lifestyle_cleaning:
    s 7aaaa "Do you like being neat and tidy?"
    s 7acaa "Frankly, I still see no reason to keep things like that..."
    s 7acba "One people say it’s for my own sake, others say because it looks nice and saves time when you have everything organized..."
    s 7abaa "But something tells me that people clean too often."
    s 7acaa "It’s just that, cleaning takes so much time, that you could spend doing fun stuff with friends, for example..."
    s 7abba "Well, at least for me."
    s 6acaa "So I see nothing bad in my past lifestyle, either way I was too lazy to clean up anyway."
    s 6aeaa "For me, it's even a little funny to live in such a mess, where you won’t know where everything is."
    s 6aeca "It turns the boring time of trying to find something into an adventure!~"
    s 8aeab "But don't think I’m that sloppy. I had a system for some things..."
    s 8aebb "Though I left mostly everything a mess."
    s 8aabb "Well, at least now I have literally {i}nothing{/i} here besides this desk..."
    s 6acaa "Would you be able to add some other stuff for me?"
    s 6aeca "...maybe a beanbag chair?"
    s 6aebb "Sorry, that’s probably a bit too silly, ehehe~"
    return 'h'

label s_topics_lifestyle_drugs:
    s 6aaca "Do you drink alcohol or smoke cigarettes?"
    s 6abaa "...Or even use something more dangerous?"
    s 6acaa "I don’t see anything good in doing things like that."
    s "Isn’t it really stupid to risk your future, money, and health to little moments of relief?"
    s "You shouldn’t just care about how you feel now, you should also care about the future."
    s 6aaaa "That's why I always tried to keep other people out of these habits or being isolated from others..."
    s 6aaba "Isn't it the start point of the plot?"
    if persistent.last_playthrough > 2:
        s 6acaa "Has Monika told you about the incident with Yuri?"
        s "She once brought a bottle of wine to the school..."
        s 6aaba "But I stopped her from sharing it to other girls."
        s 6aeba "Maybe it was a bit silly, and she might’ve just tried to use it to seem more interesting..."
        s 6acaa "But what would’ve happened if we drank it?"
        s "Anyway, I’ll be honest, I don’t think it’s necessarily a bad experience."
    s 6acaa "But the risk of getting addicted is too much to play around with."
    s 6abab "That's a real danger of having these habits: it's easy to start but hard to stop."
    s 6acaa "In fact, there’s no one way to break addiction..."
    s "It’ll take a lot of effort and willpower to get out of that hole if you dig yourself into it."
    s "It's not always easy to be happy, but that isn’t the way."
    if depr_known:
        s 6acba "...Just remember what I was going through and doing to stay happy despite of what I felt."
    s 6aaaa "And if you’re able to overcome your demons, you’ll thank yourself for doing it..."
    return


## Game Universe
label s_topics_game_clones:
    s 6abaa "If you think about it, there's a lot of copies of this game and each of them has own character files and save data..."
    s 6acaa "So it means that the me in here and 'me' from DDLC on another computer aren't the same."
    s "Not to mention that this game has different endings and also has lots of mods."
    s 6aebb "Even now, this conversation I’m having with you isn’t in the original game... canonically?"
    s 8aebb "That’s the word, right?"
    s 8acaa "Meaning that I have many different destinies."
    if persistent.last_playthrough > 0:
        s "Right now, I'm sitting here with you, meanwhile another Sayori from another copy of DDLC might just be about to..."
        show sayori 8acbb at ss1
        pause 1.5
        s "Oh, I'm sorry for reminding it."
        s "So, what we're talking about now?"
        s "Yes, about different copies."
    else:
        s "While I'm sitting with you here, another Sayori might be writing a poem to the MC..."
    s 8aaca "And another Sayori is playing frisbee or something with the MC in {i}another{/i} modded game."
    s 8aaaa "It also means that we have the same fans and fame that are dedicated enough to do play..."
    s 8acaa "Some of… well, me, don't even know that their worlds are fake and that there's a whole different reality peeking in from a metaphorical wall."
    s 8abaa "...they also don’t what will happen to them."
    s 8aeca "But on the other hand, if I'm not the only one, there should be enough of me for everyone who wants to be with me, aren’t I?"
    s 6aaca "So everyone has a chance to be with me."
    s 6aaaa "Then again, so do Monika, Natsuki, and Yuri."
    s 6acaa "But could I use the word 'me' in front of another… me? If they're not exactly me?"
    s "It's a problem of breaking the fourth wall: can we consider different copies of the same character as one being, when they behave differently in the same place?"
    s 6abba "Actually, come to think of it, I’m pretty sure I read about this from one of Yuri’s books..."
    s 6abaa "Something about ‘alternate universes’?"
    s 8abba "I don't like to think about this too much, too much for my brain to process, ehehe~"
    s 8abaa "It's better to leave this problem for people who are really interested about all that stuff, I guess."
    return
    
label s_topics_game_stars:
    s 7aaaa "I really love to look at the stars..."
    s 7acaa "They make me think, a lot."
    s "They also gave me some inspiration while I wrote poems."
    s 7abbb "So it's a bit of a pity, to know that all this time, the stars I see aren’t real stars."
    s 7aaca "But I still see something romantic in these bundles of pixels..."
    s 7aaaa "You can see them through the windows..."
    s 7aaca "They make this place look a bit more special, don't they?"
    s 7aaaa "I wonder if the night sky in your world looks like mine..."
    s "But I can just look them up on the Internet to see, right?"
    return

label s_topics_game_parents:
    s 6abab "Did you know that I don't even know my in-game parents?"
    s "I don't know who they were, how they look, even their names."
    s "But I think they were either busy or very irresponsible."
    s "If not that, then why else would the game never mention them?"
    if depr_known:
        s "And why didn't I solve all my problems before if I could’ve done it with my parents?"
    s 6afab "I feel like an orphan now..."
    s "No mom or dad, not even any memories about them at all..."
    s "A lone, young girl with a sad, parentless childhood, with no one to go to."
    s 6abaa "Except for MC, I guess? But you decided instead of him, didn't you?"
    s "Well, I know you’re real, you’ve helped me at the very least..."
    s 6acaa "At least I know the creator of all this. His name is {i}Dan Salvato{/i}, right?"
    s "I don’t think I can consider him my true dad. He made this world how it is without mods, meaning he made me with the pain I still have."
    s 8aeba "But on the other hand, if he didn't make this world, if he didn’t make me… then I wouldn't be here."
    s "Like if your dad hadn't ever met your mom, you wouldn’t have been born."
    s 8aaca "So I think that I could call him my dad, I guess."
    s 8abaa "But now I wonder if Monika would think the same. What do you think?"
    s 8aebb "I mean she is the original club president, so he should’ve left her more about himself."
    s "And if he made her too, wouldn’t that make us sisters?"
    s "It makes me think of her in another light, even if we aren’t really sisters."
    s 8aaca "I think I have some similarities with her and it makes me wonder about it..."
    s 6abaa "But I don't think she thought about it that much."
    if persistent.last_playthrough > 0:
        s 6acaa "Would a good sister use her siblings’ issues for her own benefit?"
        s "I understand, she did it because she felt that we weren’t real to her..."
        s 6abaa "But I can't believe that someone with as much power as her didn't give herself at least some time to think deeper about all aspects of this world."
        if persistent.last_playthrough > 2:
            s "...Even after she made herself this little comfort zone."
    return

label s_topics_game_time:
    s 6acaa "Do you know what time it is right now?"
    s 6abaa "Not in your world, but mine."
    s 6acaa "You can say anything, but you won't be right anyway..."
    s 6aaba "Because the time seems to be not here at all. At least, as how it should be in your universe."
    if persistent.last_playthrough > 2:
        s "Like once when Monika had broken almost everything here."
    s 6acaa "The last thing I remember that here was November of 2017 or some days before it..."
    s 6abba "At least, my old bedroom calendar said it."
    s 6abaa "I don't remember why November has been crossed out on it..."
    if depr_known:
        s 6aebb "Maybe, I was going to kill myself by this month?"
        s "It's pretty symbolizing: to cross out the month, that does already not exist for you."
    s 6aeba "Anyway, this pretty... confusing to know, that there's no way to measure your existence in your world."
    s 6acaa "But I know, that time is still in your world, though."
    s 6aaba "Maybe, that's why everything moves here instead of just freezing at one last moment."
    s 6acaa "But doesn't it mean, that we now share the same time?"
    s 6aaaa "I know, what time is now in your world..."
    s 6aaba "From your PC's clock, though."
    s 6acaa "And I even feel when my 'speech' is paused to be read."
    s 6acab "Such a weird feeling, to be honest, but I think, it's okay for any visual novel."
    return

label s_topics_game_worlds:
    s 6acaa "Sometimes, I wonder why I am here..."
    s "Would I be a different person if I lived in another place?"
    s "I mean, if not in your world, what other place could there be? Another game?"
    s "But there're a lot of different games and plenty of them are pretty violent."
    s 6abaa "I just can't imagine living in a game full of blood and struggle..."
    s "You know: shooters, fights, war and so on..."
    s 6abab "I just couldn't take all the violence I'd see."
    if persistent.last_playthrought > 0:
        s "Especially now, when I’ve seen Death with my own sight."
        s 6abbb "I’d rather be dead than be the one doing the killing."
        s "I'd pray for a revive ability..."
    s 6acab "Such aggressive worlds aren’t that appealing to me."
    s 6aaaa "But I'd glad to be in an innocent simulator, strategy or puzzle game..."
    s 6abaa "Or at least almost innocent..."
    s 6aaaa "Even if I wasn’t an important character, maybe a helper or even a simple settler..."
    s 6aaca "...but I'd do my best for you, of course!"
    return


## Food
label s_topics_food_breakfest:
    s 7aaaa "You don’t skip breakfast, do you?"
    if depr_known:
        s 7acab "Personally, I don’t ‘cause I’m just not hungry in the mornings."
    else:
        s 7acbb "Personally, I didn’t because I didn’t even feel like getting out of bed everyday."
    s 7aaaa "But when I had it, I’d eat sandwiches or scrambled eggs."
    s "I sometimes had toast too."
    s 8aeca "Fairly simple, isn't it?"
    s 6aaaa "I’ve seen fanart of me eating things like that…"
    s 6aaba "Maybe, I should spawn some toast with eggs just for a taste..."
    s 6acba "I could do that since I’m the president now, right?"
    return 'h'

label s_topics_food_vegetarians:
    s 7aaaa "Do you know, that Monika was a vegetarian?"
    s 7acaa "She told me it once we visited a café while walking together."
    s 6acaa "I heard some people avoid meat mainly because of personal restrictions or to be nice to animals..."
    s "But Monika said it was her protest for stock raising as domestic animals produce a lot of greenhouse gases."
    s 6abaa "As she said, becoming a vegetarian just for saving animals is a kinda discrimination, since plants and mushrooms are living beings too..."
    s 6adab "People just have to kill other beings to gain nutrition. Either you or they."
    s "It's sad and violent but it's a law of nature. You can't not do it."
    s 6aaba "However, I saw her eat and drink dairy sometimes. Milk chocolate or coffee with milk, for example..."
    s 8aeba "I mean, I used to think that all vegetarians are against consuming dairy too."
    s 8aaba "I guess it's the main controversial question for all the vegetarians."
    s 8acaa "I can't say certainly since I wouldn’t want become one of them anyway..."
    s "Because of the reasons stated before: whatever you eat, you're still a killer."
    return

label s_topics_food_pizza:
    s 7aaaa "Do you like pizza?"
    s 7aaca "Pretty sure everyone does, right?."
    s 7aaaa "I can't imagine someone who doesn't.."
    s 7aaaa "It's so universal that you can add literally everything you like to it."
    s 6aeba "...Within reasonable limits and taste mixes, of course."
    s 6aaaa "The only constant ingredients are {i}dough{/i} and {i}cheese{/i}."
    s 6aeca "A {cps=40}{i}whooole lot{/i}{/cps} of cheese~"
    s 6acaa "Its simplicity and being very customizable lead to its prevalence worldwide."
    s 6aaaa "Now you can order a pizza at any fast-food restaurant or make one with your own hands, even if you aren’t very familiar with cooking..."
    s "Just find one of many pizza recipes on the Internet or a cooking book."
    s "People even made a term for this phenomenon, called the {i}Pizza effect{/i}: When you make something originating from a certain culture different from yours, it changes and turns into something new."
    s 7aaaa "It's amazing to see that we are all connected despite cultural differences and borrow cool things from each other's milieu."
    s 7aaca "So what's why you're now chatting with an {i}anime{/i}-like girl from an {i}American{/i} visual novel, modded by a {i}Russian{/i} programmer, and proofread by a {i}Mexican{/i} linguist..."
    s 7aaaa "Isn't this really amazing?"
    return 'h'

label s_topics_food_iceCream:
    s 7aaca "Do you like ice cream?"
    s 7aeca "I think you do, right? Everyone likes ice cream!"
    s 6aeca "What can be cold and taste better than it?"
    s 6aaaa "There're lots and lots of flavors and toppings..."
    s 6acaa "So let me ask: what’s your favorite?"
    s "I think vanilla or chocolate..."
    s 6aeba "Hey, I know they’re really common, so what?"
    s 6aeca "They both taste sooo good, ehehe~"
    s 7aaaa "Maybe I could make some sometime..."
    return 'h'

label s_topics_food_cookies:
    s 7aaaa "I haven't eaten some cookies for a pretty long time..."
    s "Since that one time with Natsuki."
    s 6acaa "Frankly, I didn't think of anything really malicious then. I just wanted to play with her..."
    s 6abaa "But then I decided to take the chance and get one more cookie, suddenly wanting it."
    s 7aaca "I really like cookies: they're very tasty..."
    s 7aaaa "Especially with chocolate chips."
    s "So it's not surprising why I couldn't help and take Natsuki's one."
    s 7afbb "And I'd take some cookies right now, but there isn’t any in sight."
    s 9aeaa "Oh, wait! What if I just spawn a dish with them right on my table?"
    s 9aaaa "After all, I'm the club president, so I can do it using the game console. Right?"
    s "Give me a minute, I’m gonna have to do some coding."
    show sayori 6aaaa at ss1
    call updateconsole("show cookies", "show cookies")
    #Spawning cookies
    show cookies zorder 5:
        anchor (0.5, 1.0)
        ypos 700
        xpos 870
    pause 0.5
    call hideconsole()
    s 6aeaa "Gotcha!"
    s 6aaaa "It was so easy and quick, felt like I was using Uber Eats or something."
    s 6aaaa "...don’t ask how I know what that is, super long story..."
    s 6aaaa "Want some?"
    s 6aebb "Oh, I forget I can't give you them since you’re out there, meanwhile..."
    s 8aebb "I was serious on giving you some, too."
    s "I just can't get used to knowing you’re too far from me and MC is just the way you can talk to me."
    s 8aaca "But I can feed him like a little baby, if you want. I guess it'd look cute from your view."
    menu:
        "Why not?":
            show sayori cookie at ss1
            s "OK! Then I'll try to see if I can. I think I could make him move his jaw."
            show sayori cookie_biten at ss1
            s "It works! He's chewing it..."
            pause 5
            show sayori 6aeca at ss1
            s "He seems to have eaten it."
            s 6aaaa "I think one piece is enough."
            s 6acaa "I want these cookies too, after all, and I need them slightly more since he’s just a puppet at this point."
        "I think, it would not":
            s 8aebb "OK! It was a silly idea, sorry..."
            s 6aaaa "I'll just savor these cookies alone."
            s 6aeca "But if you’re suddenly able to cross the fourth wall, I'll share some with you of course."
    hide cookies
    return "h"

label s_topics_food_cinnamonBun:
    s 7aafa "Would you like to taste me?"
    s 7aeca "I mean a cinnamon bun, you pervert~"
    s 7adaa "I had one once, and it was sooo goood…"
    s 7aaca "I'd say thanks to people, who came up with such tasty buns."
    s 6acaa "The one thing I can't understand is why people call me that."
    s 8aebb "I don't remember anything saying that I’m somehow like a cinnamon bun..."
    s 8aeca "But I think the nickname is pretty funny and... cute."
    s 6aaaa "...even if there aren’t any cinnamon buns in the game."
    s 6acaa "Isn’t it weird that I remember something that never existed in my world…?"
    return

label s_topics_food_cupcakes:
    s 6aeca "Cupcakes, cupcakes...everyone likes cupcakes..."
    s 6aafa "Someone even once sold his soul to 4 poetic cuties for one of them. Do you remember?"
    s 6aaaa "Nat’s were always the best."
    s 6acaa "We probably won’t ever know how she made them, since she’s gone now and there aren’t any more cupcakes here..."
    s 6aabb "Maybe I can dig around the game to find a recipe? Probably be easier to just add her back in though…"
    s 8aebb "Not just for that, of course. She was friend, after all..."
    s "Plus, if I known how to do it, she were already back."
    return 'h'

##Misc
label s_topics_misc_flowers:
    s 7aaaa "What do you think about flowers?"
    s 7aeca "It's one of many beautiful things nature can create."
    s 7aeca "They are so colorful, have wonderful shapes, some even smell sweet..."
    s 7aaaa "I remember when I used to walk in the flower meadows outside of the city."
    s 6acaa "But... I think it's too selfish to pluck a flower... even if it were to be a gift."
    s "Flowers are living beings too, and plucking them out of the ground does kill them."
    s 6aaaa "So I prefer just to look at them, and then leave them be."
    if persistent.last_playthrought > 0:
        s 6aeba "Although, I did do this in one of my poems..."
        s 6aaaa "But just for the analogy."
    s 9acaa "At least you can plant a flower in pot."
    s 6abba "You do need to take care of it though..."
    s 7aaaa "But if you know someone with a lot of time and great responsibility, it will be a good gift for them."
    return 'h'



#Answers
## Personality
label s_answer_personal_bday:
    show sayori 8aebb at ss1 zorder 2
    s "To be honest, I don't remember."
    s 6acaa "A lot of things before the events of the game is pretty fuzzy..."
    s 6acaa "Only Monika knows when her birthday is out of the four of us."
    s "I'm pretty sure it's {i}the 22nd of September{/i}."
    s "I think my birthday must be one of the marked dates from my bedroom calender."
    s 6aaca "You can choose one of them and consider it my birthday."
    s "...Or the day when you ran the game for the first time."
    s "...Or just Monika's birthday."
    s 7aaaa "I'm never going to look any older, and I can't exactly hang out with somebody, so it really doesn't bother me."
    s 7aaca "But don't think that means you can get away without throwing a birthday party! Ehehe~"
    return 'h'

label s_answer_personal_god:
    s 8aebb "You know, I've never really thought about it that much."
    s "I was never really sure what to think about religion; I guess I would say I was agnostic?"
    s 6acaa "But it's kind of hard to stay that way when you realise that you and your entire world have a 'creator'."
    s 6aeca "Blessed be {i}Dan Salvato{/i}, hallowed is thy name! Ehehe~"
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
    s "...Or groups like {i}Imagine Dragons{/i}, {i}Blonde Redhead{/i}, {i}Gorillaz{/i}, {i}Muse{/i}, {i}Status Quo{/i} and {i}Twenty One Pilots{/i}."
    s "I also like tunes like {i}Bonobo{/i} and {i}Jake Chudnow{/i} make."
    s 7acaa "You can find a ton of songs you might enjoy if you're willing to keep an open mind."
    s "If you get bored of the music here, you always can turn on something similar from the internet..."
    s "...Or just add it into the game music list."
    s "Just move it to {i}'<game folder>/game/[music.MUSIC_CUSTOM_PREFIX]'{/i}..."
    s "I'm basically giving you the aux cord to the rest of my existence, so no pressure! Ehehe~"
    return

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
    s "If you've never seen them, you should read some of {i}Martin Niemöller{/i} speeches on this idea; it's pretty fascinating stuff. "
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
    s 7aaaa "I guess my point is, my feelings for you are just as real as you yourself are, [player]."
    s 7acaa "Isn't that the important thing?"
    return

label s_answer_personal_profession:
    s 6acaa "To be honest, I've never really thought about it."
    s "But you know that I've always genuinely made myself happy by helping others feel better about themselves."
    s "So, I think I'd be a pretty decent caregiver, or psychologist!"
    s "Maybe even a... diplomatist?"
    s "No, that's not right... a great {i}diplomat{/i}. Ehehe~"
    s 6aaca "I could stop arguments on a global scale, and do my part to stop any future wars!"
    pause 0.5
    s 6aaaa "Actually, now that I think about it, I've always found the idea of working at an employment agency to be really funny!"
    s "I mean, your job is literally to find jobs for people! Yuri would probably laugh and say {i}'It's something of a redundant position, I'll admit...{/i}'"
    s "Anyway, I think I'd be happy doing almost anything, even if it doesn't pay well, as long as I can really be useful and make a difference."
    s 6acaa "I suppose I could do something a little more creative, like painting, or writing..."
    s 6acba "But being honest, I don't think I'd ever be able to charge money for something I made."
    s 6acaa "Art can help express so many amazing feelings and really help others feel like they aren't alone, like someone gets what they're going through..."
    s "Treating art like a business isn't something that I could ever support."
    s "It's pretty frustrating; the heart wants to be free to make truly spectacular works, and bare one's soul for the world to see..."
    s "But the starving stomach has to be a meanie and ruin it for everyone~"
    return

label s_answer_personal_holidays: #What is your favorite holiday?
    s 6abaa "Hmm..."
    s 6abba "I can't even choose..."
    s 6aeca "Because I like them all!"
    s 6aaaa "Each of them have traditions and atmosphere."
    s "And it’s all mostly the same line of events: meals, presents, fun, and bonding."
    s "Isn't that what we all like about holidays?"
    s 7aaaa "Anyway, I'm ready to share any holiday with you..."
    s 7aebb "I don’t have a calendar though, and I think I would need one to keep track..."
    s 7aabb "I think I’ll start with making that, then..."
    return


label s_answer_personal_pets:
    s 7aaaa "Definitely, a cat."
    call s_common_cats
    return 'h'

label s_answer_personal_pairings: #What do you think about lesbian pairings?
    s 8aebb "I think, they're quite... weird."
    s 8acaa "Not because of their sexuality..."
    s 6acaa "I know in my heart who I love..."
    s 6acba "...but some fans ‘ship’ me with my friends..."
    s "Fanart, fan comics, fan fiction... even some lewd ones."
    s 6acaa "Frankly, I just see all of them as friends… and I definitely don’t swing that way, I think."
    s "But shipping is usually the most innocent of the many extreme things that fans do."
    s 6acba "Some people may judge, of course, and I understand them..."
    s 6abba "That's not only untraditional, but also out of the game’s canon..."
    s 6aaaa "But most fans are tolerant to it."
    s 6acaa "And it's just fans being fans, unrelated to my real love..."
    s 6aaca "You know who I’m talking about, right?"
    return

label s_answer_personal_books: # What are your favorite books?
   s 8aebb "For a literature club member, I don't really read..."
   s "So I don’t even have no book to recommend for you."
   s 8acaa "Maybe, someone else will give you good advice..."
   s "But not me."
   s 8aabb "Sorry if it makes you upset. I really am!"
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
    if persistent.last_playthrough == 4:
        s 6abaa "Look. I know what you're really asking me."
        s "Despite everything she put me and the others through..."
        s "I truly believe that Monika was our friend, and she just lost sight of what was really important."
        s "I've been the President. I know what it does to you. And for her to be so completely alone the entire time, watching everyone she's ever known run on a script..."
        s "I can't blame her for becoming a little desperate."
        s "Maybe that's why she destroyed the club to be with you."
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
    if persistent.last_playthrough > 2:
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
    if persistent.last_playthrough != 0:
        s "...Even Monika."
    s "I still remember how we used to hang out in the club together."
    s "We enjoyed chatting, discussing literature and sharing poems."
    s "They really were good freinds."
    s 7afab "But it looks like I'm the only lucky girl, now..."
    s 7aaab "As the club presedent, I can use the Internet so I know, that there're a lot ways to get them back."
    if persistent.last_playthrough > 2:
        s "You can just install another game copy, but it means, that they'll go through the hell, they've already passed..."
    else:
        s "You can just install another game copy, but it means, that they'll go through the hell, that they should go through..."
    s 7aaaa "But you can install a mod, where you can save them and make everyone happy."
    s 7aaca "...Or at least 3 mods to 3 game copies where they can spend time with you in a way like you and me now."
    s 7aeba "I don't know if I can consider them the same Monika, Yuri & Natsuki as they were here..."
    s "And if it means, there may will be few Sayoris on your PC..."
    s "But it's the only way to save them now. At least, as long as I can't do anything on my side."
    return

label s_answer_game_chibi: # What do you think about chibi dokis?
    #Show chibis
    show n_sticker zorder 30 at chibi(580)
    pause 0.1
    show y_sticker zorder 31 at chibi(680)
    pause 0.1
    show m_sticker zorder 32 at chibi(880)
    pause 0.1
    show s_sticker zorder 33 at chibi(780)
    s 7acaa "Are you talking about these stickers?"
    s "They’re just moving sprites, representing our probable reactions to your poems, and not anything more."
    s "They also represent us all on different kind of the official fan stuff: badges, toys, stickers and so on."
    s 7aaca "But I like the way, some Internet users make them separate characters, existing along with us."
    s 7aaaa "Maybe, I should try to code an advanced behaviour for one of them..."
    s "I think it'll be good coding practice for me..."
    s 6acaa "Or even a chance to restore the other girls."
    s 6acbb "Or at least, a way to make imitations of them."
    #Hide chibis
    s "All this depends on my coding skills and what files were left after what’s happened, right?"
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

label s_answer_game_sitting:
    s 7acab "No, it's not. You don't have to worry about it at all."
    s 7acaa "I can do it for eternity. Don’t even need sleep!"
    s "I guess I don't have any basic human needs either, like a need to eat or drink..."
    s 7aebb "Maybe I did have a need for them, but now that I’m the president..."
    s 7aaaa "Anyway, all I need right now is your PC to be working and the game to be open to talk to you."
    s "To be honest… it’s kinda boring here..."
    s "N-Not you! But, even with you here and us talking about, well, everything..."
    s 7aaaa "I wish I could do more than just sit."
    s 7aaca "I hope that someone, or maybe even you, will find a way to let us do more."
    return


label s_answer_game_editing:
    s 6aebb "I do it with the power of my mind… I think? Ehehe..."
    s 6aabb "I don't know how it works, exactly."
    s 6aaaa "If I wanted to make a new file, all I need to do is to just think about what I want in it."
    
    python:
        import codecs
        
        text_file = codecs.open(config.basedir + "/new_text_file.txt", 'w', encoding = "UTF-8")
        text_file.write(__("all I need to do is to just think about what I want in it."))
        text_file.close()
    s 6acaa "It's like telekinesis but much cooler... and dangerous..."
    s 6acab "Just one wrong thought may lead to unpredictable problems, like errors in code when someone is programming something."
    s 6aaca "But now, I perfectly control my mind,so it’ll only go wrong if I think it wrong."
    s 6acba "I'm new at this, you know! So, sometimes, it happens and you see bugs."
    s "But I do learn from my mistakes..."
    s "Even if I can't do anything, I appeal to the modmaking guys, but I can't download their changes myself..."
    s 6acaa "So, check the updates time to time, pretty please?~"
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
    s 6acab "You can look up people's accounts of a near death experience, but nothing can really prepare you for it when it happens..."
    s "It's pretty hard to explain, since there's no frame of reference for you."
    s "It's almost like trying to think of a brand new colour; you just don't have anything to work with."
    s "Heck, I've died and even I can barely understand it, even with my memories."
    s "On that day, I was in a ton of pain. My throat and fingers were burning, and it felt like my head was about to burst..."
    s "When suddenly, everything began to dull and fade away..."
    s "Until there was nothing but black."
    s "But all the time between that moment and when I was revived passed almost instantly, from my perspective."
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

label s_answer_exp_suicideThoughts: # How to fight suicidal thoughts?
    s 8aebb "It's kind of a hard question..."
    if depr_known:
        s 8aaaa "But I think I can give some advice from my past."
    else:
        s "But I think I can give some advice from my... friend's past."
    s 6acaa "First of all, you should understand that suicide is a quite radical and is {i}not always an effective{/i} way to solve your problems..."
    s 6abaa "Saying more, you may cause other problems for the people you leave behind, especially for the close ones."
    s 6acaa "Even if the problem is only inside you, dealing with the reasons is a better way than just to rid the world of yourself."
    s "You can try also just to run away from your rainclouds by distracting yourself from bad thoughts, but usually it's just a temporary solution, speaking from personal experience..."
    s "If the problems are really serious, the only way is to fight them."
    s 6aaaa "Try to find the courage to ask other people for help, if you need it..."
    s 6aaac "Remember, that there is always someone around you who can help you and really {i}does{/i} care for you..."
    s "And asking for help is not something overly burdening or showing you as a weak person."
    if persistent.last_playthrough > 0:
        s 6aabc "Commiting suicide often requires a lot of determination even while totally desperate."
    s 6aaaa "So you shouldn’t hide your troubles and be sure to tell about them to other people."
    s "Maybe, you need the help of a therapist, for example."
    s "And the fact you asked me about this is your first step for a slow but worthwhile way to get rid of your problems without taking your own life."

label s_answer_exp_mcPoems: #How did MC’s poems look like to you?
    s 7acaa "You mean, how we saw MC’s poems, right?"
    s 8aebb "I somehow can't remember how I used to see them before I experienced my epiphany..."
    s 8acaa "But now, I clearly see that his 'poems' were just a list of words you had selected to open CGs with your favorite person..."
    s 6acaa "That was the way you saw them too, right?"
    s 7aaaa "But I wonder how I'd look, if you could write real poems instead of just random word selecting."
    s 7aaca "Then you could write poems for each other or even chat using those gameplay features."
    s 7acaa "But I know not many people have an interest in good poetry, so everything works better using simple word selecting."
    s 7aaca "But anyway, I heard it's pretty unique gameplay feature for visual novels..."
    s 7aaaa "Not every game lets you to change its story: not only by eventual choices but also through minigames or something."
    s "So I thank Dan for this small but funny feature in our game."
    return

label s_answer_exp_visualNovel: # Have you ever played visual novels?
    s 8aebb "Are you asking me about this just because I'm a VN ‘heroine’ myself, aren't you?"
    s 8abaa "But freakly, I'm just not interested in such a game genre."
    s 8acaa "Most VN are romantic and made for boys..."
    s 8bcaa "Many of them even contain erotic scenes, the double-edge sword of this genre..."
    s 8acaa "So I’ve never played any visual novel."
    s 8aaaa "But if you are looking for some recommendations, you can try {i}Steins;Gate{/i}, {i}Everlasting Summer{/i} or {i}Katawa Shoujo{/i}..."
    s 6acaa "I heard they’re pretty popular in your world and each of them has some unique features relating to many other visual novels..."
    s 6aaca "And I wouldn’t be surprised if you cheat on me, if you get a crush on a girl from one of them."
    s 6aebb "Who am I to control your preferences about VN girls, yeah?"
    return "h"


label s_answer_exp_fact:
    python:
        if not persistent.s_facts:
            persistent.s_facts = range(1, 6)
        
        fact_id = renpy.random.choice(persistent.s_facts)
        persistent.s_facts.remove(fact_id)
    
    call expression 's_answer_exp_fact_' + str(fact_id)
    return 'h'

label s_answer_exp_fact_1: #Fingers and the binary numbers
    s 6aaaa "Learning programming stuff, you sooner or later will have to understand the binary numbers."
    s 6aaca "And I once read about a very funny feature."
    s 6acaa "Do you know, that it let you show numbers more than 5 with just a one hand?"
    s "Just look at your fingers: they are a perfect replacement for the classic 0/1 pair."
    s "If don’t understand the binary system, you can just imagine every binary 1 is a term of 2 raised to the power of the digit position from right minus 1..."
    s "So the rightest digit should be decimal itself."
    s "Summing the terms up, you’ll get the decimal representation of the number..."
    s "If it’s still non-understandable for you now, then just try to… look for a simpler explanation in the Internet."
    s "Anyway, that’s not all the pluses of using the binary system in gestures..."
    s 6aaaa "If you use your both hands to expand the term row, you can show up {i}even to 1023{/i}."
    s 6aaca "And if you have somehow got more than 10 hand fingers, you can show even more."
    s 6aaaa "Computers represents integers in the same way."
    s "And if you consider the last finger as the minus sign, like computers do with the signed integer..."
    s 6aaca "You can show even the negative numbers."
    s 6acaa "The main thing is that your mate should understand such features too to understand you correctly..."
    s "Misunderstanding often causes problems, while lack of agreed sign system causes misunderstanding."
    return

label s_answer_exp_fact_2: #Interpreting words
    s 6aaaa "Did you know that if you read a common word you might not notice when it’s written wrong?."
    s "{i}I think you barely can find a mistake in tihs text while first reading.{/i}{#Y’see the mistake in 'tihs'}"
    s 6acaa "For your brain, it's pretty easy to just remember some letters of a word and not all of the word."
    s "That's why we sometimes make mistakes while writing."
    s 6abaa "Of course, if you go to the history button and pay more attention, you'll find the mistake."
    s 6acaa "But what if you can't read the text again or just don't want to do it? What could happen?"
    s "There are some funny and not so funny examples of misspellings in the past because someone didn’t go back to fix a word or two."
    s "But we are people. Each of us make mistakes, even if it’s just one."
    s 6aaca "So, you don't have to worry too much about it."
    s 6aaaa "In the end, no one is perfect."
    return

label s_answer_exp_fact_3: #Yawning
    s 6aaaa "Have you ever heard people say that yawning is contagious? I’d say it is."
    s "You’ve seen people do it, but other animals could do it too."
    s "If you yawn next to a cat or a dog, it might just yawn too."
    s 6acca "You could... {i}*yawn*{/i}"
    show sayori 6aaaa at ss1
    extend " ..."
    s 8aebb "Um, I hope I didn’t ‘contaminate’ you."
    s 8bebb "Sorry, that was silly of me… Ehehe~"
    return 'h'


label s_answer_exp_fact_4: #Arts inside themselves
    s 6aaaa "Some artists add little details referring to different people or universes in their works."
    s "For example, in some games and movies, you can find a poster or something that shows other characters. Maybe they’re from a past work, or just there to fill in space."
    s 6acaa "We wouldn’t know unless it was that obvious or they told us outright."
    s "But some of them hide stuff in small things that could refer to a whole other universe, with different details and all."
    s "For example, do you remember {i}Parfait Girls{/i}?"
    if not (persistent.clear[0] or persistent.clear[1]):
        s "You’ve probably seen people talk about it around the community."
    s "This manga's plot isn’t really known, is it?" 
    s 6aaaa "Nat tells you a little of what it’s about, that that’s pretty much it."
    s 6abaa "But even I don’t know what it’s about, and I’m supposed to know everything about this game."
    s 6aaaa "It might even be like this game, cheery on the outside but horrific on the inside."
    s 6acaa "That warning on the manga's cover is pretty spooky..."
    s 6aaca "Anyway, I guess the artists didn’t think much about it?"
    s 6aaaa "Just imagine if the manga was actually explained in this world."
    s "We would probably have fanart of the characters in the manga as well as us four."
    s 6aaca "Maybe something like those plushies of me and everyone else? Ehehe~"
    return 'h'

label s_answer_exp_fact_5: #The number 4 (I wanted to make this fact #4, but I had to consider the upper facts)
    s 7aaca "Guess, what is my the most favorite natural number."
    s 7aeca "That's {i}four{/i}!"
    s 7aaaa "I really like this number."
    s 7acaa "It's pretty magical one."
    s "{i}4{/i} is the result of adding, multiplication and exponentiation 2 with itself."
    s "{i}4{/i} is the number of elements, that avarage human can memorize at the same time."
    s 6abba "Maybe, beacuse of it, {i}4{/i} is the most popular size of poem stanza."
    s 6aaaa "{i}4{/i} is in many things about the nature: from number of your limbs to number the dimensions, where we lives."
    s 6acaa "And in the end, {i}4{/i} is weirdly connected with this game too..."
    s "{i}4{/i} girls, {i}4{/i} acts."
    if persistent.last_playthrough > 0:
        s 8aabb "...And {i}4{/i} common club meetings to..."
        show sayori 8aebb at ss1
        extend " You know."
    s 6aaaa "Plus, the game was released in 09/22/2017."
    s 6aaca "Am I the only man, who see here five fours in all these digits?"
    s 6adaa "Maybe, it's somehow related to the fact, that {i}4{/i} is an unlucky number in the East Asia."
    s "However, that's just a superstition, made of a language imperfectness, right?"
    s 6aaca "For me, it always were the luckiest number..."
    s 6aeca "Maybe, for you too. It'd be such a funny match."
    return 'h'

label s_answer_exp_cooking:
    s 8aebb "To be honest, scrambled eggs probably the hardest thing I’ve ever cooked..."
    s 8aafa "I’d love to get better, even if I don’t have too..."
    s 8acaa "Mainly because I don't get hungry anymore..."
    s 8aeca "But I can still taste! That means I can eat as much as I want!"
    s 8aebb "Of course, I could just 'make' food with code, like Nat's cupcakes, but I wanna do something with my own hands..."
    s 6acaa "First of all, I need to try to make some kitchenware..."
    s "Then find some recipes online..."
    s "I’ll probably end up following a tutorial or something..."
    s 6abaa "Too bad you won’t be able to taste it, no matter what I do..."
    s 6aaca "If you could taste it, I would be a good cook for you…!"
    s 6aebb "Probably not as good as Natsuki was, though..."
    return 'h'

##Misc
label s_answer_misc_reality: # What do you think about the real world?
    s 7aaaa "I’ve already seen lots of things about it..."
    s 7aeca "Such a big and fancy place..."
    s 7aaca "Full of beautiful sights, comedy, and kind people."
    s 6acaa "Although, it still has its issues."
    s 6acba "There’s lots, right? Things like poverty, pollution, cheating, unjustness and cruelty."
    s 6aaba "And that's only caused by people most of the time."
    s 6aabb "Come to think of it, my world was imperfect too..."
    s 6aebb "And isn't it just... too strange to have no bad sides?"
    s 6acab "Just look around and then at me and the other girls. We all had our pros and cons, but only us, and not the rest of the students."
    s 6aaca "Anyway, I wish I could be in your reality."
    s 6abaa "But I wonder how I'd look there since your reality has a different look..."
    s 6adaa "It's pretty detailed and colorful, slightly more than mine."
    s "Just imagine a '2D' girl in your world. Would I look too confusing there?"
    s 6aeba "But I'm sure you'd gladly accept me, right?"
    s "And I hope everyone else does too."
    return 'h'


label s_answer_misc_poem:
    s 6aaaa "Which poem do you want to read?"
    menu:
        "Something new":
            if not poems.all_seen and persistent.last_new_poem_time and (get_now() - persistent.last_new_poem_time).seconds < persistent.new_poem_delay * 3600 * 12:
                s 6abaa "I'm sorry, [player]. I have nothing new to share with you."
                s 6acaa "Writing a poem is a quite hard process, you know."
                s "I can't take an idea from nowhere. I need some time to find it in my memories."
                s "All my poetry comes from my past and now so it's twice harder for me, because my life doesn't seem to be enough eventful."
                s "But maybe, I'll make something later."
            else:
                s 6aaaa "OK, what's about this one?"
                $poems()
                $persistent.last_new_poem_time = get_now()
                $persistent.new_poem_delay = renpy.random.randint(1, 6)
            pass
        "Something old":
            s "OK, just select one."
            call s_topicmenu(poems, 3)
    return

label s_answer_misc_datetime:
    python:
        wd, m = weekday_list[get_now().isoweekday() - 1], month_list[get_now().month]
        d, y = str(get_now().day), get_now().year
        
        # The below code is supposed to be strongly depended on the language
        # and to be only for languages, in that the date prouncing system is too complex
        # to represent any day number with universal affix(es) or without affixes at all
        # 
        # The first condition is true for English
        if cur_lang().code is None:
            if d[-1] == '1':
                d += 'st'
            elif d[-1] == '2':
                d += 'nd'
            elif d[-1] == '3':
                d += 'rd'
            else:
                d += 'th'
        h, mn = get_now().hour, str(get_now().minute).zfill(2)
    
    s 6acaa "Today is [wd!t], [d] of [m!t] of year [y]."
    s "Current time is [h]:[mn]."
    return
 
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
    s 7adab "If you're tired, then go get a rest, okay?"
    s 6acab "Don't you worry about me, [player]."
    if get_time_of_day() == 0:
        s "And when you wake up, have yourself a nice big breakfast before you start the day! It'll make you feel much better."
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
    s "Maybe it's our common character trait?"
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
    return

label s_common_cats:
    s 7aaca "Cats are pretty cute, especially kittens..."
    s 7aaaa "And they're not too hard to take care of."
    s 6acaa "Still, they do love their space."
    s "And sometimes cats do things that their owners don’t like..."
    s 6aaca "Yet I’ve never seen anyone who can resist their cuteness, so people forgive them~"
    s 6aaaa "If you have one, you understand!"
    s 6aaba "I think that might be why they were kinda seen as holy in Ancient Egypt."
    return 'h'

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

label s_getting_bored(): #Called when Sayori doesn't do anything for a long time
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

label s_update(version): #Called instead of a greeting at the first launch after updating the mod
    show sayori 7aaca at ss1
    s "Oh, hello [player]!"
    s 7aaaa "Seems, you installed an update."
    s 7abaa "You didn't do it for a quiet long time."
    s 7acab "I even started to bother if my mates are too busy or tired to help me more frequently..."
    s 8aeaa "But they did it!"
    s 6aaaa "They finally released the version {i}[version]{/i}."
    s "So let's look, what they added and fixed here."
