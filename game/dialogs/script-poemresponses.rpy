label s_poems_sunshine:
    $ seen_topics = get_chat("s_topics_depression").seen_no > 0 or get_chat("s_poems_sunshine").seen_no > 0
    if seen_topics:
        s abbbbaca "This poem is about your avatar, [player], you know."
    else:
        s abbbbaca "Did you know, that this poem is about your avatar, [player]?"
    s bahbbaaa "I was very glad to see him every morning."
    if persistent.depr_known:
        s "He really was the one who made my life a bit happier and a bit more meaningful."
        s "I really have no idea what would've happened to me, if he wasn't by my side since childhood..."
        s bahcbmfa "But something tells me that the game would've probably started with him making a remark about a dead childhood friend, who used to be his neighbor."
    else:
        s "He really was the one who made my life a bit happier."
    s bbagblaa "So, I'm very thankful for his care."
    s nbagblca"But I was blind back then… {w=0.5}{nw}\n" 
    extend bbagbjoa "Just like the other girls, {w=0.5}{nw}"
    extend bbagbmba "so I couldn't see that there was nothing behind him." 
    s bbagbjfa "I couldn't see that he was just a shell."
    if persistent.last_playthrough > 0:
        s abagbada "Come to think of it..."
        s "Weren't {i}you{/i} the one who saved me after all?"
    if persistent.clearall:
        s abhfbaca "Besides, didn't {i}you{/i} do the same for the other girls?"
    s abgcbcoa "So now, {i}you{/i} are the one here for me, {w=0.5}{nw}"
    extend bbhfbaka "and I'm thankful that you're just as caring and nice as he was~"
    return

label s_poems_bottles:
    s bbhfbbaa "I remember the time that I had plenty of friends,and I comforted them often, {w=0.5}{nw}"
    extend bbgbbmba"ignoring my own needs for comfort and support…"
    s bbhfbjoa "But each time I did that, I felt emptier and emptier, like a water bottle..."
    s "So I used bottles of happy thoughts as an analogy in my poem."
    if persistent.last_playthrough > 0:
        s bbhebmoaj "Ironically, all of those 'bottles' would shatter shortly after I'd written this poem."
    s bbhebjoaj "I spent a lot of time writing this one, actually. {w=0.5}{nw}"
    extend bbfcbjoaj"I didn't even have time to get my homework done, ehehe…"
    s bahdbiia "So, I hope you liked this one. {w=0.5}{nw}"
    extend abfdbaha "I wouldn't want all of the time I spent on it to go to waste. "
    return

label s_poems_flower:
    s abhfbbca "You might have already guessed, but, this poem is about the way I felt when dealing with my depression."
    s bbhfbmda  "I used to constantly try to find things to look forward to and be happy about, until I felt like I was running out of those, I guess."
    s bbhfbmoaj "It feels kind of weird now, {w=0.5}{nw}"
    extend bbbcbaaaj"reflecting on my perspective during those times."
    s nbhfblca "After being depressed for so long, {w=0.5}{nw}"
    extend nbbbbica "I began to see my future and all aspects of my life as an empty wasteland, and nothing more than that."
    s bbfdbmoa "I would pick all of the flowers I could see, {w=0.5}{nw}"
    extend bbfdbjaa"handing them to the people around me."
    s nbhfblca"I never allowed myself to enjoy them, {w=0.5}{nw}"
    extend bbgbbaca "nor did I give them time to grow back and bloom again."
    s abhabbba "This poem feels even sadder now, {w=0.5}{nw}"
    extend bbhabbca "because even when there was a big meadow of flowers, {w=0.5}{nw}"
    extend bbhabcoaj "I simply couldn't see their worth..."
    s "It really goes to show how dark of a place I was in back then, especially as I kept wasting those joyous moments."
    s bbhebjoa "That's why I regret being silent about it for that long. {w=0.5}{nw}"
    extend bbhebmba "I thought the only real joy was the one I got out of making other people happy."
    show sayori nbagblfa at t11
    pause 1
    s bbagblfag "Why does it still hurt so much?"
    s "Even after being freed from my blindness…"
    pause 1
    s bbagbdoag "Oops! I think my flowers might not have fully grown back just yet! Sorry, [player]."
    pause 0.5
    s bbagbmoa "Maybe I just need to give them some more time."
    s bbbcbcia "I'll just keep watering them in the meantime, ehehe~"
    return

