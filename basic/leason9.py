# read/write file

# \n line commend
text = "This is my first line.\nThis is my second line.\nThis is my third line.\n"
print(text)

text = "\tThis is my first line.\n\tThis is my second line.\n\tThis is my third line.\n"
print(text)

my_file = open("text.txt", "w")  # 用法: open('文件名','形式'), 其中形式有'w':write;'r':read.
my_file.write(text)  # 该语句会写入先前定义好的 text
my_file.close()  # 关闭文件

print("--------------------------")

append_text = "\tThis is append line."
my_file = open("text.txt", "a")
my_file.write(append_text)
my_file.close()

my_file = open("text.txt")
try:
    all_the_text = my_file.read()
    print(all_the_text)
finally:
    my_file.close()

print("--------------------------")

file = open("text.txt", "r")
try:
    context = file.readline()  # 读取第一行
    print(context)
    context = file.readlines(2)  # 读取第二行文本
    print(context)
finally:
    file.close()
