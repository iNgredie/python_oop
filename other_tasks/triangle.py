"""
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
"""
from typing import List


class TriangleChecker:

    sides: List[int]

    def __init__(self, sides: List[int, float]):
        self.sides = sides

    def is_triangle(self):
        if all([isinstance(side, (int, float)) for side in self.sides]):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'


triangle1 = TriangleChecker([2, 3, 4])
assert triangle1.is_triangle() == 'Ура, можно построить треугольник!'
triangle2 = TriangleChecker([77, 3, 4])
assert triangle2.is_triangle() == 'Жаль, но из этого треугольник не сделать'
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
assert triangle3.is_triangle() == 'Нужно вводить только числа!'
triangle4 = TriangleChecker([77, -3, 4])
assert triangle4.is_triangle() == 'С отрицательными числами ничего не выйдет!'
