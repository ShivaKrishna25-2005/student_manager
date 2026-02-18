students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully.\n")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        students.remove(name)
        print("Student removed successfully.\n")
    else:
        print("Student not found.\n")

def show_students():
    if len(students) == 0:
        print("No students available.\n")
    else:
        print("Student List:")
        for student in students:
            print(student)
        print()

# Main menu loop
while True:
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Show All Students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        show_students()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
