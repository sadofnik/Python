# Создание списка товаров с пользовательским вводом. Вывод и аналитика товаров.
count = 0 # Счётчик
sum_list = [] # Инициализация списка
product_dict = {"Название": list(), "Цена": list(), "Количество": list(), "Ед.измерения": list()} # Шаблон словаря
question = input("Вы хотите добавить данные?: ").lower() # Вопрос для вхождения в цикл
while question == 'да': # Цикл для внесения данных в словарь
    count += 1
    product_name = input(f"{tuple(product_dict.keys())[0]} товара: ").lower()
    product_mount = int(input(f"{tuple(product_dict.keys())[1]} товара: "))
    product_count = int(input(f"{tuple(product_dict.keys())[2]} товара: "))
    product_init = input(f"{tuple(product_dict.keys())[3]} товара: ").lower()
    sum_list.append((count, {f"{tuple(product_dict.keys())[0]}": product_name,
                             f"{tuple(product_dict.keys())[1]}": product_mount,
                             f"{tuple(product_dict.keys())[2]}": product_count,
                             f"{tuple(product_dict.keys())[3]}": product_init})) # Внесение данных и в итоговый список
    question = input("Продолжить?: ").lower() # запрос о повторении цикла

for el in range(len(sum_list)): # Вывод результата структуры
    print(sum_list[el])

product_name = []
product_mount = []
product_count = []
product_init = []
product_dict = {"Название": product_name, "Цена": product_mount, "Количество": product_count,
                "Ед.измерения": product_init}
print("\n Аналитика данных")
for i in range(len(sum_list)): # Сбор данных из словарей
    product_name.append(sum_list[i][1].get(f"{tuple(product_dict.keys())[0]}"))
    product_mount.append(sum_list[i][1].get(f"{tuple(product_dict.keys())[1]}"))
    product_count.append(sum_list[i][1].get(f"{tuple(product_dict.keys())[2]}"))
    product_init.append(sum_list[i][1].get(f"{tuple(product_dict.keys())[3]}"))
for k, v in product_dict.items(): # Вывод аналитики
    print(k, v)
