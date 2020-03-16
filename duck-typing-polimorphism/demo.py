from abc import ABC, abstractmethod
from math import pi, sqrt


# class Shape:
#     def __init__(self):
#         if type(self) == Shape:
#             raise TypeError('Shape is an abstract class')
#
#     def __str__(self):
#         return f'Area: {self.area()}; Perimeter: {self.perimeter()}'
#
#     def area(self):
#         raise TypeError
#
#     def perimeter(self):
#         raise TypeError


class Shape(ABC):
    def __str__(self):
        return f'Area: {self.calculate_area()}; Perimeter: {self.calculate_perimeter()}'

    @abstractmethod
    def calculate_area(self): pass

    @abstractmethod
    def calculate_perimeter(self): pass


class Circle(Shape):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self._radius = radius

    def calculate_area(self):
        return self._radius * self._radius * pi

    def calculate_perimeter(self):
        return 2 * self._radius * pi


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        p = self.calculate_perimeter() / 2
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))


def print_shape(s: Shape):
    print(s.calculate_area())


print_shape(Circle(3))
