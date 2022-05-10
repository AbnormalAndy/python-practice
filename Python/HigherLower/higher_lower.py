import random
from higher_lower_game_data import data
from os import system, name
from higher_lower_art import logo, vs



def clear():
  """Clear screen."""
  # For Windows
  if name == 'nt':
      _ = system('cls')  
  # For Mac and Linux
  # os.name is 'posix'
  else:
      _ = system('clear')

def choices():
  """Randomly select two choices from data and then return both choices as a list."""
  choice_a = list(random.choice(data).values())
  choice_b = list(random.choice(data).values())
  
  while choice_a == choice_b:
    choice_b = list(random.choice(data).values())

  return choice_a, choice_b

def compare_random_choices(first_choice, second_choice):
  """Compare choices and return a designated value."""
  if first_choice > second_choice:
    return 0
  elif first_choice < second_choice:
    return 1
  else:
    return 2

def compare_user_computer(user, computer):
  """Compare user and computer choices and return a designated value."""
  if user == 2 or computer == 2:
    print("Error")
  elif user != computer:
    return 0
  elif user == computer:
    return 1

def user_input():
  """Request user choice and return a designated value."""
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if guess == 'a':
    return 0
  elif guess == 'b':
    return 1
  else:
    return 2



score = 0
result = 5

end_of_game = False
while not end_of_game:

  print(logo)

  # Evaluate to end game or add to score.
  if result == 0:
    print(f"Sorry! That is wrong. Final Score: {score}.")
    end_of_game = True
    break
  if result == 1:
    score += 1
    print(f"You are right! Current Score: {score}.")

  # Assign each returned list from the choices() function to a variable.
  a = choices()[0]
  b = choices()[1]

  print(f"Compare A: {a[0]}, a {a[2]}, from {a[3]}.")

  print(vs)

  print(f"Against B: {b[0]}, a {b[2]}, from {b[3]}.")
  
  ## Debug Print Statements
  #print(a[1])
  #print(b[1])

  # Assign user_input() function to a variable.
  guess = user_input()

  # Compare user's guess and computer choice.
  result = compare_user_computer(guess, compare_random_choices(a[1], b[1]))
  clear()