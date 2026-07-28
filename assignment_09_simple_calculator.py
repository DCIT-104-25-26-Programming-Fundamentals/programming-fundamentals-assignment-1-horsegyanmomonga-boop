# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers rounded to 2 decimal places.

    Handles division by zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)


def modulus(a, b):
    """Returns the remainder of two numbers.

    Handles modulo by zero.
    """
    if b == 0:
        return "Error: Modulus by zero is undefined."
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Displays the main menu options."""
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_number(prompt):
    """Helper function to safely get a float input from the user."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Error: Please enter a valid numerical value.")


def main():
    """Main execution loop for the calculator."""
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("\nGoodbye!")
            break

        if choice in ("1", "2", "3", "4", "5", "6"):
            num1 = get_number("Enter first number : ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                res = add(num1, num2)
                op = "+"
            elif choice == "2":
                res = subtract(num1, num2)
                op = "-"
            elif choice == "3":
                res = multiply(num1, num2)
                op = "*"
            elif choice == "4":
                res = divide(num1, num2)
                op = "/"
            elif choice == "5":
                res = modulus(num1, num2)
                op = "%"
            elif choice == "6":
                res = power(num1, num2)
                op = "**"

            # Display result or error message if returned by divide/modulus
            if isinstance(res, str):
                print(res)
            else:
                # Format numbers cleanly (e.g., show 10 instead of 10.0 if integer)
                n1_str = int(num1) if num1.is_integer() else num1
                n2_str = int(num2) if num2.is_integer() else num2
                res_str = (
                    int(res)
                    if isinstance(res, float) and res.is_integer()
                    else res
                )
                print(f"Result: {n1_str} {op} {n2_str} = {res_str}")
        else:
            print(
                "Error: Invalid choice. Please select an option between 1 and 7."
            )


if __name__ == "__main__":
    main()
