import numpy as np

n = int(input("Enter the size of the square matrix: "))

arr = np.empty((n, n), dtype=int)

print("Enter the elements row-wise:")
for i in range(n):
    row_input = input(f"Enter elements for row {i + 1} separated by spaces: ")
    arr[i] = [int(x) for x in row_input.split()]

diagonal_sum = np.trace(arr)

print("Sum of diagonal elements:", diagonal_sum)
