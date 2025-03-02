first_file = r"C:\Users\abdim\Desktop\PP2\labs\lab6\dir-and-files\texts.txt"
second_file = r"C:\Users\abdim\Desktop\PP2\labs\lab6\dir-and-files\copy.txt"
file = open(first_file, "r")
reading = file.read()
file.close()
file_2 = open(second_file, "w")
copying = file_2.write(reading)
file_2.close()
print("that is all")