from sys import argv

script_name, rate_param, salary_param, prize_param = argv

# Расчёт З\п при вводимых данных из других источников с проверкой ввода

try:
    rate_param, salary_param, prize_param = float(rate_param), float(salary_param), float(prize_param)
    print(f"Выработка в часах: {rate_param}"
          f"\nСтавка в час: {salary_param}"
          f"\nПремия: {prize_param}"
          f"\nЗарплата: {rate_param * salary_param + prize_param}")
except ValueError:  # Вывод исключений, если вводимые данные не являются числовыми.
    print("Ошибка при вводе данных, должны быть только цифры.")

