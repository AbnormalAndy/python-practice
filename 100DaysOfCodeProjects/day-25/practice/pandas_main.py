import pandas


data = pandas.read_csv('weather_data.csv')


print(data)
print(data['day'])
print(data['temp'])
print(data['condition'])


temp_average = data['temp'].mean()
print(f"{temp_average:.2f}")


temp_max = data['temp'].max()
print(temp_max)


print(data[data.temp == data.temp.max()])


temp_min = data['temp'].min()
print(temp_min)


print(data[data.temp == data.temp.min()])


monday = data[data.day == 'Monday']
print(monday.temp)


data_dict = {
        "student": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65],
}


data = pandas.DataFrame(data_dict)
print(data)
#data.to_csv("student_data.csv")


