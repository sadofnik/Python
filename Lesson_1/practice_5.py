rev = int(input('Введите выручку фирмы: '))
cost = int(input('Введите издержки фирмы: '))
if rev > cost:
    prof = rev - cost
    rent = prof / rev * 100
    print(f"Прибыль фирмы составила: {prof}")
    print(f"Рентабельность выручки фирмы составила: {rent:.3}%")
    count = int(input('Сколько сотрудников в вашей фирме: '))
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {prof / count}")
elif rev == cost:
    print(f"Фирма вышла в ноль!")        
else:
    lose = cost - rev
    print(f"Убыток фирмы составил: {lose}")



