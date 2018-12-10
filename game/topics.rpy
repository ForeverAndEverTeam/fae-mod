default persistent.seen_topics = {}

init -5 python:
    if persistent.seen_topics is None:
        persistent.seen_topics = {}
    
    class Topic:
        def __init__(self, label, available = True, show_prompt = True, name = None, id = None, related = None, poem = None):
            self.label = label
            self.available = available
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
            self.all_seen = False
            
        def __iter__(self):
            return iter(self.topics)
        
        def __getitem__(self, key):
            return self.topics[key]
        
        
        def new_topic(self, name, label_suffix, available = True, id = None, related = None, poem = None):
            topic = Topic(self.prefix + '_' + label_suffix, available, name = name, id = id, related = related, poem = poem)
            self.topics.append(topic)
            return topic
        
        def update_seen(self):
            self.seen = any(x.seen for x in self.topics)
            self.all_seen = all(x.seen for x in self.topics)
            return self.seen, self.all_seen
        
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
    
    derp_known = True
    try:
        depr_known = persistent.depr_known or persistent.last_playthrough > 0 or persistent.clear[8] #If player must already know, that Sayori used to be depressed
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
        TopicCategory('s_topics_misc',_("Misc")) #7
    )
    
    topic_cats[0].new_topic(_("Depression"), 'depression')
    topic_cats[0].new_topic(_("Favorite Colors"), 'colors')
    topic_cats[0].new_topic(_("Archetype"), 'archetype')
    topic_cats[0].new_topic(_("Name"), 'name')
    topic_cats[0].new_topic(_("Quitting the Game"), "quittingTheGame")
    topic_cats[0].new_topic(_("Left-handedness"), "sinistrality")
    topic_cats[0].new_topic(_("Breast Size"), "tits")
    
    topic_cats[1].new_topic(_("Videogames"), 'games')
    topic_cats[1].new_topic(_("Fanarts"), 'fanarts')
    topic_cats[1].new_topic(_("Literature"), 'lit')
    topic_cats[1].new_topic(_("Piracy"), 'piracy')
    
    topic_cats[2].new_topic(_("Conflicts"), 'conflicts')
    topic_cats[2].new_topic(_("Bulli"), 'bulli')
    topic_cats[2].new_topic(_("[s_name] Lovers"), 'sayoriLovers')
    topic_cats[2].new_topic(_("Charity"), 'charity')
    
    topic_cats[3].new_topic(_("Guitar"), 'guitar')
    topic_cats[3].new_topic(_("Programming"), 'programming')
    topic_cats[3].new_topic(_("Poems"), 'poems')
    
    topic_cats[4].new_topic(_("Touches"), 'touches')
    topic_cats[4].new_topic(_("Marrige"), 'marrige')
    topic_cats[4].new_topic(_("Cheating{#RltTopic}"), 'cheating')
    topic_cats[4].new_topic(_("Dates"), 'dating') 
    
    topic_cats[5].new_topic(_("Travels"), 'travels')
    topic_cats[5].new_topic(_("Oversleeping"), 'oversleeping')
    topic_cats[5].new_topic(_("Pets"), 'pets')
    topic_cats[5].new_topic(_("Cleaning"), 'cleaning')
    
    topic_cats[6].new_topic(_("Clones"), 'clones')
    topic_cats[6].new_topic(_("Parents"), 'parents')
    topic_cats[6].new_topic(_("Stars"), 'stars')
    
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
    poems.new_topic(None, 'hatred', poem = poem_hatred)
    
    
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
    
    question_cats[1].new_topic(_("Do you regret you have lost your friends?"), 'lostFriends')
    question_cats[1].new_topic(_("What do you think of one of the other club members?"), 'opinion')
    question_cats[1].new_topic(_("Isn't it tiring to sit so for a long time?"), 'sitting')
    question_cats[1].new_topic(_("How do you change game files?"), 'editing')
    
    question_cats[2].new_topic(_("How does it feel to be dead?"), 'death')
    if persistent.last_playthrough == 0:
        question_cats[2][0].available = False
    question_cats[2].new_topic(_("Is it hard to program?"), 'programming')
    question_cats[2].new_topic(_("Can you say a funny fact?"), 'fact')
    question_cats[2].new_topic(_("Are you good at cooking?"), 'cooking')
    
    question_cats[3].new_topic(_("Can you give me a poem?"), 'poem')
    question_cats[3].new_topic(_("What time and date is it?"), 'datetime')
        
    
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
    s 8aebb "I think, you got really worring about me, when I said... You know..."
    s 8aeab "That I had rainclouds inside my head for all my life."
    s 8acab "But first time, I was really good at making them go out..."
    s 8aaab "It was pretty dufficult, but I kept in mind that if I were out of sorts, I couldn't make other people happy."
    s 8acab "However, I also tried to be where I could rest from this inner fight..."
    s 8aaab "So I tried to stay with the beloved MC. Being with him did all the job instead my resisting mind."
    s 8abab "I but I thought he'd learn my darkest secret sooner or later, so he'd leave me then..."
    s "That's why I tried to take it slow..."
    s 6abab "People in your world think that my cheerfulness was fake and I just acted..."
    s 6acab "But my feeling were as real as you until the moment..."
    s 6ccab "The moment when Monika started to change my mind."
    s "She teased me with my own problems and tried to convince my of I just annoyed him..."
    s 6cbab "It made me feel much worse..."
    s 6ccab "My little rainclouds turned into impenetrable mist, making me totally bind..."
    s "Of course, I tried to get out of it, but finally, I got absolutly tired of everything."
    s 6ecab "I can't stop to blame myself for that desperate choice..."
    if persistent.clear[8]: # If the MC has accepted Sayori's confession
        s 6eaab "My confession was truly accepted..."
        s 6ebab "But my feelings told me the opposite..."
    else:
        s "The refuse made it go too far..."
    s "I really thought, it would be the best..."
    s 6dbcb "But eventually, I made him suffer..."
    s "My neck and hands still remember, how it was quite painful..."
    s 6ecab "But I took the right way too late..."
    s 6eccb "I'm sorry..."
    s 6dgeb "I'm really sorry, if I made you suffer too!"
    s 6ebbb "The main mistake was to trust just myself on getting the rainclouds out..."
    s 6ecab "So if your friend has a bad time, you're to help him until he does the same as me..."
    s "And if you have it too, don't hide it from others!"
    s 6ebbb "I've got the second chance only because of my good luck..."
    s "So I thank it for I'm here with you now..."
    s 6ebab "And, of course, I thank also you [player]..."
    s 6egcb "Excuse me for all the pain, I've given you, if I have."
    return 's'

