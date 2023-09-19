import math
degree =  int(input("Enter the value of X:"))
lengthofSeries =  int(input("Enter the length of the series:"))


radian = degree * (math.pi/180)

sum = 0
for i in range(lengthofSeries):
    numerator = (-1)**i * radian**((2*i) + 1)
    denominator = math.factorial((2*i) + 1)
    result = numerator / denominator
    sum += result

print("Result: ", sum)
