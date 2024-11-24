import random


GUESSES_EASY = 10
GUESSES_HARD = 5


print("Welcome to the NUMBER GUESSING GAME!")


end_game = False


while end_game != True:
    guess_number = random.choice(range(1, 101))


    print("I am thinking of a number between 1 and 100.")
    print(f"Pssst... the correct number is {guess_number}.")
    difficulty = input("Choose a difficulty. \"Easy\" or \"Hard\": ")


    difficulty_invalid = False


    match difficulty.lower():
        case "easy":
            difficulty = GUESSES_EASY
        case "hard":
            difficulty = GUESSES_HARD
        case _:
            difficulty = False
            difficulty_invalid = True


    while difficulty != 0:
        print(f"You have {difficulty} attempts remaining to guess the number.")
        guess_player = int(input("Make a guess: "))
        if guess_player == guess_number:
            break
        elif guess_player > guess_number:
            print("Too high.")
            difficulty -= 1
        elif guess_player < guess_number:
            print("Too low.")
            difficulty -= 1
        else:
            print("Error! Invalid player guess!")
            difficulty = False


    if difficulty_invalid == True:
        print("Invalid difficulty input! Please try again!")
    elif difficulty == 0:
        print("You have run out of guesses! You lose!")
    elif difficulty > 0:
        print(f"Congratulations! You guessed the correct number: {guess_number}!")
    else:
        print("Error! Difficulty < 0!")

    
    continue_game = input("Would you like to play again? \"Yes\" or \"No\": ")
    if continue_game.lower() != "yes":
        end_game = True
    else:
        difficulty_invalid = True


