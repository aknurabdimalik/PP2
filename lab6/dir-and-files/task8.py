import os
file_path = r"C:\Users\abdim\Desktop\PP2\labs\lab6\dir-and-files\fordelete.txt" 

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)  
        print(f"File '{file_path}' has been successfully deleted.")
    else:
        print(f"Access denied: Unable to delete '{file_path}'.")
else:
    print(f"File '{file_path}' does not exist.")
