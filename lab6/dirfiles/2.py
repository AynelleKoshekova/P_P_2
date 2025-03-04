import os
def access(path):
    if os.path.exists(path):
        print(path, "is exist")
    else:
        print(path, "is gone")
    if os.access(path, os.R_OK):
        print(path, "is readability")
    else:
        print(path, "is not readability")
    if os.access(path, os.W_OK):
        print(path, "is writability")
    else:
        print(path, "is not writability")
    if os.access(path, os.X_OK):
        print(path, "is executability")
    else:
        print(path, "is not executability")

pp=os.path.join(os.getcwd(), "")
pp1=os.path.join(os.getcwd(), r"lab6/dirfiles")
access(pp)
access(pp1)