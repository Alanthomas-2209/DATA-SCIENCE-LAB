import numpy as np

input_str = input("Enter a list of numbers separated by spaces: ")
input_numbers = input_str.split()

arr = np.array([int(num) for num in input_numbers])

mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
