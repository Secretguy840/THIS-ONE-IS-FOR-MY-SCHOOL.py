# Dictionary operations
students = {}

while True:
    print("\nStudent Database")
    print("1. Add student")
    print("2. View student")
    print("3. View all students")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        roll_no = input("Enter roll number: ")
        name = input("Enter name: ")
        grade = input("Enter class: ")
        marks = input("Enter marks: ")
        
        students[roll_no] = {
            'name': name,
            'class': grade,
            'marks': marks
        }
        print("Student added successfully!")
    
    elif choice == '2':
        roll_no = input("Enter roll number: ")
        if roll_no in students:
            student = students[roll_no]
            print(f"\nName: {student['name']}")
            print(f"Class: {student['class']}")
            print(f"Marks: {student['marks']}")
        else:
            print("Student not found!")
    
    elif choice == '3':
        if students:
            print("\nAll Students:")
            for roll_no, info in students.items():
                print(f"Roll No: {roll_no}, Name: {info['name']}, Class: {info['class']}")
        else:
            print("No students in database!")
    
    elif choice == '4':
        print("Thank you for using Student Database!")
        break
    
    else:
        print("Invalid choice!")
