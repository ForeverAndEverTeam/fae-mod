# CODING STYLE

These are the coding conventions you should follow when creating dialogue for Sayori.

## INDENTS

Indents are **4** spaces. No more, no less.

## LABELS

Label names should be all lowercase, and have underscores between words.

E.G. `s_topic_example`

Specific prefixes are reserved for certain things.

- `greeting` - used for regular greetings
- `event` - used for special events
- `ch30` - used for key chapter 30 labels
- `s_topic` - used for nearly every sayori topic
- `fae_poem` - used for poemgame system
- `s_farewell` - used for farewells

There *are* more, so be careful of the labels you use.

## PERSISTENT

Persistent data is a way to store information to the disk. Persistent data does not get removed when the game exits.

You should **only** need this when you need to save data from multiple visits.

## VARIABLES

Please please please make these descriptive.

They don't need to be super-long. Just make sure it's easy to figure out what it is.

Abbreviations/acronyms are perfectly fine.

Use lowercase_underscores when naming them.

## COMMENTS

Make sure to comment your code!

Despite python being readable by definition, comments help us understand why we doing something or that the effects of doing something is helpful.

## ASSETS

Any custom files must go in the `mod_assets\` folder.

If you have a lot of assets, put them into a single subfolder.


# DIALOGUE

When making dialogue, you must use a dialogue block.

This is how to tell the game you've got dialogue you want to add.

An example of a dialogue block is below.

```renpy

init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_topics_example",
            unlocked=True,
            prompt="Example topic",
            random=True,
            category=["Misc", "Examples"]
        ),
        chat_group=CHAT_GROUP_NORMAL
    )


label s_topics_example:

    s abhfbaoa "This is an example topic."
    s abhfbboa "I don't think this actually belongs here thought."
    s abhfbloa "Who even thought of this?"
    s abhfbaoa "They really shouldn't be allowed to contribute."

    return
```

## DIALOGUE TIPS

- The label and the actual topic label match
- The labels are prefixed with `s_topics_`. All topics should be prefixed like that.
- Categories use *lowercase* letters, **EXCEPT FOR THE FIRST LETTER, WHICH IS CAPITAL**
- Categories are a list, so you can make your topic show up in multiple categories.
- The topic has `random=True`. This means that the topic will be shown in random chat. If you want the *player* to bring it up, put `random=False`.
