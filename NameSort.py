Names = []
n = int(input("Enter how many names\n"))
for i in range (n):
    name = input("Enter the names: ")
    Names.append(name)
print(Names)
Names.sort()
print(Names)
