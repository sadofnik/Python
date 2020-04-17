"""Многократный ввод пользовательских данных с записью в файл. Файл создаётся при первом вводе."""
try:
    with open("files/text_1.txt", "x", encoding="UTF-8") as f_cool:
        text = input("Please, enter words: ")
        while text != '':
            f_cool.write(f"{text}\n")
            text = input("Please, enter words: ")
except FileExistsError:
    print("File exists")
except FileNotFoundError:
    print("No such file or directory")
