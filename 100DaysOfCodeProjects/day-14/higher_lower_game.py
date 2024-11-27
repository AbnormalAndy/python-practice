import random
import game_data


print("HIGHER or LOWER")


# Could get the same Instagram user.
# TO-DO: Choose until not the same.
instagram_a = random.choice((game_data.data))
instagram_b = random.choice((game_data.data))


print(f"Compare A: {instagram_a['name']}, a {instagram_a['description']}, from {instagram_a['country']}.")
print(f"Follower Count: {instagram_a['follower_count']}.")
print(f"Compare B: {instagram_b['name']}, a {instagram_b['description']}, from {instagram_b['country']}.")
print(f"Follower Count: {instagram_b['follower_count']}.")


if instagram_a['follower_count'] > instagram_b['follower_count']:
    print(f"More Followers ({instagram_a['follower_count']}): {instagram_a['name']}, a {instagram_a['description']}, from {instagram_a['country']}.")
else:
    print(f"More Followers ({instagram_b['follower_count']}): {instagram_b['name']}, a {instagram_b['description']}, from {instagram_b['country']}.")


# TO-DO:
# - Ask who has more followers on instagram.
# - Continues until wrong answer.
# - Display Score
# - End game when wrong answer.


