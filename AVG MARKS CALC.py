n = int(input("Enter number of subjects: "))
total = 0

for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks

average = total / n
print("Average marks =", average)
