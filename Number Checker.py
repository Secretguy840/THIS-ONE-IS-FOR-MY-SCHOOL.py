# Multiple conditions
print("Number Checker")
print("==============")

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is Positive")
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("The number is Zero")
