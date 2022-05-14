MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}


# Print the cost of each drink.
print(f"Espresso ${format(MENU['espresso']['cost'], '.2f')} -- Latte ${format(MENU['latte']['cost'], '.2f')} -- Cappuccino ${format(MENU['cappuccino']['cost'], '.2f')}")


def check_resources(menu_choice):
  """Check if enough of a recource is available to make menu choice."""
  ### Possibly add so it prints multiple empty resources instead of just the first one.
  for key, info in MENU[menu_choice].items():
    if key == 'ingredients':
      for resource1, amount1 in info.items():
        for resource2, amount2 in resources.items():
          if resource1 == resource2:
            if resources[resource2] < amount1:
              return f"Sorry! There is not enough {resource2}."


def remove_resources(menu_choice):
  """Remove the resources required to make the menu choice."""
  for key, info in MENU[menu_choice].items():
    if key == 'ingredients':
      for resource1, amount1 in info.items():
        for resource2, amount2 in resources.items():
          if resource1 == resource2:
            resources[resource2] -= amount1


def print_report(menu_choice):  
  """Print a report of resources in the machine."""
  for resource in resources:
    if resource != 'money' and resource != 'coffee':
      print(f"  {resource.capitalize()}: {resources[resource]} mL")
    elif resource == 'coffee':
      print(f"  {resource.capitalize()}: {resources[resource]} g")
    else:
      print(f"  {resource.capitalize()}: ${format(resources[resource], '.2f')}")


def calculate(q, d, n, p):
  """Calculate the change provided."""
  calculation = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
  return calculation


def coffee_machine():  
  shut_down = False
  while not shut_down:
  
    coffee_type = input("\nWhat would you like? (Espresso/Latte/Cappuccino:\n").lower()
  
    if coffee_type == 'off':
      print("Shutting Down...")
      shut_down = True
      break
  
    if coffee_type == 'report':
      print_report(coffee_type)
    else:
      if check_resources(coffee_type) != None:
        print(check_resources(coffee_type))
      else:
        quarters = int(input("  How many quarters? "))
        dimes = int(input("  How many dimes? "))
        nickels = int(input("  How many nickels? "))
        pennies = int(input("  How many pennies? "))
  
        total = calculate(quarters, dimes, nickels, pennies)
        if total < MENU[coffee_type]['cost']:
          print("Sorry! That is not enough money. Money has been refunded.")
        else:
          refund = total - MENU[coffee_type]['cost']
          resources['money'] += MENU[coffee_type]['cost']
          remove_resources(coffee_type)
          if refund > 0:
            print(f"Here is ${format(refund, '.2f')} in change.")
          print(f"Here is your {coffee_type}. ☕️ Enjoy!")


coffee_machine()