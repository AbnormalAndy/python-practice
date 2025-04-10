# Open and read letter file.
with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.readlines()


# Open and read names file.
with open('./Input/Names/invited_names.txt', 'r') as file:
    names = file.readlines()


# Iterate through names and creating a letter with the name.
for name in names:
    new_name = name.strip('\n')
    new_letter = [l.replace('[name]', new_name) for l in letter]


    # Write letter to Output directory.:
    with open(f'./Output/ReadyToSend/invite_for_{new_name}.txt', mode='w') as file:
        file.writelines(new_letter)


# Why does this work:
# - new_letter = [l.replace('[name]', new_name) for l in letter]

# Why does this NOT work:
# - new_letter[0] = letter[0].replace('[name]', new_name)
#     - This seems to replace the original list.


