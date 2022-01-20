incorrect_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']
for incorrect_name in incorrect_list:
    correct_name = incorrect_name.split()[-1].capitalize()
    print('Привет, {}!'.format(correct_name))
