duration = int(input("Введите число: "))
one_minute = 60
one_hour = 3600
one_day = 86400
if duration < one_minute:
    print('{} сек'.format(duration))
elif one_minute <= duration < one_hour:
    minute = duration // one_minute
    second = duration % one_minute
    print('{} мин {} сек'.format(minute, second))
elif one_hour <= duration < one_day:
    hour = duration // one_hour
    duration = duration % one_hour
    minute = duration // one_minute
    second = duration % one_minute
    print('{} час {} мин {} сек'.format(hour, minute, second,))
elif one_day <= duration:
    day = duration // one_day
    duration = duration % one_day
    hour = duration // one_hour
    duration = duration % one_hour
    minute = duration // one_minute
    second = duration % one_minute
    print('{} дн {} час {} мин {} сек'.format(day, hour, minute, second, ))
