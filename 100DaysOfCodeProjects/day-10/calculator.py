print("\nWelcome to the CALCULATOR!\n")


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


end_calculator = False
end_calculation = False


while end_calculator != True:
    total = 0
    end_calculation = False


    first_number = int(input("\nWhat is the first number?\n"))
    operator_choice = input("\n+\n-\n*\n/\nPick an operation.\n")
    next_number = int(input("\nWhat is the next number?\n"))
    total = calculation(operator_choice, first_number, next_number)

    
    print(f"\n{first_number:.1f} {operator_choice} {next_number:.1f} = {total:.1f}\n")


    while end_calculation != True:
        print("Type 'q' to quit the calculator.")
        continue_calculating = input(f"Type 'y' to continue calculating with {total:.1f}, or type 'n' to start a new calculation.\n")


        if continue_calculating.lower() == 'n':
            end_calculation = True
        elif continue_calculating.lower() == 'y':
            first_number = total
            operator_choice = input("\n+\n-\n*\n/\nPick an operation.\n")
            next_number = int(input("\nWhat is the next number?\n"))
            total = calculation(operator_choice, first_number, next_number)
            print(f"\n{first_number:.1f} {operator_choice} {next_number:.1f} = {total:.1f}\n")
        else:
            end_calculator = True
            end_calculation = True


print("\nThanks for using the CALCULATOR!\n")