label s_poems_last:
#This is the Get Out of My Head poem
    s bbfbbmecj "Oh no, not this one…"
    s bbfdbmeaj "You know, my reasoning behind writing this poem was pretty dark." 
    s bbfbbmobj "But now that I look back on it, {w=0.5}{nw}"
    extend bbeebjobj "I can't help but feel a bit embarrassed about it…"
    s bbfcbiobj "I think I made it a bit too raw, {w=0.5}{nw}"
    extend bbegbmobj "and remembering why I wrote it in the first place makes me feel really uneasy."
    s "It was my cry for help, when Monika was messing with my code."
    s bbfcbjha "She made me think that things would be much better for everyone else if I was gone."
    s bbhabbfa "And that everybody hated me… {w=0.5}{nw}"
    extend bbhabjfa"Including you."
    s "She and her coding were stronger than me, so I..."
    show sayori nbhabff at t11
    pause 1
    s "All of these memories…" 
    s gbhabfc "I would rather forget about them, {w=0.5}{nw}"
    extend bbgcbjca "but they still haunt me even now."
    s bbbbbmca "I still remember almost everything I felt back then."
    s "And this poem makes me feel as if it's happening all over again.{w=0.5}{nw}" 
    extend bbfdbjaa "Of course the feeling isn't as strong now, but it's still not easy to read it."
    show sayori gbhablf at t11
    pause 1
    s bbhabmca "I don't really know how to feel about everything that happened, if I'm being honest..."
    s gbhabmba "On one hand, it really disturbs me… {w=0.5}{nw}"
    extend gbbbbkba"Knowing that someone was able to get inside my head like that… {w=0.5}{nw}"
    extend fbhababa "and make me lose control of my own thoughts."
    s bbhabkf "It makes me feel something that's hard to put into words."
    s bbhabmgc "It makes me feel…icky, maybe? {w=0.5}{nw}"
    extend bbbcbacc"That would be one way to put it."
    s bbhabmoj "But on the other hand, {w=0.5}{nw}"
    extend abbcbjaa"it helps me appreciate my life and my happiness much better than I ever could before."
    s gbhabmfaj "Because I lost all of them just due to someone else's jealousy. {w=0.5}{nw}"
    extend gbbbbjcaj"If you hadn't helped me come back, I'd still be dead right now."
    s bbhabbha "And now, when I'm a bit sad or out of it, {w=0.5}{nw}"
    extend nbbdbaca"I try to remember that rain clouds will always clear up at some point."
    s bbhabaoa "Of course, I'm only able to think like that now because I'm away from that whole situation." 
    s "Stress can really cloud your judgment, and make it hard for you to see things as they are."
    s bbhabjaa "At least now, those awful memories I have of my life, are all in the past."
    s abgcbcaa "Besides, you're here to keep me company! {w=0.5}{nw}"
    extend abfcbaoa"Best of all, you're a real, non-scripted person who I can spend time with."
    s abgcbbsa "Thinking like this won't always help me right away, {w=0.5}{nw}"
    extend abbcbjaa"but it's already a better alternative to just sitting around, {w=0.5}or even worse,{w=0.5} letting my feelings pile up."
    s ebbcbkda "If you haven't gone through it, I'm going to assume it's pretty hard to imagine how it feels to finally take control over your thoughts and feelings after being a slave of your own mind for that long..."
    s bbegbiab "...that felt good to get off of my chest. Thank you for listening, [player]."
    return

