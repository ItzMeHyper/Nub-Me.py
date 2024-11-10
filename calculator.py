import math

while True:
    print("Choose the operation you want to perform:")
    print("1.Addition➕")
    print("2.Substraction➖")
    print("3.Multiplication✖️")
    print("4.Division➗")
    print("5.Square Root √")
    print("6.Exit🚪")

    n = int(input("Enter your option:\n"))

    if n == 1:
        print("ADDITION")
        num1 = int(input("Enter first number:\n"))
        num2 = int(input("Enter second number:\n"))
        sum = num1 + num2
        print("Sum =", sum)
    elif n == 2:
        print("SUBTRACTION")
        num1 = int(input("Enter first number:\n"))
        num2 = int(input("Enter second number:\n"))
        difference = num1 - num2
        print("Difference =", difference)
    elif n == 3:
        print("MULTIPLICATION")
        num1 = int(input("Enter first number:\n"))
        num2 = int(input("Enter second number:\n"))
        product = num1 * num2
        print("Product =", product)
    elif n == 4:
        print("DIVISION")
        num1 = int(input("Enter first number:\n"))
        num2 = int(input("Enter second number:\n"))
        quotient = num1 / num2
        print("Quotient =", quotient)
    elif n == 5:
        print("SQUARE ROOT")
        num1 = int(input("Enter the number:\n"))
        sqrt = math.sqrt(num1)
        print("Square root =", sqrt)   
    elif n == 6:
        print("Exiting!..Good Bye!👋")
        break
    else:
        print("Invalid option. Please choose a valid option.")
        break
