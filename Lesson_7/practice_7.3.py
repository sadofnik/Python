class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        i = self.quantity - other.quantity
        if i < 0:
            return f"Некорректная операция, вычитание не может быть произведено"
        else:
            return i

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        i = self.quantity // other.quantity
        if i <= 0:
            return f"Число близко к нулю"
        else:
            return i

    def make_order(self, in_a_row):
        self.in_a_row = in_a_row
        print(f"Организация клеток по рядам: ")

        i = self.quantity
        while i > 0:
            if i > self.in_a_row:
                print('*' * self.in_a_row)
                i -= self.in_a_row
            else:
                print('*' * i)
                i -= i


a = Cell(23)
b = Cell(2)
print(f"Объединение двух клеток: {a + b}")
print(f"Разность количества двух клеток: {a - b}")
print(f"Произведение двух клеток: {a * b}")
print(f"Деление двух клеток: {a / b}")
a.make_order(5)
