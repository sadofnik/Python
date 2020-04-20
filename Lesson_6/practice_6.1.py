from time import sleep


class TrafficLight:
    __color = ("red", "yellow", "green")
    """ Функция работы светофора. Идёт перебор до конца кортежа, потом идёт в другую сторону."""
    def running(self, timer):
        self.timer = timer
        el = 1
        p = 1
        for i in range(0, 5):
            if p == 0 or p == len(self.__color) - 1:
                el = -el
            while self.__color[p] != "yellow":
                print(self.__color[p])
                p += el
                sleep(self.timer)
            print(self.__color[p])
            sleep(2)
            p += el


tl_street_1 = TrafficLight()
tl_street_1.running(7)
