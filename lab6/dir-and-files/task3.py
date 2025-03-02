import os
path = r"C:\Users\abdim\Desktop\PP2\labs\lab6\dir-and-files\task2.py"
if os.path.exists(path):
    print("The path exists")
    direc = os.path.dirname(path)
    name = os.path.basename(path)
    print("Filename:", name)
    print("Directory portion:", direc)
    
else:
    print("The path does not exist")