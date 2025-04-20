import config
import requests


API_KEY_AMADEUS = config.API_KEY_AMADEUS
API_SECRET_AMADEUS = config.API_SECRET_AMADEUS
API_TOKEN_AMADEUS = config.API_TOKEN_AMADEUS


# Use dates to find cheapest price then offers to get further details?
AMADEUS_DATES_ENDPOINT = 'https://test.api.amadeus.com/v1/shopping/flight-dates'
AMADEUS_OFFERS_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'


AMADEUS_HEADER = {
    'Authorization': f'Bearer {API_TOKEN_AMADEUS}',
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    # Tomorrow to 6 months from now?
    # - Will need to iterate through 180-ish dates for 9 cities?
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


