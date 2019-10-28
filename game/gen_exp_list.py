import re, os, sys

#Change the working directory to the script location
new_dir = re.split('[/\\\\]', sys.argv[0])
new_dir = "/".join(new_dir[:-1])
os.chdir(new_dir)

log_level = 1
for arg in sys.argv:
    if arg == "-h" or arg == "-help":
        print("EXPRESSION CODE LIST GENERATOR FOR 'FOREVER AND EVER'")
        print("By AlexanDDOS")
        print("Used to generate a exp.txt for the sprite optimization in the 'Forever and Ever' mod for DDLC\n")
        print("Argument list:")
        print("-h or -help\tDisplay this help")
        print("-log_level=[0-2]\tSet the logging level. Defaults to 1.")
        print("\t0 = No logging")
        print("\t1 = Log scanned files and additional expressions only")
        print("\t2 = Log the upper information and all the first expression code mentions")
        print("\t3 = Log the upper information and any expression code mentions")
        exit(0)
    elif arg.startswith('-log_level='):
        log_level = min(max(0,int(arg.split('=')[1])), 3)

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
SPR_TEMP = '\d+\w\w\w\w' #Expression sprite name template
exp = set() #Name buffer for used expression sprite

file_re = []
for t in file_templates:
    file_re.append(re.compile(t))

for i in extra_exp:
    exp.add(i)
    if log_level > 0:
        print('Adding %s from extra_exp' % i)

for fn in os.listdir():
    for t in file_re:
        if t.fullmatch(fn):
            break
    else:
        continue
    try:
        if log_level > 0:
            print("Scaning %s..." % fn)
        file = open(fn, 'r', encoding = 'utf-8')
        line_count = 1
        for line in file.readlines():
            res_by_show = re.search('sayori\s' + SPR_TEMP, line) #Look for a show command, summoning the needed sprite
            res_by_say = re.search('s\s' + SPR_TEMP, line) #Look for Sayori's line, calling the upper command with a 'syntactic sugar' argument before the string
            res = res_by_show or res_by_say #Get any of the upper RE results to extract the expression code
            if res:
                e = res.group().split(' ')[-1] #Expression code
                first = e not in exp #If it's the first mention of this code
                exp.add(e)
                if log_level == 3 or (log_level == 2 and first):
                    if res_by_show:
                        print("%s:%d: found expression %s in a 'show' command" % (fn, line_count, e))
                    else:
                        print("%s:%d: found expression %s in a character line" % (fn, line_count, e))
            line_count += 1
        file.close()
    except IOError:
        print("File not found: " + fn)

exp = sorted(exp)
with open('exp.txt', 'w') as output:
    output.write('\n'.join(exp))
