import menu


def menu_choice(user_coffee_input):
    match user_coffee_input.lower():
        case "espresso":
            return menu.MENU['espresso']
        case "latte":
            return menu.MENU['latte']
        case "cappuccino":
            return menu.MENU['cappuccino']
        case "refill":
            print("Refilling resources...")
            return 2
        case "report":
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


# TO-DO
# Key Points
# - Automatic Cup Dispenser
# - Counting Cup Selling


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


