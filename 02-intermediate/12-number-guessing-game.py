from random import randint

# import logo
import importlib.util
import sys
import os

# Path to the file
file_path = os.path.join(os.path.dirname(__file__), "Day 12 - Art.py")

spec = importlib.util.spec_from_file_location("art", file_path)
art = importlib.util.module_from_spec(spec)
sys.modules["art"] = art
spec.loader.exec_module(art)

#

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of guesses remaining"""
    if user_guess > actual_answer:
        print("Too High.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        # global turns
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(art.logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100) # randint includes 1 and 100
    print(f"Pssst, the correct answer is {answer}") # Hint

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

    # Track the number of turns and reduce by 1 if they get it wrong



game()