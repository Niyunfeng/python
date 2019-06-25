# loop
""" ----------------while---------------- """
condition = 10
while condition:
    print(condition)
    condition -= 1
    if condition == 2:
        condition = None

print("##")

a = range(10)
# invert order
a = a[::-1]
while a:
    print(a[-1])
    a = a[: len(a) - 1]
""" ------------------------------------- """
print("##")
""" -----------------for----------------- """
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in example_list:
    print(i)
print("#")
for i in range(10):
    print(i)

""" ------------------------------------- """
