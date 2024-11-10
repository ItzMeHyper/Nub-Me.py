#write a program to swap two numbers using function
def swap(a,b):
    temp = a
    a = b
    b = temp  #can be also used as a,b = b,a
    print("After swap:")
    print("First number =", a)
    print("Second number =", b)

a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
print("Before swap:")
print("First number =", a)
print("Second number =", b)
swap(a,b)