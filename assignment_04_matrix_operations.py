# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#


def print_matrix(matrix):
    """Prints a 2D matrix in a neat grid format."""
    for row in matrix:
        for val in row:
            print(f"{val:6g}", end="")
        print()


def create_matrix(rows, cols, name="Matrix"):
    """Helper function to read a matrix from user input row by row."""
    print(f"\nEntering {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) == cols:
                try:
                    row = [float(x) for x in row_input]
                    matrix.append(row)
                    break
                except ValueError:
                    print("Invalid numbers. Please try again.")
            else:
                print(f"Error: Expected {cols} numbers separated by spaces.")
    return matrix


def transpose_matrix(matrix):
    """PART A: Computes and returns the transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Create empty result matrix of dimensions (cols x rows)
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed


def add_matrices(matrix_a, matrix_b):
    """PART B: Computes and returns the element-wise sum of two matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    """PART C: Computes and returns the matrix product A x B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            # Compute dot product for position (i, j)
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(dot_product)
        result.append(new_row)

    return result


def main():
    print("=== MATRIX OPERATIONS PROGRAM ===")

    # PART A: Transpose
    print("\n--- PART A: Transpose a Matrix ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix_a = create_matrix(m, n, "Original Matrix")

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    transposed = transpose_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # PART B: Addition
    print("\n--- PART B: Add Two Matrices ---")
    print(f"Adding two matrices of size {m}x{n}...")
    mat1 = create_matrix(m, n, "Matrix 1")
    mat2 = create_matrix(m, n, "Matrix 2")

    sum_result = add_matrices(mat1, mat2)
    print("\nSum of Matrices:")
    print_matrix(sum_result)

    # PART C: Multiplication
    print("\n--- PART C: Multiply Two Matrices ---")
    p = int(input("Enter number of columns for Matrix B (Rows will be set to match cols of Matrix A): "))
    print(f"Matrix A is {m}x{n}. Matrix B will be {n}x{p}.")

    mult_a = create_matrix(m, n, "Matrix A")
    mult_b = create_matrix(n, p, "Matrix B")

    product = multiply_matrices(mult_a, mult_b)
    print("\nProduct (A x B):")
    print_matrix(product)


# Execute the program
if __name__ == "__main__":
    main()
