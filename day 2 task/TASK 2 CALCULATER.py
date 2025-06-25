# String Slicing & Simple Calculator - Internship Day 2

# Taking full name input
full_name = input("Enter your full name (First Last): ")

# Finding the index of space to slice names
space_index = full_name.find(" ")

# Slicing first and last names
first_name = full_name[:space_index]
last_name = full_name[space_index+1:]

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

# Taking numeric inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing arithmetic operations
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

# Displaying results
print(f"\nResults:")
print(f"Addition: {num1} + {num2} = {add}")
print(f"Subtraction: {num1} - {num2} = {subtract}")
print(f"Multiplication: {num1} * {num2} = {multiply}")
print(f"Division: {num1} / {num2} = {divide}")
