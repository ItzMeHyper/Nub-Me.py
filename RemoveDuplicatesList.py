A = []
n = int(input("How many numbers\n"))
for i in range (n):
    num = int(input("Enter the value: "))
    A.append(num)
print(A)
nL = []
for i in A:
    if i not in nL:
        nL.append(i)
print(nL)
