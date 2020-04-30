class Matrix:

    def __init__(self, param1):
        self.par1 = param1

    """Вывод матрицы красивый"""

    def __str__(self):
        return '\n'.join(['\t'.join([str(i) for i in el]) for el in self.par1])

    """Вытаскиваем каждые значения списка в цикле и сохраняем во временном списке."""

    def __add__(self, other):
        matrix = []
        for i in range(len(self.par1)):
            a = []
            for el in range(len(self.par1[i])):
                a.append(self.par1[i][el] + other.par1[i][el])
            matrix.append(a)
        return Matrix(matrix)


c1 = Matrix([[10, 11, 12], [12, 13, 12], [3, 4, 12]])
c2 = Matrix([[1, 12, 2], [1, 12, 2], [1, 3, 12]])
print(f"Первая матрица:\n{c1}")
print(f"Вторая матрица:\n{c2}")
print(f"Сумма матриц:\n{c1 + c2}")
