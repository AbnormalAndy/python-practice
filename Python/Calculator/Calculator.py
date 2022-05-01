from CalculatorArt import logo

# Calculator

print(logo)

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}



symbols = ''
for symbol in operations:
  symbols += " "
  symbols += ''.join(symbol)

def calculator():
  def calculate(n1, n2):
    calculation = operations[operation_symbol](n1, n2)
    return calculation
  
  num1 = float(input("What is the first number? "))
  
  end_calculator = False
  
  while not end_calculator:
  
    operation_symbol = input(f"Pick an Operation |||{symbols}: ")
    num2 = float(input("What is the other number? "))
  
    answer = calculate(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    continue_calculator = input("Would you like to continue? Yes (Y) - No (N)\n").lower()
  
    if continue_calculator == "yes" or continue_calculator == "y":
      num1 = answer
    else:
      end_calculator = True
      calculator()

calculator()