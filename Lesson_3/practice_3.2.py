def user_info(**kwargs):  # Простая функция с передачей именнованых параметров
    return kwargs


# Вывод результата одной строкой(словарём) с запросом данных и обработкой через функцию.
# Пока что реализован только текстовый вариант, т.к. обработку даты и эл.адреса через импорт ещё не проходили.

print(user_info(
    first_name=input("Ваше имя: ").capitalize(),
    second_name=input("Ваша фамилия: ").capitalize(),
    birthday=input("Дата рождения: "),
    location=input("Город проживания: ").capitalize(),
    email=input("Электронная почта: "),
    number_phone=input("Номер телефона: ")
))

# Вывод только аргументов
# a = user_info(
#     first_name=input("Ваше имя: ").capitalize(),
#     second_name=input("Ваша фамилия: ").capitalize(),
#     birthday=input("Дата рождения: "),
#     location=input("Город проживания: ").capitalize(),
#     email=input("Электронная почта: "),
#     number_phone=input("Номер телефона: ")
# )
#
# for k,v in a.items():
#     print(v, end=" ")
