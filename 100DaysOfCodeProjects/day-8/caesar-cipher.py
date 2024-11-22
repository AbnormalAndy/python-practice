list_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("\nWelcome to the CAESAR CIPHER!\n")


end_program = False


while end_program != True:
    secret_cipher = ""


    user_decision = input("Choose: \"Encode\" or \"Decode\"\n")


    if user_decision.lower() == "encode" or user_decision.lower() == "decode":
        phrase = input("\nWhat is to be encoded or decoded?\n")
        shift = int(input("\nHow many letters is the shift?\n"))


        for letter in phrase:
            if letter == " ":
                secret_cipher += " "
            elif user_decision.lower() == "encode":
                total = list_alphabet.index(letter) + shift
                if total > 25:
                    total = total - 26
                secret_cipher += list_alphabet[total]
            elif user_decision.lower() == "decode":
                total = list_alphabet.index(letter) - shift
                if total < -25:
                    total = total + 26
                secret_cipher += list_alphabet[total]



        print(f"\nSecret Cipher: {secret_cipher}")


        restart_decision = input("\nWould you like to restart? \"Yes\" or \"No\"\n")
        

        if restart_decision.lower() != "yes":
            print("\nThank you for using the Caesar Cipher!\n")
            end_program = True
        else:
            print("\nPlease choose one of the following choices.")


    else:
        print("\nInvalid choice. Please try again!.")
        print("Please choose one of the following choices.")


