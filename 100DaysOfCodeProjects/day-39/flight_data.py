class FlightData:
    def __init__(self, iata_origin, iata_destination, departure_date, return_date, max_price):
    # Lowest Flight
        self.iata_origin = iata_origin
        self.iata_destination = iata_destination
        self.departure_date = departure_date
        self.return_date = return_date
        self.max_price = max_price


    # Get lowest price of flight.
    def get_lowest_price(self):
        # Lowest Priced Flight
        lowest_price_one = {
            'origin': self.iata_origin,
            'destination': self.iata_destination,
            'departureDate': self.departure_date,
            'returnDate': self.return_date,
            'price': self.max_price,
        }


        # Import data and then sort for lowest.
        '''
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
        '''


        print(lowest_price_one)
        #print(test_data_data)


if __name__ == '__main__':
    print('Meow')
    test = FlightData('nyc', 'sfo', '2025-01-01', '2025-01-07', 320)
    print(test.get_lowest_price())


