#create a list and find min and max from the list
A = []
n = int(input("How many elements\n"))
for i in range (n):
    num = int(input("Enter the value: "))
    A.append(num)
print(A)
print("Minimum value =", min(A))
print("Maximum value =", max(A))