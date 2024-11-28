import game_data
import os
import random


def outcome_choice(follower_count_one, follower_count_two, follower_count_player_choice):
    if follower_count_one > follower_count_two and follower_count_one == follower_count_player_choice:
        return 1
    elif follower_count_two > follower_count_one and follower_count_two == follower_count_player_choice:
        return 2
    else:
        return 3


os.system('clear')


print("\nHIGHER or LOWER\n")


score = 0


end_game = False


while end_game != True:
    if score > 0:
        print(f"\nYou are right! Current score: {score}.\n")


    instagram_a = random.choice(game_data.data)
    instagram_b = random.choice(game_data.data)


    while instagram_a == instagram_b:
        instagram_b = random.choice(game_data.data)
    

    valid_player_choice = False


    while valid_player_choice != True:
        print(f"\nCompare A: {instagram_a['name']}, a {instagram_a['description']}, from {instagram_a['country']}.")
        #DEBUG Statement: print(f"Follower Count: {instagram_a['follower_count']}.")
        print(f"\nCompare B: {instagram_b['name']}, a {instagram_b['description']}, from {instagram_b['country']}.")
        #DEBUG Statement: print(f"Follower Count: {instagram_b['follower_count']}.")


        player_choice = input("\nWho has more followers? Type 'A' or 'B': ")


        match player_choice.lower():
            case "a":
                player_choice = instagram_a
                valid_player_choice = True
            case "b":
                player_choice = instagram_b
                valid_player_choice = True
            case _:
                print("\nPlease choose again.")


    outcome = outcome_choice(instagram_a['follower_count'], instagram_b['follower_count'], player_choice['follower_count'])
    print(outcome)


    match outcome:
        case 1:
            os.system('clear')
            score += 1
            print(f"\nMore Followers ({instagram_a['follower_count']}): {instagram_a['name']}, a {instagram_a['description']}, from {instagram_a['country']}.")
            print(f"\nLess Followers ({instagram_b['follower_count']}): {instagram_b['name']}, a {instagram_b['description']}, from {instagram_b['country']}.\n")
        case 2:
            os.system('clear')
            score += 1
            print(f"\nMore Followers ({instagram_b['follower_count']}): {instagram_b['name']}, a {instagram_b['description']}, from {instagram_b['country']}.")
            print(f"\nLess Followers ({instagram_a['follower_count']}): {instagram_a['name']}, a {instagram_a['description']}, from {instagram_a['country']}.\n")
        case _:
            os.system('clear')
            print(f"\n\nSorry! That is wrong. Final score: {score}.\n\n")
            end_game = True


