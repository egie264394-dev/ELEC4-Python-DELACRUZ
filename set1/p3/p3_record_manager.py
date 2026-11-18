
# Name: EGIE BOY P. DELA CRUZ
# Section: IV-BSIT A
# Activity: P3
# Date: November 18, 2026

# GLOBAL VARIABLES
students = []
student_names = set()


# FUNCTION 1 - ADD STUDENT
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
    elif name.casefold() in student_names:
        print("Student already exists!")
    else:
        students.append(name)
        student_names.add(name.casefold())
        print(f"{name} has been added successfully.")


# FUNCTION 2 - REMOVE STUDENT
def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.casefold() == name.casefold():
            students.remove(student)
            student_names.remove(student.casefold())
            print(f"{student} has been removed successfully.")
            return

    print("Student not found.")


# FUNCTION 3 - SEARCH STUDENT
def search_student():
    name = input("Enter name to search: ").strip().casefold()

    if name == "":
        print("Please enter a name to search.")
        return

    results = [
        student for student in students
        if name in student.casefold()
    ]

    if results:
        print("\nSearch Results:")
        for student in results:
            print("-", student)
    else:
        print("No matching student found.")


# FUNCTION 4 - DISPLAY STUDENTS
def display_students():
    print("\n========== STUDENT LIST ==========")

    if not students:
        print("No student records found.")
    else:
        sorted_students = sorted(students, key=str.casefold)

        for number, student in enumerate(sorted_students, start=1):
            print(f"{number}. {student}")

    print("----------------------------------")
    print(f"Total Students: {len(students)}")
    print("==================================")


# MAIN FUNCTION - DISPLAY MENU
def main():
    while True:
        print("\n=================================")
        print("     P3 - STUDENT RECORD MANAGER")
        print("=================================")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display Students")
        print("5. Exit")
        print("=================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting Student Record Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# LIST AND SET EXPLANATION
# A list stores student names and keeps them in an ordered collection.
# I used the students list to add, remove, search, and display student records.
# A set stores unique values and does not allow duplicates.
# I used student_names to check duplicate names without considering capitalization.
