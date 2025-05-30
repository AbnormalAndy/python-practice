import coffee_machine
import menu


resource = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
}


sold = {
        "espresso": 0,
        "latte": 0,
        "cappuccino": 0,
}


choice_menu = False
end_coffee_making = False
coffee_machine_off = False


while coffee_machine_off != True:
    choice_menu = False
    end_coffee_making = False


    while choice_menu != True:
        choice_coffee = input("What would you like? (Espresso / Latte / Cappuccino): ")
        coffee = coffee_machine.menu_choice(choice_coffee)
        if coffee == 0:
            choice_menu = True
            end_coffee_making = True
            coffee_machine_off = True
        elif coffee == 1:
            print(f"\nWater: {resource['water']} mL")
            print(f"Milk: {resource['milk']} mL")
            print(f"Coffee: {resource['coffee']} g")
            print(f"Money: ${resource['money']:.2f}\n")

            print(f"Espressos sold: {sold['espresso']}")
            print(f"Lattes sold: {sold['latte']}")
            print(f"Cappuccinos sold: {sold['cappuccino']}\n")

            print("Espresso sales: ${coffee_machine.coffee_sales(sold['espresso'], menu.MENU['espresso']['cost']):.2f}")
            print(f"Latte sales: ${coffee_machine.coffee_sales(sold['latte'], menu.MENU['latte']['cost']):.2f}")
            print(f"Cappuccino sales: ${coffee_machine.coffee_sales(sold['cappuccino'], menu.MENU['cappuccino']['cost']):.2f}")
            choice_menu = False
        elif coffee == 2:
            resource = {
                    "water": 300,
                    "milk": 200,
                    "coffee": 100,
                    "money": 0,
            }
            print(f"Water: {resource['water']} mL")
            print(f"Milk: {resource['milk']} mL")
            print(f"Coffee: {resource['coffee']} g")
            print(f"Money: ${resource['money']:.2f}")
            choice_menu = False
        else:
            choice_menu = True


    while end_coffee_making != True:
        choice_quarters = int(input("How many quarters? "))
        choice_dimes = int(input("How many dimes? "))
        choice_nickels = int(input("How many nickels? "))
        choice_pennies = int(input("How many pennies? "))


        resource["money"] = coffee_machine.total_money(choice_quarters, choice_dimes, choice_nickels, choice_pennies)


        resource_check = coffee_machine.resources_check(resource, coffee)


        print(resource)


        match resource_check:
            case 0:
                print("Sorry! That is not enough money. Money refunded.")
                resource['money'] = 0
            case 1:
                resource = coffee_machine.resources_sum(resource, coffee)
                print(f"Here is your {choice_coffee}. Enjoy!")
                if resource['money'] > 0:
                    print(f"Here is your change: ${resource['money']:.2f}.")
                    resource["money"] = 0
                sold[choice_coffee] += 1
            case _:
                for item in resource_check:
                    print(f"Resource {item} is too low to make coffee.")


        print(resource)


        end_coffee_making = True


