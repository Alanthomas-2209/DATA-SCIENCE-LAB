#1.	Write a Python program to reverse a number and also find the sum of digits of the number. Prompt the user for input.

number = int(input("Enter the number:"))
sum = 0
reversedNumber = 0
while(number>0):
    temp = number % 10
    sum += temp
    reversedNumber = ( reversedNumber * 10 ) + temp
    number = number // 10

print("Sum of the Digits :",sum)
print("Number after Reversed :",reversedNumber)
