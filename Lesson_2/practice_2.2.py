a = input("Введите список элементов: ").split()
for i in range(0, len(a) - 1, 2):
     a[i], a[i+1] = a[i+1], a[i]  # Меняем местами соседние пары элементов
print(a)
