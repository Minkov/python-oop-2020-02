from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * pi


c = Circle(5)
print(c.__dict__)
print(c.area())
