import SecretAuctionArt

print(SecretAuctionArt.logo)

# Ask for Name Input
# Ask for Bid Price
# Add Name and Bid into Dictionary - Key / Value
# Ask if there are other users who would like to bid.
# Yes -> Clear Screen -> Restart Loop
# No -> Find the Highest Bidder -> Declare them the Winner

auction_dictionary = {}
def auction(bidder, price):
  auction_dictionary[bidder] = price

end_auction = False
while not end_auction:

  bidder_name = input("What is your name? ").lower()
  bid_price = int(input("What is your bid? "))
  auction(bidder_name, bid_price)
  continue_auction = input("Are there any others who would like to bid?\nYes (Y) - No (N)\n").lower()
  if continue_auction == 'no' or continue_auction == 'n':
    name = ''
    bid_price = 0
    for bidder in auction_dictionary:
      bid = auction_dictionary[bidder]
      if bid_price < bid:
        bid_price = bid
        name = bidder
    # clear()
    print("End of the auction.")
    print(f"The winner of the auction is {name.capitalize()} with a bid price of ${bid_price}.")
    print(auction_dictionary)
    end_auction = True
  else:
    # clear()
    print("Please add the next bidder.")
    print(auction_dictionary)