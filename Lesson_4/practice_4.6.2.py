from itertools import count, cycle, islice

#  Выполнение 6-го задания со звёздочкой
# Первый вариант объединения задачи а и б
x = 0
for el in cycle([i for i in islice(count(0), 5)]):
    if x > 8:
        break
    else:
        print(el)
        x += 1

# Второй вариант объединения задачи а и б
print([el for el in islice(cycle([i for i in islice(count(0), 5)]), 9)])
