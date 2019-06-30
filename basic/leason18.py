# try

try:
    a_file = open("eer.txt", "r+")
except Exception as e:
    print(e)
    response = input("do you want to create a new file:")
    if response == "y":
        a_file = open("eer.txt", "w")
    else:
        pass
else:
    a_file.write("test try")
    a_file.close()
