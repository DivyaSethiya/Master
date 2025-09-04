
first_name = input("Enter your first name: ")
last_name = input("Enter your last name first: ")

full_name = first_name + " " + last_name

print(f"\nHello, {full_name}! Welcome to the Python programming world!")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

print("\nResults:")

print(f"Addition: {num1} + {num2} = {addition}")

print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
