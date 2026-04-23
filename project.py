import random

def play_game():
    number = random.randint(1,100)
    attemps = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
