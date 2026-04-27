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
        
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
        else:
            guesses.append(guess)
            attempts += 1
        
            if  guess > number:
                print("Too high")
            elif guess < number:
                print("Too low")
            else:
                print("Correct!")
                print("Congratulations!")
                print("Attempts:", attempts)
                print("Your guesses were:", guesses)
                guessed_correctly = True
                
play_game()