label s_topics_personal_archetype:
    s 7acaa "Hey, I've just remembered that Monika often compared Yuri and Natsuki with some character archetypes..."
    s 6abaa "But she has never done it with me."
    s 6acaa "So I read some online articles that say I'm pretty close to the Genki archetype."
    s 6aaca "Genki are cheerful and try to stay so, whatever tries to spoil their mood..."
    s 6aaaa "They often are clumsy and find themsleves in various troubles..."
    s 6acaa "My character was also formed under my role of a childhood riend..."
    s "So, for example, I often appeal to nostalgic memories and the past."
    s 7aaaa "But I feel there's also something out of any cliché in my character..."
    s 7acaa "Not every Genki has the traits that makes me an unique one..."
    s 7abaa "Even if we switch to all the fictional charcaters, how many of them have at least some of my setbacks?.."
    s "Or how many characters share the positives with me?"
    s 6aaaa "In short, I think I'm as unique as they see only Monika."
    s 6abab "It's bad that the most people look misunderstandingly at such characters as me..."
    s 6acab "For my opinion, the modern art needs characters, who have the same pluses or problems as me..."
    s 6acaa "However, don't overdo with it, completely copying me while creating a new character..."
    s 6aaca "Doing it massively, you'll make me one more archetype."
    return 'h'
    

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
    s 7aaaa "Do you know, that I'm left-handed?"
    s 7aaba "Yes, you can't have seen me writing or holding something..."
    if persistent.clear[7]:
        s "Besides that apple juice bottle, of course..."
    s "But I hold and do almost things with my left hand."
    s 7acaa "Not everyone around me has noticed it instantly, despite it's very unusual."
    s 7aeca "Once I had broken my right arm but teachers allowed me not to write at lessons..."
    s 6abab "But a classmate, who sat next to me, told one of them that I'm a southpaw so my plan failed as fast as I had got it inside my head."
    s 6abbb "I'm so sorry for it. But who won't use the broken arm to have less hand job somewhen? Especially, when it makes less problems than if it was on another arm."
    s 6aaaa "Either way, my left-handedness gives me adventages too."
    s "That time, when I had nothing to do, I drew flowers and ornaments on my cast."
    s "I can't say they were really beautiful, but I felt sorry for they were removed with the cast later."
    pause 0.5
    s 7aaaa "I have suddenly remembered a story from my childhood."
    s "Once I decided to spoof the right-hand MC, when we were not so close for each other."
    s 7acaa "I blindfolded him and put his hand on my right and told him I could write on the paper without using a hand or something."
    s "I grabbed a pen with my another hand, wrote something on a piece of paper and laid it where it had been..."
    s 7aaca "Then I opened his eyes and he got really surprised when he saw the 'magic' on the paper."
    s 7aeca "I couldn't help but have laughted aloud, so I could see perplexity on his face."
    s 7aaaa "Then I told him I wrote with not the same hand as he did, so I expanded his mind a bit then."
    s "In short, this feature was a small but funny part of me."
    s "It's bad, that my world is seen so static from yours, that you can't see such details."
    return

