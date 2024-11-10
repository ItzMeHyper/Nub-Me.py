#write a program using function to check whether the given nunber is prime or not
prime = 0
n = int(input("Enter a number\n"))
for i in range(2,n):
    if(n % i == 0):
        prime = 1
        break
if(prime == 1):
    print("The number is not prime")
else:
    print("The number is prime")