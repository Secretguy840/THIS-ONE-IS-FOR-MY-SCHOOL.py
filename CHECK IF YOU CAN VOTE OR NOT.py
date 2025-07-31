age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print(f"You cannot vote yet. Wait for {18-age} more years.")
