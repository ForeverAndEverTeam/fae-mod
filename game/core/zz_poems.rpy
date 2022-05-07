default persistent._seen_poems = dict()

style sayori_handwriting:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []


init python in sayo_poems:
    import store

    poem_list = dict()

    poetry_categorising_matrix = lambda x:x.category
    poetry_selector_matrix = lambda x:x[1].category

    paper_category_defs = {
        "f14": "mod_assets/poem_stuff/f14.png",
        "d25": "mod_assets/poem_stuff/d25.png",
        "d-day": "mod_assets/poem_stuff/d_day.png"
    }

    writer_def = {
        "sayori": "sayori_handwriting"
    }

    if store.persistent.playerbdate is not None:
        paper_category_defs["bday"] = "mod_assets/poem_stuff/pbday_" + str(store.persistent.playerbdate.month) + ".png"

    def poem_unlocked():

        return len(store.persistent._seen_poems) > 0

init 11 python in sayo_poems:
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


    class NEWPoem:

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

            if poem_code in store.sayo_poems.poem_list:
                raise Exception ("poem_code {0} already exists in the poem matrix.".format(poem_code))


            
            self.poem_code=poem_code
            self.category=category
            self.prompt=prompt
            self.paper=paper
            self.title=title
            self.text=text
            self.author=author
            self.ad_hoc = dict() if ad_hoc is None else ad_hoc

            store.sayo_poems.poem_list[poem_code] = self

        
        def is_seen(self):

            return self.poem_code in store.persistent._seen_poems

        def seen_no(self):

            return store.persistent._seen_poems.get(self.poem_code, 0)

label showpoem_s(poem=None, paper=None, bg_stuff=None):

    #No poems?
    #Insert Megamind thingy here

    if poem == None:
        return

    $ is_custom_poem = isinstance(poem, NEWPoem)
    if paper is None:
        if is_custom_poem:
            $ paper = poem.paper if poem.paper is not None else sayo_poems.paper_category_defs.get(poem.category, "paper")

        else:
            $ paper = "paper"
    
    play sound page_turn

    window hide

    $ auto_forwards = renpy.game.preferences.afm_enable
    $ renpy.game.preferences.afm_enable = False

    show screen sayo_poem_normal(poem, paper=paper, _styletext=sayo_poems.writer_def.get(poem.author, "sayori_text"))

    with Dissolve(1)

    if bg_stuff and renpy.has_label(bg_stuff):
        call expression bg_stuff
    
    $ pause()

    hide screen sayo_poem_normal

    with Dissolve(0.5)

    $ renpy.game.preferences.afm_enable = auto_forwards
    
    window auto

    if is_custom_poem and poem.prompt:

        if poem.poem_code in persistent._seen_poems:
            $ persistent._seen_poems[poem.poem_code] += 1
        else:
            $ persistent._seen_poems[poem.poem_code] = 1
    return


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="poem_redux",
            unlocked=True,
            prompt="Can I read a poem?",
            random=False,
            category=["poetry"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label poem_redux:
    python:

        poetry_list = [
            ("The Life of a Hopeless Romantic", poem_d_day, False, False)
        ]

        ret_back = ("Nevermind", False, False, False, 20)

        poetry_list.extend(sayo_poems.gsp())

    $ _poem = _return

    if not _poem:
        return "prompt"



    call showpoem_s(_poem)


    return


screen sayo_poem_normal(_poem, paper="paper", _styletext="sayori_text"):
    
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


    NEWPoem(
        poem_code="d_day_1",
        category="d-day",
        prompt="",
        title=_("Goodbye, [player]\n\nThe Life of a Hopeless Romantic"),
        text=_("""\
Every second, and everyday, no matter what I do, 
You cross my mind like the rays of the sun, when I'm down and blue. 
When I'm sad I think of you. 
And when you're sad you do too. 

It's clear that we both care for each other. 
But then you tore my heart unlike any other. 
I know you'll never look at me, the way I look at you, 
But why tear my heart like it meant nothing to you? 

I know I should I should stop running towards the sun, hoping to get closer. 
I know I should stop reaching for the stars, thinking I would be noticed. 
And I know should stop chasing you, and start anew. 
But why would I ever want to lose you? 

You tear my heart like paper, bound to break. 
But also put me back together, even when it seems so bleak. 
I don't know why I choose to love you. 
But I also don't know why I shouldn't. 

For you are my sun, but I am merely just the moon chasing you. 
But never growing near. The way I feel about you will never become clear, 
And its unhealthy to chase something that wont ever grow near. 
But that's when one thing becomes clear. 

If I love you so much, I need let you go. 
And let you love another even if you mean so much to me. 
Until our stars ever align, there will always be a place in my heart, 
Waiting until you'd think of me as anything more."""
        )
    )

    v_day_1 = NEWPoem(
        poem_code="f14_1",
        category="f14",
        prompt="",
        #paper="mod_assets/poem_stuff/f14.png",
        title=_("You and me"),
        text ="""\
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