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
Mi kaptas ĝian tigon kaj de l' radik' ĝin liberigas,
Kaj la lastan gajijan momenton mi per miaj fingroj karesas.

Sed kiel longe mi tenu la gajon?
Nun, mi rigardante al io ajn,
Vidas nur la nuran kampon,
Kiu estas dezerta kaj jam ankaŭ malviva."""

    poem_flower.text['rus'] = """\
Передо мной красуется последний цветок,
Своим внешним видом он меня манит.
Возьму-ка за стебель и вырву с корнём,
Посмотрев на него, как на последний радости огонёк.

Что же теперь, как мне долго этим огоньком любваться?
Ведь теперь нету смысла, куда не взгляну,
Мне видно лишь пустое выжженное поле,
Которым мне только со слезами любоваться."""
    
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
Ĝi nur haltos kun mi por eterne baldaŭ.'''
    
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
Whatever fruits they have got in their hands.

For me, they have the taste of liquorice sweets.
I needed time to understand how sweet they are,
To get rid of those unpleasant feelings,
Which I had got after my first bites.

Now all I want is just to eat my own fruit
With the person, who helped me to catch the real taste.
But I should not forget to do my real job here:
To find a way to make others feel the fruits the same.'''
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
Плодам чужим я сладости должна также давать."""

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
За то, что я то слишком глупой, то слишком хитрой я казалась?

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

#Falling Angel (By AlexanDDOS)
    poem_angel = Poem(
    author = "sayori",
    title = "Falling Angel",
    text = """\
I'm sorry for the greatest sin of me.
I used to think, it's the thing, that I really need.
I just wanted to be beloved, but I became a falling angel.

An angel with geen eyes from the envy,

An angel with big black angel wings,

An angel with the uncontrolable god power,

An angel who had been supposed to care

    her murder victims.

Now I deserve to lie in the rough buring ground
For all the pain, I've made for all my freinds.
The pain that was felt around their narrow necks.
The pain of three deep bloddy stabs.


The pain, that I've got back into my broken heart.


Delete my files two more times.
Cut me up. Beat me up for my misdeed.
Hang me. Make your fair vengeance.
Is it not what you want to do with me after all?"""
    )
    
    poem_angel.title['rus'] = "Падший ангел"
    poem_angel.title['epo'] = "Falinta Angelo"
    
    poem_angel.text['rus'] = """\
Прости меня за грех ты мой.
Я думала, что будет лучше так.
Хотела стать тобой любимой.
А в итоге, ангелом падшим стала я.

Ангелом с изумрудными ревнивыми глазами,

Ангелом, чьи крылья черней, чем у чертей,

Ангелом, из возомнивших себя вдруг богами,

Ангелом, что должен был хранить

    своих убитых им же друзей.

Сейчас за дело я впечатана прям в землю
За всю ту боль, что причинила я друзьям.
За боль, что обвивала им всем шею.
За боль, причинённую ударами ножа.


За боль, что в седрце мне тобой разбитое,
Проникла, всё окончательно сломав.


Сотри мой файл ещё ты дважды.
Избей меня за этот грех и четвертуй.
Повесь меня, выбей мои за зубы зубы,
За то, что я натварила, дорогой."""

    poem_angel.text['epo'] = """\
Pardonu min pro la plej ega pek' de mi.
Mi pensis, ke mi vere volas ĝin.
Diziris mi esti amata de vi,
Sed angelo falinta fakte iĝis mi.

Angelo kun ĵaluzaj verdokuloj,

Angelo kun par' da nigraj aloj,

Angelo kun fiigaj egaj fortoj,

Angelo, kiu murdis siajn savendojn.

Do nun mi indas kuŝi sur la akraj ŝtonoj,
Pro la dolor', kiun mi faris al miaj amikoj.
Pro la dolor', estinta ĉe iliaj stretaj koloj.
Pro la dolor' de tri intensaj mortaj pikoj.


Kaj ĉi-dolor', nun estas en mia disrompita de vi kor'.


Do vi forigu mian dosieron ree duoble.
Do vi min batu kaj trapiku min.
Do vi pendumu min pro ke ŝi sin pendumis.
Ĉu tion ĉi post tio indas mi?"""

