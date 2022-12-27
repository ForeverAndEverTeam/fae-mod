
default persistent.fae_screenshot_first = None

default persistent.fae_good_photos = 0

default persistent.fae_bad_photos = 0

init -1 python in fae_screenshots:

    import os
    import random
    import store

    _photo_dir = os.path.join(renpy.config.basedir)
    if not os.path.exists(_photo_dir):
        os.makedirs(_photo_dir)
    

    __allow_photos = True

    bad_photo = 0

    __has_consent_photo = False

    __photos_disallowed = False

    
    reactions = [
        "D-did you just take a picture of me?"
        "Uwaaaa, I wasn't ready for a picture."
        "It's rude to take photos of people without asking, [player]!"
        "Please ask me next time, 'kay?"
    ]


    def allow_photos():

        global __allow_photos
        __allow_photos = True

    
    def forbid_photos():

        global __allow_photos
        __allow_photos = False
    

    def photo_allow_checker():

        return __allow_photos

    def photo_forbid_checker():

        return __allow_photos
    

    def permitted_to_photograph():

        return not __allow_photos and __has_consent_photo

    def retract_photo_perms(block=False):

        global __has_consent_photo

        __has_consent_photo = False

        if block:
            kill_photos()
        
    
    def grant_photograph_perms(unblock=False):

        global __has_consent_photo

        __has_consent_photo = False

        if unblock:
            resurrect_photos()
    
    def kill_photos():

        global __photos_disallowed
        __photos_disallowed = True
    
    def resurrect_photos():

        global __photos_disallowed
        __photos_disallowed = False

    
    for shutter_key in ("s", "alt_K_s", "alt_shift_K_s", "noshift_K_s"):
        store.fae_reg_keymap("attempt_photograph", "photo_topic", shutter_key)


label take_photo:

    hide window
    with Fade(.15, 0, .50, color="#fff")
    return

label photo_topic:

    if (
        fae_intro.FAEIntroStatus(persistent.fae_intro_status) != fae_intro.FAEIntroStatus.complete
        or fae_screenshots.photo_forbid_checker()
    ):
        return

    $ fae_screenshots.kill_photos()

    if persistent.fae_screenshot_first is None:

        $ persistent.fae_screenshot_first = datetime.datetime.now()

        call take_photo from _call_take_photo

        s "Did you just take a photo of me?"

        menu:
            "Yes, I did.":
                s "Well..."

    elif fae_screenshots.permitted_to_photograph():
        $ persistent.fae_good_photos += 1

        s "Oh...{w=0.5} you're taking that photo now?"
        s "Sure!"

        call take_photo from _call_take_photo_1

        if Affection.isHappy(higher=True):
            s "Just ask again if you wanna take another."
        
        else:
            s "Done? {w=0.5}Just make sure you ask again, if you want to take another."
        
        $ fae_screenshots.retract_photo_perms()
    
    elif not fae_screenshots.permitted_to_photograph():

        $ persistent.fae_bad_photos += 1

        call take_photo from _call_take_photo_2

        $ chosen_reaction = renpy.substitute(renpy.random.choice(fae_screenshots.reactions))

        s "[chosen_reaction]"

        $ fae_screenshots.allow_photos()

    return

init 5 python:
    chatReg(
        Chat(
            persistent._chat_db,
            label="s_player_picture",
            unlocked=True,
            prompt="Can I take a picture of you?",
            conditional="persistent.fae_screenshot_first is not None",
            category=["You", "Photography"],
            random=True
        ),
        chat_group=CHAT_GROUP_NORMAL
    )

label s_player_picture:

    if fae_screenshots.photo_forbid_checker():
        s "No. I won't turn the camera back on."
        return

    if Affection.isEnamoured(higher=True):
        if fae_screenshots.permitted_to_photograph():
            s "I already told you you could!"
        
        else:
            s "Sure!"
            $ fae_screenshots.grant_photograph_perms()
    
    elif Affection.isAffectionate(higher=True):
        if fae_screenshots.permitted_to_photograph():
            s "You already asked, silly!"
            s "So go ahead, whenever you're ready!"
        
        else:
            s "A picture? Sure!"
            $ fae_screenshots.grant_photograph_perms()
    
    elif Affection.isHappy(higher=True):
        if fae_screenshots.permitted_to_photograph():
            s "You already asked me that, silly!"
        
        else:
            s "A picture?{w=0.5} Of me?"
            s "Okay!"
            $ fae_screenshots.grant_photograph_perms()
    
    else:
        s "Sorry, [player].{w=0.5} I don't want my photo taken right now."
        $ fae_screenshots.retract_photo_perms()

    return



