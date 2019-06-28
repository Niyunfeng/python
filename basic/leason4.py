# basic data set

# tuple
tup = ("python", 2.7, 64)
for i in tup:
    print(i)

print(tup[0])

print("#")

# dictionary
dic = {}
dic["lan"] = "python"
dic["version"] = 2.7
dic["platform"] = 64
for key in dic:
    print(key, dic[key])

print(dic["lan"])

person = {"name": "lisi", "age": 16, "city": "shanghai"}

for key, value in person.items():
    print(key, ":", value)

print("#")

# set
s = set(("python", "python2", "python3", "python"))
for item in s:
    print(item)

print("python" in s)

print(len(s))

print(s.pop())
