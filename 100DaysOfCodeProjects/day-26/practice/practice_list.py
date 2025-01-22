numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(numbers)
print(new_numbers)


name = 'Angela'
name_list = [letter for letter in name]
print(name)
print(name_list)


range_list = [num * 2 for num in range(1, 5)]
print(range_list)


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names_list = [name for name in names if len(name) < 5]
all_cap_long_names_list = [name.upper() for name in names if len(name) > 4]
print(names)
print(short_names_list)
print(all_cap_long_names_list)


