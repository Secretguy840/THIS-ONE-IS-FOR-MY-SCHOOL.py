class CopyTracker:
    def __init__(self):
        self.students = {}
        self.teacher_name = ""
        
    def set_teacher_name(self):
        self.teacher_name = input("Enter teacher's name: ")
        print(f"Teacher: {self.teacher_name}\n")
        
    def add_student(self):
        roll_no = input("Enter student's roll number: ")
        name = input("Enter student's name: ")
        self.students[roll_no] = {"name": name, "submitted": False}
        print(f"Student {name} (Roll No: {roll_no}) added successfully!\n")
        
    def mark_submitted(self):
        roll_no = input("Enter roll number of student who submitted copy: ")
        if roll_no in self.students:
            self.students[roll_no]["submitted"] = True
            print(f"{self.students[roll_no]['name']}'s copy marked as submitted.\n")
        else:
            print("Student not found!\n")
            
    def display_status(self):
        print("\nCopy Submission Status")
        print(f"Teacher: {self.teacher_name}")
        print("-" * 30)
        print("Roll No\tName\t\tStatus")
        print("-" * 30)
        for roll_no, data in self.students.items():
            status = "Submitted" if data["submitted"] else "Pending"
            print(f"{roll_no}\t{data['name']}\t\t{status}")
        print()
        
    def menu(self):
        while True:
            print("1. Set Teacher Name")
            print("2. Add Student")
            print("3. Mark Copy as Submitted")
            print("4. View Submission Status")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                self.set_teacher_name()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.mark_submitted()
            elif choice == "4":
                self.display_status()
            elif choice == "5":
                print("Thank you for using the Copy Tracker!")
                break
            else:
                print("Invalid choice. Please try again.\n")

# Main program
if __name__ == "__main__":
    tracker = CopyTracker()
    print("Welcome to Student Copy Submission Tracker\n")
    tracker.menu()
