with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.readlines()

print(letter)
letter[0] = letter[0].replace('[name]', 'meow')
print(letter)


with open('./Input/Names/invited_names.txt', 'r') as file:
    names = file.readlines()
    for name in names:
        print(name)


