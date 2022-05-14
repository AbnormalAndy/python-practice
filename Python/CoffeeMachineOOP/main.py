from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


shut_down = False
while not shut_down:
    order = input(f"\n{menu.get_items()}\nWhat would you like? ")
    print(order)
    if order == 'off':
        shut_down = True
        break
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) == True and money_machine.make_payment(drink.cost) == True:
            coffee_maker.make_coffee(drink)