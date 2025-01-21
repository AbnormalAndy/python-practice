import pandas


data = pandas.read_csv('weather_data.csv')


print(data)
print(data['day'])
print(data['temp'])
print(data['condition'])


