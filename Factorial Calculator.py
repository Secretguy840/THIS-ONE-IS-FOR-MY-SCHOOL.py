# While loop
print("Factorial Calculator")
print("===================")

num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"Factorial of {num} is {factorial}")
