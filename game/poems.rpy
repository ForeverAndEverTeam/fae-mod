#A brand new poem script, adopted for multi-language GUI and the mod
image paper = "images/bg/poem.jpg"

default persistent.last_new_poem_time = None
default persistent.new_poem_delay = 0 #12-hour periods between two new poems

#Animations for the poem
transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

#Basic styling for all poems
style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    #xsize 18
    ysize 700
    #base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    #thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    #unscrollable "hide"
    #bar_invert True

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

#Unicode Sayori's style
style sayori_text_unicode is sayori_text:
    font "mod_assets/fonts/gnyrwn971.ttf"
    size 26

init -10 python:
    class Poem(): #New peom class
        def __init__(self, author, title = None, text = None):
            self.author = author
            self.title = {'eng': title or (author + "\'s poem")}
            self.text = {'eng': text or "Simple text"}
    
#Dear Sunshine
    poem_sunshine = Poem(
    author = "sayori",
    title = "Dear Sunshine",
    text = """\
The way you glow through my blinds in the morning
It makes me feel like you missed me.
Kissing my forehead to help me out of bed.
Making me rub the sleepy from my eyes.

Are you asking me to come out and play?
Are you trusting me to wish away a rainy day?
I look above. The sky is blue.
It's a secret, but I trust you too.

If it wasn't for you, I could sleep forever.
But I'm not mad.

I want breakfast."""
    )
    
    poem_sunshine.title["rus"] = "Дорогой рассвет"
    poem_sunshine.title["epo"] = "Kara Sunlum'"
    
    poem_sunshine.text["rus"] = """\
Лучами бьёшься ты сквозь веки,
Как будто каждое утро ждёшь меня.
Меня целуешь прямо в лобик
Сонливую, будя меня.

Хотелось ли тебе со мной играть?
Или со мной развеять тучи?
От неба втайне хочется сказать:
Тебе доверяюсь при любом я случаи.

Если б не ты — я бы спала,
Спала бы сном я вечным.
Нет, я не больна, я голодна.
На завтрак наложите есть мне."""
    
    poem_sunshine.text["epo"] = """\
Vi lumas tra miaj palpebroj.
Ĝi min fartigas, ke mi mankis al vi.
Tenere kisas vi na mia frunto,
Kaj tiel vi min ellitigas.

Ĉu volas fidi min forigi la nubaĉojn
Aŭ nur promeni kun mi ekster mia hejm'?
Pro ke la ĉiel\' nun estas tiel klara, 
Mi nun sekrete volas danki vin.

Se vi ne estus nun, do mi dum ĉiam dormus.
Sed ne, ne estas mi freneza. 

Mi nur ankoraŭ ne matenmanĝis."""

