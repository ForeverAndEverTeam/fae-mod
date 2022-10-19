init python:

    class Poem:
        def __init__(self, author="", title="", text=""):
            self.author = author.lower()
            self.title = title
            self.text = text
        


image paper = "images/bg/poem.jpg"
transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0


screen poem(currentpoem, paper="paper"):
    style_prefix "poem"

    vbox:
        add paper

    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True

        has vbox
        null height 40

        null height 100
    
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

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

