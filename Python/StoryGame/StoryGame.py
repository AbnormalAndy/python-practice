print(r'''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________       \####/       _________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |====          .'.'^'.'.         ====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

''')

print("Rak'tika Cave\n\n")

print(r"""You find yourself at the entrance of Rak'tika's cavern.
""")

def prompt1():
    choice1 = input("Would you like to enter the cavern?\n\nYes (Y) - No (N)\n\n").lower()
    if choice1 == 'yes' or choice1 == 'y':
        print("\nYou enter dark mouth of Rak'tika's cavern.\n")
        prompt2()
    elif choice1 == 'torch':
        print("\nYou ignite the torch.\n")
        prompt3()
    elif choice1 == 'no' or choice1 == 'n':
        print("\nYou decide that the entrance of this cavern is too ominous and creepy. You head back to your room at the end and get a good night's sleep, never knowing what Rak'tika's cavern holds.\n")
    else:
        print("\nWrong input. Try again.\n")
        prompt1()

def prompt2():
    choice2 = input("Would you like to feel your way through the cavern from the left or right side?\n\nRight (R) - Left (L)\n\n").lower()
    if choice2 == 'right' or choice2 == 'r':
        print("Right")
    elif choice2 == 'left' or choice2 == 'l':
        print("Left")
    else:
        print("Wrong input. Try again.")
        prompt2()

def prompt3():
    choice2 = input("Would you like to pick up the sword?\n\nYes (Y) - No (N)\n\n").lower()
    if choice2 == 'yes' or choice2 == 'y':
        sword == True
        print("Yes")
    elif choice2 == 'no' or choice2 == 'n':
        print("No")
    else:
        print("Wrong input. Try again.")
        prompt3()

prompt1()

#if sword == True:
#    print("The dragon in front of you is monstrous. You fight a valorant fight and slay the dragon with the magical sword.\n\nYou take the dragon's treasure and set off into the sunset.")
#elif staff == True:
#    print("The dragon in front of you is monstrous.")
#else:
#    print("The dragon in front of you is monstrous. You prepare your fists. The dragon does not believe in mercy and devours you viciously.\n\nGame Over")


