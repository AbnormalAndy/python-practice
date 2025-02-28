import pandas


nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}


def generate_phonetic():
    user_input = input('\nEnter a word: ').upper()
    try:
        user_input_nato_alphabet = [nato_alphabet_dict[letter] for letter in user_input]


    except KeyError as error_message:
        print('Please use a letter in the alphabet.')
        generate_phonetic()


    else:
        print(f'\nNato Alphabet Output: {"-".join(user_input_nato_alphabet)}\n')


generate_phonetic()


