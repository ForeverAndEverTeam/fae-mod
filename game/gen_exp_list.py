import re, os, sys

#Change the working directory to the script location
new_dir = re.split('[/\\\\]', sys.argv[0])
new_dir = "/".join(new_dir[:-1])
os.chdir(new_dir)

file_templates = (
    'greetings\.rpy',
    'farewells\.rpy',
    'topics\.rpy',
    'intro\.rpy',
    'script-fae\.rpy',
    'poems\.rpy',
    "mg_.*\.rpy"
)
extra_exp = ( #Add expressions from the Python scripts here
    '7aeaa',
    '7afbb',
    '7affb',
    '7aeba',
    '7afbb',
    '7aaba',
    '6aeca',
    '7bafa',
    '6afac',
    '6afbc',
    '7baba'
)
exp = set()

file_re = []
for t in file_templates:
    file_re.append(re.compile(t))

for i in extra_exp:
    exp.add(i)
    #print(i + ' from extra_exp')

for fn in os.listdir():
    for t in file_re:
        if t.fullmatch(fn):
            break
    else:
        continue
    try:
        print("Opening %s..." % fn)
        file = open(fn, 'r', encoding = 'utf-8')
        for line in file.readlines():
            res = re.search('sayori\s\d+\w\w\w\w', line)
            res = res or re.search('s\s\d+\w\w\w\w', line)
            if res:
                e = res.group().split(' ')[-1]
                exp.add(e)
                #print('%s from %s' % (e, fn))
        file.close()
    except IOError:
        print("File not found: " + fn)

exp = sorted(exp)
with open('exp.txt', 'w') as output:
    output.write('\n'.join(exp))
