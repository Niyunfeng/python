# True/false break/continue

a = True
while a:
    b = input("type something:")
    if b == "1":
        # a = False
        # break
        continue
    else:
        pass
    print("still in while")

print("finish run")

