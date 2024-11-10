d1 = {"Roll No.": "23cs001", "Name": "Akhil", "Course":"B.Tech"}
print(d1)
print(d1.get("Name"))
print(d1.get("Marks", 0))
d1["Marks"] = 50
print(d1)
d1["Course"] = "BCA"
print(d1)
del d1["Roll No."]
print(d1)
for i in d1.keys():
    print(i)
for i in d1.values():
    print(i)

for x,y in d1.items():
    print(f"{x}:{y}")
#print("test")
for x,y in sorted(d1.items(), reverse=True):
    print(f"{x}:{y}")
print(len(d1))