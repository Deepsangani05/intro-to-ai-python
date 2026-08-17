# ==============================================================================
# Loops and Conditionals in Python
# ==============================================================================
# This program demonstrates control structures in Python:
# - Conditionals: if, elif, else
# - Loops: for, while, break, continue
# It implements a interactive Number Guessing Game.
# ==============================================================================

import random
import time

def main():
    print("==================================================")
    print("Welcome to the AI Number Guessing Game!")
    print("==================================================")
    
    # 1. demonstrating a standard 'for' loop (Game Setup Countdown)
    print("Initializing game engine. Get ready...")
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(0.5)
    print("Go!\n")

    # Generate a random secret number between 1 and 50
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 6
    
    print(f"I have selected a secret number between 1 and 50.")
    print(f"You have {max_attempts} attempts to guess it correctly!")
    print("--------------------------------------------------")

    # 2. demonstrating a 'while' loop with conditionals
    while attempts < max_attempts:
        attempts += 1
        guess_str = input(f"Attempt {attempts}/{max_attempts} - Enter your guess: ")
        
        # Validate input is numeric
        if not guess_str.isdigit():
            print("Invalid input! Please enter a whole number.")
            attempts -= 1  # Do not penalize for bad input
            continue
            
        guess = int(guess_str)
        
        # 3. demonstrating nested 'if-elif-else' conditionals
        if guess < 1 or guess > 50:
            print("Remember, the number is between 1 and 50!")
            attempts -= 1  # Do not penalize
            continue
            
        if guess < secret_number:
            print("Too LOW! Try a higher number.")
        elif guess > secret_number:
            print("Too HIGH! Try a lower number.")
        else:
            # Player guessed it correctly!
            print(f"\n*** CONGRATULATIONS! You found the secret number {secret_number} in {attempts} attempts! ***")
            break
            
        # Give hints along the way using modulus (even/odd hint)
        if attempts == 3 and guess != secret_number:
            print("[Hint] ", end="")
            if secret_number % 2 == 0:
                print("The secret number is an EVEN number.")
            else:
                print("The secret number is an ODD number.")
        print()

    # 4. else clause on while-loop or simple fallback if player ran out of attempts
    if attempts >= max_attempts and guess != secret_number:
        print("\n[Game Over] You've run out of attempts.")
        print(f"The secret number was: {secret_number}. Better luck next time!")
    
    print("\n--------------------------------------------------")
    print("Summary of numbers you could have guessed (Demo of 'for' loop filtering):")
    # Demonstrate 'for' loop and 'continue' by showing even numbers in a range
    print("Even numbers from 2 to 10: ", end="")
    for num in range(1, 11):
        if num % 2 != 0:
            continue  # skip odd numbers
        print(num, end=" ")
    print("\n==================================================")

if __name__ == "__main__":
    main()