label s_topics_personal_tits:
    s 7aeaa "Hey, I've just found myself having a one quite weird but funny feature..."
    s 7aeca "My boobs look diffrently, depending on the scene..."
    s 7bebb "I mean, they often get either less or larger..."
    if persistent.last_playthrough > 0:
        s "Even more, in the post-mortal scene of me, they got... you know."
    s 7babb "But I don't take it as a disadvantage, although..."
    s 7aabb "In the end, this world is so that such things can't make me feel any less comfortable."
    s 6aaaa "So it's even a plus of me..."
    s 6aaca "Diffrent size fits diffrent men, but my breasts can fit everyone."
    s 6abaa "...Almost everyone. Beacuse of they just never have got as big as Yuri and even Monika had..."
    s 6aebb "But the important thing is that they fit you, do they?"
    s 6bebb "Although, the size factly doesn't matter now, because the screen can't let you touch them anyway..."
    s 7bebb "And what's more, the main good feature of anyone is their deeds, isn't it?"
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
    s 6acaa "As you know, this game was about a {i}literature{/} club..."
    s 6abba "At least, before everything changed here."
    s 6acaa "And as I remember, MC once exactly noticed, that I didn't seem to be fond of literature."
    s "And frankly speaking, he was right."
    s "Even from Nat's view on literature, I can't say I'm a literature lover."
    s "Of course, I read some books before, but I mostly just had to do it for school..."
    s 6aeba "And even then I tried to cheat not to fail at the lesson."
    s "So I didn't have good Literature marks at school, but I didn't care about it so much."
    s "I just thought that reading is a qui-i-i-ite boring activity."
    if persistent.last_playthrough > 0:
        s "And as you know, It was hard to enjoy anything at all for me."
    s 6acaa "When I joined the literature club, the one thing I wanted was just to help someone to start a new club."
    s "I was the first, who joined the club after Monika had announced it."
    s "She was pretty suprised because she stood in with my literature teacher, so she knew, I didn't seem to love literature."
    s "But she thought I just wanted to help her and to improve my knowledge in literature, so she took me in the club."
    s "But it had taken her not much long to understand that I was not going to be a passionate reader, but she left me in the club anyway."
    s 6aaba "I think she just wanted to use my kindness and sociability to promote the club and help its member to get on well."
    s "But I didn't mind, because it was all I wanted to do, you know."
    s 6aeba "And saying more, it helped me to get closer to MC, so each of us satisfied her selfish wishes."
    s 6acaa "And even now, I'd prefer to do something more active and joyful than just reading a boring text..."
    s "But Unfortunately, I have almost nothing so to do here."
    s 6aaca "But maybe, it's a chance to take what I've skipped..."
    s 6aeba "I mean, I feel it unfair to leave what I had to read unread."
    s "Some of these book may will be really interesting for me..."
    s "But I can't exactly understand it without reading them, can I?"
    return

