import random
import listofwords


def start_game():
    end_game = False

    
    while end_game == False:
        print("\nWelcome to the WORD GUESSING GAME!\n")

        word_to_win = list(random.choice(listofwords.words))
        #print(f"(DEBUG) Word to win is: {"".join(word_to_win)}")
        player_word = ["_"] * len(word_to_win)


        print(f"Word to guess: {" ".join(player_word)}")


        guesses = 5
        guessing = True 


        while guessing == True:
            print(f"\nNumber of guesses: {guesses}")
            player_choice = input("Guess a letter: ")


            if player_choice in player_word:
                guesses -= 1
                print("\nAlready guessed this letter!")
                print(" ".join(player_word))
                print(f"You have {guesses} guesses remaining.")
            elif player_choice in word_to_win:
                for letter in range(len(player_word)):
                    if player_choice == word_to_win[letter]:
                        player_word[letter] = player_choice
                print(" ".join(player_word))
                print(f"You have {guesses} guesses remaining.")
            else:
                guesses -= 1
                print("\nWrong guess!")
                print(" ".join(player_word))
                print(f"You have {guesses} guesses remaining.")


            if guesses == 0:
                print("\nYou lose!")
                print(f"The correct word was: {"".join(word_to_win)}")
                continue_game = input("Would you like to play again? \"Yes\" or \"No\" ").lower()
                if continue_game != "yes":
                    print("\nThanks for playing!\n")
                    guessing = False
                    end_game = True
                else:
                    guessing = False
            else:
                if word_to_win == player_word:
                    print(f"\nCongratulations! You guessed the correct word: {"".join(player_word)}")
                    continue_game = input("Would you like to play again? \"Yes\" or \"No\" ").lower()
                    if continue_game != "yes":
                        print("\nThanks for playing!\n")
                        guessing = False
                        end_game = True
                    else:
                        guessing = False
                        print("\nThanks for playing!\n")


start_game()
