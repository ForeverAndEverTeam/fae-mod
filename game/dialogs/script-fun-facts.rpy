default persistent._fae_fun_facts_db = dict()


init -10 python in fae_fun_facts:

    fun_fact_db = {}

    def getUnseenFacts():

        return [
            fun_fact_label
            for fun_fact_label, label in fun_fact_db.items()
            if not label.unlocked
        ]
    
    def getAllFactsLabels():

        return list(fun_fact_db.keys())


init 5 python:

    chatReg(
        Chat(
            persistent._chat_db,
            label="s_fun_fact_beginning",
            category=["misc"],
            prompt="Can you tell me a fun fact?",
            random=False
        )
    )


label s_fun_fact_beginning:

    s abbcaoa "Do you want to hear a fun fact, [player]?"

    python:

        unseen_fact_labels = fae_fun_facts.getUnseenFactsLabel()
        if len(unseen_fact_labels) > 0:
            fact_label_list = unseen_fact_labels
        else:
            fact_label_list = fae_fun_facts.getAllFactsLabel()

        

        fun_fact_labels = renpy.random.choice(fact_label_list)
        ats(fun_fact_labels)

    return
    

label fae_fun_facts_end:
    s abbccoa "I hope you enjoyed that one!"

    return


init 5 python:
    chatReg(
        Chat(
            persistent._fae_fun_facts_db,
            label="s_fun_fact_arts"
        )
    )

label s_fun_fact_arts: #Arts inside themselves
    s abaaaoa "Some artists add little details referring to different people or universes in their works."
    s "Like in some games and movies, you can find a poster or something that shows other characters. Maybe they're from a past work, or just there to fill in space."
    s abhaaca "We wouldn't know unless it was that obvious or they told us outright."
    s abbbaca "But some of them hide stuff in small things that could refer to a whole other universe, with different details and all."
    s "For example, do you remember {i}Parfait Girls{/i}?"
    s bbbbbaa "You've probably seen people talk about it around the community."
    s "This manga's plot isn't really known, is it?" 
    s abaaaoa "Nat tells you a little of what it's about, then that's pretty much it."
    s abbcaoa "But who knows! Maybe it’s alluding to an upcoming game or manga!"

    call fae_fun_facts_end
    return
