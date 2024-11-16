import random


choiceDict = {
    0:  "Rock",
    1:  "Paper",
    2:  "Scissors"
}


endGame = False


while endGame != True:
    userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    computerChoice = random.randint(0, 2)


    print(userChoice)
    print(computerChoice)


    if userChoice == 0 and computerChoice == 2:
        print(f"You chose: {choiceDict[userChoice]}.")
        print(f"Computer chose: {choiceDict[computerChoice]}.")
        print(f"You win!")
    elif userChoice == 1 and computerChoice == 0:
        print(f"You chose: {choiceDict[userChoice]}.")
        print(f"Computer chose: {choiceDict[computerChoice]}.")
        print(f"You win!")
    elif userChoice == 2 and computerChoice == 1:
        print(f"You chose: {choiceDict[userChoice]}.")
        print(f"Computer chose: {choiceDict[computerChoice]}.")
        print(f"You win!")
    elif userChoice == computerChoice:
        print(f"You chose: {choiceDict[userChoice]}.")
        print(f"Computer chose: {choiceDict[computerChoice]}.")
        print(f"You draw!")
    else:
        print(f"You chose: {choiceDict[userChoice]}.")
        print(f"Computer chose: {choiceDict[computerChoice]}.")
        print(f"You lose!")

    
    continueGame = input("Would you like to try again? \"Yes\" or \"No\"\n").lower()
    if continueGame != "yes":
        endGame = True


print("Thanks for playing!")
