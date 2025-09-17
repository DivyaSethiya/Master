def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

sample_number = 5
fact = factorial(sample_number)


print("\n")
print(f"The factorial of {sample_number} is: {fact}")
print("\n")

import math


number = float(input("Enter a number: "))


sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)


print("\n")
print(f"Square root of {number} is: {sqrt_result}")
print(f"Natural logarithm of {number} is: {log_result}")
print(f"Sine of {number} radians is: {sine_result}")
print("\n")
