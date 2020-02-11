init -9 python:
    #Arms
    arm_range = [str(x) for x in range(6, 10)]
    arm_range.append("cookie")
    for x in arm_range:
        exp_codes[0][x] = SpriteInfo('arms', x, body_depended = True)
    
    #Skins
    exp_codes[1]['a'] = DummySprite()## Dummy image
    for x in l_range('b','f'):
        exp_codes[1][x] = SpriteInfo('skin', x)
    for x in l_range('e','f'):
        exp_codes[1][x+'c'] = SpriteInfo('skin', x+'c')
    
    #Mouths
    for x in l_range('a','k'):
        exp_codes[2][x] = SpriteInfo('mouth', x)
    
    #Eyes
    for x in l_range('a','h'):
        exp_codes[3][x] = SpriteInfo('eyes', x)
    exp_codes[3]['cc'] = SpriteInfo('eyes', 'cc')
    exp_codes[3]['ec'] = SpriteInfo('eyes', 'ec')
    
    #Eyebrows
    for x in l_range('a','d'):
        exp_codes[4][x] = SpriteInfo('brows', x)
    
    #Hair styles
    def addHair(code, name, back = False, front = False):
        CUSTOM_TEMPLATES['hair'][code] = SpriteInfo('hair', code, name)
        if back:
            CUSTOM_TEMPLATES['hair_back'][code] = SpriteInfo('hair', code+"_back", name = name)
        else:
            CUSTOM_TEMPLATES['hair_back'][code] = DummySprite()
        if front:
            CUSTOM_TEMPLATES['hair_front'][code] = SpriteInfo('hair', code+"_front", name = name)
        else:
            CUSTOM_TEMPLATES['hair_front'][code] = DummySprite()
    
    addHair('usual',_('Usual hairstyle'))
    #Bodies
    CUSTOM_TEMPLATES['body']['uniform'] = SpriteInfo('body', 'uniform', name=_('School uniform'))
