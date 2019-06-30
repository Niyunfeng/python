# list operation

a = [1, 3, 54, 5, 6, 7, 7, 3, -1]
a.append(19)  # add 19 to the end of the list
print(a)
a.insert(1, 2)  # add 2 to the index 2 position of the list
print(a)
a.remove(1)  # delete the first item in the list that appears with a value of 1
print(a)

print(a[0])  # show the first value in the list

print(a[-1])  # show the last value in the list

# show the values of the all items in list from index 0 through index 2(defore index 3)
print(a[0:3])

# print the index of the item of value 2 that first appears in the list a
print(a.index(2))

# Count the number of the occurrences of a value in the list
print(a.count(-1))

# default sort from smallest to largest
a.sort()
print(a)

# sort form largest to smallest
a.sort(reverse=True)
print(a)
