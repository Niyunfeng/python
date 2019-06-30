# tuple list

a_tuple = (1, 21, 23, 5)

print("Print tuple: ", a_tuple)

print("Traversing tuple")

j = 0
for i in a_tuple:
    j += 1
    print(j, ":", i)

for index in range(len(a_tuple)):
    print("Index:", index, "number in tuple =", a_tuple[index])

a_list = [1, 235, 566, 45, 23]
print("Print list: ", a_list)

j = 0
print("Traversing list")
for i in a_list:
    j += 1
    print(j, ":", i)

for index in range(len(a_list)):
    print("Index:", index, "number in list =", a_list[index])

