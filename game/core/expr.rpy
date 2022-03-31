
init python:

    pose = "/sitting/"


    _SAYORI_IMAGES_PATH = "mod_assets/sayori/"


    #EYEBROW DEFS
    class FAEEyebrows():
        normal = "a"
        frown = "b"
        angry = "c"
        lfrn = "d"
        smug = "e"
        furrowed = "f"
        numb = "n"

        def __str__(self):
            return self.name

    #LEFT OR BOTH ARMS ONLY! NO RIGHT ARMS STUFF
    
    class FAEArms():
        cookiebite = "cb"
        cookie = "cookie"
        doublepoint = "double-point"
        folded = "folded"
        rest = "hand-restingtop"
        lefttouch = "left-fingers-touching"
        leftindex = "left-index-point"
        leftrest = "left-table-rest"

        def __str__(self):
            return self.name
    
    
    # RIGHT ARM DEFS
    class FAEArms2():

        rf = "right-fist"
        rrest = "right-table-rest"
        folded = "folded"
        rfpe = "right-finger-pup-ext"
    #EYE DEFS
    class FAEEyes():
        normal = "a"
        lookleft = "b"
        closed = "c"
        wink = "d"
        eyaa = "e"
        sad = "f"
        crazy = "g"
        wide = "h"
        smug = "h"
        unk = "f1"
        
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
        normal = "a"
        smallagape = "b"
        delicateagape = "c"
        ajar = "d"
        eidesmile = "e"
        sad = "f"
        surprised = "g"
        frown = "h"
        tongue = "i"
        pout = "j"
        widesmile = "k"
        
        def __str__(self):
            return self.name

    def realgen(
        arms,
        arms2,
        eyes,
        hair,
        eyebrows,
        mouth
    ):
        """
        """
        ad_hoc = [
            (1280, 720),
            (0, 0), "{0}{1}/arms/uniform/back-sleeve.png".format(_SAYORI_IMAGES_PATH, pose),
            (0, 0), "{0}{1}/arms/uniform/unknown.png".format(_SAYORI_IMAGES_PATH, pose),
            (0, 0), "{0}{1}/body/1.png".format(_SAYORI_IMAGES_PATH, pose),
            (0, 0), _SAYORI_IMAGES_PATH + "table/desk_sh.png",
            (0, 0), _SAYORI_IMAGES_PATH + "table/desk.png",
            (0, 0), "{0}{1}/arms/uniform/{2}.png".format(_SAYORI_IMAGES_PATH, pose, arms),
            (0, 0), "{0}{1}/arms/uniform/{2}.png".format(_SAYORI_IMAGES_PATH, pose, arms2),
            (0, 0), "{0}{1}/eyes/{2}.png".format(_SAYORI_IMAGES_PATH, pose, eyes),
            (0, 0), "{0}{1}/hair/{2}.png".format(_SAYORI_IMAGES_PATH, pose, hair),
            (0, 0), "{0}{1}/eyebrows/{2}.png".format(_SAYORI_IMAGES_PATH, pose, eyebrows),
            (0, 0), "{0}{1}/mouth/{2}.png".format(_SAYORI_IMAGES_PATH, pose, mouth),
        ]
       
        return renpy.display.layout.LiveComposite(
            *ad_hoc
            )

init 1 python:
    #EYEBROWS
    EYEBROWS_DEF = {
        "a": FAEEyebrows.normal,
        "b": FAEEyebrows.frown,
        "c": FAEEyebrows.angry,
        "d": FAEEyebrows.lfrn,
        "e": FAEEyebrows.smug,
        "f": FAEEyebrows.furrowed,
        "g": FAEEyebrows.numb
    }
    #Arms with BOTH or ONLY LEFT NO RIGHT
    ARMS_DEF = {
        "a": FAEArms.folded,
        "b": FAEArms.leftindex,
        "c": FAEArms.cookie,
        "d": FAEArms.cookiebite,
        "e": FAEArms.doublepoint,
        "f": FAEArms.leftindex,
        "g": FAEArms.leftrest,
        "h": FAEArms.lefttouch
    }
    ARMS2_DEF = {
        "a": FAEArms2.rf,
        "b": FAEArms2.rrest,
        "c": FAEArms2.rfpe,
        "d": FAEArms2.folded,
    }
    #EYES ONLY
    EYES_DEF = {
        "a": FAEEyes.normal,
        "b": FAEEyes.lookleft,
        "c": FAEEyes.closed,
        "d": FAEEyes.wink,
        "e": FAEEyes.eyaa,
        "f": FAEEyes.sad,
        "g": FAEEyes.crazy,
        "h": FAEEyes.wide,
        "i": FAEEyes.smug,
        "j": FAEEyes.unk
    }
    #HAIR
    HAIR_DEF = {
        "b": FAEHair.bow,
        "n": FAEHair.no_bow
    }
    #MOUTH
    MOUTH_DEF = {
        "a": FAEMouth.normal,
        "b": FAEMouth.smallagape,
        "c": FAEMouth.delicateagape,
        "d": FAEMouth.ajar,
        "e": FAEMouth.eidesmile,
        "f": FAEMouth.sad,
        "g": FAEMouth.surprised,
        "h": FAEMouth.frown,
        "i": FAEMouth.tongue,
        "j": FAEMouth.pout,
        "k": FAEMouth.widesmile

    }



    def _exp_renderer(exp_code):
        if len(exp_code) < 6:
            raise ValueError("Invalid expression code: {0}".format(exp_code))
        

        eyebrows = exp_code[0]
        exp_code = exp_code[1:]

        arms = exp_code[0]
        exp_code = exp_code[1:]

        arms2 = exp_code[0]
        exp_code = exp_code[1:]

        eyes = exp_code[0]
        exp_code = exp_code[1:]

        hair = exp_code[0]
        exp_code = exp_code[1:]

        mouth = exp_code[0]
        exp_code = exp_code[1:]


        return {

            "eyebrows": EYEBROWS_DEF[eyebrows],
            "arms": ARMS_DEF[arms],
            "arms2": ARMS2_DEF[arms2],
            "eyes": EYES_DEF[eyes],
            "hair": HAIR_DEF[hair],
            "mouth": MOUTH_DEF[mouth]
        }

        



    def _auto_gen(exp_code):
        

        disp = realgen(**_exp_renderer("sayori", exp_code))

        renpy.display.image.images[("sayori" + exp_code)] = disp



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


