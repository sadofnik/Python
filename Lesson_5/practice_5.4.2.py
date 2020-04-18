from translate import Translator

translator = Translator(to_lang="ru")
# print(translation)

"""Сделал перевод с применением translate"""
with open("files/text_4.txt", "r", encoding="UTF-8") as english:
    rus = open("files/text_4.2.txt", "w+", encoding="UTF-8")
    for i in english.readlines():
        a = i.split()[0]
        translation = translator.translate(a)
        rus.writelines(f"{translation} {i.split()[1]} {i.split()[2]}\n")
    print(rus.readlines())
    rus.close()
