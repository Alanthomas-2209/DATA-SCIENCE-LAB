#with handling of division by zero
import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

array1 = np.empty((rows, cols), dtype=float)
array2 = np.empty((rows, cols), dtype=float)

print("Enter elements for the first array:")
for i in range(rows):
    for j in range(cols):
        array1[i, j] = float(input(f"Enter element at row {i + 1}, column {j + 1}: "))

print("Enter elements for the second array:")
for i in range(rows):
    for j in range(cols):
        array2[i, j] = float(input(f"Enter element at row {i + 1}, column {j + 1}: "))

addition_result = array1 + array2
subtraction_result = array1 - array2
multiplication_result = array1 * array2

division_result = np.divide(array1, array2, out=np.zeros_like(array1), where=array2 != 0)

print("\nArray 1:\n", array1)
print("Array 2:\n", array2)
print("Element-wise Addition:\n", addition_result)
print("Element-wise Subtraction:\n", subtraction_result)
print("Element-wise Multiplication:\n", multiplication_result)
print("Element-wise Division :\n", division_result)
