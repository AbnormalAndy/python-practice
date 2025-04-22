class FlightData:
    #This class is responsible for structuring the flight data.
    pass

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


if __name__ == '__main__':
    print('Meow')


