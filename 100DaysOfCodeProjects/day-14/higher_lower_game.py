import random
import game_data


print("\nHIGHER or LOWER\n")


score = 0


end_game = False


while end_game != True:
    if score > 0:
        print(f"\nYou are right! Current score: {score}.\n")


    # Could get the same Instagram user.
    # TO-DO: Choose until not the same.
    instagram_a = random.choice((game_data.data))
    instagram_b = random.choice((game_data.data))


    print(f"\nCompare A: {instagram_a['name']}, a {instagram_a['description']}, from {instagram_a['country']}.")
    #print(f"Follower Count: {instagram_a['follower_count']}.\n")
    print(f"\nCompare B: {instagram_b['name']}, a {instagram_b['description']}, from {instagram_b['country']}.")
    #print(f"Follower Count: {instagram_b['follower_count']}.\n")


    # TO-DO: Make this a separate function.
    player_choice = input("\nWho has more followers? Type 'A' or 'B': ")
    if player_choice.lower() == "a":
        player_choice = instagram_a
    elif player_choice.lower() == "b":
        player_choice = instagram_b
    else:
        print("Please choose again.")


    # TO-DO: Refactor. Separate function?
    if instagram_a['follower_count'] > instagram_b['follower_count']:
        print(f"\nMore Followers ({instagram_a['follower_count']}): {instagram_a['name']}, a {instagram_a['description']}, from {instagram_a['country']}.\n")
        if player_choice == instagram_a:
            score += 1
        else:
            print(f"\nSorry! That is wrong. Final score: {score}.\n")
            end_game = True
    else:
        print(f"\nMore Followers ({instagram_b['follower_count']}): {instagram_b['name']}, a {instagram_b['description']}, from {instagram_b['country']}.\n")
        if player_choice == instagram_b:
            score += 1
        else:
            print(f"\nSorry! That is wrong. Final score: {score}.\n")
            end_game = True


# TO-DO:
# - Ask who has more followers on instagram.
# - Continues until wrong answer.
# - Display Score
# - End game when wrong answer.
# - Clear screen with correct or wrong guess.


