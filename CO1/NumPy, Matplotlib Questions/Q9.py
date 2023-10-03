# 9.Generate Random Numbers from the Uniform Distribution using NumPy

import numpy as np

low = float(input("Enter the lower bound of the uniform distribution: "))

high = float(input("Enter the upper bound of the uniform distribution: "))

rows = int(input("Enter the number of rows for the output array: "))
cols = int(input("Enter the number of columns for the output array: "))

random_numbers = np.random.uniform(low, high, (rows, cols))

print(random_numbers)
