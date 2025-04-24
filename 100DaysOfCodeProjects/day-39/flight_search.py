import config
import requests


API_KEY_AMADEUS = config.API_KEY_AMADEUS
API_SECRET_AMADEUS = config.API_SECRET_AMADEUS


# Use dates to find cheapest price then offers to get further details?
# Error in assignment.
# SFO to NYC as a test.
AMADEUS_DATES_ENDPOINT = 'https://test.api.amadeus.com/v1/shopping/flight-dates'
AMADEUS_OFFERS_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
AMADEUS_TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.token = self.get_new_token()


    def get_new_token(self):
        token_header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }


        token_body = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY_AMADEUS,
            'client_secret': API_SECRET_AMADEUS
        }


        token_response = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=token_header, data=token_body)
        print(f'Your token is {token_response.json()['access_token']}')
        print(f'Your token expires in {token_response.json()['expires_in']}')
        return token_response.json()['access_token']


    def check_dates(self, iata_origin, iata_destination, from_date, to_date, max_price):
        authorization_header = {'Authorization': f'Bearer {self.token}'}


        amadeus_dates_params = {
            'origin': f'{iata_origin}',
            'destination': f'{iata_destination}',
            'departureDate': f'{from_date},{to_date}',
            'maxPrice': max_price,
        }


        amadeus_get_request = requests.get(url=AMADEUS_DATES_ENDPOINT, params=amadeus_dates_params, headers=authorization_header)
        amadeus_get_request.raise_for_status()
        response_amadeus = amadeus_get_request.json()['data']
        return response_amadeus


    # Add params.
    # Params from CHECK_DATES. 
    # Tomorrow to 6 months from now?
    # - Will need to iterate through 180-ish dates for 9 cities?
    def check_flights(self, iata_origin, iata_destination, from_date, to_date, max_price):
        authorization_header = {'Authorization': f'Bearer {self.token}'}



        amadeus_offers_params = {
            'originLocationCode': f'{iata_origin}',
            'destinationLocationCode': f'{iata_destination}',
            'departureDate': f'{from_date}',
            'returnDate': f'{to_date}',
            'adults': 1,
            'nonStop': 'false',
            'currencyCode': 'USD',
            'maxPrice': max_price,
        }


        amadeus_get_request = requests.get(url=AMADEUS_OFFERS_ENDPOINT, params=amadeus_offers_params, headers=authorization_header)
        amadeus_get_request.raise_for_status()
        response_amadeus = amadeus_get_request.json()
        return response_amadeus
        # Figure out what information we need.
        #print(response_amadeus)
        #print(response_amadeus['data'][0]['price']['grandTotal'])
        #print(response_amadeus['data'][0]['itineraries'][0]['segments'])


if __name__ == "__main__":
    test = FlightSearch()
    test_data = test.check_dates('SFO', 'NYC', '2025-04-22', '2025-05-22', 190)
    

    
    # Lowest Flight
    # Find details in data
    lowest_price_one = {
        'origin': '',
        'destination': '',
        'departureDate': '',
        'returnDate': '',
        'price': 190.00,
        'flightOffers': '',
    }


    for flight in range(len(test_data)):
        if lowest_price_one['price'] > float(test_data[flight]['price']['total']):
            lowest_price_one['origin'] = test_data[flight]['origin']
            lowest_price_one['destination'] = test_data[flight]['destination']
            lowest_price_one['departureDate'] = test_data[flight]['departureDate']
            lowest_price_one['returnDate'] = test_data[flight]['returnDate']
            lowest_price_one['price'] = float(test_data[flight]['price']['total'])
            lowest_price_one['flightOffers'] = test_data[flight]['links']['flightOffers']


        print(test_data[flight]['origin'])
        print(test_data[flight]['destination'])
        print(test_data[flight]['departureDate'])
        print(test_data[flight]['returnDate'])
        print(test_data[flight]['price']['total'])


    test_data_data = test.check_flights(
        'SFO',
        'NYC',
        lowest_price_one['departureDate'],
        lowest_price_one['returnDate'],
        int(round(lowest_price_one['price'], -2))
    )


    print(lowest_price_one)
    print(test_data_data)


