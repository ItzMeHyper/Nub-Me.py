def check_num(n):
    if(n>0):
        return 1
        #print("The number is positive")
    elif(n<0):
        return -1
        #print("The number is negative")
    else:
        return 0
        #print("The number is zero")

num = int(input("Enter a number\n"))
result = check_num(num)
if (result == 1):
    print("The number is positive")
elif (result == -1):
    print("The number is negative")
else: 
    print("The given number is zero")
