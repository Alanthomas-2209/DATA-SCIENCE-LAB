number = abs(int(input("Enter the number: ")))
sumOfCube = 0

for i in range(1,number+1):
    if i % 2 == 0:
        sumOfCube = sumOfCube + (i ** 3)

print("Sum of Cube: ",sumOfCube)