import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while not guessed_correctly:
        # Get the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        attempts += 1
        
        # Compare the user's guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
            print(f"It took you {attempts} attempts to guess the number.")

# Run the game
if __name__ == "__main__":
    guessing_game()
