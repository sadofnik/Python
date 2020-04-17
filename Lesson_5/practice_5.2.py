with open("files/text_2.txt", "r", encoding="UTF-8") as f_obj:
    for ind, el in enumerate([i for i in f_obj], 1):
        print(f"{ind} - row (строка); {len(el.split())} - amount words (количество слов); text (текст): {el}")
    """Дополнительный вывод итоговых значений"""
    print(
        f"Итого: {f_obj.seek(0) + len([line for line in f_obj])}"
        f" строк, {f_obj.seek(0) + len(f_obj.read().split())} слов")
