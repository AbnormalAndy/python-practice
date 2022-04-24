import random
import GuessGameWords
import GuessGameArt

chosen_word = random.choice(GuessGameWords.word_list)

end_of_game = False
lives = 6

# The logo.
print(GuessGameArt.logo)

# Testing code.
print(f'\nThe solution is {chosen_word}.\n')

# Create blanks.
display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    guess = input("Guess a Letter: ").lower()

    # Check if guess has already been guessed.
    if guess in display:
        print(f'\nLetter "{guess.capitalize()}" has already been guessed. Try again.')

    # Check guessed letter.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f'\nThe letter "{guess.capitalize()}" is not in the word.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.\n")

    # Print the stage.
    print(GuessGameArt.stages[lives])

    # Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}\n")