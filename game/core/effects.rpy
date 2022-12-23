## effects.rpy

# This file defines all the effects in DDLC used in Act 2.

init -2 python:
    # This screenshot is used to screenshot the game which is used for different
    # effects in-game.
    def screenshot_srf():
        if renpy.version_tuple > (7, 3, 5, 606):
            srf = renpy.display.draw.screenshot(None)
        else:
            srf = renpy.display.draw.screenshot(None, False)
        
        return srf

    # This function inverts the image in-game for the Invert Class.
    def invert():
        srf = screenshot_srf()
        inv = renpy.Render(srf.get_width(), srf.get_height()).canvas().get_surface()
        inv.fill((255,255,255,255))
        inv.blit(srf, (0,0), None, 2) 
        return inv

    # This class defines the code to invert the screen in 'screen invert'
    class Invert(renpy.Displayable):
        def __init__(self, delay=0.0, screenshot_delay=0.0):
            super(Invert, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.height = self.width * 9 / 16
            self.srf = invert()
            self.delay = delay
        
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            if st >= self.delay:
                render.blit(self.srf, (0, 0))
            return render

    # This function hides all the windows in-game.
    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled

## Invert(length, delay)
# This screen is called using the state `show screen invert(0.15, 0.3)` to invert the screen.
# Syntax
#   length - This declares how long the effect plays for.
#   delay - Delays the effect for X time before it starts.
screen invert(length, delay=0.0):
    add Invert(delay) size (1280, 720)
    timer delay action PauseAudio("music")
    timer delay action Play("sound", "sfx/glitch1.ogg")
    timer length + delay action Hide("invert")
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action PauseAudio("music", False)
    on "hide" action Stop("sound")
    on "hide" action Function(hide_windows_enabled, enabled=True)

init -2 python:
    # This class defines the code for the tear piece effect in 'screen tear'.
    class TearPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax
        
        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0
    
    # This class defines the code for the 'screen tear' effect in-game.
    class Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf=None):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()

            if float(self.width) / float(self.height) > 16.0/9.0:
                self.width = self.height * 16 / 9
            else:
                self.height = self.width * 9 / 16
            self.number = number
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf

            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))
        
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            for piece in self.pieces:
                piece.update(st)
                subsrf = self.srf.subsurface((0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY)))
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render

## Tear
# This screen is called using `show screen tear()` to tear the screen.
# Syntax
#   number - This declares how many pieces the screen tears on-screen.
#   offtimeMult - This declares the multiplier of time the effect lasts off.
#   ontimeMult - This declares the multiplier of time the effect lasts on.
#   offsetMin - This declares the minimum offset of time by the multiplier.
#   offsetMax - This declares the minimum offset of time by the multiplier.
#   srf - This declares the screen image from 'screenshot_srf' if it is declared.
screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150
    add Tear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (1280,720)
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action Function(hide_windows_enabled, enabled=True)

# RectStatic
# These images transforms show glitched rectangles in-game during Act 3 when Monika
# is deleted from the game.

# This image transform adds multiple black squares to the screen.
image m_rectstatic:
    RectStatic(Solid("#000"), 32, 32, 32).sm
    pos (0, 0)
    size (32, 32)

# This image transform adds multiple squares of the DDLC logo to the screen.
image m_rectstatic2:
    RectStatic(im.FactorScale(im.Crop("gui/logo.png", (100, 100, 128, 128)), 0.25), 2, 32, 32).sm

# This image transform adds multiple squares of Sayori's menu sprite to the screen.
image m_rectstatic3:
    RectStatic(im.FactorScale(im.Crop("gui/menu_art_s.png", (100, 100, 64, 64)), 0.5), 2, 32, 32).sm

