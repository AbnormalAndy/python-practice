class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username.capitalize()
        self.followers = 0
        self.following = 0
        print(f"New user being created... {self.username}.")


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_one = User("001", "meow")


user_two = User("002", "jack")


user_two.follow(user_one)


print(user_one.id, user_one.username, user_one.followers, user_one.following)
print(user_two.id, user_two.username, user_two.followers, user_two.following)


