import config
import requests


API_KEY_AMADEUS = config.API_KEY_AMADEUS
API_SECRET_AMADEUS = config.API_SECRET_AMADEUS


# Use dates to find cheapest price then offers to get further details?
# Error in assignment.
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
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }


        token_response = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=token_header, data=token_body)
        print(f'Your token is {token_response.json()['access_token']}')
        print(f'Your token expires in {token_response.json()['expires_in']}')
        return token_response.json()['access_token']


    # Add params.
    # Tomorrow to 6 months from now?
    # - Will need to iterate through 180-ish dates for 9 cities?
    def check_flights(self):
        authorization_header = {'Authorization': f'Bearer {self.token}'}

        amadeus_dates_params = {
            'origin': 'MSP',
            'destination': 'PAR',
            'departureDate': '2025-04-23',
        }


        amadeus_offers_params = {
            'originLocationCode': 'MSP',
            'destinationLocationCode': 'PAR',
            'departureDate': '2025-04-23',
            'adults': 1,
        }


        amadeus_get_request = requests.get(url=AMADEUS_DATES_ENDPOINT, params=amadeus_dates_params, headers=AMADEUS_HEADER)
        amadeus_get_request.raise_for_status()
        response_amadeus = amadeus_get_request.text
        # Figure out what information we need.
        print(response_amadeus)
        #print(response_amadeus['data'][0]['price']['grandTotal'])
        #print(response_amadeus['data'][0]['itineraries'][0]['segments'])


if __name__ == "__main__":
    test = FlightSearch
    test