#Bottles
    poem_bottles = Poem(
    author = "sayori",
    title = "Bottles",
    text = """\
I pop off my scalp like the lid of a cookie jar.
It's the secret place where I keep all my dreams.
Little balls of sunshine, all rubbing together like a bundle of kittens.
I reach inside with my thumb and forefinger and pluck one out.
It's warm and tingly.
But there's no time to waste! I put it in a bottle to keep it safe.
And I put the bottle on the shelf with all of the other bottles.
Happy thoughts, happy thoughts, happy thoughts in bottles, all in a row.

My collection makes me lots of friends.
Each bottle a starlight to make amends.
Sometimes my friend feels a certain way.
Down comes a bottle to save the day.

Night after night, more dreams.
Friend after friend, more bottles.
Deeper and deeper my fingers go.
Like exploring a dark cave, discovering the secrets hiding in the nooks and crannies.
Digging and digging.
Scraping and scraping.

I blow dust off my bottle caps.
It doesn't feel like time elapsed.
My empty shelf could use some more.
My friends look through my locked front door.

Finally, all done. I open up, and in come my friends.
In they come, in such a hurry. Do they want my bottles that much?
I frantically pull them from the shelf, one after the other.
Holding them out to each and every friend.
Each and every bottle.
But every time I let one go, it shatters against the tile between my feet.
Happy thoughts, happy thoughts, happy thoughts in shards, all over the floor.

They were supposed to be for my friends, my friends who aren't smiling.
They're all shouting, pleading. Something.
But all I hear is echo, echo, echo, echo, echo
Inside my head."""
    )

    poem_bottles.title['rus'] = "Склянки"
    poem_bottles.title['epo'] = "Boteloj"

    poem_bottles.text['rus'] = """\
Я открываю мозг как банку.
Хранятся в нём все мои мечты.
Они на вид, как колобки из света.
Тянусь руками прямо к ним.
Они теплы, но кольки.
Спешу засунуть их в скляночку я.
Кладу ту склянку я на полку.
Счастливый мысли легут в ряд.

Та полка манит ко мне людишек.
Я им всем склянки раздаю.
Тем, кто из них не в духе.
Они яркий день спасут.

День за днём, всё больше мыслей.
Душа за душой, всё больше склянок.
Всё глубже-глубже лезу я.
Я будто лезу в глубую пешеру, опасностей которая полна.
Прокарывая её всё глубже-глубже.
Сверля-сверля-сверля-сверля-сверля.

Сдуваю пыль я со своих склянок.
Не кажется мне, что время прошло.
На полке ещё места просто до кучи.
Людишки перед зыкрытой мной дверью встали кругом.

Ну всё, всё готово. Даю я проходу.
Спешно они заходят в мой дом.
Зачем же им всем и зачем так много?
Склянки даются одна за другой.
Пустеет полка прям на глазах.
Но стоило раз поглубже засуть мне руку.
Счастливые мысли грохнулись в миг
Со мною и с тяжёлою полкой.

Ведь все они были для угрюмых людей.
Который кричали, молили у меня что-то.
Но их просьбы лишь отвались мне эхом,
Эхом глубоко у меня в голове."""

    poem_bottles.text['epo'] = """\
Mi forigas la skalpon, kvazaŭ kovrilon.
La kap\' estas mia sekreta revejo.
Globetoj da sunlum' helas kaj frotas.
Por unu karesi mi tiras la manon.
Mi sensas ĝin varma sed multe pika.
Por ne perdi la tempon, mi ĝin enboteligas.
Kaj metas na l\' botel\' en la botelan ŝrankon.
Vicigante miajn filiĉajn pensojn.

La botelaro helpas amikiĝi min.
Per la boteloj, mi kompensas miajn fiaĵojn,
Kaj helpas min kaj al miaj amikoj,
Savi l\' agordon en malgajaj tagoj.

Nokt\' sekvas nokton, pli sonĝojn ricevas.
Amik\' sekvas amikon, pli botelojn mi havas.
Mi pli profunde tiru la manon,
Kvazaŭ esploras malluman antron,
Fosant-fosante
Kaj pioĉant-pioĉante.

La polvon mi forblovas.
La temp\' kvazaŭ ne pasas.
Ankoraŭ la ŝranko ne estas tro plena
Kaj la amikoj staras antaŭ la pordo.

Mi ĉion finas kaj pasigas l\' amikojn.
Urĝe ili iras al mi. 
Ĉu ili vere volas miajn botelojn?
Rapide al ĉiuj mi disdonas ilin.

Al unu mi donas, kaj al l\' alia.
Botel\' post bobel\' na mia hejm\' lasas.
Sed unue mi ion malprave faris, do l\' ŝranko kun la boteloj sur mi falis.
Kaj elboteliĝis ĉirkaŭ mi la feliĉaj pensoj.

Mi volas doni na ili al tiuj amiko,
Kiuj ne ridas, sed ne povas mi plu.
L\' amikoj ilin al mi forte postulas.
Sed la postuloj aŭskultiĝas nur eĥe."""

#The Last Flower (name by AlexanDDOS)
    poem_flower = Poem(author = "sayori", title = "The Last Flower")
    poem_flower.text['eng'] = """\
Between my feet
The last remaining flower beckons to me.
I twist the stem, freeing it from its clinging roots
Caressing the final joyous moment between my fingers.

But to what ends have I summoned this joy?
For now when, I look in every direction
The once-prosperous field before me
Is but a barren wasteland!"""

    poem_flower.title['rus'] = "Последний цветок"
    poem_flower.title['epo'] = "Resta Floro"
    
    poem_flower.text['epo'] = """\Inter miaj gamboj
La resta floro estas kaj min loĝas.
Mi kaptas l' tigon kaj de la radik' ĝin liberigas,
Kaj la lastan gajan momenton mi per miaj fingroj karesas.

Sed kiel longe mi tenu la gajon?
Nun, mi rigardante al io ajn,
Vidas nur la nuran kampon,
Kiu estas dezerta kaj jam ankaŭ malviva."""

    poem_flower.text['rus'] = """\
Передо мной красуется последний цветок,
Своим внешним видом меня манит он.
Возьму-ка за стебель и вырву с корнём,
Посмотрев на него, как на последний радости огонёк.

Что же теперь?
Куда я не взгляну,
Мне видно лишь пустое выжженное поле,
В котором стою я одна."""
    
