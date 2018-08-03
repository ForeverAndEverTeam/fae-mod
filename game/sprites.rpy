init -9 python:
    #Bodies
    bodies['6'] = Body(SpriteInfo(0, '6', (0, 0), (1020, 703))) ## Folded Arms
    bodies['7'] = Body(SpriteInfo(0, '7', (0, 0), (1020, 703)), (SpriteInfo(0, "7_rf", (390, 283), (83, 116)),))## Right fist on a cheek (original pose)
    bodies['8'] = Body(SpriteInfo(0, '8', (0, 0), (1020, 703)), (SpriteInfo(0, "8_fgs", (492, 363), (90, 46)),))## Finger-to-finger (like standing pos #5)
    
    #Skins
    exp_codes[0]['a'] = DummySprite()## Dummy image
    exp_codes[0]['b'] = SpriteInfo(1, 'b', (466, 307), (179,54))## Blush
    exp_codes[0]['c'] = SpriteInfo(1, 'c', (471, 289), (162,17))## Tears on the eyes
    exp_codes[0]['d'] = SpriteInfo(1, 'd', (475, 300), (155,25)) ## Tears on the cheeks
    exp_codes[0]['e'] = SpriteInfo(1, 'e', (471, 289), (162,36)) ## c+d
    exp_codes[0]['f'] = SpriteInfo(1, 'f', (466, 289), (179,72))##  e+b
    
    #Mouths
    exp_codes[1]['a'] = SpriteInfo(2, 'a', (538, 363), (38, 15))##  The holy precious smile
    exp_codes[1]['b'] = SpriteInfo(2, 'b', (548, 365), (18, 10))##  A bit open mouth with teeth
    exp_codes[1]['c'] = SpriteInfo(2, 'c', (547, 364), (24, 12))##  Open mouth
    exp_codes[1]['d'] = SpriteInfo(2, 'd', (553, 368), (8, 6))##  Suprised mouth
    exp_codes[1]['e'] = SpriteInfo(2, 'e', (536, 360), (38, 19))##  Laughter/wide smile (like she's very happy or tries to deny something)
    exp_codes[1]['f'] = SpriteInfo(2, 'f', (546, 367), (25, 5))##  Upset mouth
    exp_codes[1]['g'] = SpriteInfo(2, 'g', (541, 362), (36, 16))##  Shocked mouth
    
    #Eyes
    exp_codes[2]['a'] = SpriteInfo(3, 'a', (465, 252), (184, 56))##  Open eyes looking straight at the player
    exp_codes[2]['b'] = SpriteInfo(3, 'b', (465, 252), (184, 56))##  Open eyes looking at left (rel. to Sayori)
    exp_codes[2]['c'] = SpriteInfo(3, 'c', (465, 252), (184, 56))##  Closed eyes
    exp_codes[2]['d'] = SpriteInfo(3, 'd', (465, 252), (184, 56))##  Wink with the right eye (c+a)
    exp_codes[2]['e'] = SpriteInfo(3, 'e', (465, 252), (184, 56))##  Tightly closed eyes (>.<-like from Sayori's standing-pose 'p.png')
    exp_codes[2]['f'] = SpriteInfo(3, 'f', (465, 252), (184, 56))##  Half-closed eyes
    
    #Eyebrows
    exp_codes[3]['a'] = SpriteInfo(4, 'a', (473, 225), (182, 24))##  Normal eyebrows
    exp_codes[3]['b'] = SpriteInfo(4, 'b', (477, 219), (176, 26))##  Upset eyebrows
    exp_codes[3]['c'] = SpriteInfo(4, 'c', (486, 246), (162, 12))##  Frowning eyebrows