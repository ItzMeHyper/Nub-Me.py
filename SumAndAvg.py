sum = 0
number = 1
n = int(input("Enter the number\n"))
while(number<=n):
    sum = sum + number
    number = number + 1
avg = sum/n
print("The sum of first", n ,"numbers is", sum)
print("The average of first", n ,"numbers is", avg)