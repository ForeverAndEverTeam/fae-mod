init -10 python:# in sayo_sprites:

    import store
    import store.sayo_utilities as sayo_utilities

    sayo_zorder = 3

    pose = "/sitting/"


    _SAYORI_IMAGES_PATH = "mod_assets/sayori/"


    #EYEBROW DEFS
    class FAEEyebrows():
        a = "a"
        b = "b"
        c = "c"
        d = "d"
        e = "e"
        f = "f"
        g = "unamused"
        numb = "n"

        def __str__(self):
            return self.name

    class FAEBackarms():
        unknown = "a"
        empty = "b"

        def __str__(self):
            return self.name

    #LEFT OR BOTH ARMS ONLY! NO RIGHT ARMS STUFF
    
    class FAEArms():
        cookiebite = "cb"
        cookie = "cookie"
        doublepoint = "double-point"
        folded = "folded"
        lefttouch = "left-fingers-touching"
        leftindex = "left-index-point"
        leftrest = "left-table-rest"
        none = "empty"

        def __str__(self):
            return self.name
    
    
    # RIGHT ARM DEFS
    class FAEArms2():

        folded = "folded"
        rtr = "right-table-rest"
        rf = "right-fist"
        rfpe = "right-finger-pup-ext"
        dp = "double-point"
        hrt = "hand-restingtop"
        none = "empty"

        def __str__(self):
            return self.name
    
    #EYE DEFS
    class FAEEyes():
        a = "a"
        b = "b"
        c = "c"
        d = "d"
        e = "e"
        f = "f"
        g = "g"
        h = "h"
        i = "i"
        j = "f1"
        k = "semi-wide"
        l = "closed-sad"
        m = "averted"
        n = "sparkle"

        
        def __str__(self):
            return self.name
    #HAIR DEFS
    class FAEHair():
        no_bow = "n"
        bow = "b"
        
        def __str__(self):
            return self.name
    #MOUTH DEFS
    class FAEMouth():
        a = "a"
        b = "b"
        c = "c"
        d = "d"
        e = "e"
        f = "f"
        g = "g"
        h = "h"
        i = "i"
        j = "j"
        k = "k"
        l = "big_frown"
        m = "drool"
        n = "drool_frown"
        o = "open"
        p = "pout"
        q = "GRIN"
        r = "unamused"
        s = "O_MOUTH"

        def __str__(self):
            return self.name


    class FAETears():
        d_tears = "d_tears"
        happy_d_tears = "happy_d_tears"
        pooled_tears = "pooled_tears"
        sad_d_tears = "sad_d_tears"
        crumbs = "crumbs"
        sweat_drop = "sweat-drop"
        none = None

        def __str__(self):
            return self.name

    class FAEBlush():
        blushing = "blushing"
        default_cheeks = "default_cheeks"
        red_eyes = "eye-redness"
        gloomy = "gloomy"
        none = None

        def __str__(self):
            return self.name

    def realgen(
        arms,
        arms2,
        backarm,
        hair,
        eyes,
        eyebrows,
        mouth,
        blush=None,
        tears=None
    ):
        """
        """
        ad_hoc = [
            (1280, 720),
            (0, 0), "{0}{1}/arms/uniform/back-sleeve.png".format(_SAYORI_IMAGES_PATH, pose),
            (0, 0), "{0}{1}/body/1.png".format(_SAYORI_IMAGES_PATH, pose),
            (0, 0), "{0}{1}/backarms/{2}.png".format(_SAYORI_IMAGES_PATH, pose, backarm),
            ]

        ad_hoc.extend([
            (0, 0), _SAYORI_IMAGES_PATH + "table/desk_sh.png",
            (0, 0), _SAYORI_IMAGES_PATH + "table/desk.png",
            (0, 0), "{0}{1}/arms/uniform/{2}.png".format(_SAYORI_IMAGES_PATH, pose, arms),
            (0, 0), "{0}{1}/arms/uniform/{2}.png".format(_SAYORI_IMAGES_PATH, pose, arms2),
            (0, 0), "{0}{1}/hair/{2}.png".format(_SAYORI_IMAGES_PATH, pose, hair),
        ])

        if blush:
            ad_hoc.extend([
                (0, 0), "{0}{1}/body/blush/{2}.png".format(_SAYORI_IMAGES_PATH, pose, blush),
            ])
        
        ad_hoc.extend([
            (0, 0), "{0}{1}/eyes/{2}.png".format(_SAYORI_IMAGES_PATH, pose, eyes),
            (0, 0), "{0}{1}/mouth/{2}.png".format(_SAYORI_IMAGES_PATH, pose, mouth),
            ])

        if tears:
            ad_hoc.extend([
                (0, 0), "{0}{1}/eyes/{2}.png".format(_SAYORI_IMAGES_PATH, pose, tears),
            ])
        
        ad_hoc.extend([
              
            (0, 0), "{0}{1}/eyebrows/{2}.png".format(_SAYORI_IMAGES_PATH, pose, eyebrows)
            
        ])
       
        return renpy.display.layout.LiveComposite(
            *ad_hoc
            )

