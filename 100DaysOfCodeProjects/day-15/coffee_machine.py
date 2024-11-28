import menu


def menu_choice(user_coffee_input):
    match user_coffee_input.lower():
        case "espresso":
            return menu.MENU['espresso']
        case "latte":
            return menu.MENU['latte']
        case "cappuccino":
            return menu.MENU['cappuccino']
        case "report":
            print(f"Water: {resource['water']} mL")
            print(f"Milk: {resource['milk']} mL")
            print(f"Coffee: {resource['coffee']} g")
            print(f"Money: ${resource['money']:.2f}")
            return 1
        case "off":
            print(f"Shutting down...")
            return 0
        case _:
            print("Invalid choice. Please try again.")
            return 1


def total_money(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickels * 0.05
    total += pennies * 0.01
    return total


def resources_check(machine_resource, machine_coffee):
    resource_low = []
    if machine_resource['money'] < machine_coffee['cost']:
        return 0
    else:
        for ingredient in machine_coffee['ingredients']:
            if machine_coffee['ingredients'][ingredient] > machine_resource[ingredient]:
                resource_low.append(ingredient)
        if len(resource_low) > 0:
            return resource_low
        else:
            return 1


def resources_sum(machine_resource, machine_coffee):
    resource = machine_resource
    resource['money'] = machine_resource['money'] - machine_coffee['cost']
    for ingredient in machine_coffee['ingredients']:
        resource[ingredient] = machine_resource[ingredient] - machine_coffee['ingredients'][ingredient]
    return resource


resource = {
        "water": 30, #300,
        "milk": 20, #200,
        "coffee": 100,
        "money": 0,
}


choice_coffee = input("What would you like? (Espresso / Latte / Cappuccino): ")
coffee = menu_choice(choice_coffee)


choice_quarters = int(input("How many quarters? "))
choice_dimes = int(input("How many dimes? "))
choice_nickels = int(input("How many nickels? "))
choice_pennies = int(input("How many pennies? "))


resource["money"] = total_money(choice_quarters, choice_dimes, choice_nickels, choice_pennies)


resource_check = resources_check(resource, coffee)


print(resource_check)
print(resource)


match resource_check:
    case 0:
        print("Sorry! That is not enough money. Money refunded.")
        resource['money'] = 0
    case 1:
        resource = resources_sum(resource, coffee)
    case _:
        for item in resource_check:
            print(f"Resource {item} is too low to make coffee.")


# TO-DO:
# Print Coffee
# Keep Track of Resource
# Create a Quit
print(resource)


print(f"${resource['money']:.2f}")


print(resource)

#resource = resources_sum(resource, coffee)

print(resource)


print(f"${resource['money']:.2f}")


# TO-DO
# Key Points
# - 3 Hot Flavors
#     - Espresso ($1.50)
#         - 50 mL Water
#         - 18 g Coffee
#     - Latte ($2.50)
#         - 200 mL Water
#         - 24 g Coffee
#         - 150 mL Milk
#     - Cappuccino ($3.00)
#         - 250 mL Water
#         - 24 g Coffee
#         - 100 mL Milk
# - Coins Operate
#     - How many pennies?
#         - Peny (0.01)
#     - How many nickels?
#         - Nickel (0.05)
#     - How many dimes?
#         - Dime (0.10)
#     - How many quarters?
#         - Quarter (0.25)
# - Automatic Cup Dispenser
# - Counting Cup Selling


# Water (300 mL)
# Milk (200 mL)
# Coffee (100 g)


# Analytic Table
# - Water Inlet
# - Coin Outlet
# - Coin Acceptor
# - LCD Display
#     - Drink 1
#     - Drink 2
#     - Drink 3
# - Menu
# - Drink Outlet
# - Waste Water Box


# Requirement
# - Report
#     - Describe inventory quantity.
# - Off
#     - Secret word to end program.
# - Check Resources Sufficient
#     - Example: Sorry! There is not enough water.
# - Process Coins
#     - Example: Sorry! That is not enough money. Money refunded.
# - Check Transaction Successful
#     - Example: Here is $2.14 in change.
# - Make Coffee
#     - Example: Here is your espresso. Enjoy!


