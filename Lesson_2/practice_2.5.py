# Вставка вводимых значений, в имеющийся список по ранжированию
question = input("Хотите ввести число? да/нет: ").lower()
my_list = [7, 5, 3, 3, 3, 2]
while question == "да":  # Начало цикла по согласию пользователя
    number = int(input("Введите натуральное чило: "))
    if number > 0:
        if number <= my_list[-1]:  # Проверка наименьшего числа
            my_list.append(number)
        else:
            for i in my_list:  # Условие вставки введённого числа в список
                if number > i:
                    my_list.insert(my_list.index(i), number)
                    break
        print(my_list)  # Вывод результата
        question = input("Хотите ввести ещё число? да/нет: ").lower()  # Запрос на продолжение ввода
    else:
        print("Это не натуральное число")  # Обработка исключения

print(my_list)  # Вывод результата
