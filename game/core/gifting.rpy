image cookies = "mod_assets/images/food/cookies.png"

init -10 python:
    
    import os

    FAE_COOKIE_ZORDER = 5

    GIFT_PATH = "/characters/"
    GIFT_PATH_PATH = os.path.normcase(renpy.config.basedir + GIFT_PATH)

init python:

    def look_for_gift():

        

        if renpy.exists("cookies.gift"):
            
            store.fae_utilities.removeFileDir("game/cookies.gift")

            renpy.call("fae_cookies")

        else:
            renpy.call("fae_no_gift")
        
        return

label fae_cookies:

    $ store.fae_gifts.cookies = True
    
    $ store.fae_sprites._auto_gen("abhfaaa")

    s "I found cookies!"

    s "Yum!"

    $ refresh()

    return

label fae_no_gift:

    s "I didn't find anything!"

    return


init -100 python in fae_gifts:

    import store

    FAE_GIFT_ZORDER = 5

    cookies = False

    class FAEGift():
        def __init__(self, gift, zorder):

            self.gift = gift
            self.zorder = zorder
            ext = "{0}.gift".format(gift)

        def find(self):

            renpy.show(
                gift=ext,
                zorder=self.zorder
            )
    
    COOKIES = FAEGift(
        gift="cookies",
        zorder=FAE_GIFT_ZORDER
    )

    

