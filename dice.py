"""Геттеры и сеттеры — это методы в объектно-ориентированном программировании,
используемые для доступа к приватным свойствам объекта."""

import random

class Dice:
    def __init__(self):
        self.__side = None #private
        self.nun_side = 6

    @property # Геттеры читают значение свойства.
    def side(self):
        return self.__side

    def roll(self):
        self.__side = random.randint(1, self.nun_side)

    @side.setter # Сеттеры изменяют значение свойства.
    def side(self, new_side: int):
        if 1 <= new_side <= self.nun_side and type(new_side) == int:
            self.__side = new_side
        else:
            raise ValueError("Неверное значение.")

    def __str__(self):
        if self.__side:
            return f'{self.__side}'
        else:
            raise ValueError("Кубик не подброшен.")

    def __lt__(self, other):
        return self.side < other.side

    def __gt__(self, other):
        return self.side > other.side

    def __eq__(self, other):
        return self.side == other.side


