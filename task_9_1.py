import time
a = 1


class TrafficLight:
    __color_r = 'красный'
    __color_y = 'жёлтый'
    __color_g = 'зелёный'

    @staticmethod
    def runnig(num):
        time.sleep(num)


while a == 1:
    color = TrafficLight()
    print('\033[31m' + color._TrafficLight__color_r)
    color.runnig(7)
    print('\033[33m' + color._TrafficLight__color_y)
    color.runnig(3)
    print('\033[32m' + color._TrafficLight__color_g)
    color.runnig(5)