init 1 python:# in sayo_sprites:
    #EYEBROWS
    EYEBROWS_DEF = {
        "a": FAEEyebrows.a,
        "b": FAEEyebrows.b,
        "c": FAEEyebrows.c,
        "d": FAEEyebrows.d,
        "e": FAEEyebrows.e,
        "f": FAEEyebrows.f,
        "g": FAEEyebrows.g,
        "n": FAEEyebrows.numb
    }

    BACKARM_DEF = {
        "a": FAEBackarms.unknown,
        "b": FAEBackarms.empty
    }

    #Arms with BOTH or ONLY LEFT NO RIGHT
    ARMS_DEF = {
        "a": FAEArms.folded,
        "b": FAEArms.leftindex,
        "c": FAEArms.cookie,
        "d": FAEArms.cookiebite,
        "e": FAEArms.doublepoint,
        #"f": FAEArms.leftindex,
        "f": FAEArms.leftrest,
        "g": FAEArms.lefttouch,
        "h": FAEArms.none
    }
    ARMS2_DEF = {
        "a": FAEArms2.folded,
        "b": FAEArms2.rtr,
        "c": FAEArms2.rf,
        "d": FAEArms2.rfpe,
        "e": FAEArms2.dp,
        "f": FAEArms2.hrt,
        "g": FAEArms2.none
    }
    #EYES ONLY
    EYES_DEF = {
        "a": FAEEyes.a,
        "b": FAEEyes.b,
        "c": FAEEyes.c,
        "d": FAEEyes.d,
        "e": FAEEyes.e,
        "f": FAEEyes.f,
        "g": FAEEyes.g,
        "h": FAEEyes.h,
        "i": FAEEyes.i,
        "j": FAEEyes.j,
        "k": FAEEyes.k,
        "l": FAEEyes.l,
        "m": FAEEyes.m,
        "n": FAEEyes.n
    }
    #HAIR
    HAIR_DEF = {
        "b": FAEHair.bow,
        "n": FAEHair.no_bow
    }
    #MOUTH
    MOUTH_DEF = {
        "a": FAEMouth.a,
        "b": FAEMouth.b,
        "c": FAEMouth.c,
        "d": FAEMouth.d,
        "e": FAEMouth.e,
        "f": FAEMouth.f,
        "g": FAEMouth.g,
        "h": FAEMouth.h,
        "i": FAEMouth.i,
        "j": FAEMouth.j,
        "k": FAEMouth.k,
        "l": FAEMouth.l,
        "m": FAEMouth.m,
        "n": FAEMouth.n,
        "o": FAEMouth.o,
        "p": FAEMouth.p,
        "q": FAEMouth.q,
        "r": FAEMouth.r,
        "s": FAEMouth.s
    }
    
    BLUSH_DEF = {
        "a": FAEBlush.default_cheeks,
        "b": FAEBlush.blushing,
        "c": FAEBlush.gloomy,
        "d": FAEBlush.red_eyes,
        "": FAEBlush.none
    }

    TEARS_DEF = {
        "e": FAETears.d_tears,
        "f": FAETears.happy_d_tears,
        "g": FAETears.pooled_tears,
        "h": FAETears.sad_d_tears,
        "i": FAETears.crumbs,
        "j": FAETears.sweat_drop,
        "": FAETears.none
    }

    

    def _exp_renderer(exp_code):
        if len(exp_code) < 7:
            raise ValueError("Invalid expression code: {0}".format(exp_code))
        

        eyebrows = exp_code[0]
        exp_code = exp_code[1:]

        backarm = exp_code[0]
        exp_code = exp_code[1:]

        arms = exp_code[0]
        exp_code = exp_code[1:]

        arms2 = exp_code[0]
        exp_code = exp_code[1:]

        hair = exp_code[0]
        exp_code = exp_code[1:]

        eyes = exp_code[0]
        exp_code = exp_code[1:]

        mouth = exp_code[0]
        exp_code = exp_code[1:]
        
        blush = None
        tears = None
        


        while exp_code:
            exp_part = exp_code[0]
            exp_code = exp_code[1:]

            if exp_part in BLUSH_DEF:
                blush = exp_part
            #Check if part is a tear
            if exp_part in TEARS_DEF:
                tears = exp_part

            #Otherwise it might be a blush
            

        return {

            "eyebrows": EYEBROWS_DEF[eyebrows],
            "backarm": BACKARM_DEF[backarm],
            "arms": ARMS_DEF[arms],
            "arms2": ARMS2_DEF[arms2],
            "hair": HAIR_DEF[hair],
            "eyes": EYES_DEF[eyes],
            "mouth": MOUTH_DEF[mouth],
            "blush": BLUSH_DEF.get(blush),
            "tears": TEARS_DEF.get(tears)
            
        }

        



    def _auto_gen(exp_code):
        

        disp = realgen(**_exp_renderer(exp_code))

        _existing_attr_list = renpy.display.image.image_attributes["sayori"]

        renpy.display.image.images[("sayori", exp_code)] = disp

        #if exp_code not in _existing_attr_list:
        #    _existing_attr_list.append(exp_code)

    def _find_target_override(self):
        
        name = self.name

        if isinstance(name, renpy.display.core.Displayable):
            self.target = name
            return True

        if not isinstance(name, tuple):
            name = tuple(name.split())

        def error(msg):
            self.target = renpy.text.text.Text(msg, color=(255, 0, 0, 255), xanchor=0, xpos=0, yanchor=0, ypos=0)

            if renpy.config.debug:
                raise Exception(msg)

        args = [ ]

        while name:
            target = renpy.display.image.images.get(name, None)

            if target is not None:
                break

            args.insert(0, name[-1])
            name = name[:-1]

        if not name:
            if (
                isinstance(self.name, tuple)
                and len(self.name) == 2
                and self.name[0] == "sayori"
            ):
                #Reset name
                name = self.name
                #Generate
                _auto_gen(name[1])
                #Try to get the img again
                target = renpy.display.image.images[name]

            else:
                error("Image '%s' not found." % ' '.join(self.name))
                return False

        try:
            a = self._args.copy(name=name, args=args)
            self.target = target._duplicate(a)

        except Exception as e:
            if renpy.config.debug:
                raise

            error(str(e))

        #Copy the old transform over.
        new_transform = self.target._target()

        if isinstance(new_transform, renpy.display.transform.Transform):
            if self.old_transform is not None:
                new_transform.take_state(self.old_transform)

            self.old_transform = new_transform

        else:
            self.old_transform = None

        return True

    renpy.display.image.ImageReference.find_target = _find_target_override






image sayori idle:

    "sayori aahcnaa"
