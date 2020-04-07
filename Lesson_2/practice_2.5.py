# Вставка вводимых значений, в имеющийся список по ранжированию
a = int(input("Введите натуральное чило: "))
my_list = [7, 5, 3, 3, 3, 2]

if a > 0:
    if a <= my_list[-1]:
        my_list.append(a)
    else:
        for i in my_list:
            if a > i:
                my_list.insert(my_list.index(i), a)
                break
    print(my_list)
else:
    print("Это не натуральное число")
