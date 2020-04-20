from random import randrange

"""Родительский класс определяет общие атрибуты экземпляров. Методы, определяющие движение, аправление
движения автомобиля и текущую скорость. Вывод базовой информации."""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Марка: {self.name}, Цвет: {self.color}, Скорость: {self.speed}, "
              f"{'Полицеская машина' if self.is_police else 'гражданская машина'}")

    def go(self):
        print(f"Машина едет.")

    def stop(self):
        print(f"Машина остановилась.")

    def turn(self):
        direction = ["Север", "Запад", "Юг", "Восток"]
        for i in range(0, randrange(1, 5)):
            print(f"Машина повернула {direction[randrange(0, 4)]}.")

    def show_speed(self):
        print(f"Текущая скорость {self.speed}.")


"""Определение дочерних классов и методов."""


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, trunk):
        super().__init__(speed, color, name, is_police)
        self.trunk = trunk

    def show_speed(self):
        print("Машина едет с превышением скорости.") if self.speed > 60 else Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, roof):
        super().__init__(speed, color, name, is_police)
        self.roof = roof


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, salon):
        super().__init__(speed, color, name, is_police)
        self.salon = salon

    def show_speed(self):
        print("Машина едет с превышением скорости.") if self.speed > 40 else Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, flash_light):
        super().__init__(speed, color, name, is_police)


"""Функция вызова методов родительского класса."""


def mod_car(a):
    a.go()
    a.show_speed()
    a.turn()
    a.stop()


car_town_car = TownCar(55, "grey", "Audi", False, "300l")
mod_car(car_town_car)

car_sport_car = SportCar(125, "red", "Ferrari", False, "No")
mod_car(car_sport_car)

car_work_car = WorkCar(55, "grey", "Mercedes", False, "leather salon")
mod_car(car_work_car)

car_police_car = PoliceCar(75, "black", "Porsche", True, "On")
mod_car(car_police_car)
