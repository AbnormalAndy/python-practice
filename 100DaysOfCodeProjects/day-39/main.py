from data_manager import DataManager


datamanager = DataManager()


data = datamanager.get_request()


# Testing retrieving data, changing data, and then retrieving data again.
print(data['prices'][0])
print(data['prices'][0]['city'])
print(data['prices'][0]['iataCode'])
print(data['prices'][0]['lowestPrice'])


datamanager.city = 'Mexico'
datamanager.iataCode = 'MEOW1234'
datamanager.lowestPrice = 13
datamanager.row_number = 2


datamanager.put_request()


data = datamanager.get_request()


print(data['prices'][0])
print(data['prices'][0]['city'])
print(data['prices'][0]['iataCode'])
print(data['prices'][0]['lowestPrice'])


# Example GET Response
#{'prices':
#   [
#   {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
#   {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
#   {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
#   {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
#   {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
#   {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
#   {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
#   {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
#   {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}
#   ]
#}


# FlightSearch
# - Communicating with Amadeus API
# FlightData
# - Structuring Data
# DataManager
# - Communicating with Sheety API
# NotificationManager
# - Sending Email / Twilio


# TO-DO:
# 1. Use the Flight Search and Sheety API to populate copy of IATA codes for each city.
# 2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later.
# 3. If the price is lower than the lowest price listed in the Google Sheet, then send email / SMS.
# 4. The SMS should include the departure airport IATA code, destination airport IATA, flight price, and flight dates.
#     - "Low price alert! Only $255.09 to fly from LHR to CDG, on 2024-05-25 until 2024-11-20.