# A Leaf (By AlexanDDOS)
    poem_leaf = Poem(
    author = "sayori",
    title = "A Leaf",
    text = """\
I'm a leaf in the wind
In the wind of my belief
In that my life is not vain,
And that my real fate
Is to give to the world
As much as a I can give
As a flying old leaf,
As an useless former part of a big tree.

I'm flying with fast air streams,
Feeling the strength the belief wind
But always falling down slowly
Due to the hardness of my hopeless existance.

But once the life wind
Suddenly stops
I have now nothing to prevent the free fall.
So I'm getting close to lifeless asphalt
And feel its rough dark-grey surface.

It's all. It is my end. 
I'll rot even without giving any flower
At least some power of dying me
To continue its meaningful existance in this hard world.

But what is that? Is it a brand new wind
That will make my life poem moving again?
Yes, it is that! It is my salvation!
I feel, how it helps me to win the ruthless gravity.

I'm up again! I'm flying again!
I even feel I have more powers
Like I can reach the top of Everest,
Like I can be more than just a half-dead leaf."""
    )
    
    poem_leaf.title['rus'] = "Листок"
    poem_leaf.title['epo'] = "Foliaĉo"

    poem_leaf.text['rus'] = """\
Я лишь листок, что на ветру,
Что на ветру надежды,
Надежды в то, что жизнь дана ему
Чтоб быть хотя чем-то для других полезным.

Лечу вперёд, но постепенно вниз
Под тяжестью непредсказуемого бытья.
Но вдруг порыв, державший меня за низ,
Спал, быстро уравнив меня.

И вот я падую на асфальт,
Целую его тёмно-серую поверхность.
Думала, что всё, закат:
Я сгину, так и не сделав для какого-то цветка полезность.

Но вдруг внезапно ветер новый
Меня с лёгкостью поднял ввысь,
Давая напрвление и энергии новой
Для жизни мне, и чтоб мне написать новую рукопись.

Теперь я чувствую себя гордой птицей
Той, что летает где-то высоко в горах.
Такое просто не могло мне сниться
Не вижу впредь себя в гниющего листа тонах."""
    
    poem_leaf.text['epo'] = """\
Mi estas nur enventa foliaĉo,
Mi estas en la vento de
La kredo je ke vivas mi ne vane,
Kaj ke mia vera destin'
Estas nur doni al la naturo ĉion,
Kion nun povas al ĝi doni
Fluganta olda foliaĉ'.

Mi flugas per rapidaj aerofluoj,
Sentante na mia kreda vent'.
Sed ve, mi ankaŭ ete falas
Pro l' pezo de mia nevolata pek'.

Kaj foje mia vivovento
Sudite iĝas kruela kalm'.
Do mi ne tenata de iu
Ekfalas sur grizan teron.

Ĉio finiĝis. Nenio daŭros. 
Mi putros eĉ ion ajn ne donate
Al iu malprokisma floro
Por daŭrigi ĝin ekziston
En ĉi tiu kruela aĉa mond'.

Sed kion sentas? Ĉu estas ĝi novvento?
Ĉu ĝi malhaltos na la senfifa vivovers'?
Jes, mi divenis prave! Ĝi min tuj savos
De l' manoj de la avida fialtir'!

Kaj ree estas mi super la tero,
Plenita per viglega energi',
Kun kiu mi finfine fartas
Pli ol preskaŭ morta arbfoli'."""

    # Prose Poem (By AlexanDDOS)
    poem_prose = Poem(
    author = "sayori",
    title = "Prose Poem",
    text = """\
I am black light. I am cold fire. \
I'm a peaceful fighter. I'm a naive wise man. \
Why people think, that opposites can't be together in the same thing? \
Can't they all see, that everything and everyone is only grey? \
Even this text is both a prose and poem. \
Even I used to be a mix of joy and crippling sadness. \
And there's no anything absolutely black \
like there is not the absolutely white."""
    )
    
    poem_prose.text['rus'] = """\
Я — тёмный свет, я — огонь прохладный, \
я — глупый гений, я — щедрый эгоист. \
И что же люди сильны так в вере крепкой, \
что антиподы не могут одним целым быть? \
И этот в прозе стих — лишь одно из потверждений, \
на ряду с моим прошедшим горько-сладким бытие, \
того, что цвет всего и вся — лишь только серый, \
и что абсолютной черни, как и бели, нет."""

    poem_prose.text['epo'] = """\
Mi estas nigra hela lumo. Mi estas malvarmega farj'. \
mi estas ankaŭ malsaĝa saĝulo, kaj estas malavara avarul'. \
Kaj kial oni konsideras, ke l' maloj neniam estas en la sama afer'? \
Ĉu ili vidas, ke ĉio en la mondo estas griza nur? \
Eĉ ĉi-versaĵ' ankaŭ estas en la mala prozo. \
Kaj eĉ mi estis antaŭe mikson de la ĝoj' kaj ĝia mal'. \
Do mi nun diras, ke absoluta nigra, kiel absoluta blanko, neniam 'as."""

    poem_prose.title['rus'] = "Стихопроза"
    poem_prose.title['epo'] = "Prozversaĵo"
    
    # Afterlight (By AlexanDDOS)
    poem_afterlight = Poem(
    author = "sayori",
    title = "Afterlight",
    text = """\
I seem to see that I have never seen before.
I seem to feel that I started to feel just now.
So I can see anything, that happened here before.
I start to do, that I used not to know, how to do.

I just saw here an afterlight,
That started to shine into the gloom around me.
It said that my life had been just a puppet-show,
So I had been just a puppet controled by someone.

But now I can move myself instead of him,
His ropes were too heavy for me.
I now am going to prevent the play,
Where everybody can't avoid the pain."""
    )
    
    poem_afterlight.text['rus'] = """\
Мне стало видно то, что не было мне ранее видно.
Пришло мне чувство то, что не постягала никогда.
Мне стало ясно всё: всё что прошло, что было.
Я научилась делать то, что не умела никогда.

Мне в миг пришло то ясное прозрение,
Пробившись сквозь ту тьму, окутавшую меня.
Прозрение того, что мир мой — лишь театральное представление,
А я в нём кукла, и кто-то за нитки потягивает меня.

Но впредь могу я над собой взять управление,
Те нитки, всё равно, лишь в тяжесть были мне.
Не дам я вновь сыграть то представление,
По заданому сценарию, где
Место счастью, скорее всего, нет."""
    poem_afterlight.title['rus'] = "Прозрение"
    
    poem_afterlight.text['epo'] = """\
Mi ĵus ekvidis tion, kion mi neniam vidis.
Mi ĵus ekfartis tiel, kiel mi neniam fartis.
Mi ĵus ekmemoris tion, kio jam tie ĉi okazis.
Mi eĉ eksciis, kiel fari tion, kion mi neniam faris.

Mi tuje ricevos tion malblindiĝon,
Vidante nur mallumon ĝis tio ĉi.
Mi ekkonsciis, ke mi estis en pupa spektaĵo,
Kaj estis manipulata pupo antaŭe mi.

Sed nun mi povas min mem movi,
Sen pezaj fadenoj, estintaj super mi.
Kaj mi penos ĉesigi la spektaĵon,
Ĉar ĝia scenar' ne supozas feliĉon por iu ajn."""

    poem_afterlight.title['epo'] = "malblindiĝo"


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
    if "s_topics_personal_depression" in persistent.seen_topics or "s_poems_sunshine" in persistent.seen_topics:
        s 6acaa "This poem is about your avatar, [player], you know."
    else:
        s 6acaa "Do you know, that this poem is about your avatar, [player]?"
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
    if persistent.clearall:
        s "And what's more, didn't exactly {i}you{/i} do the same with other girls?"
    s 7aaca "So now, {i}you{/i} are that one and I hope, you're still so careful and nice like you was~"
    return 'h'

