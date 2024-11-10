#write a program top find the factorial of a number using function
def fact(n):
    f=1
    for i in range(1,n+1):
        f = f * i
    return f

num = int(input("Enter a number\n"))
factorial = fact(num)
print("Factorial =", factorial)