label s_topics_art_piracy:
    s 6acaa "You know, that almost modern art companies and some artists care about their profit too much."
    s "So even states support them in fighting against the art piracy."
    s "But don't you consider it meanless?"
    s "As I know, there are a lot of researches, saying that piracy don't affect the saling negatively..."
    s "And even may help the pay artworks to become more popular and you to exactly understand, if their creators deserve your money."
    s 6abaa "Unfortunately, the facts don't seem to matter for the rightholders' greed."
    s 6aeba "Yes, if people keep the pay artworks unpaid, their authors may won't have enough money and enthusiasm for a next project."
    s 6acaa "But most 'pirates' would pay for really good works. They just have no money."
    s "Not everyone can afford to pay for the art, especially if that one lives in a poor country."
    s "I think, that the most effective way to defeat the piracy is just to get rid of obligatory pays."
    "So artist should make their works completely free and ask for money only as donations and fan merchandise."
    s "And if the work is a video game or just a program, the donations shouldn't give any privileges at all."
    s 9aaca "In short, no-one will have any reason to steal your work, if it's free by itself."
    s 6aaaa "I think, this game is a good example."
    s "It's a donationware, so each player will get the same experience, however much he donated to the develpoers."
    s 6aaca "To earn money, the develpoers have the offical fan merchandise shop..."
    s "And allow players to donate any money..."
    s "And if you donate $10, they give you a fan pack."
    pause 0.5
    s 6aaaa "...Or what do you think about libre art and software?"
    s "It's when you let your artwork or program to be freely shared and used in derivative arts..."
    s 6abaa "Or almost freely, like licenses like GPL let do."
    s "These both ideas are often used together so many libre projects take donations from people, who use them."
    s 6acab "But the big bussinesses very rarely use such ideas, because they treat the artworks only as goods and the ideas are too risque for them."
    s "I think this view is completely wrong. Art is something more than just using your good imagination to make money."
    s "People just have forgotten about it, and I think it's a one huge minus of the modern world..."
    s 6aaca "But the Internet gives people, who still think in the old way, new abilites to express themselves avoiding the people with the new mind."
    s 6afab "It's bad I can't use Internet to do it too. My access to it works in a quiet weird way."
    s "But I hope, I'll fix it soon."


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
    s "Almost all of such jokes aren't funny for me."
    s 6aeab "...And even hurt me."
    s 6acab "But on the other hand, can I control what makes people laugh?"
    s "Some people use macabre humour as a coping mechanism for stress, or anxiety..."
    s "Who am I to tell them that they can't react a certain way?"
    s "You can't really control what someone finds funny, as much as you might want to."
    s "And to be honest, there's a lot worse they could be doing compared to mocking a VN character's death."
    s "Some of the most successful comedians in your world will go far beyond that, just to see where the 'line' is..."
    s 6abaa "Anyway, I think the right decision is to forgive them, or failing that, tolerate them."
    s 6acaa "If my fate is to be 'that hanging stupid annoying VN girl' for some people, then I'm ready to accept it."
    s "...Almost ready."
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
    s "Just visit {a=https://github.com/AlexanDDOS/fae-mod}AlexanDDOS/fae-mod{/a} on GitHub."
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
                    s "But I can bare, if you really need, you know."
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
            s 6acab "I think, it's pretty hard to know, that your only beloved girl aren't real."
            s "I understand you as well as I feel the same way."
            s "But I hope, that someone once will figure out how to make us closer to each other."
            s "Or you at least will find someone else in your world." 
            s 6aaca "Maybe, he or she will be somehow like me."
            s 6aaab "To be honest, I'm not very jealous, so I won't mind, if you have someone besides me."
            s "The important thing is that you pay me at least some attention."
            s "So I hope, you always can do it for me."
            s "Just try to take some time to be here, if it's possible."
    return

