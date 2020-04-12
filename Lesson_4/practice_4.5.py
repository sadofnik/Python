from functools import reduce

"""Необходимо получить результат вычисления произведения всех элементов списка 
всех чётных чисел от 100 до 1000 включительно"""


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, [i for i in range(100, 1001, 2)]))
