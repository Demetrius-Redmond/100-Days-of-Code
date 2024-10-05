import random
print("Welcome to the Number Guessing Game!\n" "I'm thinking of a number between 1 and 100.")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] 
secret_number = random.choice(list)
attempts = 0
guess = ""




difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10   
else:
    attempts = 5
print(f"You have {attempts} remaining to guess the number.")

while guess != secret_number and attempts != 0:
    guess = int(input("Make a guess: "))
    if guess == secret_number:
        print(f"You got it! The answer was {secret_number}")
        
    elif attempts == 0:
        print("You've run out of guess, you lose.")
        
    elif guess < secret_number:
        attempts -= 1
        if attempts == 0:
            print("Too low.\n" "You've run out of guesses, you lose.")
            break
        print(f"Too low.\n" "Guess again.\n" f"You have {attempts} remaining to guess the number.")
    elif guess > secret_number:
        attempts -= 1
        if attempts == 0:
            print(f"Too high.\n" "You've run out of guesses, you lose.")
            break
        print(f"Too high.\n" "Guess again.\n" f"You have {attempts} remaining to guess the number.")
            



