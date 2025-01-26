def add(*args):
    total = 0
    for n in args:
        total += n
    
    return total


print(add(2, 4, 6, 1))


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')


my_car = Car(make='GT-R')


print(my_car.make)
print(my_car.model)


