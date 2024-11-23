import random


def deal_card():
    random_card = random.choice(cards)
    return random_card


def card_total(cards):
    card_total = 0
    for card in cards:
        card_total += card
    return card_total


def hand_total(cards):
    hand_total = card_total(cards)
    if hand_total <= 21:
        return hand_total
    else:
        for card in cards:
            if hand_total > 21 and card == 11:
                hand_total -= 10
        return hand_total


def computer_hand():
    computer_hand = []
    if hand_total(computer_hand) < 17:
        while hand_total(computer_hand) < 17:
            computer_hand.append(deal_card())
        return computer_hand
    else:
        return_computer_hand


def determine_winner(player, computer):
    if hand_total(player) > 21:
        return False
    elif hand_total(computer) > 21:
        return True
    elif hand_total(player) > hand_total(computer):
        return True
    else:
        return False


def game_outcome(outcome):
    match outcome:
        case True:
            print("You win!")
            print(f"Your cards: {player_cards}")
            print(f"Your total: {hand_total(player_cards)}")
            print(f"Computer's final hand: {computer_cards}")
            print(f"Computer total: {hand_total(computer_cards)}")
        case False:
            print("You lose!")
            print(f"Your cards: {player_cards}")
            print(f"Your total: {hand_total(player_cards)}")
            print(f"Computer's final hand: {computer_cards}")
            print(f"Computer total: {hand_total(computer_cards)}")
        case _:
            print("It is a draw!")
            print(f"Your cards: {player_cards}")
            print(f"Your total: {hand_total(player_cards)}")
            print(f"Computer's final hand: {computer_cards}")
            print(f"Computer total: {hand_total(computer_cards)}")

            

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


player_cards = []
player_cards.append(deal_card())
player_cards.append(deal_card())


computer_cards = computer_hand()


print("\nWelcome to BLACKJACK!\n")


print(f"Your cards: {player_cards}")
print(f"Computer's first card: {computer_cards[0]}")


if hand_total(player_cards) == hand_total(computer_cards):
    game_outcome(0)
else:
    winner = determine_winner(player_cards, computer_cards)
    game_outcome(winner)


# TO-DO:
# - Make a conditional statement before determining winner to calculate a draw.
# - Computer must draw until at 17 or greater than stay.
# - Player gets 21 with first two cards should immediately win unless computer has 21, then tie.
# - Restart


