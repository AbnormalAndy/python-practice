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


def player_hand():
    player_hand = []
    player_hand.append(deal_card())
    player_hand.append(deal_card())
    return player_hand


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
            print(f"\n\nYour cards: {player_cards}")
            print(f"Your total: {hand_total(player_cards)}")
            print(f"\nComputer's final hand: {computer_cards}")
            print(f"Computer total: {hand_total(computer_cards)}\n")
            print("\nYou win!\n")
        case False:
            print(f"\n\nYour cards: {player_cards}")
            print(f"Your total: {hand_total(player_cards)}")
            print(f"\nComputer's final hand: {computer_cards}")
            print(f"Computer total: {hand_total(computer_cards)}\n")
            print("\nYou lose!\n")
        case 13:
            print(f"\n\nYour cards: {player_cards}")
            print(f"Your total: {hand_total(player_cards)}")
            print(f"\nComputer's final hand: {computer_cards}")
            print(f"Computer total: {hand_total(computer_cards)}\n")
            print("\nBLACKJACK! You WIN!\n")
        case 0:
            print(f"\n\nYour cards: {player_cards}")
            print(f"Your total: {hand_total(player_cards)}")
            print(f"\nComputer's final hand: {computer_cards}")
            print(f"Computer total: {hand_total(computer_cards)}\n")
            print("\nIt is a draw!\n")
        case _:
            print("\n\nInvalid outcome. Please evaluate code.\n")
            

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


end_blackjack = False


while end_blackjack != True:
    player_cards = player_hand()
    computer_cards = computer_hand()


    print("\n\nBLACKJACK!\n")


    print(f"\nYour cards: {player_cards}\n")
    print(f"Computer's first card: {computer_cards[0]}\n")


    stop_adding_cards = False


    if hand_total(player_cards) == 21:
        stop_adding_cards = True


    while stop_adding_cards != True:
        another_card = input("\nType \"Yes\" for another card. Type \"No\" to pass.\n")
        if another_card.lower() != "yes":
            stop_adding_cards = True
        else:
            player_cards.append(deal_card())
            if hand_total(player_cards) > 21:
                stop_adding_cards = True
            else:
                print(f"\nYour cards: {player_cards}")
                print(f"Your total: {hand_total(player_cards)}\n")


    if hand_total(player_cards) == hand_total(computer_cards):
        game_outcome(0)
    elif hand_total(player_cards) == 21:
        game_outcome(13)
    else:
        winner = determine_winner(player_cards, computer_cards)
        game_outcome(winner)


    continue_blackjack = input("\nDo you want to play a game of Blackjack? \"Yes\" or \"No\"\n")
    if continue_blackjack.lower() != "yes":
        print("\nThank you for playing BLACKJACK!\n")
        end_blackjack = True
    else:
        stop_adding_cards = False


