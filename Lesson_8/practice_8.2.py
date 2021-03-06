class OwnError(Exception):
    """Создание исключение и привязка его с существующему родительскому классу Exception."""

    def __init__(self, txt):
        self.txt = txt


inp_data_1 = 2  # input("Введите делимое - ")  # Пользовательский запрос на ввод данных.
inp_data_2 = 1 # input("Введите делитель: ")  # Пользовательский запрос на ввод данных.

"""Проверка введённых значений на принадлежность к числам и обработка исключений."""
try:
    inp_data_1, inp_data_2 = int(inp_data_1), int(inp_data_2)
    if inp_data_2 == 0:
        raise OwnError("Сan`not be divided by zero!!!")  # Вызов исключения через raise при выполнении условия.
except ValueError:
    print("Not number!")  # Стандартное исключение если ввели не номер.
except OwnError as err:  # Вывод исключения после вызова raise.
    print(err)
else:
    print(f"Division result - {inp_data_1 / inp_data_2}")  # Вывод, если всё корректно.
finally:
    print("Done.")  # Вывод окончания процедуры.