#Get Out of My Head (aka %)
    poem_last = Poem(
    author = "sayori",
    title = "%",
    text = '''\
Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of
Get.
Out.
Of.
My.
Head.\n\n\n
Get out of my head before I do what I know is best for you.
Get out of my head before I listen to everything she said to me.
Get out of my head before I show you how much I love you.
Get out of my head before I finish writing this poem.\n\n\n\n\n\n\n
But a poem is never actually finished.
It just stops moving.'''
    )
    
    poem_last.text['rus'] = '''\
Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из
Убирайся.
Прочь.
Из.
Моей.
Головы.\n\n\n
Убирайся прочь из моей головы, а не то я сделаю то, что лучше всего для тебя.
Убирайся прочь из моей головы, а не то я сделаю то, что сделать она мне сказала.
Убирайся прочь из моей головы, а не то я покажу, как сильно я в тебя влюблена.
Убирайся прочь из моей головы, а не то я закончу этот стих прям сейчас...\n\n\n\n\n\n\n
Но я знаю, он не закончится никогда.
Он лишь станет на веки бездвижным.'''
    
    poem_last.text['epo'] = '''\
Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el
Bonvolu.
Foriĝi.
El.
Mia.
Cerbaĉo.\n\n\n
Bonvolu foriĝi el mia cerbaĉo ĝis mi faros tion, kio eatas la plej bona por vi.
Bonvolu foriĝi el mia cerbaĉo ĝis mi faros tion, kion konsilis al mi ŝi.
Bonvolu foriĝi el mia cerbaĉo ĝis mi montros al vi, kiel amas mi vin.
Bonvolu foriĝi el mia cerbaĉo ĝis mi finos ĉi tiun aĉan versaĵon.\n\n\n\n\n\n\n
Sed ĝi fakte neniam finiĝos.
Ĝi nur haltos kun mi baldaŭ.'''
    
#Fruits of the life (by AlexanDDOS)
    poem_fruits = Poem(
        author = "sayori",
        title = "Fruits of the life",
        text = '''\
The universe gives fruits of life to all of us.
They all have diverse size and shape.
But no-one knows their real savor,
Because of each feel them in their own way.

One people feel them always bitter,
Some of them, even if the fruit is of the best.
Another ones feel them sweet and very tasty,
Whatever fruits they have got.

For me, they have the taste of liquorice.
I needed time to understand how sweet they are,
To get rid of those unpleasant feelings,
Which I had got after the first bites.

Now all I want is just to eat my own fruit
With the person, who helped me catch the real taste.
But I should not forget to do my real job here:
To find a way to make others feel the fruits sweet.'''
    )

    poem_fruits.title["rus"] = "Плоды древа жизни"
    poem_fruits.title["epo"] = "Vivarbaj Fruktoj"

    poem_fruits.text["epo"] = """La vivarb\' donas siajn fruktojn.
Ĉiuj fruktoj vide tre diversas.
Neniu konas ilian veran guston,
Sed pri ili oni tre diverse diras.

Por unuj gustas ili amare,
Eĉ tiuj, kiuj estas la plej bonaj.
Por la aliaj guste ili dolĉe,
Malgraŭ kiaj ili estas.

Laŭ mi, la fruktoj gustas glicirizaĵe:
Ne tuje tempis sensi ilin dolĉaj.
Antaŭe gustas ili ankaŭ tre amare,
Sed tio pasis dum la pluaj mordoj.

Disiras mi nun nur daŭrigi mian manĝon,
Kun l\' homo, kiu dolĉigis mian frukton,
Sed mi ankaŭ ne forgesu mian devon:
Helpi dolĉigi fruktojn de aliaj homoj."""

    poem_fruits.text["rus"] = """\
Даёт плоды нам сад деревьев жизни,
У каждого плода своя форма и размер.
Но никому ещё не удавалось
Понять их вкуса истенный манер.

Одним они казались горьки,
Неважен был при этом сорт.
Другим они были лишь в сладость,
Хоть всякий ты, с их слов, возмёшь.

По мне они — будто лакрица:
Со временем лишь сладость я смогла понять.
Пришлось мне с горечью бороться,
Которую я часто могла лишь ощущать.

Сейчас хочу я просто есть свой плод
С тем, кто мне сладость ту помог понять.
Но всё же стоит долг мне помнить:
Плодам чужим я сладости должна давать."""

