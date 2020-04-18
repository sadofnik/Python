from math import factorial

""" Функция, создающая объект-генератор и, возращающая факториал числа"""


def generator():
    for i in range(1, 16):
        yield i, factorial(i)


for el in generator():
    print(f"Факториал числа {el[0]} равен: {el[1]}")  # Вывод результата работы функции в цикле.
