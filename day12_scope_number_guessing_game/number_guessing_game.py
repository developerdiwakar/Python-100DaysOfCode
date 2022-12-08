#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def getTotalAttempts():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def playGame():
    print(logo)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Get total attemps according to difficulty level
    remaining_attempts = getTotalAttempts()
    # Set Answer
    answer = randint(1, 100)
    game_finished = False
    
    while not game_finished:
        print(f"You have {remaining_attempts} left to guess the number.")
        guess = int(input("Make a guess: "))
        if 100 < guess < 1:
            continue
        # apply game logic 
        if guess != answer:
            remaining_attempts -= 1
            if guess > answer:
                print("Too high.")
            else: 
                print("Too low.")
        else:
            print(f"You got it! The answer is {guess}")
            game_finished = True
        
        if remaining_attempts == 0:
            game_finished = True
            print(f"You have run out of the guesses, you lose.")
            print(f"The right answer is: {answer}")

# Start the game
playGame()