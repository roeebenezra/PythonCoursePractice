# ex3 -  Roee Ben Ezra 206123994
#        Yinon Tzomi  208489369
#
#  Ex3 - Shapes classes with operations


import bisect
from abc import ABC, abstractmethod


# Abstract Shape class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def perimeter(self):
        return 3.14 * self._radius * 2

    def area(self):
        return 3.14 * self._radius ** 2

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, length):
        if length < 1:
            self._radius = 1
        else:
            self._radius = length

    def __str__(self):
        return f'Circle:radius = {self._radius}'


class Rectangle(Shape):
    def __init__(self, width, height):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @height.setter
    def height(self, length):
        if length < 1:
            self._height = 1
        else:
            self._height = length

    @width.setter
    def width(self, length):
        if length < 1:
            self._width = 1
        else:
            self._width = length

    def __str__(self):
        return f'Rectangle:width = {self._width}, ' \
               f'height = {self._height}'

    def perimeter(self):
        return (2 * self._height) + (2 * self._width)

    def area(self):
        return self._height * self._width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return f'Square:length = {self.width}'


class ShapesCollection:
    def __init__(self, shapes):
        self.shapes = shapes
        self.shapes.sort(key=lambda x: x.area())

    def __len__(self):
        return len(self.shapes)

    def insert(self, s):
        if type(s) == Shape:
            bisect.insort(self.shapes, s)

    def __str__(self):
        lst_str = 'Shapes in collection: '
        for x in self.shapes:
            lst_str += '\n' + str(x)
        return lst_str

    def biggestPerimeterDiff(self):
        max_perimeter = 0
        for x in self.shapes[::-1]:
            for y in self.shapes:
                curr = x.perimeter() - y.perimeter()
                if curr > max_perimeter:
                    max_perimeter = curr
        return max_perimeter

    def sameAreaAs(self, s):
        return [x for x in self.shapes if x.area() == s.area()]

    def howManyQuadrilaterals(self):
        return sum(isinstance(i, Rectangle) for i in self.shapes)


# if __name__ == '__main__':
#     c = Circle(3)
#     c2 = Circle(5)
#     r = Rectangle(4, 5)
#     s = Square(10)
#     r2 = Rectangle(5, 5)
#
#     lst = [c, c2, r, s, r2]
#     shapes_object = ShapesCollection(lst)
#
#     print(*shapes_object.sameAreaAs(c2))
#     print(shapes_object.biggestPerimeterDiff())
#     print(shapes_object.howManyQuadrilaterals())
#     print(shapes_object.__len__())
#     print(shapes_object.__str__())
