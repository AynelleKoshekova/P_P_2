import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = '/Users/ajnelkosekova/Desktop/pp2/lab6/dirfiles/7file.txt'
f2 = '/Users/ajnelkosekova/Desktop/pp2/lab6/dirfiles/7filenew.txt'
copy(f1, f2)