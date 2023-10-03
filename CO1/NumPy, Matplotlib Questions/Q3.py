# 3.	Find the k smallest values of a NumPy array

import numpy as np

input_str = input("Enter elements of the array separated by spaces: ")
arr = np.array([int(x) for x in input_str.split()])

k = int(input("Enter the value of k: "))

k_smallest = np.partition(arr, k)[:k]

print(f"The {k} smallest values are: {k_smallest}")
