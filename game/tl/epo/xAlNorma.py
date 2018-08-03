from os import system, path
from sys import argv

s = ""

while len(argv) > 1:
	if not path.exists(argv[1]):
		argv.pop(1)
	else:
		break
if len(argv) <= 1:
	print("Enter the text. Enter \"<!>\" to finish input.")
	print("Entajpu la tekston. Entajpu na \"<!>\" por fini entajpadon.")
	print("")
	while True:
		inp = input()
		if inp == '<!>':
			break
		elif s != "":
			s += '\n'
		s += inp
else:
	while len(argv) > 1:
		if s != "":
			s += '\n'
		f = open(argv[1], 'r', encoding="utf-8")
		s += f.read()
		f.close()
		del f
		argv.pop(1)

i = 0
with open("transcripted.txt", 'w', encoding="utf-8") as f:
    while i < len(s):
        if i + 1 < len(s) and s[i + 1].lower() == 'x':
            ch = s[i]
            for nch in range(14):
                if ch == "XxCGHJSUcghjsu"[nch]:
                    f.write("XxĈĜĤĴŜŬĉĝĥĵŝŭ"[nch])
                    i += 1
                    break
            else:
                f.write(s[i])
        else:
            f.write(s[i])
        i += 1
system("transcripted.txt")
