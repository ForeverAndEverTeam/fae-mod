import re

file_list = (
    'greetings.rpy',
    'farewells.rpy',
    'topics.rpy',
    'intro.rpy',
    'script-fae.rpy',
    'poems.rpy'
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

for i in extra_exp:
    exp.add(i)
    #print(i + ' from extra_exp')

for file in file_list:
    try:
        file, fn = open(file, 'r', encoding = 'utf-8'), file
        
        for line in file.readlines():
            res = re.search('sayori\s\d+\w\w\w\w', line)
            res = res or re.search('s\s\d+\w\w\w\w', line)
            if res:
                e = res.group().split(' ')[-1]
                exp.add(e)
                #print('%s from %s' % (e, fn))
        
        file.close()
    except IOError:
        print("File not found: " + file)

with open('exp.txt', 'w') as output:
    output.write('\n'.join(exp))
