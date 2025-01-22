with open('file1.txt') as file_one:
    data_one = file_one.readlines()


with open('file2.txt') as file_two:
    data_two = file_two.readlines()
    

data_one_int = [int(data.strip('\n')) for data in data_one]
data_two_int = [int(data.strip('\n')) for data in data_two]
print(data_one_int)
print(data_two_int)


result = [num for num in data_one_int if num in data_two_int]
print(result)


