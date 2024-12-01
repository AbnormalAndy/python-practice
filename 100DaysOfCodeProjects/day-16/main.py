from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


print("\nCOFFEE MACHINE")


coffee_maker_off = False


while coffee_maker_off != True:
    choice_coffee = input("\nWhat would you like? Espresso / Latte / Cappuccino: ")


    if choice_coffee.lower() == "refill":
        coffee_maker.resource_refill()
    elif choice_coffee.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice_coffee.lower() == "off":
        print("\nShutting Down...\n")
        coffee_maker_off = True
    else:
        drink = menu.find_drink(choice_coffee)
        sufficient = coffee_maker.is_resource_sufficient(drink)


        if drink == None:
            drink
        else:
            if sufficient == False:
                sufficient
            else:
                print(f"{drink.name.capitalize()} Price: ${drink.cost:.2f}")


                payment = money_machine.make_payment(drink.cost)


                if payment == False:
                    payment
                else:
                    coffee_maker.make_coffee(drink)