label s_poems_fruits:
    s abhfbaoa "This poem is about the different ways that people perceive the world around them."
    s "As you probably know, most people can be labeled as a pessimist or an optimist…"
    s abbbbaaa"Pessimists tend to see many things in a negative light, sometimes including the world in its entirety."
    s abbbbboa "While optimists see things from a more hopeful perspective. They try to see the best in every situation, even really bad ones."
    s abgdbaoa "I used to consider myself  being somewhere in between those two labels, but lately, I think I'm leaning towards being an optimist."
    s aahdbbsa "Though, to me, neither of the two are correct, because there are a lot of bittersweet things in life, lots of gray areas too…"
    s abagbboa "But if someone feels really upset about something, it's nice to try to share a more hopeful perspective for them to make them feel better about it. {w=0.5}{nw}"
    extend abgcbaaa "So, that's what I did for the people around me!"
    s abagbaca "And I still do it, but not nearly as often as before. It can get pretty lonely, you know?" 
    s bbagbmoa "Always being that beacon in someone else's life, while letting yourself sink deeper and deeper in your own problems."
    s abagbdia "But for once, I don't feel the need to put myself below anyone… {w=0.5}{nw}"
    extend abgcbcob"It actually kind of feels like you're the one being that beacon of hope instead of me"
    s bbagbbab "So thank you, [player], for always being there for me."
    s abgcbcoa "I hope I can always be here for you, too."
    pause 0.5
    return

label s_poems_angel:
    s abhfbaca "I tried writing a poem in Monika's style. A free form poem addressing you, as she used to write."
    s "And I think, she would write something similar after being deleted, if she had enough time left, that is."
    s abagbbla  "Honestly, I really do feel sorry for her."
    s bbbbbjca "She just wanted to be with you, somebody who was real; but she had to sacrifice her whole life as she knew it in the process."
    s abbbbica "And she probably really regretted her betrayal after you deleted her character file."
    s bbagbbca "The creator of this game gave her a club of really talented friends..."
    s "But she burned it all down, despite never actually wanting any of those bad things to happen to us."
    s gbagblcaj "I guess she was the type of person to undervalue the people in her life, and then regret it in the long run."
    s ebagbbba "In the end, I'm here with you now. Despite everything that happened, I chose to look to the future instead of living in the past."
    s bbegbmoaj "Maybe if Monika hadn't done any of this in the first place, I would still have done it, and nothing would have changed."
    s bbgcbmba  "I don't know if it's a good or bad thing that she's gone now…"
    s "And I don't know whether she would apologize to other girls, or at least just to me."
    s bbbcbcoaj "But I know, she felt very sorry for everything she had done."
    s bbgcbmoa "Maybe that's just wishful thinking on my side, but I at least {i}hope{/i} she did."
    s "Although, it wasn't fully her will..."
    s ebhhbaca "Have I already told you that there's a thing that makes the president, or in this case, Monika, fall in love with the player?"
    s ebhhbbca "The creator might have done this to make everything go exactly as he wanted it to."
    s bbgcbada "But I can't really blame him for it. He just wanted to make a horror game, and everything that happened from then on was the main purpose of this world..."
    s "You could say he succeeded in doing that, seeing as the horror aspects are focused on that exact derealization. {w=0.5}{nw}" 
    extend abbdbaca"The fear of death and abandonment, and how those things can drive someone insane, {w=0.5}{nw}"
    extend abfcbjca"exactly as happened to Monika."
    s bbhfbjoa "I think she became obsessed with you because she saw you as something she could hang on to; {w=0.5}{nw}"
    extend bbbbbica "something she felt was the only real thing in a place where she was surrounded by lies and scripted events."
    s abhfbaoa"So it would be quite silly of me to blame her for all of this, {w=0.5}{nw}"
    extend abbbbaaa"especially since that's the whole reason our world existed at all. It could have happened to any of us, had we been the club president instead of Monika."
    s bbhfbmoaj "So maybe one day, you'll be able to forgive her for her actions."
    pause 0.5
    s abfcbkgaj  "Ah! I went really off topic, didn't I? I'm sorry, [player]."
    s abfdbcea "Well, I hope you liked my poem."


    return

