print("\nWelcome to the tip calculator!")

totalBill = float(input("What is the total bill?\n"))

tipAmount = float(input("How much tip would you like to give? 10, 12, or 15?\n"))

tipAmount = 1 + (tipAmount / 100)

numberOfPeople = float(input("How many people to split the bill?\n"))

payPerPerson = (totalBill * tipAmount) / numberOfPeople

print(f"Each person should pay: ${payPerPerson:.2f}.\n")


