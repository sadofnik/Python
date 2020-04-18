from random import randrange

"""Запись списка в файл, расчёт всех значений из файла"""
sum_number_list = 0  # Переменная для вывода результата
a = [el for el in range(0, randrange(1, 20))]  # Сгенерированный список с цифрами
with open("files/text_5.txt", "w+") as numbers:     # Использован метод извлечения w+ для записи и чтения
    for el in a:  # Перебор всех позиций в списке для записи в файл
        numbers.write(str(el) + " ")
    numbers.seek(0)  # Возврат курсора
    for i in numbers.readline().split():  # Перебор всех значений в списке для расчёта
        sum_number_list += int(i)
print(f"Сумма всех чисел в файле: {sum_number_list}")  # Вывод результата
