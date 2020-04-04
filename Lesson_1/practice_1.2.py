time = int(input("Введите число: "))
hour = time // 3600 ## Вычисляем целые часы
minute = (time - (hour * 3600)) // 60  ## Вычисляем целые минуты
second = time - (hour * 3600) - minute * 60  ## Вычисляем целые секунды
print(f"{hour :02} : {minute :02} : {second :02}") ## Выводим результат в формате чч:мм:сс
