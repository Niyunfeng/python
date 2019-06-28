# def function
def function(a, b, value=10):
    print("This is a function")
    c = a + b
    print("a + b :", c)
    print("Function default value :", value)


function(1, 2)

if __name__ == "__main__":
    print("unit test")

# variable function
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, "total grade is:", total_grade)


report("Mkie", 99, 100)

# key parameter
def portrait(name, **kw):
    print("name is", name)
    for k, v in kw.items():
        print(k, v)


portrait("Mike", age=24, country="china", education="bachelor")

