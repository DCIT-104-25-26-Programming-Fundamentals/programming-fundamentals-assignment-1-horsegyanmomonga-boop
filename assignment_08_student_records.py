# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================


def display_menu():
    """Displays the main menu options to the user."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Prompts the user for student details and adds a dictionary record."""
    name = input("Student name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return

    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Error: Student ID cannot be empty.")
        return

    # Check for duplicate ID
    for s in students:
        if s["id"] == student_id:
            print(
                f"Error: A student with ID '{student_id}' already exists."
            )
            return

    num_scores_input = input("How many scores? ").strip()
    if not num_scores_input.isdigit() or int(num_scores_input) <= 0:
        print("Error: Please enter a valid positive number for scores.")
        return

    num_scores = int(num_scores_input)
    scores = []

    for i in range(1, num_scores + 1):
        while True:
            score_input = input(f"Enter score {i}: ").strip()
            try:
                score = float(score_input)
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print(
                        "Error: Score must be between 0 and 100. Try again."
                    )
            except ValueError:
                print("Error: Please enter a valid numeric score. Try again.")

    # Create dictionary and append to main student list
    student_record = {"name": name, "id": student_id, "scores": scores}

    students.append(student_record)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Prints a formatted table of all students, their scores, and averages."""
    if not students:
        print("\nNo student records found.")
        return

    print("\n--------------------------------------------------")
    print(f"{'Name':<15} {'ID':<11} {'Scores':<14} {'Average':<8}")
    print("--------------------------------------------------")

    for student in students:
        scores_str = ", ".join(
            str(int(s)) if s.is_integer() else f"{s:.1f}"
            for s in student["scores"]
        )
        avg = sum(student["scores"]) / len(student["scores"])
        print(
            f"{student['name']:<15} {student['id']:<11} {scores_str:<14} {avg:<8.2f}"
        )

    print("--------------------------------------------------")


def calculate_student_average(students):
    """Finds a student by ID and displays their calculated average score."""
    if not students:
        print("\nNo student records found.")
        return

    target_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == target_id:
            avg = sum(student["scores"]) / len(student["scores"])
            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    print(f"Error: Student with ID '{target_id}' not found.")


def main():
    """Main application loop."""
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print(
                "Error: Invalid choice. Please enter a number between 1 and 4."
            )


if __name__ == "__main__":
    main()
