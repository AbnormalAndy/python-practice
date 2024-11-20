from os import system


system('clear')
print("\nWelcome to the SECRET AUCTION!\n")


blind_auction = {}


finish_auction = False


while finish_auction != True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    blind_auction[name] = bid


    additional_bidders = input("Are there any other bidders? \"Yes\" or \"No\"\n")
    if additional_bidders.lower() != "yes":


        highest_bid = 0
        highest_bidder = {}


        for bidder in blind_auction:
            if blind_auction[bidder] > highest_bid:
                highest_bid = blind_auction[bidder]

        
        for bidder in blind_auction:
            if blind_auction[bidder] == highest_bid:
                highest_bidder[bidder] = blind_auction[bidder]


        if len(highest_bidder) > 1:
            system('clear')
            print("There is a tie!")
            for bidder in highest_bidder:
                print(f"{bidder.capitalize()} bid ${highest_bidder[bidder]}.")
        else:
            system('clear')
            for bidder in highest_bidder:
                print(f"\nThe winner is {bidder.capitalize()} with a bid of ${highest_bidder[bidder]}.\n")


        finish_auction = True

        
    else:
        system('clear')


