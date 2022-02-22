class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Все верно!'
                else:
                    return f'Ввели неверную дату!'
            else:
                return f'Ввели неверную дату!'
        else:
            return f'Ввели неверную дату!'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('22 - 02 - 2022')
print(today)
print(today.valid(22, 2, 2022))
print(Data.valid(11, 11, 2023))
print(today.valid(11, 13, 2011))
print(Data.extract('22 - 02 - 2022'))
print(today.extract('26 - 07 - 1997'))