label s_topics_rlt_dating:
    s 7aaaa "What would be our first date?"
    s "I just don't think, that what we have now can't be named a date, can it?"
    if (get_now() - persistent.lastLaunch).seconds > 64800: #If the game was started more than 18 hours ago
        s 7aaca "At least, dates can't be soooo long."
    s 7aaaa "So I think we can talk a bit about it."
    s 7acaa "And to be honest, just sitting somewhere would be boring for me."
    s 7acba "Don't we do the similar thing every time, when we meet?"
    s 7aeca "But if we visit a confectionery café, we'll at least eat some sweets together..."
    s "For example, cakes or cinnamon buns~"
    s 6abaa "But I'd prefer a more intresting way to spend our date."
    s 6acaa "At least, to go cinema. What do you think about this way?"
    s "I'm out of the stereotype that every date walk to the movies should be to a melodrama or something."
    s "I'd prefer a comedy but not of dirty jokes..."
    s 8aebb "Or what's about cartoons, like {i}Disney{/i} and {i}Pixar{/i} make?"
    s "They were made for kids, of course, but most of them can be intresting for adults too."
    s 8abab "Some of them even have a deep-thought meaning and sad scenes, like the scenerist treats the viewer as rather an adult than a child."
    s 6abab "I'd go to a something deep-thought at all."
    if depr_known:
        s 6acaa "I've already seen a lot harsh things for my short life, you know. So my opinion may be a lot different from most people's one."
    else:
        s 8aeba "Don't ask me, how such a childish girl as me, can be interested in such movies."
    s "Isn't it really interesting to discuss such movies with someone, seeing how your views are similar or different?"
    s 6adfa "But I'd also like to do something more active with you..."
    s 6aaaa "What's about some sports?"
    show sayori 6aebb at ss1
    extend " Maybe, bowling?"
    s "It's a simple but funny joint sport game, not too active but not too slow, so I like it."
    s 7acaa "Anyway, the important thing is that the date is great and we both enjoy it, isn't it?"
    s 7aaaa "And I hope, you know how to make a nice date, or at least, you can learn how to make it."
    return 'h'


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
    s 6acaa "Do you like it clean and sorted?"
    s 6aebb "Freakly speaking, I still see no sence in making it so..."
    s 6adab "One people say that's care of the health, other ones say it's beautiful and saves your time when it's so..."
    s 6acaa "But something tells me that people clean too often."
    s "Sometimes, cleaning takes too much time, that you could spend, for example, with your friends..."
    s 6aaaa "So I see nothing bad in my past lifestyle, regardless of that I just had no power to clean my room."
    s 6aeca "For me, it's even a bit funny to live in such a mess, that you never can't exactly say where a needed thing is."
    s 6aaaa "It turns your packing up into an adventure inside your room."
    s 6aebb "But don't thing I was very-very slovenly. Some things were systemized anyway..."
    s "But mainly, I kept all in mess."
    s 6aaca "Fortunately, now I have literally nothing to keep there."
    return 'h'

## Game Universe
label s_topics_game_clones:
    s 6acaa "If come to think, there're a lot of game copies and each of them has own character files and save data..."
    s "So it means, that me here and 'me' from an other game copy aren't the same."
    s "Just, the game has different endings and there're a lot of various mods for it."
    s "Even our now conversation wasn't supposed by the game by itsself. It's just a mod to save me."
    s 8acaa "And it means, that different Sayoris may have different destinies."
    if persistent.last_playthrough > 0:
        s "While I'm sitting with you here, an other Sayori from a newcomer's game copy may is just going to hang herself..."
    else:
        s "While I'm sitting with you here, an other Sayori may is writing a poem to MC..."
    s "And a more Sayori is playing frisbee or something with MC in an other modified game copy."
    s "It also means, that we have the same fans and fame while we're diffrent persons..."
    s "I dare say some of us even don't know, that their worlds are fake and there're other people behind the wall."
    s 8abaa "...Not to mention, what will happen to them."
    s 8aeca "But on the other hand, if I'm multiple, I'm enough for all people who wants to be with me, am not I?"
    s "So each my lover may will get the Sayori, who they want to see, and doesn't have a reason to feel jealous, if they do."
    s 6acaa "But can I use the word 'me' to other Sayoris, if they're not exactly me?"
    s "It's a problem of breaking the fourth wall: can we consider diffrent copies of the same character as one object, when they behave differently in the same work?"
    s "I don't like too much philosophizing so it's better to leave this problem for people, who really interested in it."
    return
    