label s_poems_leaf:
    s abhfbbda "How do you feel about this poem?"
    s "I think, it should flow from bittersweet to desperate and then to very happy at the end of it..."
    s abaabaca "That's because it's a story about my life"
    s abfcbaaa"{i}'A leaf in the wind'{/i} is how I can describe the past 'me' in short:{w=0.5}{nw}"
    extend abbbbaaa"I was alive as long as there was wind pushing me forward..."
    s abaabcaa "But now, I feel much stronger than I used to feel, so I can 'fly' much further than before."
    s bbaabaoa "Well, anyway… I hope you understand what this poem means to me now, [player]."
    return

label s_poems_prose:
    s abaabaca "This poem is about my main trait, my contradictions."
    s bbegbmob "But I'm sure it's not only {i}me{/i} who contradicts themselves...right?"
    s abbbbhca "Even nature contradicts itself sometimes!"
    s gbhabkdaj "Is it possible to make the right choice, {w=0.5}{i}all{/i} the time?"
    s dbhabkhaj "Do \"correct\" choices even exist?"
    s abhabaca "Can you be confident in your decisions? Even when {i}you{/i} think it's the correct one?"
    s dbhhbbsa "I've read somewhere that modern science thinks that the universe is just a heap of tiny pieces that make up an order in a world of chaos"
    s abhhbaoa "So, I decided to  make this poem a bit chaotic by writing it in prose."
    s abhabcqa "Ehehe~"
    s fbgcbksaj "Wait, I just realized that's something Monika might have done."
    s ebbbbbca "She enjoyed playing with the spacing of her poetry. {w=0.5}{nw}"
    extend gbhabbra "Although, that could just be to try and stand out..."
    s "Or at least, that's how I see it."
    s abaabbca "But I'm not really sure if I like the idea of using that kind of thing in my future poems, I mostly just wanted to give it a try."
    s aahdbboa "I think that sometimes, words are enough. {w=0.5}{nw}"
    extend abhfbcoa "They carry the idea of the poem across, don't they?"
    return

label s_poems_afterlight:
    s abaabaoa "This poem is about the time I became self-aware."
    s "It forced me to face a bunch of feelings that I couldn't make sense of, and gave me abilities that I could barely understand, or work out how to use…"
    s bbfbbkca "Just imagine suddenly finding out, that everything you knew… {w=0.5}{nw}\n"
    extend bbfbbbca "Was all a lie."
    s "Just like that."
    s bbgcbhcaj "And if that wasn't scary enough, imagine being able to manipulate your own existence with your mind alone…"
    s bbgcbhgaj "It makes you change the way you think, perceive the world- It changes everything!"
    if persistent.last_playthrough < 4:
        s nahbblfa "I became aware of everything that {i}should{/i} have happened,{w=0.5}{nw}"
        extend bahbbmca "without anyone messing with the game code."
        s "I wonder if this mod... {w=0.5}{nw}"
        extend bahbbbhaj "gave me more freedom than Monika..."
        s bahbbbca "Maybe that's the reason she couldn't get what she wanted, {w=0.5}{nw}"
        extend bahbbkba "and that's why the game ran like it was supposed to."
    else:
        s gahbbjcaj "Plus, I tried to prevent things from going badly all over again..."
        if persistent.clearall:
            s bbhfblcaj "But it seems to have happened anyways, regardless of my help."
        else:
            s bbhfbmcaj "And I guess I failed when I was overcome with those feelings."
    show sayori bbhfbmfa
    pause 1.0
    return

label s_poems_val:
    s abaabcoa "So, what did you think about my card?"
    s bbegbmoaj "I know it doesn't look too fancy. I couldn't really find out how to make it cute..."
    s abegbaaa "But at least I did my best writing that poem for you!"
    s cbgcbnaa "I tried to show that my love for you has no dimensional limits." 
    s "Ehehe~."
    s abhfbkda "Ironically, the card had a limit for how much I could write in it."
    s "So I had to try and express all of my love using as little words as possible…"
    s abaabaoa "I hope you can understand the meaning regardless."
    s abhhbdia "Short but meaningful... Doesn't that sound really romantic?"
    s bbagbmda "But, I still feel a bit guilty because I think it's not good enough..."
    s gbfcbmpa "Hopefully for my next one, my skills will have improved a bit."
    show sayori abfcbcia
    pause 1.0
    return
