#write a program to enter a number and then calculate the sum of its digits
num = int(input("Enter the number\n"))
sum = 0
while(num != 0):
    rem = num % 10
    num = num // 10
    sum = sum + rem
print("The sum of the digits is", sum)



