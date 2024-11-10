a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))
c = int(input("Enter the third number\n"))

if ((a>b) and (a>c)):
    print("The largets is", a)
elif ((b>a) and (b>c)):
    print("The largest is", b)
else:
    print("The largest is", c)