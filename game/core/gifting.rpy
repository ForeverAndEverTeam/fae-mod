

init -100 python:

    import os

    def look_for_gift():
        

        if renpy.exists("gifts/cookies.gift"):
            
            store.fae_utilities.removeFileDir("{0}/gifts/cookies.gift".format(renpy.config.basedir))

            renpy.call("fae_cookies")
        
        elif renpy.exists("otter.gift"):

            store.fae_utilities.removeFileDir("otter.gift")

            renpy.call("fae_otter")


        else:
            renpy.call("fae_no_gift")
        
        return

label fae_cookies:

    $ refresh()

    $ store.fae_gifts.cookies = True

    $ store.fae_sprites._auto_gen("abhfaaa")

    s abhfaaa "I found cookies!"

    s "Yum!"

    return

label fae_otter:

    $ store.fae_gifts.otter = True
    
    $ store.fae_sprites._auto_gen("abhfaaa")

    s "I found an otter!"

    s "She's so cute!"

    return


label fae_no_gift:

    s "I didn't find anything!"

    return


init -100 python in fae_gifts:

    import store

    FAE_GIFT_ZORDER = 5

    cookies = False

    otter = False

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

    