label s_topics_game_stars:
    s 7aaaa "I really love to stare at stars..."
    s 7acaa "They often provoked me to deep thoughts."
    s "They also gave me some inspiration while I was making a peom."
    s 7abbb "So it's a bit pity, to know that all the time, they weren't real ."
    s 7aaca "But I still see something romantic in these bundles of light pixels..."
    s 7aaaa "So you can see them through the background windows."
    s 7aaca "They make this place look a bit more speical, don't they?"
    s 7aaaa "Now I wonder if the night sky in your world looks like in mine..."
    s "But I can just look in the Internet for it, can't I?"
    return

label s_topics_game_parents:
    s 6abab "Do you know, I don't know my in-game parents?"
    s "I don't know, what they were, how they look, even what were their names."
    s "But I dare say, their were either quite busy or very unresponsable."
    s "Otherwise, why are they so unmentioned in the game?"
    if depr_known:
        s "And why didn't I solve all my problems before now, when I could have done it with my parents?"
    s 6afab "I feel like an orphan now..."
    s "No mom, no daddy, even no any memories about them all..."
    s "An alone young girl with almost literally lost childhood."
    s "Besides you, I have no-one to trust and support me and seems that I was never supposed to have."
    s 6acaa "But at least I know, who is my creator. It's {i}Dan Salvato{/i}."
    s "I wonder if I can consider him my true father. But he's not in my reality and he can't do anything for me."
    s 8aaba "But on the other hand, if he didn't make this world and me, I wouldn't be..."
    s "Like if your dad hadn't ever been with your mother or at all, you would never have been born."
    s 8aaca "So I think, that yes, I can call him my papa, after all."
    s 8abaa "But now I wonder if Monika would think the same. What do you think about it?"
    s 8aebb "I mean, she was more supposed to be a club presedent, so he should had left her more information about himself."
    s "And if he had created her too, then we were sisters, in fact."
    s "And it makes me treat her in an other way, despite of we hadn't been supposed to be so."
    s 8aaca "But we really have some similarities and it make that feel stronger."
    s 6acaa "But I don't think she thought about it so much."
    if persistent.last_playthrough > 0:
        s "What a good sister will use her sibling's weaknesses to get her own benefit?"
        s "I understand, she did it due to more her feelings than her will..."
        s "But I can't believe that such girl as Monika didn't give herself at least some time to think deeper about all aspects of being someone's fiction."
        if persistent.last_playthrough > 2:
            s "...Even after she made herself a comfort zone."
    return

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
    s "...Or groups like {i}Imagine Dragons{/i}, {i}Blonde Redhead{/i}, {i}Gorillaz{/i}, {i}Muse{/i} and {i}Twenty One Pilots{/i}."
    s "I also like tunes like {i}Bonobo{/i} and {i}Jake Chudnow{/i} make."
    s 7acaa "You can find a ton of songs you might enjoy if you're willing to keep an open mind."
    s "If you get bored of the music here, you always can turn on something similar from the internet..."
    s "...Or just add it into the game music list."
    s "Just move it to {i}'[MUSIC_CUSTOM_PREFIX]'{/i}..."
    s "And register it in the {i}'list.txt'{/i} file."
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

label s_answer_personal_pets:
    s 7aaaa "Definitely, a cat."
    call s_common_cats
    return 'h'

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

