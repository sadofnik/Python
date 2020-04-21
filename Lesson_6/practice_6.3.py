"""Родительский класс с определением атрибутов"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


"""Дочерний класс с определением методов"""
"""Метод get_full_name складывает атрибуты ФИО и вывод
 метод get_total_income определяет общий доход с выводом"""


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + " " + self.surname
        print(f"Ф.И.О. сотрудника: {full_name}")

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        print(f"Доход сотрудника: {total_income}")


def quest_data():
    try:
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        position = input("Введите должность: ")
        income_wage = float(input("Введите размер оклада: "))
        income_bonus = float(input("Введите размер премии: "))
        return name, surname, position, income_wage, income_bonus
    except:
        print("Вы ввели некорректное значение.")


try:
    user_1 = Position(*quest_data())
    user_1.get_full_name()
    user_1.get_total_income()
except:
    print("Enter error!")
