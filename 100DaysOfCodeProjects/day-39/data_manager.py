import config
import requests


API_KEY_SHEETY = config.API_KEY_SHEETY


SHEETY_ENDPOINT = 'https://api.sheety.co/99857e1bc2a42bffc6f6a39865ac096e/flightDeals/prices/'


class DataManager:
    sheety_params = {
        # Key must be CAMEL CASE and NO spaces even if the Google Sheets column title is title cased and has spaces.
        'price': {
            'city': 'Test',
            'iataCode': 'TestTestTest',
            'lowestPrice': 012345,
        }
    }


    sheety_header = {
        'Authorization': f'Bearer {API_KEY_SHEETY}',
    }


    sheety_put_response = requests.put(url=f'{SHEETY_ENDPOINT}2', json=sheety_params, headers=sheety_header)
    sheety_put_response.raise_for_status()
    print(sheety_put_response.text)


if __name__ == '__main__':
    test = DataManager()
    test
    

