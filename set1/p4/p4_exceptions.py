
# Name: EGIE BOY P. DELA CRUZ
# Section: IV-BSIT A
# Activity: P4
# Date: November 18, 2026

# FUNCTION 1 - DIVISION
def divide_numbers():
    print("\n========== DIVISION ==========")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division operation completed.")


# FUNCTION 2 - OPEN FILE
def open_file():
    print("\n========== OPEN FILE ==========")

    filename = input("Enter filename: ")

    try:
        file = open(filename, "r")
        content = file.read()

    except FileNotFoundError:
        print("Error! File not found.")

    else:
        print("\nFile Contents:")
        print(content)
        file.close()

    finally:
        print("File operation completed.")


# MAIN FUNCTION - DISPLAY MENU
def main():
    while True:
        print("\n=================================")
        print("       P4 - EXCEPTION HANDLING")
        print("=================================")
        print("Name: EGIE BOY P. DELA CRUZ")
        print("Section: IV-BSIT A")
        print("=================================")
        print("1. Division")
        print("2. Open File")
        print("3. Exit")
        print("=================================")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                divide_numbers()
            elif choice == "2":
                open_file()
            elif choice == "3":
                print("Exiting Exception Handling Program. Goodbye!")
                break
            else:
                print("Invalid menu choice! Please select 1, 2, or 3.")

        finally:
            print("Returning to main menu...")


if __name__ == "__main__":
    main()
