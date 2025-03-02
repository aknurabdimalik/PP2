list = ["PP2", "Discrete Structures", "Calculus2", "Socio", "English" ]
file = open(r'C:\Users\abdim\Desktop\PP2\labs\lab6\dir-and-files\texts.txt', 'w')
for subject in list:
    file.write(subject + "\n")
    
file.close()
print("ok")