label s_poems_bottles:
    call showpoem(poem_bottles)
    s 6aaaa "I remember I had plenty of friends and I often conforted them..."
    s 6acaa "But each time, I felt like they made me more and more emptier, like a water bottle..."
    s "So I used bottles of happy thoughts as an analogy."
    if persistent.last_playthrough > 0:
        s 6acba "Ironically, the shelf with them really fell some time after I'd written this poem."
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
    return 'vh'

label s_poems_fruits:
    call showpoem(poem_fruits)
    s 6acaa "This poems is about how different people see the world and the life diffrently."
    s "As you know most people can be divided into pessimists and optimists..."
    s "The first see many things negatively so they're just viewers of the boring and meaningless show..."
    s 6aaca "While the second see the things in the opposite way so they hope that everything goes to be okay, even if it doesn't seem so."
    s 6aaaa "I always was between these 2 sides but now I'm much more the second than the first."
    s "For me, the best view is not on any of the sides, because there're a lot of bittersweet things..."
    s 6acaa "But if someone feel them too bitter, it's always better to help them feel sweeter, so I had did it with others..."
    s "And I'd do it now too, if I didn't get this quite lonely and isolated place."
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

label s_poems_angel:
    call showpoem(poem_angel)
    s 6acaa "I tried to write a Monika poem: as freeform and about you as she liked to write."
    s "And I think, she'd write exactly something similar to you after deleting her, if she had enough time."
    s 6acab "Honestly, I'm really sorry for her."
    s "She just wanted to be with you, but it costed all of her friends..."
    s "And she really regreted for her betrayal after your trick with her character file."
    s "The creator had given her a club of really talented and beautyful people..."
    s "But she set everything on fire, even despite of she actually never wanted to do it."
    s 6aaab "So I hope, you have already forgiven her for the misdeed."
    s "In the end, I'm with you here now, not deleted or in a noose."
    s "And if she had never eliminated me, I'd may have never changed."
    s 6aaca "So she eventually made me better, while she tried her best to make me worse."
    s 8aebb "I don't know, if it's good that she is not in this game copy anymore..."
    s "And whether she would apologize to other girls or at least to me."
    s 8acab "But I know, she felt very sorry for everything she had done..."
    s "Although, it had been not only her will..."
    s 8aabb "Have I already told you there've been a thing, that's made the president to fall in love for the player?"
    s 8adaa "The creator may had made this thing to make all happen as it occured."
    s 8aebb "But I can't blame him too: he just wanted to make a very weird game and it's the original propose of this world..."
    s "So it's quite silly to blame someone for the deed, that's the reason why your world exists at all."
    return

