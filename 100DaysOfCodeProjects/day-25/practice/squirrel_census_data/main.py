import pandas


squirrel_data = pandas.read_csv('2018_squirrel_census.csv')


gray_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray']
cinnamon_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon']
black_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == 'Black']


gray_squirrel_count = gray_squirrel['Primary Fur Color'].count()
cinnamon_squirrel_count = cinnamon_squirrel['Primary Fur Color'].count()
black_squirrel_count = black_squirrel['Primary Fur Color'].count()


squirrel_dictionary = {
        'Fur Color': ['Gray', 'Cinnamon', 'Black'],
        'Count': [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count],
}


squirrel_dataframe = pandas.DataFrame(squirrel_dictionary)
#squirrel_dataframe.to_csv('squirrel_color_count.csv')


print(squirrel_dataframe)
