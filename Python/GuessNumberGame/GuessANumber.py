import random
from GuessANumberArt import logo



# Number of guesses depending on difficulty.
guesses_easy = 10
guesses_hard = 5



def compare(guess, number, guesses):
  """Compares the user's guess to the randomly generated number."""
  if guess > number:
    print("Too high.")
    return guesses - 1
  elif guess < number:
    print("Too low.")
    return guesses - 1
  elif guess == number:
    print(f"You guessed correctly! The number was {number}.")

def set_difficulty():
  """Sets the difficulty of the game."""
  level = input("Choose Difficulty: 'Easy' or 'Hard'\n").lower()
  if level == 'easy' or level == 'e':
    return guesses_easy
  else:
    return guesses_hard

def game():
  print(logo)
  print("Welcome to Number Guesser!")
  print("Pick a number between 1 and 100.")
  # Randomly generates a number to guess.
  number_to_guess = random.randint(0, 100)

  # Testing
  print(f"The number is {number_to_guess}")

  guesses = set_difficulty()
  guess = 0

  while guess != number_to_guess:
    print(f"You have a total of {guesses} guesses.")

    guess = int(input("Guess a Number: "))

    guesses = compare(guess, number_to_guess, guesses)
    if guesses == 0:
      print("You have run out of guesses. You lose.")
      return
    elif guess != number_to_guess:
      print("Guess again.")

game()