"""
Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она
реализовала методы set_kg() - для задания нового значения килограммов, get_kg()  - для вывода текущего
значения кг. Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и
вывода значений. Помогите ей переделать класс с использованием функции property() и свойств-декораторов.
Код приведен ниже.


class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def get_kg(self):
        return self.__kg
"""
from typing import Union


class KgToPounds:

    def __init__(self, kg: Union[int, float]):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg: Union[int, float]):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


weight = KgToPounds(12)
assert weight.to_pounds() == 26.46
assert weight.kg == 12
weight.kg = 41
assert weight.kg == 41
weight.kg = 'десять'
