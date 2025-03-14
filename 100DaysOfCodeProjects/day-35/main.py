import config
import requests


API_KEY = config.API_KEY


weather_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'


weather_params = {
    'appid': API_KEY,
    'lat': 66.497231,
    'lon': 24.724880,
    'cnt': 4,
    'units': 'imperial',
}


response_weather = requests.get(url=weather_endpoint, params=weather_params)
response_weather.raise_for_status()


data_weather = response_weather.json()


# Used to DEBUG
#print(data_weather)
#print(data_weather['list'][0]['weather'][0]['id'])
#print(data_weather['list'][0]['dt_txt'])


def is_it_raining(weather: list):
    date_time_list = weather['dt_txt'].split(' ')
    date = date_time_list[0]
    time = date_time_list[1]


    if len(weather['weather']) > 1:
        if weather['weather'][0]['id'] < 700 or weather['weather'][1]['id'] < 700:
            return f'Bring an umbrella! It will be wet at {time} on {date}.'
        else:
            return None
        pass
    else:
        if weather['weather'][0]['id'] < 700:
            return f'Bring an umbrella! It will be wet at {time} on {date}.'
        else:
            return None


def weather_output(weather_result: list):
    for weather in weather_result:
        if weather is not None:
            print(weather)


meow = map(is_it_raining, data_weather['list'])


weather_output(list(meow))


