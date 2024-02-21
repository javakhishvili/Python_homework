

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (between 1 and 100): ")

        
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

       
        attempts += 1

       
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try again. The number is higher.")
        else:
            print("Try again. The number is lower.")


number_guessing_game()