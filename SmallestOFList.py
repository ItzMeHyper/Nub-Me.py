A = []
n = int(input("Enter how many numbers\n"))
for i in range (n):
    num = int(input("Enter the value: "))
    A.append(num)
print(A)
smallest = A[0]
for i in A:
    if i < smallest:
        smallest = i
print("smallest =", smallest)
