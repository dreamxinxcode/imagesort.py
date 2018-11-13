import os
import shutil

source="/home/gentoo/Downloads"
#input("Enter your source directory: ")
imageDestination="/home/gentoo/Pictures"
videoDestination="/home/gentoo/Videos"
files = os.listdir(source)

for file in files:
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif"):
        shutil.move(os.path.join(source, file), os.path.join(imageDestination, file))
    if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".flv") or file.endswith(".wmv") or file.endswith(".mov"):
        shutil.move(os.path.join(source, file), os.path.join(videoDestination, file))
