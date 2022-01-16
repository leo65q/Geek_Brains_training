for percent in range(-1, 100):
    number = str(percent + 1)
    number_list = list(number)
    if int(number_list[-1]) == 1 and percent + 1 != 11:
        print('{} процент'.format(percent + 1))
    elif 1 < int(number_list[-1]) <= 4:
        if 10 < percent + 1 <= 14:
            print('{} процентов'.format(percent + 1))
        else:
            print('{} процента'.format(percent + 1))
    else:
        print('{} процентов'.format(percent + 1))
