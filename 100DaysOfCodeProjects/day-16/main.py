from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()


coffeemaker.report()


choice_coffee = input("What would you like? Espresso / Latte / Cappuccino: ")


drink = menu.find_drink(choice_coffee)


if drink == None:
    drink
else:
    if coffeemaker.is_resource_sufficient(drink) == True:
        coffeemaker.make_coffee(drink)


# TO-DO
# 1. Print Report
# 2. Check Resources Sufficient
# 3. Process Coins
# 4. Make Transaction Successful
# 5. Make Coffee


