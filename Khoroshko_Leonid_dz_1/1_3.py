percent = 0
list_1 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
list_2 = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
while percent <= 100:
    if percent in list_1:
        print('{} процент'.format(percent))
    elif percent in list_2:
        print('{} процента'.format(percent))
    else:
        print('{} процентов'.format(percent))
    percent += 1
