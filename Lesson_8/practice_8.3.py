class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


def list_number():
    numbers = input("Введите числа через пробел, "
                    "для выхода введите 'q': ").split()  # Принимаем пользовательские значеия
    try:
        while numbers[-1] != 'q':  # Проверка условия завершения программы
            for i in range(len(numbers)):
                if not numbers[i].isdigit():   # Проверка введённых значений
                    raise OwnError(f"Введён неверный тип данных: {type(numbers[i])}, '{numbers[i]}' - не число.")
                else:
                    list_numbers.append(numbers[i])
            numbers = input("Введите числа через пробел, "
                            "для выхода введите 'q': ").split()  # Принимаем пользовательские значеия
    except OwnError as err:  # Вывод исключения после вызова raise
        print(err)
        list_number()


list_numbers = []  # Объявление переменной для сохранения промежуточных\итоговых результатов
list_number()   # Вызов функции
print(f"Вы завершили работу программы. Ваш список: {list_numbers}")
