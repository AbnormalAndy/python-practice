import config
import requests


API_KEY_SHEETY = config.API_KEY_SHEETY
SHEETY_ENDPOINT = 'https://api.sheety.co/99857e1bc2a42bffc6f6a39865ac096e/flightDeals/prices/'


SHEETY_HEADER = {
    'Authorization': f'Bearer {API_KEY_SHEETY}',
    }


class DataManager:
    # Use to Change Sheety Params Values
    def __init__(self):
        self.city = 'TestCity'
        self.iataCode = 'TestIATACode'
        self.lowestPrice = 0
        self.row_number = 0


    # Use to get data from Sheety to compare to cost.
    def get_request(self):
        sheety_get_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
        sheety_get_response.raise_for_status()
        sheety_data = sheety_get_response.json()
        return sheety_data

        
        # DEBUG Statement
        #print(sheety_data)


    # Replace price if lower than what is on Sheety.
    def put_request(self):
        sheety_params = {
            # Key must be CAMEL CASE and NO spaces even if the Google Sheets column title is title cased and has spaces.
            'price': {
                'city': self.city,
                'iataCode': self.iataCode,
                'lowestPrice': self.lowestPrice,
            }
        }


        row_number = self.row_number


        sheety_put_response = requests.put(url=f'{SHEETY_ENDPOINT}{row_number}', json=sheety_params, headers=SHEETY_HEADER)
        sheety_put_response.raise_for_status()


        # DEBUG Statement
        #print(sheety_put_response.text)


if __name__ == '__main__':
    test = DataManager()
    #test.city = 'Mexico'
    #test.iataCode = 'MEOW1234'
    #test.lowestPrice = 30
    #test.put_request()
    test.get_request()
    

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


