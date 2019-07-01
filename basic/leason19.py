# zip lambda map

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
abc = zip(a, b, c)
print(list(abc))

func = lambda x, y: x + y
# x = int(input("input x:"))
# y = int(input("input y:"))
x = 1
y = 2
print(func(x, y))


def fun(x, y):
    return x + y


# print(list(map(fun, [1], [2])))
print(list(map(fun, [1, 2], [3, 4])))
