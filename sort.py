import glob, shutil, os

newdir = input("Where do you want your files to go? ")

isExist = os.path.exists(newdir)

if isExist == True:
    print("The folder already exists")
    exit
else:
    print("Creating " + str(newdir))
    newdir = os.makedirs(str(newdir))

extension = input("What is your file extension?")
print(extension)
for files in glob.glob(f"*{extension}", recursive=True):
    print(files)
    shutil.move(files, newdir)
