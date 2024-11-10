#wirte a program to find the grade of a student
marks = int(input("Enter the marks\n"))

if (marks>=90):
    print("The grade is A")
elif (marks<90 and marks>=80):
    print("The grade is B")
elif (marks<80 and marks>=70):
    print("The grade is C")
elif (marks<70 and marks>=60):
    print("The grade is D")
else:
    print("Failed")
