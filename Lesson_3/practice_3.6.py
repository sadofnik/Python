def int_func():
    slow_lat_letter = input("Введите слово маленькими латинскими буквами: ")  # Ввод пользователского значения
    slow_lat_letter_after = []  # Объявление переменной для дальнейшего сравнения
    if len(slow_lat_letter.split()) > 1:    # Условие выполнения функции для массового ввода
        if all(96 < ord(i) < 123 or i == ' ' for i in slow_lat_letter):
            print(slow_lat_letter.title())
        else:
            print("Вы ввели недопустимые символы.")
    else:
        for i in list(slow_lat_letter):  # Цикл для проверки Unicode каждого введенного символа для еденичного ввода
            if 96 < ord(i) < 123:  # Проверка по диапозону мал.лат.букв
                slow_lat_letter_after.append(i)
            else:
                print(f"{i} - не подходит под условие")
    if len(slow_lat_letter_after) == len(slow_lat_letter):  # Услвие вывода результата
        print(slow_lat_letter.capitalize())


int_func()