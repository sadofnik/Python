dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыри"}
with open("files/text_4.txt", "r", encoding="UTF-8") as english:
    rus = open("files/text_4.1.txt", "w+", encoding="UTF-8")
    for i in english.readlines():
        for el in dictionary.keys():
            if i.split()[0] == el:
                rus.writelines(f"{dictionary.get(el)}"
                          f" {chr(8212)}"
                          f" {i.split()[2]}\n")
    rus.close()

