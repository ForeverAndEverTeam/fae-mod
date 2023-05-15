
init 1 python in fae_poems:

    class Author(object):
        """
        A class used to default values of a `Poem` instance.

        `name`: str
            The auhtor's name
        
        See the `Poem` class for more information.
        """

        def __init__(self, name, style=True, paper="images/bg/poem.jpg", separate_title_from_text=True, music=None):
            self.name = name
            self.style = style
            self.paper = paper
            self.separate_title_from_text = separate_title_from_text
            self.music = music
    
    author_s = Author("sayori")

    class Poem(renpy.text.text.Text):
        """
        `author`: str | Author
            The author (no way!!!) of the poem. Either a string or an `Author` instance, and if it's the case,
            the `style`, `paper`, `separate_title_from_text` and `music` arguments are set to the object's respectives attributes
            if no value was passed, after what `author` will take `author.name`.
        
        `text`: str
            The text to be displayed.
        
        `title`: str
            The title of the poem.
        
        `style`: bool | str
            Either the name of a style as string or a boolean.
            If passed as `False`, will take `"default"`.
            If passed as `True`:
                Will first take `author.style` if `author` is an instance of `Author`.
                Then, if author isn't an empty string, will take `author + "_text"`, or take `"default"` otherwise.
            
        `paper`: renpy.Displayable | None
            A displayable to use as background. If `None` is passed, a `Null` is created.
        
        `separate_title_from_text`: bool
            If true and that the title isn't an empty string, will add 2 newlines after the title.
        
        `music`: str | None
            A music to be played when showing the poem.
        
        Additionnal text properties can be passed as keyword arguments.
        """

        def __init__(self, author, text, title="", style=True, paper=None, separate_title_from_text=False, music=None, **properties):
            if isinstance(author, Author):
                paper = paper or author.paper
                separate_title_from_text = separate_title_from_text or author.separate_title_from_text
                music = music or author.music

                if style is True:
                    style = author.style

                author = author.name
                
            for t in (author, title, text):
                if not isinstance(t, basestring):
                    raise TypeError("'author', 'title' and 'text' must all be strings.\n(if 'author' is an instance of 'Author', 'author.name' must be a string)")

            if style is True:
                if author:
                    style = author + "_text"
                else:
                    style = "default"

            elif style is False:
                style = "default"

            poem = title + ("\n\n" + text if separate_title_from_text and title else text)

            super(Poem, self).__init__(poem, style=style, **properties)
            
            self.author = author
            self.paper = renpy.easy.displayable_or_none(paper) or Null()
            self.music = music
    
    def format_music_string(music, pos=0):
        """
        Given a filename `music` and a position `pos`, returns a string that will make the music start from `pos`,
        replacing the previous `from XXX` should it be found in `music`.

        3 possible cases:
        ```
        format_music_string("music/song_1.ogg", 3.0)
        >>> "<from 3.0>music/song_1.ogg"

        format_music_string("<loop 4.0 to 26.55>music/song_1.ogg", 3.0)
        >>> "<from 3.0 loop 4.0 to 26.55>music/song_1.ogg"

        format_music_string("<loop 80 from 69>music/song_1.ogg", 3.0)
        >>> "<loop 80 from 3.0>music/song_1.ogg"
        ```
        """
        if re.match(r"^<.*?>", music): # if the string looks like "<...>music/song_1.ogg"
            PATTERN = re.compile(r"from( *)((\d+\.\d*)|(\d+)|(\.\d+))") # "<from 0.0>..." or "<from 0.>..." or "<from 0>..." or "<from .0>..." 
            info, gt, path = music.partition(">")

            if PATTERN.search(info):
                info = PATTERN.sub("from {}".format(pos), info)
                music = info + gt + path
            else:
                music = "<from {} {}".format(pos, music[1:])
        else:
            music = "<from {}>{}".format(pos, music)

        return music

    def show_poem(poem, paper_sound=audio.page_turn, music=True, from_current=True, revert_music=True):
        """
        Call this function to show a poem from a label.

        `poem`: Poem | None
            The poem to show. If for some reason `None` is used, the function will return.
        
        `paper_sound`: str | None
            If not `None`, a sound to be played when showing the poem.

        `music`: str | bool
            A music to be played. If passed as `True`, `poem.music` is used.
            If no music was found or that it was passed as `False`, plays nothing.
        
        The following parameters assume the `music` channel is used.
        
        `from_current`: bool
            If true and that a music has been found, will play that music from the position of the music currently playing.
        
        `revert_music`: bool
            If true and that a music has been played, will play the music used before showing the poem. If `from_current`,
            will play from the current position (does nothing is no music was used previously).
        """
        if poem is None:
            return
        
        if not isinstance(poem, Poem):
            raise TypeError(f"poem must be a Poem instance, not {type(poem).__name__}")
    
        if paper_sound is not None:
            renpy.sound.play(paper_sound)

        _window_hide()

        if music is True:
            music = poem.music

        if music:
            previous_music = renpy.music.get_playing()
            music = format_music_string(music, get_pos()) if from_current else music
            renpy.music.play(music, "music_poem", loop=True, fadein=2.0)
            renpy.music.stop(fadeout=2.0)
        
        allow_skipping = config.allow_skipping
        config.allow_skipping = False
        skipping = store._skipping
        store._skipping = False

        renpy.transition(dissolve)
        renpy.show_screen("poem", poem)
        pause()
        renpy.hide_screen("poem")
        renpy.transition(dissolve)

        if not persistent.first_poem:
            persistent.first_poem = True

        config.allow_skipping = allow_skipping
        store._skipping = skipping
        
        if music and revert_music:
            if previous_music:
                previous_music = format_music_string(previous_music, get_pos("music_poem")) if from_current else previous_music
                renpy.music.play(previous_music, loop=True, fadein=2.0)

            renpy.music.stop("music_poem", fadeout=2.0)
        
        store._window_auto = True


    #TODO: MAKE SCREEN AND STUFF

    # These variables declare each poem for the characters' in the game for
    # the poem sharing mini-game.

    long_wait = Poem(
        author_s,
        title=_(""),
        text=_("""\
Hi
Not dead
Taking a very long nap\n
-Sayori (alive)"""
        )
    )


    poem_sunshine = Poem(
        author_s,
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
    poem_bottles = Poem(
        author_s,
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
    poem_flower = Poem(
        author_s,
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
    poem_last = Poem(
        author_s,
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
    poem_fruits = Poem(
        author_s,
        title = _("Fruits of life"),
        text = _("""\
The universe gives fruits of life to all of us.
They all have diverse sizes and shapes.
But no-one knows their real taste,
Because each person tastes them in their own way.
Some people can only feel a bitter taste,
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
    poem_angel = Poem(
        author_s,
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
    poem_leaf = Poem(
        author_s,
        title = _("A Leaf"),
        text = _("""\
I'm a leaf in the wind
In the wind of my beliefs
The belief that my life is not vain,
And that my real fate
Is to give to the world
As much as I can give
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
    poem_prose = Poem(
        author_s,
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
    poem_afterlight = Poem(
        author_s,
        title = _("Afterlight"),
        text = _("""\
I seem to see things that I have never seen before.
I seem to just now feel all that I’ve never felt around.
So I can see anything that has happened here before.
I started doing what I used to not know how to do.
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
    poem_val = Poem(
        author_s,
        title = _("A Valentine"),
        text = _("""\
I have someone, who's no-one here.
They live in a place that's named nowhere, here.
But even though there is a wall
Between our worlds, I truly love them."""
        )
    )



    
screen poem(poem):
    style_prefix "poem"

    fixed:

        frame:
            style "poem_paper"

            add poem.paper:
                subpixel True align (0.5, 0.5)

        frame:
            background None
            
            hbox:
                viewport id "poem_vp":
                    draggable True
                    mousewheel True

                    add poem

                vbar value YScrollValue("poem_vp")
        
    if not persistent.first_poem:
        add "gui/poem_dismiss.png" xpos 1050 ypos 590
    
    key ["repeat_K_UP", "K_UP"] action Scroll("poem_vp", "vertical decrease", 20)
    key ["repeat_K_DOWN", "K_DOWN"] action Scroll("poem_vp", "vertical increase", 20)

    on "show" action SetVariable("poem_last_author", poem.author)

style poem_vscrollbar:
    xsize 20
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style poem_paper:
    modal True
    align (0.5, 0.5)

style poem_fixed:
    align (0.5, 0.5)
    xsize 720

style poem_frame:
    padding (4, 35)

style poem_hbox:
    xfill True

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []


default poem_last_author = None

# Depreciation Warning
label showpoem(poem, **properties):
    "This feature is now depreciated. Please use {i}$ show_poem(){/i} instead.\nRefer to {u}poem_responses/poems.rpy{/u}on how to call a poem anew."
    return


label poem_list:
    
    python:

        poem_list = list()

        poem_list = [((_("sunshine"), poem_sunshine)), ((_("bottles"), poem_bottles)), ((_("flower"), "poem_flower")), ((_("last"), "poem_last")), ((_("angel"), "poem_angel")), ((_("fruits"), "poem_fruits")), ((_("leaf"), "poem_leaf")), ((_("prose"), "poem_prose")), ((_("afterlight"), "poem_afterlight")), ((_("nevermind"), "nevermind"))] 

        madechoice = renpy.display_menu(poem_list, screen="talk_choice")

    if not madechoice == "nevermind":
        $ fae_poems.show_poem(madechoice)
    

    return