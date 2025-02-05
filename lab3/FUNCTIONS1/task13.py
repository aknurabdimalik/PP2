import random

def guess_number():
    number_to_guess = random.randint(1, 20)
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        guess = int(input("Take a guess: "))  
        attempts += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break  

guess_number()
