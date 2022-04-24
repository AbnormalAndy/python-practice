import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input("How many symbols would you like in your password?\n"))

nr_numbers = int(input("How many numbers would you like in your password?\n"))

total_char = ""
random_char = []
random_pass = ""

for char in range(0, nr_letters):
    total_char += random.choice(letters)
    random_char += random.choice(letters)

for char in range(0, nr_symbols):
    total_char += random.choice(symbols)
    random_char += random.choice(symbols)

for char in range(0, nr_numbers):
    total_char += random.choice(numbers)
    random_char += random.choice(numbers)

random.shuffle(random_char)

for i in random_char:
    random_pass += i

print(total_char)
print(random_pass)