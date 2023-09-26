import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

Arr = np.empty((rows, cols), dtype=int)

print("Enter the elements of the array row by row:")

for i in range(rows):
    row = input().split()
    if len(row) != cols:
        print("Error: Each row should have", cols, "elements.")
        exit(1)
    Arr[i] = [int(x) for x in row]

seq_str = input("Enter the sequence to find separated by spaces: ")
seq = np.array([int(x) for x in seq_str.split()])

occurrences = 0

for i in range(rows):
    for j in range(cols):
        if i + len(seq) <= rows and j + len(seq) <= cols:
            subarray = Arr[i:i+len(seq), j:j+len(seq)]
            if np.array_equal(subarray.flatten(), seq):
                occurrences += 1

print("Number of occurrences:", occurrences)
