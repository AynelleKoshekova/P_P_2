import os

if os.path.exists('dirfiles/delete.txt'):
    os.remove('dirfiles/delete.txt')
    print('deleted')