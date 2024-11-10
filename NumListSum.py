A = []
n = int(input("How many numbers\n"))
for i in range (n):
    num = int(input("Enter the value: "))
    A.append(num)
print(A)

sum_odd = 0
sum_even = 0
for i in A:
    if(i % 2 != 0):
        sum_odd += i
    else:
        sum_even += i
print("The sum of odd numbers is:", sum_odd)
print("The sum of even numbers is:", sum_even)
