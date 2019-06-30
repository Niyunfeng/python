# Class


class Calaulator:
    name = "Good Calaulator"
    price = 18

    def add(self, x, y):
        print(self.name)
        result = x + y
        return result

    def minus(self, x, y):
        result = x - y
        return result

    def times(self, x, y):
        result = x * y
        print(result)

    def divide(self, x, y):
        result = x / y
        print(result)


cal = Calaulator()
print(cal.name)
print(cal.add(1, 2))
print(cal.minus(1, 2))
print(cal.times(2, 1))
print(cal.divide(2, 1))


class Calaulator1:
    name = "Good Calaulator"
    price = 18

    def __init__(self, name, price, height, wight, width):
        self.name = name
        self.price = price
        self.height = height
        self.wight = wight
        self.width = width


c = Calaulator1("Bad Calaulator", 10, 11, 12, 13)
print(c.price)
print(c.name)
print(c.height)
print(c.width)
print(c.wight)

c.wight = 100
print(c.wight)
