"""
try:
    file = open('a_file.txt')

except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Wrote something.')

except KeyError as error_message:
    print(f'The key {error_message} does not exist.')

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print('File was closed.')
"""


height = float(input('Height: '))
weight = int(input('Weight: '))


if height > 3:
    raise ValueError('Human should not be over 3 meters.')

bmi = weight / height ** 2


print(bmi)
