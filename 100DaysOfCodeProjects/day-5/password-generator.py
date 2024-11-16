import lists
import random


print("Welcome to the PyPassword Generator!")


password = []


numberOfLetters = int(input("How many letters would you like in your password?\n"))
for x in range(0, numberOfLetters):
    password.append(random.choice(lists.letters))


numberOfNumbers = int(input("How many numbers would you like?\n"))
for x in range(0, numberOfNumbers):
    password.append(random.choice(lists.numbers))


numberOfSymbols = int(input("How many symbols would you like?\n"))
for x in range(0, numberOfSymbols):
    password.append(random.choice(lists.symbols))


random.shuffle(password)
finalPassword = ''.join(password)
print(f"Here is your password: {finalPassword}")
