"""  Задание: должен вернуть [12, 44, 4, 10, 78, 123] из
списка [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] даже если удалить первый и/или последний элемент списка."""

number_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([number_list[el] for el in range(1, len(number_list)) if number_list[el] > number_list[el - 1]])

