import os
import shutil

print(".___                                _________              __")                    
print("|   | _____ _____     ____   ____  /   _____/ ____________/  |_    ______ ___.__.")
print("|   |/      \\__  \   / ___\_/ __ \ \_____  \ /  _ \_  __ \   __\   \____ <   |  |")
print("|   |  Y Y  \/ __ \_/ /_/  >  ___/ /        (  <_> )  | \/|  |     |  |_> >___  |")
print("|___|__|_|__(_____/  \___  / \____>_______  /\____/|__|   |__| /\  |   __// ____|")
print("                    /_____/               \/                   \/  |__|   \/")     
print("                                                     Developed by: @dream.in.code")                        

#source="/home/gentoo/Downloads"
source=input("Enter your source directory: ")
#imageDestination="/home/gentoo/Pictures"
imageDestination=input("Enter your image destination path: ")
#videoDestination="/home/gentoo/Videos"
videoDestination=input("Enter your video destination path: ")
files = os.listdir(source)

for file in files:
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif"):
        shutil.move(os.path.join(source, file), os.path.join(imageDestination, file))
    if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".flv") or file.endswith(".webm") or file.endswith(".wmv") or file.endswith(".mov"):
        shutil.move(os.path.join(source, file), os.path.join(videoDestination, file))
print("moving...")
print("Done")
