import zipfile, re, os

pack_krom = ( #Filename patterns, skipped by the script
    '.*\.rpa$',
    '.*\.svg$',
    '.*\.xcf$',
    '.*_d\.png$',
    './cache',
    './saves',
    './calendar\..*',
    './mod_assets/images/calendar',
    './test.zip',
    './mod_assets/images/santa_hat',
    '.*santa_hat.*',
    '.*beret.*',
    '.*info.txt$',
    '.*singleton.py$',
    './pack.py',
    './to_proofread.txt'
)
pack_external = (
    "LICENSE",
    "README.md",
    "IPGuidelines.md",
    "icon.ico"
)

pack_krom = tuple(re.compile(x) for x in pack_krom)

arc = zipfile.ZipFile("test.zip", "w", zipfile.ZIP_DEFLATED)

def wrong_name(fn):
    return any(x.match(fn) for x in pack_krom)

def add_dir(dir = ".", depth = 1):
    for f in os.listdir(dir):
        full = dir + "/" + f

        if wrong_name(full):
            print("-" * depth + full + ": skipped")
            continue
        else:
            print("-" * depth + full)
        try:
            add_dir(full, depth + 1)
        except NotADirectoryError:
            arc.write(full, "game/" + full)

print("Packing the 'game' folder...")
add_dir()
print('Packing the root folder...')
for f in pack_external:
    arc.write("../" + f, f)
    print(f)

arc.close()
