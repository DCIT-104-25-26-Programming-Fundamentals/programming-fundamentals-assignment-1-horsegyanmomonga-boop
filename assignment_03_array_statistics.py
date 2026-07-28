# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#


def calculate_sum(numbers):
    """Calculates the sum of a list of numbers without using built-in sum()."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        return 0
    # Reuses our custom sum function divided by list length
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Finds the maximum value in a list without using built-in max()."""
    highest = numbers[0]
    for num in numbers[1:]:
        if num > highest:
            highest = num
    return highest


def find_minimum(numbers):
    """Finds the minimum value in a list without using built-in min()."""
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest


def main():
    n = int(input("How many numbers? "))

    # Validate that N is positive
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    # Collect numbers from the user
    numbers = []
    for i in range(1, n + 1):
        value = float(input(f"Enter number {i}: "))
        numbers.append(value)

    # Compute results using custom functions
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    # Print formatted output
    print("\nResults:")
    print(f"Sum:     {total:g}")
    print(f"Average: {avg:g}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


# Execute the program
if __name__ == "__main__":
    main()
