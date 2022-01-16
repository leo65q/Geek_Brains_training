cubes = []
for x in range(1, 1000, 2):
    if x % 2 != 0:
        x = x ** 3
        cubes.append(x)
print(cubes)
summ_list = []
for x in cubes:
    summ = 0
    number = str(x)
    number_list = list(number)
    for y in number_list:
        summ += int(y)
    if summ % 7 == 0:
        summ_list.append(x)
print(summ_list)
