list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


user_decision = input("\"Encode\" or \"Decode\"\n")


if user_decision.lower() == "encode":
    shift = int(input("How many letters would you like to shift?\n"))
    phrase = input("What would you like to encode?\n")
    secret_cipher = ""

    for letter in phrase:
        if letter == " ":
            secret_cipher += " "
        else:
            total = list_alphabet.index(letter) + shift
            if total > 25:
                total = total - 26
            secret_cipher += list_alphabet[total]

    print(secret_cipher)


if user_decision.lower() == "decode":
    shift = int(input("How many letters would you like to shift?\n"))
    phrase = input("What would you like to decode?\n")
    secret_cipher = ""

    for letter in phrase:
        if letter == " ":
            secret_cipher += " "
        else:
            total = list_alphabet.index(letter) - shift
            if total < -25:
                total = total + 26
            secret_cipher += list_alphabet[total]

    print(secret_cipher)


