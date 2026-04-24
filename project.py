import random

def get_guess():
    user_input = input("Enter your guess: ")

    while not user_input.isdigit():
        print("Invalid input, please enter a number.")
        user_input = input("Enter your guess: ")

    return int(user_input)

def play_game():
    number = random.randint(1,100)
    attemps = 0
    guessed_correctly = False
    guesses = []

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while not guessed_correctly:
        guess = get_guess()
        guesses.append(guess)
        attemps += 1
