from sys import argv

rules = {
'a': 'aaaa',
'aa': 'agaa',
'ab': 'adab',
'b': 'abaa',
'c': 'acaa',
'd': 'aaab',
'e': 'bdab',
'f': 'afab',
'g': 'abab',
'h': 'acab',
'i': 'abac',
'j': 'acac',
'k': 'abbb',
'l': 'aebb',
'm': 'agba',
'n': 'adaa',
'o': 'adac',
'p': 'acec',
'q': 'aaca',
'r': 'aeba',
's': 'beba',
't': 'caab',
'u': 'cfab',
'v': 'fbab',
'w': 'fgab',
'x': 'aeaa',
'y': 'babb',
'z': 'aaac'
}

def upd_str(s):
    cols = s.count('    ')
    s = s.replace('    ', '')
    
    s = s.split(' ', 2)
    if s[:2] == ['show', 'sayori']:
        s = ' '.join(s).split(' ')
        s[2] = s[2][0] + rules[s[2][1:]]
    elif len(s) > 2:
        s[1] = s[1][0] + rules[s[1][1:]]
        
    return '    ' * cols + ' '.join(s)

if len(argv) < 2:
    inp = input()
    print(upd_str(inp))
else:
    for i in argv[1:]:
        info = ''
        with open(i, 'r') as f:
            for j in f.readlines():
                try:
                    info += upd_str(j)
                except:
                    info += j
        with open(i, 'w') as f:
            f.write(info)