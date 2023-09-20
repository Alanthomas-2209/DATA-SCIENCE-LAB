def insertion(row,column):
    matrix[][]
    for i in range(row):
        for j in range(column):
            matrix[i][j] = int(input())
    return matrix

def display(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end="\t")
        print()

def displayTranspose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end="\t")
        print()

print("Enter the row and column size of the Matrix 1:")
m1Row = int(input("Enter the row size:"))
m1Column = int(input("Enter the column size:"))

print("Enter the row and column size of the Matrix 2:\n Make sure the row sizes of matrix 1 and 2 are same")
m2Row = int(input("Enter the row size:"))
m2Column = int(input("Enter the column size:"))

if(m1Row != m2Row):
    print("row sizes of matrix 1 and 2 are not same....!")
    exit()

