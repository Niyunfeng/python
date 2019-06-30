# multiple list

multi_dim_a = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]

print(multi_dim_a)

print(multi_dim_a[0][2])

# dictionary

a_list = [1, 2, 3, 4, 5, 6, 7, 8]

d1 = {"apple": 1, "pear": 2, "orange": 3}
d2 = {1: "a", 2: "b", 3: "c"}
d3 = {"1": "a", "b": 2, "c": 3}

print(d1["apple"])
print(a_list[0])
print(d3["b"])

del d1["pear"]
print(d1)
d3["b"] = 20
print(d3)


def fun():
    return 1


d4 = {"apple": [1, 2, 3], "pear": {1: 3, 3: "a"}, "orange": fun}
out = d4["orange"]()
print(out)
print(d4["pear"][1])
