class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    """ Расчёт массы асфальта из расчёта высоты 5см """

    def calc(self, height=5, mass=25):
        asphalt_mass = int(self._length * self._width * height * mass)
        print(f"Понадобится: {asphalt_mass // 1000} т. асфальта")


""" Запрос данных о длине и ширине дороги. Можно добавить высоту асфальта в пользовательский ввод"""
asphalt_calc = Road(int(input("Введите длину дороги в метрах: ")), int(input("Введите ширину дороги в метрах: ")))
asphalt_calc.calc()
