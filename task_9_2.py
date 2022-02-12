class Road:
    def __init__(self, x, y):
        self._lenght = x
        self._width = y

    def asphalt(self):
        asphalt_masses = (self._lenght * self._width * 25 * 5) // 1000
        print('Необходимо {} т. асфальта.'.format(asphalt_masses))


Road_m = Road(20, 5000)
Road_m.asphalt()
