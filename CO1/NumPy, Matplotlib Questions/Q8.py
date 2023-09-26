import numpy as np

n = int(input("Enter the size of the square matrix: "))

matrix = np.empty((n, n), dtype=float)

print("Enter the elements of the square matrix row-wise:")
for i in range(n):
    row_input = input(f"Enter elements for row {i + 1} separated by spaces: ")
    matrix[i] = [float(x) for x in row_input.split()]

determinant = np.linalg.det(matrix)


if determinant != 0:
    inverse_matrix = np.linalg.inv(matrix)
else:
    inverse_matrix = None

print("\nMatrix:")
print(matrix)
print("\nDeterminant:", determinant)

if inverse_matrix is not None:
    print("\nInverse Matrix:")
    print(inverse_matrix)
else:
    print("\nThe matrix is not invertible (determinant is zero). Inverse does not exist.")
