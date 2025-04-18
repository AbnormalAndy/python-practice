import config
import requests


API_KEY_SHEETY = config.API_KEY_SHEETY
SHEETY_ENDPOINT = 'https://api.sheety.co/99857e1bc2a42bffc6f6a39865ac096e/flightDeals/prices/'


class DataManager:
    # Make class.
    sheety_params = {
        # Key must be CAMEL CASE and NO spaces even if the Google Sheets column title is title cased and has spaces.
        'price': {
            'city': 'Test',
            'iataCode': 'TestTestTest',
            'lowestPrice': 12345,
        }
    }


    sheety_header = {
        'Authorization': f'Bearer {API_KEY_SHEETY}',
    }


    #sheety_put_response = requests.put(url=f'{SHEETY_ENDPOINT}2', json=sheety_params, headers=sheety_header)
    #sheety_put_response.raise_for_status()
    #print(sheety_put_response.text)


    sheety_get_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
    sheety_get_response.raise_for_status()
    sheety_data = sheety_get_response.json()
    print(sheety_data)


if __name__ == '__main__':
    test = DataManager()
    test
    

# TO-DO:
# - Create GET response.
#     - Use in main.py to store data.
# - Will compare in main after Flight API call.
# - Create PUT response.
#     - Will use PUT response when price is lower than in the Google Sheet.
# - Create an average price over time with a spread.


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


