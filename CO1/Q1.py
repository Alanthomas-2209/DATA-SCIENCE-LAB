number = int(input("Enter the number:"))
sum = 0
reversedNumber = 0
while(number>0):
    temp = number % 10
    sum += temp
    reversedNumber = ( reversedNumber * 10 ) + temp
    number = number // 10

print("Sum of the Digits :",sum)
print("Number after Reversed ",reversedNumber)

