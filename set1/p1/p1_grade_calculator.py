# Date: November 18, 2026
# P1 - STUDENT GRADE CALCULATOR
# Name: EGIE BOY P. DELA CRUZ
# Section: IV-BSIT A


# GLOBAL VARIABLE
grades = []


# FUNCTION 1 - ACCEPT STUDENT GRADES
def add_grades(grades):
    while True:
        try:
            number = int(input("Enter number of grades: "))

            if number > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")


# FUNCTION 2 - COMPUTE AVERAGE
def calculate_average(grades):
    if len(grades) == 0:
        return 0

    return sum(grades) / len(grades)


# FUNCTION 3 - GET HIGHEST GRADE
def get_highest_grade(grades):
    if len(grades) == 0:
        return None

    return max(grades)


# FUNCTION 4 - GET LOWEST GRADE
def get_lowest_grade(grades):
    if len(grades) == 0:
        return None

    return min(grades)


# FUNCTION 5 - DETERMINE PASS OR FAIL
def determine_pass_fail(grades):
    if len(grades) == 0:
        return "No grades available"

    if calculate_average(grades) >= 75:
        return "PASSED"

    return "FAILED"


# FUNCTION 6 - MAIN MENU AND DISPLAY RESULTS
def main():
    while True:
        print("\n=================================")
        print("     STUDENT GRADE CALCULATOR")
        print("=================================")
        print("[1] Enter Grades")
        print("[2] View Results")
        print("[3] Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_grades(grades)

        elif choice == "2":
            if len(grades) == 0:
                print("\nNo grades available. Please enter grades first.")
            else:
                print("\n=================================")
                print("         STUDENT RESULTS")
                print('Name: EGIE BOY P. DELA CRUZ')
                print('Section: IV-BSIT A')
                print("=================================")
                print("Grades:", grades)
                print(f"Average Grade: {calculate_average(grades):.2f}")
                print(f"Highest Grade: {get_highest_grade(grades)}")
                print(f"Lowest Grade: {get_lowest_grade(grades)}")
                print(f"Status: {determine_pass_fail(grades)}")
                print("=================================")

        elif choice == "3":
            print("\nThank you for using Student Grade Calculator!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


# PROGRAM START
if __name__ == "__main__":
    main()


# LOCAL AND GLOBAL VARIABLES:
# The grades variable is global because it is declared outside the functions.
# The number and grade variables are local because they are declared inside add_grades().
# The grades parameter receives the grade list when it is passed to a function.
# Local variables are accessible only within their function, while global variables
# can be accessed throughout the program.
