import os
path = r"C:\Users\abdim\Desktop\PP2\labs\lab6\dir-and-files\task1.py"
def checking(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
    
checking(path)