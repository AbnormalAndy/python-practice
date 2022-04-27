import SecretAuctionArt

print(SecretAuctionArt.logo)

# Yes -> Clear Screen -> Restart Loop
# No -> Find the Highest Bidder -> Declare them the Winner

# Empty dictionary for the auction.
auction_dictionary = {}

# End while loop condition.
end_auction = False

# Function to add bidder and respective bid price.
def auction(record_of_bid):
    name = ''
    bid_price = 0
    for bidder in auction_dictionary:
      bid = auction_dictionary[bidder]
      if bid_price < bid:
        bid_price = bid
        name = bidder
    # clear()
    # print(auction_dictionary)
    print("End of the auction.")
    print(f"The winner of the auction is {name.capitalize()} with a bid price of ${bid_price}.")



while not end_auction:

  # Ask for Name Input
  bidder_name = input("What is your name? ").lower()

  # Ask for Bid Price
  bid_price = int(input("What is your bid? "))

  # Add to the auction dictionary.
  auction_dictionary[bidder_name] = bid_price

  # Ask if there are other users who would like to bid.
  continue_auction = input("Are there any others who would like to bid?\nYes (Y) - No (N)\n").lower()
  if continue_auction == 'no' or continue_auction == 'n':
    end_auction = True
    # Finds the highest bidder.
    auction(auction_dictionary)
  elif continue_auction == 'yes' or continue_auction == 'y':
    # Adds another bidder.
    # clear()
    # print(auction_dictionary)
    print("Please add the next bidder.")