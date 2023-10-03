# 2.	Find the number of occurrences of a sequence in a NumPy array
# Eg: Arr = [[2,8,9,4],
#        [9,4,9,4],
#        [4,5,9,7],
#        [2,9,4,3]]
# and the seq = [9,4] then output is 4

import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

arr = np.empty((rows, cols), dtype=int)

print("Enter the elements of the array row by row:")

for i in range(rows):
    row = input().split()
    if len(row) != cols:
        print("Error: Each row should have", cols, "elements.")
        exit(1)
    arr[i] = [int(x) for x in row]

seq_str = input("Enter the sequence to find separated by spaces: ")
seq = np.array([int(x) for x in seq_str.split()])

arr_1d = arr.ravel()
seq_1d = seq.ravel()

arr_1d = arr_1d.tolist()
seq_1d = seq_1d.tolist()
count = 0
for i in range(0, len(arr_1d) - len(seq_1d) + 1):
    if arr_1d[i:i+len(seq_1d)] == seq_1d:
        count += 1 
print('Solution1:', count)

# arr_1d = arr.ravel()
# seq_1d = np.array([-9, 4])  
# res = np.convolve(arr_1d, seq_1d)
# print('Solution2:', res.size - np.count_nonzero(res))


# import numpy as np

# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# Arr = np.empty((rows, cols), dtype=int)

# print("Enter the elements of the array row by row:")

# for i in range(rows):
#     row = input().split()
#     if len(row) != cols:
#         print("Error: Each row should have", cols, "elements.")
#         exit(1)
#     Arr[i] = [int(x) for x in row]

# seq_str = input("Enter the sequence to find separated by spaces: ")
# seq = np.array([int(x) for x in seq_str.split()])

# occurrences = 0

# for i in range(rows):
#     for j in range(cols):
#         if i + len(seq) <= rows and j + len(seq) <= cols:
#             subarray = Arr[i:i+len(seq), j:j+len(seq)]
#             if np.array_equal(subarray.flatten(), seq):
#                 occurrences += 1

# print("Number of occurrences:", occurrences)