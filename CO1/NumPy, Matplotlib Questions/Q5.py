# 5.Find indices of elements equal to zero in a NumPy array

import numpy as np

input_str = input("Enter elements of the array separated by spaces: ")
arr = np.array([int(x) for x in input_str.split()])

zero_indices = np.where(arr == 0)

print("Indices of elements equal to zero:", zero_indices)
