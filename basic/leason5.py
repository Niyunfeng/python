# iterator

# define Fib class
class Fib(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        return StopIteration()


# using fib object
for i in Fib(10):
    print(i)

# iterator yield
def Fib_(max):
    a, b = 0, 1
    while max:
        r = b
        a, b = b, a + b
        max -= 1
        yield r


for i in Fib_(10):
    print(i)
