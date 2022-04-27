import SecretAuctionArt

print(SecretAuctionArt.logo)

# Yes -> Clear Screen -> Restart Loop
# No -> Find the Highest Bidder -> Declare them the Winner

# Empty dictionary for the auction.
auction_dictionary = {}

# Function to add bidder and respective bid price.
def auction(bidder, price):
  auction_dictionary[bidder] = price

end_auction = False
while not end_auction:

  # Ask for Name Input
  bidder_name = input("What is your name? ").lower()
 
  # Ask for Bid Price
  bid_price = int(input("What is your bid? "))

  # Add Name and Bid into Dictionary - Key / Value
  auction(bidder_name, bid_price)

  # Ask if there are other users who would like to bid.
  continue_auction = input("Are there any others who would like to bid?\nYes (Y) - No (N)\n").lower()
  if continue_auction == 'no' or continue_auction == 'n':
    # Finds the highest bidder.
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
    end_auction = True
  else:
    # Adds another bidder.
    # clear()
    # print(auction_dictionary)
    print("Please add the next bidder.")