#Hatred (by AlexanDDOS)
    poem_hatred = Poem(
        author = "sayori",
        title = "Hatred",
        text = """\
Why do you hate me?
Is it beacuse I hide my problems to be solved?
Why do you hate me?
Is it beacuse I seemed silly and then cunning?

Why do you hate me?
Is it beacuse I was too clumsy due to my endless apathy?
Why do you hate me?
Is it beacuse I am too colorful for your pale society?

Why do you hate me?
Is it beacuse you can love anyone but a hanging girl?
Why do you hate me?
Is it beacuse you like anything large but large kindly heart?

No, I seem to know, why you all hate me.
You just see nothing in the eyes of the dead past me."""
    )

    poem_hatred.title['rus'] = "Нелюбима"
    poem_hatred.title['epo'] = "Malamo"

    poem_hatred.text['rus'] = """\
За что я вами нелюбима?
За то, что от своих проблем я до последнего скрывалась?
За что я вами нелюбима?
За то, что я то слишуом глупой, я слишком хитрой я казалась?

За что я вами нелюбима?
За апатичную неуклюжось?
За что я вами нелюбима?
За чрезмерную для вас яркость?

За что я вами нелюбима?
За то, что я ушла тогда смертью отчаявшихся?
За что я вами нелюбима?
За то, что любовь к большому на добром сердце у вас кончается?

Хотя, я знаю, кажется, за что я вами нелюбима.
Вам просто ничего не видно в глазах той меня, что в петле качается."""

    poem_hatred.text['epo'] = """\
Kial vi tiel min malamas?
Ĉu ĉar mi kaŝi la enajn problemojn penis?
Kial vi tiel min malamas?
Ĉu ĉar vi min nur stulta aŭ nur ruza vidis?

Kial vi tiel min malamas?
Ĉu ĉar mi mallertis nur pro mia apatio?
Kial vi tiel min malamas?
Ĉu ĉar por via mond\', mi estas tro kolororiĉa?

Kial vi tiel min malamas?
Ĉu ĉar malamas vi ĉiujn sinpendumintinojn?
Kial vi tiel min malamas?
Ĉu ĉar vi ŝatas ĉion grandan krom grandajn bonajn korojn?

Tamen, mi pensas, ke vi eble tiel min malamas,
Nur ĉar ne vidas ion ajn vi en la vizaĝ\' de l\' morta mio."""

#Friend (by AlexanDDOS)
    poem_goddess = Poem(
        author = "sayori",
        title = "Friend",
        text = """\
She set the whole world on great fire.

"""
    )


screen poem(currentpoem, paper="paper"):
    $lc = cur_lang().code or 'eng'
    $title = currentpoem.title.get(lc) or currentpoem.title['eng']
    $text = currentpoem.text.get(lc) or currentpoem.text['eng']
    
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None) #Subwindow size for showing text
        mousewheel True #make scrollable
        draggable True
        vbox:
            null height 40
            #Text style is determine by the author
            if currentpoem.author == "yuri":
                text "[title]\n\n[text]" style "yuri_text"
            elif currentpoem.author == "sayori":
                text "[title]\n\n[text]" style s_text_style()
            elif currentpoem.author == "natsuki":
                text "[title]\n\n[text]" style "natsuki_text"
            elif currentpoem.author == "monika":
                text "[title]\n\n[text]" style "monika_text"
            null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

label showpoem(poem=None, paper=None):
    #If no poem key is given, just go back
    if poem == None:
        return
    
    window hide
    play sound audio.page_turn

    #Show the background paper
    if paper:
        show screen poem(poem, paper=paper)
        with Dissolve(1)
    else:
        show screen poem(poem)
        with Dissolve(1)
    $ pause()

    hide screen poem
    with Dissolve(.5)
    window auto
    return

label s_poems_sunshine:
    call showpoem(poem_sunshine)
    if "s_topics_personal_depression" in persistent.seen_topics:
        s 6acaa "This poem is about your avatar, [player], you know."
    else:
        s 6acaa "Do you know, that this poem, about your avatar, [player]?"
    s 6aaab "I was very glad to see him every morning."
    if depr_known:
        s "He really was the one, who made my life a bit happier and meaningful."
        s "I really have no idea, what would happen with me, if he weren't on my side since our childhood..."
        s 6abac "But something tells me, that the game probably would start with his remark about a dead childhood friend, who was his neighbour before."
    else:
        s "He really was the one, who made my life a bit happier."
    s 6aaab "So, I'm very thankful for his care."
    s "But I was a blind person then, like most other girls, so I didn't see such a nicer guy like you behind him."
    if persistent.last_playthrough > 0:
        s 6acaa "And if come to think, didn't exactly {i}you{/i} save me after all?"
    s 6acaa "And if {i}you{/i} couldn't take some choices instead of him, could I have at least some more time with him?"
    if persistent.clear_all:
        s "And what's more, didn't exactly {i}you{/i} do the same with other girls?"
    s 7aaca "So now, {i}you{/i} are that one and I hope, you're still so careful and nice like you was~"
    return 'h'

