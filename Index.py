import zipfile, os, shutil

directory = "E:\Plex\Tv Shows\One Piece\Files"
zipedFolder = "E:\Plex\Tv Shows\One Piece\Zipped"
os.chdir(directory)


def extract():
    for file in os.listdir(directory):
        if file.endswith(".zip"):
            print(file)
            if zipfile.is_zipfile(file): # if it is a zipfile, extract it
                with zipfile.ZipFile(file) as item: # treat the file as a zip
                    item.extractall()  # extract it in the working directory
                shutil.move(file, zipedFolder)


extract();
