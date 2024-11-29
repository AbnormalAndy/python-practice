import coffee_machine
import menu


resource = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
}


choice_menu = False
end_coffee_making = False


while choice_menu != True:
    choice_coffee = input("What would you like? (Espresso / Latte / Cappuccino): ")
    coffee = coffee_machine.menu_choice(choice_coffee)
    if coffee == 0:
        choice_menu = True
        end_coffee_making = True
    elif coffee == 1:
        print(f"Water: {resource['water']} mL")
        print(f"Milk: {resource['milk']} mL")
        print(f"Coffee: {resource['coffee']} g")
        print(f"Money: ${resource['money']:.2f}")
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
        case _:
            for item in resource_check:
                print(f"Resource {item} is too low to make coffee.")


    print(resource)


    end_coffee_making = True


