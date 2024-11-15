print("\nWelcome to Treasure Island")
print("Your mission is to find the treasure.")


def gameOver():
    print("Game Over\n")


def beginGame():
    print("\nYou are at a crossroad. Where would you like to go?")
    userChoice = input("    Type \"left\" or \"right\".\n").lower()

    while True:
        if userChoice == "left":
            return 2
            break
        elif userChoice == "right":
            print("\nYou fell into a hole.")
            return 0
            break
        else:
            print("\nInvalid response.")
            userChoice = input("    Type \"left\" or \"right\".\n").lower()


def goLeft():
    print("\nYou've come to a lake. There is an island in the middle of the lake.")
    userChoice = input("   Type \"wait\" to wait for a boat. "
                       "Type \"swim\" to swim across.\n").lower()

    while True:
        if userChoice == "wait":
            return 3
            break
        elif userChoice == "swim":
            print("\nYou were attacked by a trout.")
            return 0
            break
        else:
            print("\nInvalid response.")
            userChoice = input("   Type \"wait\" to wait for a boat. "
                               "Type \"swim\" to swim across.\n").lower()


def onIsland():
    print("\nYou arrive at the island unharmed."
          "There is a hosue with 3 doors."
          "One red, one yellow, and one blue."
          "Which color do you choose?")
    userChoice = input("    Type \"red\", \"yellow\", or \"blue\".\n").lower()

    while True:
        if userChoice == "red":
            print("\nYou were burned by fire.")
            return 0
        elif userChoice == "yellow":
            return 13
        elif userChoice == "blue":
            print("\nYou were eaten by beasts.")
            return 0
        else:
            print("\nInvalid response.")
            userChoice = input("    Type \"red\", \"yellow\", or \"blue\".\n").lower()


def win():
    print("\nCongratulations! You have obtained the treasure!\n")


decision = 1

decisionDict = {
    0:  gameOver,
    1:  beginGame,
    2:  goLeft,
    3:  onIsland,
    13: win
}

def processDecision(number):
    return decisionDict[number]()


while True:
    decision = processDecision(decision)

    if decision == 0:
        processDecision(decision)
        print("Would you like to play again?")
        userChoice = input("    \"Yes\" or \"No\"\n").lower()
        if userChoice == "yes":
            print("\nYou wake up from a dream...")
            decision = 1
        else:
            break

    if decision == 13:
        processDecision(decision)
        print("Would you like to play again?")
        userChoice = input("    \"Yes\" or \"No\"\n").lower()
        if userChoice == "yes":
            print("\nYou wake up from a dream...")
            decision = 1
        else:
            break


print("\nThanks for playing!\n")