init -2 python:
    import math

    # This class declares the code used for the RectStatic effect.
    class RectStatic(object):
        def __init__(self, theDisplayable, numRects=12, rectWidth = 30, rectHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.timers = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.rectWidth = rectWidth
            self.rectHeight = rectHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
                self.timers.append(random.random() * 0.4 + 0.1)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = random.randint(0, 40) * 32
            s.y = random.randint(0, 23) * 32
            s.width = self.rectWidth
            s.height = self.rectHeight
            self.rects.append(s)
        
        def update(self, st):
            for i, s in enumerate(self.rects):
                if st >= self.timers[i]:
                    s.x = random.randint(0, 40) * 32
                    s.y = random.randint(0, 23) * 32
                    self.timers[i] = st + random.random() * 0.4 + 0.1
            return 0

    ## ParticleBurst
    # This class declares the code used for the ParticleBurst effect.
    class ParticleBurst(object):
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 5):
            self.sm = SpriteManager(update=self.update)

            self.stars = [ ]
            self.displayable = theDisplayable
            self.explodeTime = explodeTime
            self.numParticles = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.gravity = 240
            self.timePassed = 0
            
            for i in range(self.numParticles):
                self.add(self.displayable, 1)
        
        def add(self, d, speed):
            s = self.sm.create(d)
            speed = random.random()
            angle = random.random() * 3.14159 * 2
            xSpeed = speed * math.cos(angle) * self.particleXSpeed
            ySpeed = speed * math.sin(angle) * self.particleYSpeed - 1
            s.x = xSpeed * 24
            s.y = ySpeed * 24
            pTime = self.particleTime
            self.stars.append((s, ySpeed, xSpeed, pTime))
        
        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x = xSpeed * 120 * (st + .20)
                    s.y = (ySpeed * 120 * (st + .20) + (self.gravity * st * st))
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            return 0
    
    ## Blood
    # This class declares the code used for the Blood effect for Yuri in Act 2.
    class Blood(object):
        def __init__(self, theDisplayable, density=120.0, particleTime=1.0, dripChance=0.05, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=100, burstSpeedX=200.0, burstSpeedY=400.0, numSquirts=4, squirtPower=400, squirtTime=0.25):
            self.sm = SpriteManager(update=self.update)
            self.drops = []
            self.squirts = []
            self.displayable = theDisplayable
            self.density = density
            self.particleTime = particleTime
            self.dripChance = dripChance
            self.dripSpeedX = dripSpeedX
            self.dripSpeedY = dripSpeedY
            self.gravity = 800.0
            self.dripTime = dripTime
            self.burstSize = burstSize
            self.burstSpeedX = burstSpeedX
            self.burstSpeedY = burstSpeedY
            self.lastUpdate = 0
            self.delta = 0.0
            
            for i in range(burstSize): self.add_burst(theDisplayable, 0)
            for i in range(numSquirts): self.add_squirt(squirtPower, squirtTime)
        
        # This function makes a single squirt of blood that follows an arc.
        def add_squirt(self, squirtPower, squirtTime):
            angle = random.random() * 6.283
            xSpeed = squirtPower * math.cos(angle)
            ySpeed = squirtPower * math.sin(angle)
            self.squirts.append([xSpeed, ySpeed, squirtTime])
        
        # This function makes a burst of blood that pops out of some area
        def add_burst(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.burstSpeedX + 20
            ySpeed = (random.random() - 0.75) * self.burstSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        # This function makes a dripping stream of blood
        def add_drip(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.dripSpeedX + 20
            ySpeed = random.random() * self.dripSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])
        
        def update(self, st):
            delta = st - self.lastUpdate
            self.delta += st - self.lastUpdate
            self.lastUpdate = st

            sindex = 0
            for xSpeed, ySpeed, squirtTime in self.squirts:
                if st > squirtTime: self.squirts.pop(sindex)
                sindex += 1
            
            pindex = 0
            if st < self.dripTime:
                while self.delta * self.density >= 1.0:
                    self.delta -= (1.0 / self.density)
                    if random.random() >= 1 - self.dripChance: self.add_drip(self.displayable, st)
                    for xSpeed, ySpeed, squirtTime in self.squirts:
                        s = self.sm.create(self.displayable)
                        s.x += (random.random() - 0.5) * 5
                        s.y += (random.random() - 0.5) * 5
                        self.drops.append([s, xSpeed + (random.random() - 0.5) * 20, ySpeed + (random.random() - 0.5) * 20, self.particleTime, st])
            for s, xSpeed, ySpeed, particleTime, startTime in self.drops:
                if (st - startTime < particleTime):
                    s.x += xSpeed * delta
                    s.y += ySpeed * delta
                    self.drops[pindex][2] += self.gravity * delta
                else:
                    s.destroy()
                    self.drops.pop(pindex)
                pindex += 1
            return 0

# This image transform adds a blood drop that gets longer and 
# thinner over time.
image blood_particle_drip:
    "gui/blood_drop.png"
    yzoom 0 yanchor 0.2 subpixel True
    linear 10 yzoom 8

# This image transform adds a blood drop that gets thinner
# randomly by time.
image blood_particle:
    subpixel True
    "gui/blood_drop.png"
    zoom 0.75
    alpha 0.75
    choice:
        linear 0.25 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.55 zoom 0