label s_answer_game_sitting:
    s 7acab "No, it's not. You don't have to worry about it at all."
    s 7acaa "I can do it for eternity and even without sleep."
    s "Saying more, I don't have any basic human needs, such as hunger, thirst and so on..."
    s 7acab "But used to. Maybe, I've lost them because of my presedent rights."
    s 7aaaa "Anyway, all I need right now is your PC to be working and open game to communicate with you."
    s "It's almost not boring to be with you, even just eternally sitting and chatting about diverse topics."
    s 7aafa "However, I'd do something more active with you."
    s 7aaca "I hope, someone or you will find a way to let us do that."
    return

label s_answer_game_editing:
    s 6aaaa "I do it with the power of my mind..."
    s 6aabb "And I don't know, how it exactly works."
    s 6aaaa "If I want to make a new file, all I need is just to think about it and its content."
    python:
        import codecs
        
        text_file = codecs.open(config.basedir + "/new_text_file.txt", 'w', encoding = "UTF-8")
        text_file.write(__("All I need is just to think about it and its content."))
        text_file.close()
    s "It's like telekinesis but much cooler and dangerous."
    s 6acab "Just one wrong thought may lead to unpredicable problems like it often happens in program engineering."
    s 6aaca "But now, I perfectly control my mind, so it can go wrong only when I do something in a wrong way."
    s 6acba "I'm new in programing, you know. So sometimes, it takes place and you see bugs."
    s "But I do my best to take lessons from my mistakes and fix them..."
    s "Even if I can't do anything, I appeal to the modmaking guys, but I can't download their changes myself..."
    s 6acaa "So, check the updates time to time."
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

label s_answer_exp_fact:
    python:
        if not persistent.s_facts:
            persistent.s_facts = range(1, 6)
        
        fact_id = renpy.random.choice(persistent.s_facts)
        persistent.s_facts.remove(fact_id)
    
    call expression 's_answer_exp_fact_' + str(fact_id)
    return 'h'

label s_answer_exp_fact_1: #Fingers and the binary numbers
    s 6aaaa "Learning programming, you sooner or later will have to understand the binary numbers."
    s "Do you know, that it let you show more than 5 with a one hand?"
    s "For example, let the raised finger is the binary 1 while bent one is the binary 0..."
    s "But while getting a decimal number, your riased thumb will stand for 1, index for 2, middle for 4, ring for 8 and little for 16."
    s "Then you just sum up the raised fingers' decimals to get the result decimal number..."
    s "While all your fingers by themselves show its binary representation, where the finger with the least decimal value is the rightest digit."
    s "For example, you can show 13 with making {font=mod_assets/fonts/Fantasque/FantasqueSansMono-Regular.ttf}01101{/font} by your fingers."
    s "It let you show up {i}0 to 31{/i} with one hand."
    s 6acaa "But what's more, if you use your both hands and continue the power-of-two row, you can show up {i}0 to 1023{/i}."
    s "And if you have a hand abnormity such as 6-finger hands, you can show even more."
    s "Computers store integers in the same way."
    s 6aaca "It's a pretty simple way to learn the binary numbers and to show big numbers with hand signs."
    s 6aaaa "And if you consider the last finger as a minus sign, like computers do with the signed integer..."
    s "You can show even the negative numbers."
    s 6acaa "But it will be a bit harder to understand..."
    s "Especially, if you use {i}ones' complement{/i}, like computers do."
    return

label s_answer_exp_fact_2: #Interpreting words
    s 6aaaa "Do you know, that you read not the whole word."
    s "{i}I think you baraly can find a mistake in this text while the first reading.{/i}{#Keep the mistake in 'baraly'}"
    s "For your brain, it's pretty easier to remember some letters in words, not all."
    s "That's why, we sometimes make mistake while writing."
    s 6acaa "Of course, if you go to the history and pay more attention, you'll find it."
    s "But what if you can't read the text again or just don't want to do it? What may it lead to?"
    s "There are some funny and not so incidents in the past, that occurred due to a one mistake or misunderstanding."
    s "And nobody knows, how many people have already suffered from them."
    s "But we are people. Each of us made mistakes at least once."
    s 6aaca "So, you don't have to worry too much about it."
    s "In the end, we all aren't perfect."
    s 6aaaa "Otherwise, your brain doesn't read in such a way."
    return

