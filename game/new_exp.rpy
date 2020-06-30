init -9 python:
    #Arms
    arm_range = [str(x) for x in range(6, 10)]
    for x in arm_range:
        exp_codes[0][x] = SpriteInfo('arms', x, body_depended = True)
    exp_codes[0]['9'] = SpriteInfo('arms', '9', body_depended = True, allowed = "**{de}**")
    exp_codes[0]['cookie'] = SpriteInfo('arms', 'cookie', body_depended = True, allowed = "*a**{ab}")
    
    #Skins
    exp_codes[1]['a'] = DummySprite()## Dummy image
    for x in l_range('b','d'):
        exp_codes[1][x] = SpriteInfo('skin', x)
    exp_codes[1]['c'] = SpriteInfo('skin', 'c', allowed = "***!d*")
    exp_codes[1]['cc'] = DummySprite()
    for x in 'ef':
        exp_codes[1][x] = SpriteInfo('skin', x, allowed = "***!d*")
        exp_codes[1][x+'c'] = SpriteInfo('skin', x+'c', allowed = "***!d*")
    
    #Mouths
    for x in l_range('a','k'):
        exp_codes[2][x] = SpriteInfo('mouth', x)
    exp_codes[2]['f'] = SpriteInfo('mouth', 'f', allowed = "***{cef}*")
    exp_codes[2]['h'] = SpriteInfo('mouth', 'h', allowed = "****c")
    
    #Eyes
    for x in l_range('a','h'):
        exp_codes[3][x] = SpriteInfo('eyes', x, allowed = "****!{bde}")
    exp_codes[3]['d'] = SpriteInfo('eyes', 'd', allowed = "****d")
    exp_codes[3]['f'] = SpriteInfo('eyes', 'f', allowed = "****b")
    exp_codes[3]['i'] = SpriteInfo('eyes', 'i', allowed = "****e")
    exp_codes[3]['cc'] = SpriteInfo('eyes', 'cc')
    exp_codes[3]['ec'] = SpriteInfo('eyes', 'ec')
    for ch in 'ef':
        exp_codes[3]['c' + ch] = exp_codes[3]['cc']
        exp_codes[3]['e' + ch] = exp_codes[3]['ec']
    
    #Eyebrows
    for x in l_range('a','e'):
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
