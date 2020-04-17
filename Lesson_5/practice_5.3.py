salary_list = []    # Объявляем список для вывода результата
middle_salary = float()    # Объявляем переменную для записи из цикла
with open("files/text_3.txt", "r", encoding="UTF-8") as employee:
    for line in employee:   # Цикл, проверяющий условия задания, где зп < 20000
        salary = float(line.split()[1])
        if 20000.00 > salary:
            salary_list.append(line.split()[0])     # Передаём данные в список
        middle_salary = middle_salary + salary  # Передаём данные в список
    print(f"Сотрудники, чья З/П менее 20000.00:\n{', '.join(salary_list)}")     # Вывод первого условия задания
    print(f"Средний доход: {middle_salary / (employee.seek(0) + len([el for el in employee]))}")    # Вывод второго условия задания
