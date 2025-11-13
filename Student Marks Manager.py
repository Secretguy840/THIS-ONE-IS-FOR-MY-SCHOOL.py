# List operations
print("Student Marks Manager")
print("=====================")

marks = []
n = int(input("How many subjects? "))

for i in range(n):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

print(f"\nAll marks: {marks}")
print(f"Highest marks: {max(marks)}")
print(f"Lowest marks: {min(marks)}")
print(f"Average marks: {sum(marks)/len(marks):.2f}")
