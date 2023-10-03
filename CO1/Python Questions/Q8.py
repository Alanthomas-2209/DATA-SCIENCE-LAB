#8.	Given two matrices A and B, write a program to find the product of A and BT.


# def create_empty_matrix(rows, columns):
#     matrix = []
#     for i in range(rows):
#         row = []
#         for j in range(columns):
#             row.append(0)
#         matrix.append(row)
#     return matrix

# def insertion(matrix, rows, columns):
#     for i in range(rows):
#         for j in range(columns):
#             matrix[i][j] = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))

# def display(matrix, rows, columns):
#     for i in range(rows):
#         for j in range(columns):
#             print(matrix[i][j], end="\t")
#         print()

# def transpose(matrix, rows, columns):
#     transposeMatrix = create_empty_matrix(columns, rows)
#     for i in range(rows):
#         for j in range(columns):
#             transposeMatrix[j][i] = matrix[i][j]
#     return transposeMatrix

# def matrix_product(A, BT):
#     if len(A[0]) != len(BT[0]):
#         print("Matrix multiplication is not possible.")
#         return None

#     rows_A, columns_A = len(A), len(A[0])
#     rows_BT, columns_BT = len(BT), len(BT[0])
#     C = [[0 for _ in range(columns_BT)] for _ in range(rows_A)]

#     for i in range(rows_A):
#         for j in range(rows_BT):
#             for k in range(columns_A):
#                 C[i][j] += A[i][k] * BT[j][k]

#     return C

# print("Enter the row and column size of Matrix A:")
# m1Row = int(input("Enter the row size: "))
# m1Column = int(input("Enter the column size: "))

# matrixA = create_empty_matrix(m1Row, m1Column)
# insertion(matrixA, m1Row, m1Column)

# print("\nEnter the row and column size of Matrix B:")
# m2Row = int(input("Enter the row size: "))
# m2Column = int(input("Enter the column size: "))

# matrixB = create_empty_matrix(m2Row, m2Column)
# insertion(matrixB, m2Row, m2Column)

# if m1Column != m2Column:
#     print("Column sizes of Matrix A and Matrix B are not the same. Cannot perform multiplication.")
# else:
#     BT = transpose(matrixB, m2Row, m2Column)
#     result = matrix_product(matrixA, BT)

#     if result is not None:
#         print("\nMatrix A:")
#         display(matrixA, m1Row, m1Column)

#         print("\nMatrix B:")
#         display(matrixB, m2Row, m2Column)

#         print("\nTranspose of Matrix B (BT):")
#         display(BT, m2Column, m2Row)

#         print("\nProduct of A and BT:")
#         display(result, m1Row, m2Row)

import numpy as np

# Function to take matrix input from the user
def input_matrix(rows, columns):
    matrix = np.zeros((rows, columns), dtype=int)
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
    return matrix

# Input matrices A and B
print("Enter the row and column size of Matrix A:")
m1Row = int(input("Enter the row size: "))
m1Column = int(input("Enter the column size: "))
matrixA = input_matrix(m1Row, m1Column)

print("\nEnter the row and column size of Matrix B:")
m2Row = int(input("Enter the row size: "))
m2Column = int(input("Enter the column size: "))
matrixB = input_matrix(m2Row, m2Column)

# Check if matrices can be multiplied
if m1Column != m2Column:
    print("Column sizes of Matrix A and Matrix B are not the same. Cannot perform multiplication.")
else:
    # Transpose matrix B to get BT
    BT = np.transpose(matrixB)

    # Calculate the product of A and BT
    result = np.dot(matrixA, BT)

    print("\nMatrix A:")
    print(matrixA)

    print("\nTranspose of Matrix B (BT):")
    print(BT)

    print("\nProduct of A and BT:")
    print(result)


# def matrix_product():
#     # Step 1: Get dimensions of matrices A and B
#     rows_A = int(input("Enter the number of rows in matrix A: "))
#     cols_A = int(input("Enter the number of columns in matrix A: "))
#     rows_B = int(input("Enter the number of rows in matrix B: "))
#     cols_B = int(input("Enter the number of columns in matrix B: "))

#     # Step 2: Initialize empty matrices A and B
#     A = []
#     B = []

#     # Step 3: Get elements of matrix A from user input
#     print("Enter the elements of matrix A:")
#     for i in range(rows_A):
#         row = []
#         for j in range(cols_A):
#             element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
#             row.append(element)
#         A.append(row)

#     # Step 4: Get elements of matrix B from user input
#     print("Enter the elements of matrix B:")
#     for i in range(rows_B):
#         row = []
#         for j in range(cols_B):
#             element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
#             row.append(element)
#         B.append(row)

#     # Step 5: Transpose matrix B
#     B_T = [[B[j][i] for j in range(rows_B)] for i in range(cols_B)]

#     # Step 6: Perform matrix multiplication
#     product = [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in B_T] for row_A in A]

#     # Step 7: Print the resulting matrix
#     print("Product of A and B^T:")
#     for row in product:
#         print(row)

# matrix_product()
