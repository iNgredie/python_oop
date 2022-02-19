"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""
from collections.abc import Iterator


class Counter:
    value: int

    def __init__(self):
        self.value = 0

    def increase(self, num: int = 1):
        self.value += num

    def decrease(self, num: int = 1):
        self.value -= num

    def __iter__(self):
        return self

    def __next__(self) -> int:
        value = self.value
        self.increase()
        return value
