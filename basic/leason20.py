# copy

from copy import *

a = [1, 2, 3]
b = a
print("id a:", id(a))
print("id b:", id(b))

b[0] = 100
print("id :", b)
print("a :", a)

# copy

c = copy(a)
c[1] = 1
print("id a:", id(a))
print("id c:", id(c))
print("c:", c)

a = [1, 2, [3, 4]]
c = copy(a)

print("id a:", id(a[2]))
print("id c:", id(c[2]))
print("a[2]:", a[2])
print("c[2]:", c[2])

# deep copy
e = deepcopy(a)
a[1] = 100
print(e)
