def is_polindrome(string):
    string = string.lower().strip()
    if string == string[::-1]:
        return True  
    return False  

word = input()
print(is_polindrome(word))
