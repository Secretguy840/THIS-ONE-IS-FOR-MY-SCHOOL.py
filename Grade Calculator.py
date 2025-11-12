# If-elif-else statements
print("Grade Calculator")
print("================")

marks = float(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A+"
    remark = "Excellent!"
elif marks >= 80:
    grade = "A"
    remark = "Very Good!"
elif marks >= 70:
    grade = "B"
    remark = "Good!"
elif marks >= 60:
    grade = "C"
    remark = "Average"
elif marks >= 40:
    grade = "D"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail"

print(f"\nGrade: {grade}")
print(f"Remarks: {remark}")
