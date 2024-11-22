print("Welcome to the CALCULATOR!")


def addition(number_one, number_two):
    return float(number_one + number_two)


def subtraction(number_one, number_two):
    return float(number_one - number_two)


def multiplication(number_one, number_two):
    return float(number_one * number_two)


def division(number_one, number_two):
    return float(number_one / number_two)


def calculation(operator, number_one, number_two):
    match operator:
        case "+":
            return addition(number_one, number_two)
        case "-":
            return subtraction(number_one, number_two)
        case "*":
            return multiplication(number_one, number_two)
        case "/":
            return division(number_one, number_two)
        case _:
            return False


number1 = 15
number2 = 3


print(calculation("+", number1, number2))
print(calculation("-", number1, number2))
print(calculation("*", number1, number2))
print(calculation("/", number1, number2))
print(calculation("", number1, number2))


# Calculator
# What's the first number?
# Pick an operation? + - * /
# What's the next number?
# Return FALSE should repeat previous numbers.


