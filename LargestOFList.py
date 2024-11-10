A = []
n = int(input("Enter how many numbers\n"))
for i in range (n):
    num = int(input("Enter the value: "))
    A.append(num)
print(A)
largest = 0
for i in A:
    if i > largest:
        largest = i
print("Largest =", largest)
