def is_polindrome(string):
    string = string.lower().strip()
    if string == string[::-1]:
        return True  
    return False  

word = input()
print(is_polindrome(word))

"""
def is_polindrome(string):

    cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
    left, right = 0, len(cleaned_string) - 1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
    return True
word = input()
print(is_polindrome(word))
"""
