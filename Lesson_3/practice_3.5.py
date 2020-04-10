def func_sum():
    numbers = input("Введите числа через пробел: ").split()  # Принимаем пользовательские значеия
    sum_number = 0  # Объявление переменной для сохранения промежуточных результатов
    try:
        while numbers[-1] != 'q':   # Проверка условия завершения программы
            for i in range(len(numbers)):
                sum_number = sum_number + int(numbers[i])   # Суммирование введённых значений и запись в переменную
            print(sum_number)
            numbers = input("Введите числа через пробел: ").split()
        for i in range(len(numbers) - 1):   # Расчёт, исключая последний аргумент
            sum_number = sum_number + int(numbers[i])
        print(f"Общая сумма: {sum_number}")
        print("Вы завершили работу программы.")
    except ValueError:
        print(f"Вы ввели недопустимый символ - '{numbers[-1]}'")  # Вывод исключений


func_sum()
