# PRODIGY_SD_02
# Number Guessing Game

Welcome to the Number Guessing Game! 🎮

This project is a simple and engaging Python program that challenges users to guess a randomly generated number. It is a great exercise for beginners looking to practice basic programming concepts such as loops, conditionals, and user input handling.

## Project Overview

The Number Guessing Game works as follows:
1. **Random Number Generation**: The program generates a random number between 1 and 100.
2. **User Interaction**: Users are prompted to guess the number.
3. **Feedback**: The program provides feedback on whether the guess is too high or too low.
4. **Attempts Tracking**: The program keeps track of the number of attempts it takes for the user to guess the number correctly.
5. **Completion**: When the correct number is guessed, the program congratulates the user and displays the total number of attempts.

## Features

- Generates a random number between 1 and 100.
- Provides real-time feedback on user guesses (too high or too low).
- Handles invalid inputs gracefully.
- Counts and displays the number of attempts taken to guess the number correctly.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Roshith42/number-guessing-game.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd number-guessing-game
   ```
3. **Run the Game**:
   Ensure you have Python installed. Run the game using:
   ```bash
   python guessing_game.py
   ```

## Code Explanation

- The game generates a random number between 1 and 100 using `random.randint()`.
- The program uses a `while` loop to continuously prompt the user until the correct number is guessed.
- It provides feedback on whether the guess is too high or too low.
- Invalid inputs are handled to ensure the user enters an integer.
- The number of attempts is tracked and displayed when the user guesses correctly.

## Contributing

Feel free to fork this repository and contribute! If you have any suggestions or improvements, please submit a pull request or open an issue.
