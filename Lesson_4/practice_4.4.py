"""Вернуть все неповторяющиеся элементы в порядке их следования из списка
[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]. Сравнить с  [23, 1, 3, 10, 4, 11]"""

number_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in number_list if number_list.count(el) < 2])