# This image transform adds a blood drop that squirts and
# drops for three minutes.
image blood:
    size (1, 1)
    truecenter
    Blood("blood_particle").sm

# This image transform adds a blood drop that doesn't squirts,
# and increases the chance of dropping.
image blood_eye:
    size (1, 1)
    truecenter
    Blood("blood_particle", dripChance=0.5, numSquirts=0).sm

# This image transform adds a blood drop that has a very low
# chance to drop.
image blood_eye2:
    size (1, 1)
    truecenter
    Blood("blood_particle", dripChance=0.005, numSquirts=0, burstSize=0).sm

init -2 python:
    import math

    ## AnimatedMask
    # This class declares the code used for the AnimatedMask effect in Act 3.
    class AnimatedMask(renpy.Displayable):
        
        def __init__(self, child, faek, faekb, oc, op, moving=True, speed=1.0, frequency=1.0, amount=0.5, **properties):
            super(AnimatedMask, self).__init__(**properties)
            
            self.child = renpy.displayable(child)
            self.faek = renpy.displayable(faek)
            self.faekb = renpy.displayable(faekb)
            self.oc = oc
            self.op = op
            self.null = None
            self.size = None
            self.moving = moving
            self.speed = speed
            self.amount = amount
            self.frequency = frequency
        
        def render(self, width, height, st, at):
            
            cr = renpy.render(self.child, width, height, st, at)
            mr = renpy.render(self.faek, width, height, st, at)
            mb = renpy.Render(width, height)
            
            
            if self.moving:
                mb.place(self.faek, ((-st * 50) % (width * 2)) - (width * 2), 0)
                mb.place(self.faekb, -width / 2, 0)
            else:
                mb.place(self.faek, 0, 0)
                mb.place(self.faekb, 0, 0)
            
            
            
            cw, ch = cr.get_size()
            mw, mh = mr.get_size()
            
            w = min(cw, mw)
            h = min(ch, mh)
            size = (w, h)
            
            if self.size != size:
                self.null = Null(w, h)
            
            nr = renpy.render(self.null, width, height, st, at)
            
            rv = renpy.Render(w, h)#, opaque=False)
            
            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = 1.0
            rv.operation_complete = self.oc + math.pow(math.sin(st * self.speed / 8), 64 * self.frequency) * self.amount
            rv.operation_parameter = self.op
            
            rv.blit(mb, (0, 0), focus=False, main=False)
            rv.blit(nr, (0, 0), focus=False, main=False)
            rv.blit(cr, (0, 0))
            
            renpy.redraw(self, 0)
            return rv

    # This function makes a image be transparent for a bit then 
    # fade in and out in Act 3.
    def monika_alpha(trans, st, at):
        trans.alpha = math.pow(math.sin(st / 8), 64) * 1.4
        return 0

## The Old Blue Screen of Death
# These images tricks the player to think their PC has crashed.
# This feature has been depreciated in favor for Better BSODs 
# but here for compatibility.

image bsod_1:
    "images/bg/bsod.png"
    size (1280,720)
image bsod_2:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

image bsod = LiveComposite((1280, 720), (0, 0), "bsod_1", (0, 0), "bsod_2")

## Veins
# This image transform creates a veiny border around the screen that shakes and pulses
# during a random playthrough in Act 2.
image veins:
    AnimatedMask("images/bg/veinfaek.png", "images/bg/veinfaek.png", "images/bg/veinfaekb.png", 0.15, 16, moving=False, speed=10.0, frequency=0.25, amount=0.1)
    xanchor 0.05 zoom 1.10
    xpos -5
    subpixel True
    parallel:
        ease 2.0 xpos 5
        ease 1.0 xpos 0
        ease 1.0 xpos 5
        ease 2.0 xpos -5
        ease 1.0 xpos 0
        ease 1.0 xpos -5
        repeat
    parallel:
        choice:
            0.6
        choice:
            0.2
        choice:
            0.3
        choice:
            0.4
        choice:
            0.5
        pass
        choice:
            xoffset 0
        choice:
            xoffset 1
        choice:
            xoffset 2
        choice:
            xoffset -1
        choice:
            xoffset -2
        repeat
transform fade_in(time=1.0):
    alpha 0.0
    ease time alpha 1.0


transform fae_kissing(_zoom, _y, time=2.0):

    i11
    xcenter 640 yoffset 700 yanchor 1.0
    linear time ypos _y zoom _zoom

