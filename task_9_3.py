class Worker:
    name = 'Леонид'
    surname = 'Хорошко'
    position = 'Менеджер смены'
    _income = {'wage': 30000, 'bonus': 10000}


class Position(Worker):

    @staticmethod
    def get_full_name():
        print('Полное имя работника: {} {}!'.format(Worker.surname, Worker.name))

    @staticmethod
    def get_total_income():
        full_incom = Worker._income['wage'] + Worker._income['bonus']
        print('Зарабатная плата с надбавками: {} руб.'.format(full_incom))


x = Position()
x.get_full_name()
x.get_total_income()
