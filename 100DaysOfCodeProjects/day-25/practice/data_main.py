import csv


with open('weather_data.csv') as file:
    data = csv.reader(file)
    weather_data = []
    days = []
    temperatures = []
    conditions = []
    for row in data:
        weather_data.append(row)

    
    for data in weather_data[1:]:
        days.append(data[0])
        temperatures.append(int(data[1]))
        conditions.append(data[2])


print(weather_data)
print(days)
print(temperatures)
print(conditions)