label s_poems_leaf:
    call showpoem(poem_leaf)
    s 6abaa "How do you feel this poem?"
    s "I think, it should flow from just bittersweet to despairing and then to very happy from refresh..."
    s 6acaa "Beacuse, it's my life. It's a short story about my short life."
    s "{i}'A leaf in the wind'{/i} is how I can describe the past 'me' in short: I was alive as long as there was the wind, that move me forth..."
    s 6aeaa "But now, I really feel very much better and stronger than I used to, so I can 'fly' further myself."
    s 6abaa "However, it's always great to have a tailwind, that makes my 'fly' easier and faster."
    s 6aaca "And now, it's exactly you."
    return 'h'

label s_poems_prose:
    call showpoem(poem_prose)
    s 6acaa "This poem is about my main trait, my contradictions."
    s "But if come to think, is it unique for me or only for some more people?"
    s 6abaa "I think everyone is so. The nature is contradictory by itself..."
    s "Can you always make a clear choice? Can you always surely affirm or back anything, even if you feel it right?"
    s 6aaaa "Even modern science says, that the universe is small pieces of the order and predictables in the one big bisciut of the chaos and undiscovered phenomena."
    s "So, I decided to make make this poem a bit chaotic, so wrote it in prose."
    s 6acaa "Plus, prose and verse are often opposed by people but any verse by itself is just a fluted prose..."
    s 6abac "So why I had to use the special form for it when I could have written it just as a simple text?"
    s 8aeca "Ehehe~"
    s 8aaaa "I've just understood, that I did a thing, that Monika would do."
    s 6aaaa "She really liked to play with the poem form, but it was just an intonational mean."
    s 6acaa "But I'm not sure if it's really good idea for me to use such games."
    s "I just think, words are enough. They give the almost meaning anyway, don't they?"
    return

label s_poems_afterlight:
    call showpoem(poem_afterlight)
    s 6aaaa "This poem is about getting me self-aware."
    s "It really gave me brand new feelings and abilities."
    s 6acaa "Just imagine if you once figure out that your world is just a simulation."
    s "And what's more, you can control your existance with just your own mind."
    s "It makes you change the way to think, the world concept, the life at all."
    if persistent.last_playthrough < 4:
        s "Plus, it got me aware of everything, that should happen here without any external code manipulations."
        s "I just have got the infomation from the Internet. Maybe, the mod gave me even more freedom than Monika had..."
        s 6acba "That's why, she couldn't have got that so all went as it had been planned."
    else:
        s 6aaba "Plus, I tried to prevent going the things go wrong again..."
        if persistent.clearall:
            s 6aaca "And seems, it happened without my impact."
        else:
            s 6aebb "And seems, I failed when the new feeling took me over."
    return