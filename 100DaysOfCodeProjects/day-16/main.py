from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


coffee_maker.report()
money_machine.report()


choice_coffee = input("What would you like? Espresso / Latte / Cappuccino: ")
drink = menu.find_drink(choice_coffee)


if drink == None:
    drink
else:
    print(f"{drink.name.capitalize()} Price: ${drink.cost:.2f}")


    payment = money_machine.make_payment(drink.cost)


    if payment == False:
        payment
    else:
        if coffee_maker.is_resource_sufficient(drink) == True:
            coffee_maker.make_coffee(drink)


coffee_maker.report()
money_machine.report()


# TO-DO
# 1. Print Report
# 2. Check Resources Sufficient
# 3. Process Coins
# 4. Make Transaction Successful
# 5. Make Coffee


