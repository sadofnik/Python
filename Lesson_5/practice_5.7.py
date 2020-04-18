import json
# Объявляем переменные и словари
profit = {}
pr = {}
prof = 0
average_profit = 0
i = 0
with open("files/text_7.txt", "r", encoding="UTF-8") as data:
    for el in data:     # Излекаем данные из файла построчно для дальнейшей обработки
        name, firm, margin, damage = el.split()
        profit[name] = int(margin) - int(damage)    # Расчёт прибыли
        if profit.setdefault(name) >= 0:    # Заносим результаты вычислений в словарь
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:  # Расчёт средней прибыли
        average_profit = prof / i
        print(f"Средняя прибыль - {average_profit:.2f}")
    else:
        print(f"Средняя прибыль - отсутсвует. Все работают в убыток")
    print(f"Прибыль каждой компании - {profit}")
    pr = {"Средняя прибыль": round(average_profit)}
    list_prof_dict = [profit, pr]   # Создаём список словарей для дальнейшей работы


with open("files/file_7.json", "w+", encoding="UTF-8") as write_json:
    json.dump(list_prof_dict, write_json, ensure_ascii=False, indent=4)    # Вносим данные в json файл с форматированием
    js_str = json.dumps(list_prof_dict, ensure_ascii=False)
    print(f"Создан json-файлв папке files")
