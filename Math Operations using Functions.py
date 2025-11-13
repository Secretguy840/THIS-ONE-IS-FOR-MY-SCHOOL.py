# Function definition and calling
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

# Main program
print("Math Operations using Functions")
print("===============================")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\n{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} × {num2} = {multiply(num1, num2)}")
print(f"{num1} ÷ {num2} = {divide(num1, num2)}")
