number = int(input('Введите целое положительное число: '))
max = 0 ## Переменная для сравнения с макс. цифрой

while number > 0:
    i = number % 10
    if i == 9:
        max = i
        break
    elif i > max:
         max = i
    number = number // 10

print(f"Самая большая цифра: {max}")
           
        