transform fae_kiss_return(time, y):

    linear time xcenter 640 yoffset (y) zoom 0.80


label fae_kiss_engine(
    transition=4.0,
    duration=2.0,
    hide_ui=True,
    initial_exp="aahcnaaa",
    mid_exp="aahcnaaa",
    final_exp="aahcnaaa",
    fade_duration=1.0
):

    window hide
    if hide_ui:
        hide screen hidden1
    
    show sayori at i11

    $ _fae_kiss_zoom = 4.9 / fae_sprites.value_zoom
    $ _fae_kiss_y = 2060 - ( 1700 * (fae_sprites.value_zoom - 1.1))
    $ _fae_kiss_y2 = -1320 + (1700 * (fae_sprites.value_zoom - 1.1))

    $ renpy.show("sayori {}".format(initial_exp), [fae_kissing(_fae_kiss_zoom, int(_fae_kiss_y), transition)])

    $ renpy.pause(transition)

    show black zorder 100 at fade_in(fade_duration)

    $ renpy.pause(duration/2)
    play sound "mod_assets/sfx/kissing.ogg"
    window auto
    "chu~{fast}{w=1}{nw}"
    window hide
    $ renpy.pause(duration/2)
    # hide the black scene
    hide black

    $ renpy.show("sayori {}".format(mid_exp), [fae_kiss_return(transition, _fae_kiss_y2)])
    pause transition

    $ renpy.show("sayori {}".format(final_exp),[i11()])

    show sayori with dissolve_sayori
    if hide_ui:

        show screen hidden1(True)
    
    window auto
    return


label fae_kiss_short(**kwargs):

    python:
        kwargs.setdefault("duration", 0.5)
        kwargs.setdefault("fade_duration", 0.5)
        kwargs.setdefault("initial_exp", "6hua")
    call fae_kiss_engine(**kwargs) from _call_fae_kiss_engine
    return


label fae_zoom_value_transition(new_zoom, transition=3.0):

    if new_zoom == fae_sprites.value_zoom:
        return
    
    if new_zoom > 2.1:
        $ new_zoom = 2.1
    
    elif new_zoom < 1.1:
        $ new_zoom = 1.1
    
    $ _fae_transition_time = transition

    $ _fae_old_zoom = fae_sprites.zoom_level
    $ _fae_old_zoom_value = fae_sprites.value_zoom
    $ _fae_old_y = fae_sprites.adjust_y

    # calculate and store the new values
    $ _fae_new_zoom = ((new_zoom - fae_sprites.default_value_zoom) / fae_sprites.zoom_step ) + fae_sprites.default_zoom_level
    if _fae_new_zoom > fae_sprites.default_value_zoom:
        $ _fae_new_y = fae_sprites.default_y + ((_fae_new_zoom-fae_sprites.default_zoom_level) * fae_sprites.y_step)
    else:
        $ _fae_new_y = fae_sprites.default_y
    $ _fae_new_zoom = ((new_zoom - fae_sprites.default_value_zoom) / fae_sprites.zoom_step ) + fae_sprites.default_zoom_level

    # calculate and store the differences between new and old values
    $ _fae_zoom_diff = _fae_new_zoom - _fae_old_zoom
    $ _fae_zoom_value_diff = new_zoom - _fae_old_zoom_value
    $ _fae_zoom_y_diff = _fae_new_y - _fae_old_y
    # do the transition and pause so it force waits for the transition to end
    show sayori at fae_smooth_transition
    $ renpy.pause(transition, hard=True)
    return

label fae_zoom_fixed_duration_transition(new_zoom,transition=3.0):
    # Sanity checks
    if new_zoom == fae_sprites.zoom_level:
        return
    if new_zoom > 20:
        $ new_zoom = 20
    elif new_zoom < 0:
        $ new_zoom = 0
    # store the time the transition will take
    $ _fae_transition_time = transition

    # store the old values
    $ _fae_old_zoom = fae_sprites.zoom_level
    $ _fae_old_zoom_value = fae_sprites.value_zoom
    $ _fae_old_y = fae_sprites.adjust_y

    # calculate and store the new values
    if new_zoom > fae_sprites.default_zoom_level:
        $ _fae_new_y = fae_sprites.default_y + (
            (new_zoom - fae_sprites.default_zoom_level) * fae_sprites.y_step
        )
        $ _fae_new_zoom_value = fae_sprites.default_value_zoom + (
            (new_zoom - fae_sprites.default_zoom_level) * fae_sprites.zoom_step
        )
    else:
        $ _fae_new_y = fae_sprites.default_y
        if new_zoom == fae_sprites.default_zoom_level:
            $ _fae_new_zoom_value = fae_sprites.default_value_zoom
        else:
            $ _fae_new_zoom_value = fae_sprites.default_value_zoom - (
                (fae_sprites.default_zoom_level - new_zoom) * fae_sprites.zoom_step
            )
    # calculate and store the differences between new and old values
    $ _fae_zoom_diff = new_zoom - _fae_old_zoom
    $ _fae_zoom_value_diff = _fae_new_zoom_value - _fae_old_zoom_value
    $ _fae_zoom_y_diff = _fae_new_y - _fae_old_y
    # do the transition and pause so it force waits for the transition to end
    show sayori at fae_smooth_transition
    $ renpy.pause(transition, hard=True)
    return

