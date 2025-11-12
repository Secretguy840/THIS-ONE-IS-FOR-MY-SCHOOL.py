# For loop
print("Multiplication Table")
print("===================")

num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")
