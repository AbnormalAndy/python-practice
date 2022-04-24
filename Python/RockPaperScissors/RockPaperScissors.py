import random
import RockPaperScissorsArt

game_images = [RockPaperScissorsArt.rock, RockPaperScissorsArt.paper, RockPaperScissorsArt.scissors]

print("Rock Paper Scissors\n")

user_choice = int(input("What do you choose?\nType: 0 for Rock - 1 for Paper - 2 for Scissors\n\n"))

if user_choice >= 3 or user_choice < 0: 
  print("\nYou typed an invalid number. You LOSE!")
else:
    print("\nYour Choice")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Choice")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You WIN!")
    elif computer_choice == 0 and user_choice == 2:
        print("You LOSE!")
    elif computer_choice > user_choice:
        print("You LOSE!")
    elif user_choice > computer_choice:
        print("You WIN!")
    elif computer_choice == user_choice:
        print("It is a draw.")