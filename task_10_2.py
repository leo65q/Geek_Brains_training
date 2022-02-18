class Clothes:

    def __init__(self, V, H):
        self.V = V
        self.H = H

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {(self.V / 6.5 + 0.5) + (2 * self.H + 0.3) :.2f} м. ткани'


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Для пошива пальто нужно: {self.V / 6.5 + 0.5 :.2f} м. ткани'


class Costume(Clothes):
    @property
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.H + 0.3 :.2f} м. ткани'


сlothes = Clothes(55, 55)
coat = Coat(55, None)
costume = Costume(None, 55)
print(coat.consumption)
print(costume.consumption)
print(сlothes.consumption)
