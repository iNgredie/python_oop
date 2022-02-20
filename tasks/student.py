"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:

    surname: str
    name: str
    group: int
    average_score: float

    def __init__(
        self,
        surname: str,
        name: str,
        group: int,
        average_score: float,
    ):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score


if __name__ == '__main__':
    s1 = Student('Иванов', 'Иван', 1, 4.7)
    s2 = Student('Петров', 'Петр', 1, 5.0)
    s3 = Student('Сидоров', 'Сидр', 1, 5.5)
    s4 = Student('Олегов', 'Олег', 1, 6.7)
    s5 = Student('Смирнов', 'Коля', 1, 4.1)

    students_list = [s1, s2, s3, s4, s5]
    print(sorted(students_list))
    print(sorted(students_list, reverse=True))