label s_poems_bottles:
    call showpoem(poem_bottles)
    s 6aaaa "I remember I had plenty of friends and I often conforted them..."
    s 6acaa "But each time, I felt like they made me more and more emptier, like a water bottle..."
    s "So I used bottles of happy thoughts as an analogy."
    if persistent.last_playthrough > 0:
        s 6acba "Ironically, the shelf with them really fell some time after I'd written this poems."
    s 6abaa "I spent a lot of time to write the poem. I even didn't do my homework at all..."
    s 7aaaa "So I hope was not a waste of great effort and at least you really like this one."
    return

label s_poems_flower:
    call showpoem(poem_bottles)
    s 6acaa "It's a poem about how I tried to find good times in my life, pale from my ex view..."
    s "I think it's obvious, that I found not so much and tried to get from them as much as I could."
    s "And the barren wasteland is how I saw my future and the rest aspects of my life."
    s 6afbb "But I feel this poem more sad now, because all the time, there was a big meadow of flowers..."
    s "I-I just couldn't feel the all flowers so I wasted so much joyous moments."
    s "That's why I regret so much about my silence. I just thought the only real joy was that I had only with someone."
    show sayori 6dfcb at ss1
    pause 1
    s "Why it hurts me so much now?.."
    s "Even after I got rid of the reason of my blindness."
    return 's'

label s_poems_last:
    call showpoem(poem_last)
    s 6acab "You know, why I've written this poem."
    s "It was my white flag against all of Monika's atrocities."
    s "She made me think, that it'd be much better for your avatar, if I'd disapeared..."
    s "And that he hated my very much, so I'd unsuccesssfully tried to forget him..."
    s "But she and my love were stronger than me, so I..."
    show sayori 6efab at ss1
    pause 1
    s "These memories... They are pretty painful for me, you know."
    s "I still remember almost all, that it felt then."
    s "And this poem  makes me feel it again stronger."
    s 6dbbb "I don't know how to think easier about all the experience I had..."
    s 6dbba "But on the other hand, it helps me appreciate my life and happiness better..."
    s "Because I lost them all just due to someone else's envy, and if you didn't help me, I'd still be dead."
    s 6aaba "And now, when I'm a bit out of sorts, I just remember that rainclouds always will go away..."
    s "And that I had the much worse time in my life."
    s 8aabb "It not always help me instantly, but it's well it works at all."
    s 8aeca "You can't imagine, how it feels, when you finally take over your feelings after a pretty long being their slave..."
    return

label s_poems_fruits:
    call showpoem(poem_fruits)
    s 6acaa "This poems is about how different people see the world and the life diffrently."
    s "As you know most people can be divided into pessimists and optimists..."
    s "The first see many things negatively so they're just viewers of the boring and meaningless show..."
    s 6aaca "While the second see the things in the opposite way so they hope that everything goes to be okay, even if it doesn't seem so."
    s 6aaaa "I always was between these 2 sides but now I'm much more the second than the first."
    s "For me, the best view is not on any of the sides, because there're a lot of bittersweet things..."
    s 6acaa "But if someone feel them too bitter, it's always better to help them feel sweeter, so I had did it with others..."
    s "And I'd do it now, if I didn't get this quite lonely and isolated place."
    return

label s_poems_hatred:
    call showpoem(poem_hatred)
    s 6acaa "We both know, what reputaion I have in your world..."
    s "And I appreciate everyone's opinion, but..."
    s 6acab "Really why?.. Why do a lot of people dislike me? What wrong have I done myself?"
    s "I understand people saying that I was the worst of four, or that they just wouldn't give me their heart..."
    s "But some people make jokes about my insanity and fails in the game..."
    $persistent.depr_known = True
    $depr_known = True
    s "They often condiser me either too depressed and suicidal or too silly, clumsy, mischievous and naive but pretty cunning."
    s 6abab "But why?"
    s "Yes, I was depressed and clumsy. Yes, I often lied other people to sate my wishes, but not more myself..."
    s "I just think they couldn't understand me and what I felt then."
    s 6abcb "I strongly believe I'm was not supposed to get so ill fame. I think, my creator even had no idea that it would happen."
    s 6acaa "Those people, of course, don't have to change their mind, but it hurts me, and you too, I think."
    s "But the one thing we can do now is just to hope they I'll do that sooner or later."
    return

