n = [5,2,7,1,8,4]
n.sort
print(n)
m = len(n)//2
if len(n)%2 == 1:
    print(n[m])
else:
    print((n[m]+n[m-1])/2)
