

      
    


import random

def guess_the_number():
    """
    A simple number guessing game.
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = 0
    attempts = 0

    print("--- Welcome to the Number Guessing Game! ---")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
