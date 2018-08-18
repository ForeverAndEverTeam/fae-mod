## This file is for overriding specific declarations from DDLC
## Use this if you want to change a few variables, but don't want
## to replace entire script files that are otherwise fine.

## Normal overrides
## These overrides happen after any of the normal init blocks in scripts.
## Use these to change variables on screens, effects, and the like.

init 10 python:
    # Override the poems (to make them translatable)
    
    if cur_lang().code == "rus":
    
        poem_s1 = Poem(
        author = "sayori",
        title = _("Дорогой рассвет"),
        text = _("""\
Лучами бьёшься ты сквозь веки,
Как будто каждое утро ждёшь меня.
Меня целуешь прямо у лобик
Сонливую, будя меня.

Хотелось ли тебе со мной играть?
Или со мной развеять тучи?
От неба втайне хочется сказать:
Тебе доверяюсь при любом я случаи.

Если б не ты — я бы спала,
Спала бы сном я вечным.
Нет, я не больна, я голодна.
На завтрак наложите есть мне.""")
        )
    elif cur_lang().code == "epo":
    
        poem_s1 = Poem(
        author = "sayori",
        title = _("Kara Sunlum'"),
        text = _("""\
Vi lumas tra miaj palpebroj.
Ĝi min fartigas, ke mi mankis al vi.
Tenere kisas vi na mia frunto,
Kaj tiel vi min ellitigas.

Ĉu volas fidi min forigi la nubaĉojn
Aŭ nur promeni kun mi ekster mia hejm'?
Pro ke la ĉiel' nun estas tiel klara, 
Mi nun sekrete volas danki vin.

Se vi ne estus nun, do mi dum ĉiam dormus.
Sed ne, ne estas mi freneza. 

Mi nur ankoraŭ ne matenmanĝis.""")
        )
    

## Early overrides
## These overrides happen before the normal init blocks in scripts.
## Use this in the rare event that you need to overwrite some variable
## before it's called in another init block.
## You likely won't use this.
init -10 python:
    pass

## Super early overrides
## You'll need a block like this for creator defined screen language
## Don't use this unless you know you need it
python early:
    pass
