#  Выполнение функции возведения в степень помощью операции '**' (первый способ)
def my_func(a, b):
    if b >= 0:  # Проверка условия 'y < 0'
        print(f"Аргумент 'y' должен быть меньше нуля")
    else:
        return print(f"Первый способ: {a ** b:.5}")  # Выполнение функции и вывод результата

#  Объявление переменных, можно задать через 'input' для ввода пользователем
x = float(3.523)
y = int(-2)

my_func(x, y)   # Вызов функции


# Выполнение функции возведения в степень при помощи цикла (второй способ)
def my_func(a, b):
    if b >= 0:  # Проверка условия 'y < 0'
        print(f"Аргумент 'y' должен быть меньше нуля")
    else:
        c = 1  # Объявление переменной для сохранения промежуточных значений
        for i in range(0, b, -1):   # Выполнение цикла можно также сделать через abs(y), чтобы взять число по модулю
            c = a * c
        print(f"Второй способ: {1 / c:.5}")


my_func(x, y)   # Вызов функции

# Вывод результата возмедения с помощью встроенной функции 'pow' для проверки работы функций (проверка)
print(f"Проверка результата: {pow(x, y):.5}")
