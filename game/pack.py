import zipfile, re, os, sys

archive_name = "test"

#Change the working directory to the script location
new_dir = re.split('[/\\\\]', sys.argv[0])
new_dir = "/".join(new_dir[:-1])
os.chdir(new_dir)

def read_info(f, pattern):
    return re.search(pattern, f.read()).groups()

with open("./options.rpy", "r") as f:
    archive_name = read_info(f, "define config.version = \"(.+)\"")[0] #Name the archive with the version's name
    print("The release will be packed into %s.zip" % archive_name)

pack_krom = ( #Filename patterns, skipped by the script
    '.*\.rpa$',
    '.*\.svg$',
    '.*\.xcf$',
    '.*_d\.png$',
    './cache',
    './saves',
    './calendar\..*',
    './mod_assets/images/calendar',
    './' + archive_name + '.zip',
    './mod_assets/images/santa_hat',
    '.*santa_hat.*',
    '.*beret.*',
    '.*info.txt$',
    '.*singleton.py$',
    './pack.py',
    './to_proofread.txt',
    './zz_developer\..*'
)
pack_external = (
    "LICENSE",
    "README.md",
    "IPGuidelines.md",
    "icon.ico"
)

pack_krom = tuple(re.compile(x) for x in pack_krom)

arc = zipfile.ZipFile(archive_name + ".zip", "w", zipfile.ZIP_DEFLATED)
print("Archive openned!")

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
print("Closing the archive...")
arc.close()

print("Release sucessfully packed!")
