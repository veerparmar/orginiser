from configparser import ExtendedInterpolation
from fileinput import filename
import os
import shutil
fromdir = "C:/Users/Veer/Downloads"
todir = "C:/Users/Veer/Desktop/wallpapers"
listOfFiles = os.listdir(fromdir)
print(listOfFiles)

for file_name in listOfFiles:
    name, extention = os.path.splitext(file_name)
    '''print(name)
    print(extention)'''
    if extention == '':
        continue
    if extention in ['.gif','.png',',jpg','jpeg','jfif']:
        path1= fromdir + '/' + file_name 
        path2= todir + '/' + 'wallpapers'
        path3= todir + '/' + 'wallpapers' + '/' + file_name
        '''print("path1 ", path1)
        print("path3", path3)'''
        if os.path.exists(path2):
            print("moving"+file_name+"...")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moving"+file_name+"...")
            shutil.move(path1,path3)