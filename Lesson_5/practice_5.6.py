a = open("files/text_6.txt", "r", encoding="UTF-8")
b = dict()  # Словарь для итогового вывода
"""Цикл извлечения числовых данных по условиям"""
for i in a:
    sum_number = 0
    for el in i.partition(":")[2].split():
        if el == "-":
            continue
        else:
            sum_number += int(el.partition("(")[0])
    b[i.partition(":")[0]] = sum_number     # Ввод данных из цикла в словарь с формированием ключа
a.close()
# print(b)    # Обычный вывод словаря
for k, v in b.items():  # Красивый вывод словаря
    print(f"{k:<15}  {v:>5}")