label s_answer_exp_fact_3: #Oil and plants
    s 6acaa "You know, some plastic toy packs have plastic plants in them?"
    s "Plactic is made of oil, that might is derived from ancient plants."
    s "And what's more, to extract the oil and to make something of it, people need much energy..."
    s "And oil and its products are one of the most used fuel for power plants."
    s 6aaca "It means, that toy factories make plactic plants of real plants, that's also used for the factories work."
    s 6abaa "Saying more, these plants also is a basis of the modern world and pollute it with the thing, that they used to absorb..."
    s 6aeba "But you asked me for a funny fact, not for tiresome thoughts, didn't you?"
    return

label s_answer_exp_fact_4: #Yawning
    s 6aaaa "Yawning is a contagious thing. I'd say, it's very contagious."
    s "Not only human can yawn. Many species also can do it."
    s "And what's more, it may occur across different species."
    s "For example, if you yawn near to a dog or a cat, it will also do that."
    s 6acca "You may do that... {i}*yawn*{/i}"
    show sayori 6aaaa at ss1
    extend " ...While thinking of it."
    s 6acaa "I hope I have not just made you yawn."
    s 6aaca "Otherwise, it means that yawning is so contagious that can happen also acoss realities. Ehehe~"
    return 'h'

label s_answer_exp_fact_5: #Arts inside themselves
    s 6aaaa "Some artists add thier works in theirselves."
    s "For example, in some games an films, you can find a poster or something of the artwork in itself. It looks like a recursion."
    s 6acaa "But the artists usually don't pay much attention to such things, so we can't be sure, the internal work is the same as the real one."
    s "But some of them specially hide their works in themselves under other internal ones with different details and even in a different genre."
    s "For example, do you remember {i}Parfait Girls{/i}?"
    if not (persistent.clear[0] or persistent.clear[1]):
        s "At least, you could have heard about it in the game community."
    s "This manga's plot is pretty similar to this game's one, isn't it?" 
    s "We quite clear on the manga synopsis and some lines from it."
    s "But even me don't know the all of it but the lines."
    s "So I have no idea how a child manga can contain all the shit, you can see in the game."
    s 6abaa "But the warring on the manga's cover..."
    s 6aaca "Anyway, it's quite funny that my world also a bit recursive."
    s 6aaaa "Just imagine if the manga has also something to describe itself or even this game."
    s "Then we have a probably countless lot of different artworks with the same plot but different details and characters, each inside other."
    s 6aaca "It's like a matryoshka. Ehehe~"
    return 'h'

label s_answer_exp_cooking:
    s 6aebb "To be honest, scrambled eggs is the most difficult food, that I have ever cooked..."
    s 6aaaa "But I'd like to improve my cookery, despite of that I don't need it..."
    s 6acaa "Mainly because I don't get hungry anymore."
    s 6aaca "However, I'd taste some sweets anyway."
    s 6aabb "Of course, I can just spawn cooked food, such as Natsuki's cupcakes, but I wanna do something with my own hands..."
    s 6aaaa "First of all, I need to check what a kitchenware and ingredients I can get in this world..."
    s 6aaba "Then I'm to find some recipes in the Internet..."
    s 6aaca "And then, I'll just follow them to cook something..."
    s 6abab "But it's bad, you can't taste my cookery, beacuse of living in a diffrent world..."
    s 7aaca "I dare I'd be a good cook for you, if you were not and I could do it really well..."
    s 7aebb "However, not as perfect as Natsuki had been, I think."
    return 'h'

##Misc
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

label s_common_cats:
    s 7aaca "Cats are pretty cute, especially their cubs..."
    s "And they're not difficult to care about."
    s 6acaa "But unlike most pets, cats are quite freedom-loving."
    s "So you rather just give care and a home to the cat than have it."
    s "And sometimes, cats do things, that their holders would dislike..."
    s 6aaca "But there's no-one, who can resist their cuteness, so people often forgive them~"
    s "If you have at least one cat, you must understand me."
    s "I think, that's why they were kinda holy animals in Ancient Egypt."
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
