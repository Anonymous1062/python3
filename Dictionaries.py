x = {"Douwe": "Sheep", "Karsten": "Jesus"}

print(x["Douwe"])
x["Jacques"] = "Vikuotin"

del x["Douwe"]

for key in x:
    print(key)
    print(x[key])

if "Jacques" in x:
    print(x["Jacques"])

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

dic4 = {}

for key in dic1:
    dic4[key] = dic1[key]
for key in dic2:
    dic4[key] = dic2[key]
for key in dic3:
    dic4[key] = dic3[key]
print(dic4)

dic5 = {}
for i in range(20):
    j = i + 1
    dic5[j] = j ** 2
print(dic5)
