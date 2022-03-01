"""
Строки в Питоне сравниваются на основании значений символов.
Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
Такое положение дел не устроило Анну.
Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.
"""


class RealString:

    string: str

    def __init__(self, string: str):
        self.string = str(string)

    def __eq__(self, other) -> bool:
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.string) == len(other.string)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.string) < len(other.string)

    def __le__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.string) <= len(other.string)


str1 = RealString('Молоко')
str2 = RealString('Абрикосы растут')
str3 = 'Золото'
str4 = [1, 2, 3]
str5 = 'Золотой'
assert str1 < str4
assert not str1 >= str2
assert str1 == str3
assert str1 < str5



