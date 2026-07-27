print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print("  ".join(str(x) for x in row))


def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    return matrix

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

print("=== PART A: Transpose a Matrix ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = read_matrix(rows, cols)
print_matrix(matrix, "Original Matrix")
transposed = transpose(matrix)
print_matrix(transposed, "Transposed Matrix")


print("\n=== PART B: Add Two Matrices ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter first matrix:")
matrix1 = read_matrix(rows, cols)
print("Enter second matrix:")
matrix2 = read_matrix(rows, cols)
print_matrix(matrix1, "Matrix 1")
print_matrix(matrix2, "Matrix 2")
sum_matrix = add_matrices(matrix1, matrix2)
print_matrix(sum_matrix, "Sum of Matrices")


print("\n=== PART C: Multiply Two Matrices ===")
rows_a = int(input("Enter rows of Matrix A: "))
cols_a = int(input("Enter columns of Matrix A: "))
print("Enter Matrix A:")
matrix_a = read_matrix(rows_a, cols_a)

rows_b = cols_a
cols_b = int(input("Enter columns of Matrix B: "))
print("Enter Matrix B:")
matrix_b = read_matrix(rows_b, cols_b)

print_matrix(matrix_a, "Matrix A")
print_matrix(matrix_b, "Matrix B")
product = multiply_matrices(matrix_a, matrix_b)
print_matrix(product, "Product of Matrices (A x B)")
