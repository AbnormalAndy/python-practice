import pandas


nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}


user_input = input('\nEnter a word: ').upper()
user_input_nato_alphabet = [nato_alphabet_dict[letter] for letter in user_input]


print(f'\nNato Alphabet Output: {"-".join(user_input_nato_alphabet)}\n')


