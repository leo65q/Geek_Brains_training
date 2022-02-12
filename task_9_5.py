class Stationery:
    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "Ручка."

    def draw(self):
        print("Пишем конспект.")


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "Карандаш."

    def draw(self):
        print("Рисуем эскиз.")


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "Маркер."

    def draw(self):
        print("Выделяем важную часть конспекта.")


pen = Pen()
pencil = Pencil()
handle = Handle()
for some in [pen, pencil, handle]:
    print(some.title)
    some.draw()
    print()
