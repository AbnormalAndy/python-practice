import random
from BlackjackArt import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw(num):
  """Draw a chosen number of cards randomly."""
  hand = []
  for num_cards in range(0, num):
    card_number = random.randint(0, 12)
    hand.append(cards[card_number])
  return hand

def eleven_finder(list):
  """Find 11 and convert to 1."""
  list[:] = [1 if x==11 else x for x in list]
  return list

def winner(player, dealer):
  """Defines winner."""  
  if player > 21:
    return False
  elif player > dealer or player == 21 and player < 22 and dealer < 22:
    return True
  elif player > dealer or dealer > 21 and player < 22:
    return True
  elif dealer > player or dealer == 21 and player < 22 and dealer < 22:
    return False

def outcome(decision, player, player_total, dealer, dealer_total):
  """Prints the outcome."""
  player_hand = player
  player_hand_total = player_total
  dealer_hand = dealer
  dealer_hand_total = dealer_total
  if decision == True:
    print(f"\nYou WIN with {player_hand}: {player_hand_total}.")
    print(f"The dealer has {dealer_hand}: {dealer_hand_total}.\n")
  elif decision == False:
    print(f"\nYou LOSE with {player_hand}: {player_hand_total}.")
    print(f"The dealer has {dealer_hand}: {dealer_hand_total}.\n")
  else:
    print("\nIt is a push.")
    print(f"You have {player_hand}: {player_hand_total}.")
    print(f"The dealer has {dealer_hand}: {dealer_hand_total}.\n")

def dealer():
  """Dealer hand."""
  dealer_hand = draw(2)

  # Draw cards until a win or lose hand.
  end_hand = False
  while not end_hand:
    hand_total = 0
    hand_total = sum(dealer_hand)

    ##Debug print statements.
    # print(dealer_hand)
    # print(hand_total)

    # Replaces 11 if soft 17.
    if hand_total == 17 and 11 in dealer_hand:  
      dealer_hand = eleven_finder(dealer_hand)
      hand_total = sum(dealer_hand)
      if hand_total >= 17:
        end_hand = True
        return dealer_hand
    # Returns dealer hand if hard 17 or greater.
    elif hand_total == 21 or hand_total >= 17 and hand_total < 22:
      end_hand = True
      return dealer_hand
    # Returns dealer hand if busts.
    elif hand_total > 21:
      end_hand = True
      return dealer_hand
    # If conditions not met above, dealer draws a card.
    dealer_hand += draw(1)

def blackjack():
  # Dealer hand and total.
  dealer_hand = dealer()
  dealer_hand_total = sum(dealer_hand)

  # Player hand.
  player_hand = draw(2)
  
  end_of_game = False
  while not end_of_game:
  
    # Resets player hand total to 0 and calculates the hand.
    player_hand_total = 0
    player_hand_total = sum(player_hand)
  
    print(f"\nYour Hand: {player_hand}. Your Total: {player_hand_total}.")
    print(f"The dealer's first card is a {dealer_hand[0]}.\n")
    player_input = input("Would you like to draw another card? Yes (Y) or No (N)\n").lower()

    # Receives player input of yes.
    if player_input == "yes" or player_input == "y":
      player_hand += draw(1)

      # If 11 in hand and hand > 21, will try to reduce the hand before calculating a loss.
      if player_hand_total > 21 and 11 in player_hand:
        player_hand = eleven_finder(player_hand)
      player_hand_total = sum(player_hand)

      # Player busts if hand > 21.
      if player_hand_total > 21:
        result = False
        outcome(result, player_hand, player_hand_total, dealer_hand, dealer_hand_total)
        print("You busted.\n")
        end_of_game = True

    # Receives player input of no.
    elif player_input == "no" or player_input == "n":
      # Calculates winner.
      result = winner(player_hand_total, dealer_hand_total)
      # Prints the outcome based on the winner.
      outcome(result, player_hand, player_hand_total, dealer_hand, dealer_hand_total)
      end_of_game = True



# The start of the game.
print(logo)
try_again = False
while not try_again:
  reset = input("Would you like to play Blackjack? Yes (Y) - No (N)\n").lower()
  if reset == 'yes' or reset == 'y':
    blackjack()
  else:
    try_again = True