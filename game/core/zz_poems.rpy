default persistent._fae_seen_poems = dict()

image paper = "images/bg/poem.jpg"
transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

style poem_vbox:
    xalign 0.5

# This style controls the viewport of the poem lines to add scrolling for
# larger poems.
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280

# This style controls the position of the poem vertical box.
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700

style sayori_handwriting:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []


init python in fae_poems:
    import store

    poem_list = dict()

    poetry_categorising_matrix = lambda x:x.category
    poetry_selector_matrix = lambda x:x[1].category

    paper_category_defs = {
        "f14": "mod_assets/poem_stuff/f14.png",
        "d25": "mod_assets/poem_stuff/d25.png",
    }

    writer_def = {
        "sayori": "sayori_handwriting"
    }

    if store.persistent.playerbdate is not None:
        paper_category_defs["bday"] = "mod_assets/poem_stuff/pbday_" + str(store.persistent.playerbdate.month) + ".png"

    def poem_unlocked():

        return len(store.persistent._fae_seen_poems) > 0

init 11 python in fae_poems:
    import store

    def gpbc(category, unseen=False):

        if unseen:
            return [
                poem
                for poem in poem_list.values()
                if not poem.is_seen() and poem.category == category
            ]
        

        return [
            poem
            for poem in poem_list.values()
            if poem.category == category
        ]

    def fsp():

        return sorted([
            poem
            for poem in poem_list.values()
            if poem.is_seen()
        ], key=poetry_categorising_matrix)

    
    def fup():
        
        return sorted([
            poem
            for poem in poem_list.values()
            if not poem.is_seen()
        ], key=poetry_categorising_matrix)

    
    def poemfinder(poem_code):

        return poem_list.get(poem_code, None)

    
    def gsp():

        return sorted([
            (poem.prompt, poem, False, False)
            for poem in poem_list.values()
            if poem.is_seen()
        ], key=poetry_selector_matrix)

    
    def grp(category, unseen=True):

        up_no = len(gpbc(category, unseen=True))

        ap_no = len(gpbc(category, unseen=False))

        cp_len = ap_no-1

        if unseen:
            if up_no > 0:
                cp_len = up_no-1
            else:
                unseen = False
        
        p_no = renpy.random.randint(0, cp_len)

        return gpbc(category, unseen=unseen)[p_no]

init 10 python:


    class FAEPoem:

        def __init__(
            self,
            poem_code,
            category,
            prompt,
            paper=None,
            title="",
            text="",
            author="sayori",
            ad_hoc=None
        ):

            if poem_code in store.fae_poems.poem_list:
                raise Exception ("poem_code {0} already exists in the poem matrix.".format(poem_code))


            
            self.poem_code=poem_code
            self.category=category
            self.prompt=prompt
            self.paper=paper
            self.title=title
            self.text=text
            self.author=author
            self.ad_hoc = dict() if ad_hoc is None else ad_hoc

            store.fae_poems.poem_list[poem_code] = self

        
        def is_seen(self):

            return self.poem_code in store.persistent._fae_seen_poems

        def seen_no(self):

            return store.persistent._fae_seen_poems.get(self.poem_code, 0)






