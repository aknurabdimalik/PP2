text = input("Enter string:")
uppercase = len([char for char in text if char.isupper()])
lowercase = len([char for char in text if char.islower()])
print("Upper case letters:", uppercase)
print("Lower case letters:", lowercase)