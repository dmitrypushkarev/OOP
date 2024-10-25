"""Класс прямоугольник"""

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        """Выводит площадь прямоугольника"""
        print(self.width * self.length)

    def perimetr(self):
        """Выводит периметр прямоугольника"""
        print((self.width + self.length) * 2)

    def scale(self, amount):
        """Увеличивает масштаб"""
        self.width, self.length = self.width * amount, self.length * amount

    def rotate(self):
        """Ротация, меняет длину и ширину местами"""
        self.width, self.length = self.length, self.width

    def __str__(self):
        return f'ширина: {self.width}, длина: {self.length}'

    def __repr__(self):
        return f'ширина: {self.width}, длина: {self.length}'


def test_scale():
    r = Rectangle(3, 4)
    assert r.width == 3
    assert r.length == 4
    r.scale(10)
    assert r.width == 30
    assert r.length == 40




# r = Rectangle(3, 4)
#
# print(f'{r!s}')

# r.area()
# r.perimetr()
# print(r)
# r.rotate()
# print(r)
# r.scale(10)
# print(r)
# print(repr(r))