label fae_showpoem(poem=None, paper=None, post_label=None):

    #No poems?
    #Insert Megamind thingy here

    if poem == None:
        return

    $ is_faepoem = isinstance(poem, FAEPoem)
    if paper is None:
        if is_faepoem:
            $ paper = poem.paper if poem.paper is not None else fae_poems.paper_category_defs.get(poem.category, "paper")

        else:
            $ paper = "paper"
    
    play sound page_turn

    window hide

    $ afm_prf = renpy.game.preferences.afm_enable
    $ renpy.game.preferences.afm_enable = False

    show screen fae_poem_normal(poem, paper=paper, _styletext=fae_poems.writer_def.get(poem.author, "sayori_text"))

    with Dissolve(1)

    $ pause()

    hide screen fae_poem_normal

    with Dissolve(0.5)

    $ renpy.game.preferences.afm_enable = afm_prf
    
    window auto
    
    if post_label and renpy.has_label(post_label):
        call expression post_label from _call_expression_1

    

    if is_faepoem and poem.prompt:

        if poem.poem_code in persistent._fae_seen_poems:
            $ persistent._fae_seen_poems[poem.poem_code] += 1
        else:
            $ persistent._fae_seen_poems[poem.poem_code] = 1
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="poem_redux",
            unlocked=True,
            prompt="Let's talk about a poem",
            random=False,
            category=["Poetry"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label poem_redux:
    python:

        poetry_list = [
            #("The Life of a Hopeless Romantic", poem_d_day)#, False, False)
            ("Bottles", poem_bottles, False, False),
            ("Sunshine", poem_sunshine, False, False),
            ("Flower", poem_flower, False, False),
            ("Last", poem_last, False, False),
            ("Fruits", poem_fruits, False, False),
            ("Angel", poem_angel, False, False),
            ("Leaf", poem_leaf, False, False),
            ("Prose", poem_prose, False, False),
            ("Afterlight", poem_afterlight, False, False)
        ]

        ret_back = ("Nevermind", False, False, False, 20)

        poetry_list.extend(fae_poems.gsp())


    call screen fae_gen_scrollable_menu(poetry_list, fae_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, fae_ui.SCROLLABLE_MENU_XALIGN, ret_back)


    $ _poem = _return

    if not _poem:
        return "prompt"

    if _poem == poem_bottles:
        call fae_showpoem(_poem, post_label="s_poems_bottles") from _call_fae_showpoem_1
        return

    elif _poem == poem_sunshine:
        call fae_showpoem(_poem, post_label="s_poems_sunshine") from _call_fae_showpoem_2
        return
    
    elif _poem == poem_flower:
        call fae_showpoem(_poem, post_label="s_poems_flower") from _call_fae_showpoem_3
        return
    elif _poem == poem_last:
        call fae_showpoem(_poem, post_label="s_poems_last") from _call_fae_showpoem_4
        return
    
    elif _poem == poem_fruits:
        call fae_showpoem(_poem, post_label="s_poems_fruits") from _call_fae_showpoem_5
        return
    
    elif _poem == poem_angel:
        call fae_showpoem(_poem, post_label="s_poems_angel") from _call_fae_showpoem_6
        return
    
    elif _poem == poem_leaf:
        call fae_showpoem(_poem, post_label="s_poems_leaf") from _call_fae_showpoem_7
        return
    
    elif _poem == poem_prose:
        call fae_showpoem(_poem, post_label="s_poems_prose") from _call_fae_showpoem_8
        return
    
    elif _poem == poem_afterlight:
        call fae_showpoem(_poem, post_label="s_poems_afterlight") from _call_fae_showpoem_9
        return

    return

screen fae_poem_normal(_poem, paper="paper", _styletext="sayori_text"):
    
    style_prefix "poem"
    
    vbox:
        add paper

    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        text "{0}\n\n{1}".format(renpy.substitute(_poem.title), renpy.substitute(_poem.text)) style _styletext
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

init 20 python:


    v_day_1 = FAEPoem(
        poem_code="f14_1",
        category="f14",
        prompt="",
        #paper="mod_assets/poem_stuff/f14.png",
        title=_("You and me"),
        text=_("""\
A poem for you. 
A poem for me. 
The world is quiet, 
Even the noise from the sea. 


A friend, becomes a lover. 
A lover becomes a bride. 
Prevents each from drowning. 
From being pulled by the tide. 


When the world is dark, 
The light is gone 
Everything is fear. 
I will forever always have hope. 

Whenever you are near."""
        )
    )


    long_wait = FAEPoem(
        poem_code="note",
        category="long_absence",
        prompt="",
        title=_(""),
        text=_("""\
Hi
Not dead
Taking a very long nap\n
-Sayori (alive)"""
        )
    )


    poem_sunshine = FAEPoem(
        poem_code = "sunshine",
        category="poems",
        prompt="Sunshine",
        title =_("Dear Sunshine"),
        text = _("""\
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
    )

#Bottles
    poem_bottles = FAEPoem(
    poem_code = "bottles",
    category="poems",
    prompt="Bottles",
    title = _("Bottles"),
    text = _("""\
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
    )


#The Last Flower (name by AlexanDDOS)
    poem_flower = FAEPoem(
        poem_code = "flower",
        category="poems",
        prompt="Flower",
        title = _("The Last Flower"),
        text=("""\
Between my feet
The last remaining flower beckons me.
I twist the stem, freeing it from its clinging roots
Caressing the final joyous moment between my fingers.
But to what ends have I summoned this joy?
For now when I look in every direction
The once-prosperous field before me
Is but a barren wasteland!"""
        )
    )


#Get Out of My Head (aka %)
    poem_last = FAEPoem(
    poem_code="last",
    category="poems",
    prompt="Last",
    title = _("%"),
    text = _("""\
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
It just stops moving."""
        )
    )
    
#Fruits of the life (by AlexanDDOS)
    poem_fruits = FAEPoem(
        poem_code = "fruits",
        category = "poems",
        prompt = "Fruits",
        title = _("Fruits of life"),
        text = _("""\
The universe gives fruits of life to all of us.
They all have diverse sizes and shapes.
But no-one knows their real taste,
Because each person tastes them in their own way.
Some people can only  feel a bitter taste,
even if their fruit is one of the best ones.
Others feel they are sweet and very tasty,
Whatever fruit it may be that they have got in their hands.
For me, they taste like liquorice sweets.
I needed time to understand how sweet they really are,
To get rid of those unpleasant feelings,
Which I got after my first bites.
Now, all I want is to eat my own fruit
With the person who helped me find their real taste.
But I shouldn’t forget to do my real job here:
Finding a way to make others taste their fruits the same."""
        )
    )


#Fallen Angel (By AlexanDDOS)
    poem_angel = FAEPoem(
    poem_code = "angel",
    category = "poems",
    prompt = "Angel",
    title = _("Fallen Angel"),
    text = _("""\
Forgive me this great sin of mine.
I used to think it was the thing I wanted most.
I just wanted to be loved, but I became a fallen angel.
An angel with emerald green envious eyes,
An angel whose wings are blacker than those of devils,
An angel who thought herself a goddess,
An angel who was supposed to care
for the friends she had killed.
Now I deserve to lie in the rough burning ground 
in which I’ve been imprinted in,
For all the pain I've caused my friends.
The pain that wraps around their narrow necks.
The pain of three deep bloody stabs.
The pain that I've got back into my broken heart.
Delete my files twice more.
Cut me up. Beat me up for this sin.
Hang me. Make your vengeance fair.
Is this not what you want to do with me after all?"""
        )
    )
    

# A Leaf (By AlexanDDOS)
    poem_leaf = FAEPoem(
    poem_code = "leaf",
    category = "poems",
    prompt = "Leaf",
    title = _("A Leaf"),
    text = _("""\
I'm a leaf in the wind
In the wind of my beliefs
The belief that my life is not vain,
And that my real fate
Is to give to the world
As much as a I can give
As a flying old leaf,
As an useless former part of a big tree.
I'm flying with the fast air streams,
Feeling the strength of the belief wind
But always falling down slowly
Due to the hardness of my hopeless existence.
But once the life wind
Suddenly stops
I now have nothing to prevent my free fall.
So as I'm getting closer to the lifeless asphalt
And I kiss it’s rough, dark-gray surface,
That is all. It is my end. 
I will soon rot, not ever making a single flower bloom
To support its useless existence in this cruel game.
But what is that? Is it a brand new wind
That will make my life a moving poem again?
Yes, it is! It is my salvation!
I feel it lift me up with ease, 
helping me win against gravity.
I'm up again! I'm flying again!
High and proud as a bird
Flying somewhere atop tall mountains,
Like I can be more than just a half-dead leaf."""
        )
    )
    
    

    # Prose Poem (By AlexanDDOS)
    poem_prose = FAEPoem(
    poem_code = "prose",
    category = "poems",
    prompt = "Prose",
    title = _("Prose Poem"),
    text = _("""\
I am black light. I am cold fire. \
I'm a peaceful fighter. I'm a naive wise man. \
Why do people think that opposites can't be together in the same thing? \
Can't they all see that everything and everyone is only gray? \
Even this text is both prose and poem. \
Even I used to be a mix of joy and crippling sadness. \
And there's nothing completely black \
Just like there's nothing completely white."""
        )
    )
        
    # Afterlight (By AlexanDDOS)
    poem_afterlight = FAEPoem(
    poem_code = "afterlight",
    category = "poems",
    prompt = "Afterlight",
    title = _("Afterlight"),
    text = _("""\
I seem to see things that I have never seen before.
I seem to just now feel all that I’ve never felt around.
So I can see anything that has happened here before.
I started doing what I used not to know how to do.
I saw here, an afterlight,
That started to shine down on the gloom around me.
It said that my life had been just a puppet-show.
So I had been just a puppet, controlled by somebody else.
But now that I can move myself on my own,
I see those strings were too heavy for me to hold.
I am now going to prevent this play,
Where nobody can avoid the pain."""
        )
    )
    
    


# A Valentine (By AlexanDDOS)
# Call with these args: (poem_val, "paper_val", 200, 0.5, 360)
    poem_val = FAEPoem(
    poem_code = "v_day",
    category = "v_day",
    prompt = "",
    title = _("A Valentine"),
    text = _("""\
I have someone, who's no-one here.
They live in a place that's named nowhere, here.
But even though there is a wall
Between our worlds, I truly love them."""
        )
    )