# Zoom Transition label #3
# Used to transition from any valid zoom value to another valid
# zoom valid zoom value in a smooth way
# IN:
#     new_zoom - the new zoom level to move to
#     transition - the time in seconds used to transition from the maximum to the
#         minimum zoom level, this works in a way that the time used in the
#         transition is lower the nearer the current zoom level is to the
#         new zoom level (Default: 3.0)
label fae_zoom_transition(new_zoom,transition=3.0):
    # Sanity checks
    if new_zoom == fae_sprites.zoom_level:
        return
    if new_zoom > 20:
        $ new_zoom = 20
    elif new_zoom < 0:
        $ new_zoom = 0

    # store the old values
    $ _fae_old_zoom = fae_sprites.zoom_level
    $ _fae_old_zoom_value = fae_sprites.value_zoom
    $ _fae_old_y = fae_sprites.adjust_y

    # calculate and store the new values
    if new_zoom > fae_sprites.default_zoom_level:
        $ _fae_new_y = fae_sprites.default_y + (
            (new_zoom - fae_sprites.default_zoom_level) * fae_sprites.y_step
        )
        $ _fae_new_zoom_value = fae_sprites.default_value_zoom + (
            (new_zoom - fae_sprites.default_zoom_level) * fae_sprites.zoom_step
        )
    else:
        $ _fae_new_y = fae_sprites.default_y
        if new_zoom == fae_sprites.default_zoom_level:
            $ _fae_new_zoom_value = fae_sprites.default_value_zoom
        else:
            $ _fae_new_zoom_value = fae_sprites.default_value_zoom - (
                (fae_sprites.default_zoom_level - new_zoom) * fae_sprites.zoom_step
            )

    # calculate and store the differences between new and old values
    $ _fae_zoom_diff = new_zoom - _fae_old_zoom
    $ _fae_zoom_value_diff = _fae_new_zoom_value - _fae_old_zoom_value
    $ _fae_zoom_y_diff = _fae_new_y - _fae_old_y

    # store the time the transition will take
    $ _fae_transition_time = abs(_fae_zoom_value_diff) * transition

    # do the transition and pause so it force waits for the transition to end
    show sayori at fae_smooth_transition
    $ renpy.pause(_fae_transition_time, hard=True)
    return

label fae_zoom_transition_reset(transition=3.0):
    call fae_zoom_transition(store.fae_sprites.default_zoom_level, transition) from _call_fae_zoom_transition
    return

init python:
    def zoom_smoothly(trans, st, at):

        # check if the transition time is lower than the elapsed time
        if _fae_transition_time > st:
            # do some calcs
            step = st / _fae_transition_time
            fae_sprites.zoom_level = _fae_old_zoom + (step * _fae_zoom_diff)
            fae_sprites.value_zoom = _fae_old_zoom_value + (step * _fae_zoom_value_diff)
            fae_sprites.adjust_y = int(_fae_old_y + (step * _fae_zoom_y_diff))
            if fea_sprites.adjust_y < fae_sprites.default_y:
                fea_sprites.adjust_y = fae_sprites.default_y

            renpy.restart_interaction()
            # to be called as soon as possible we return 0
            return 0.1
        else:
            # get the zoom level and call adjust zoom to be sure it works
            fae_sprites.zoom_level = int(round(fae_sprites.zoom_level))
            fae_sprites.change_zoom()
            renpy.restart_interaction()
            # we return None to be able to move to the next statement
            return None

# zoom transition animation transform
transform fae_smooth_transition:
    i11 # this one may not be needed but I keep it just in case
    function zoom_smoothly

