# Пункт A)

print('--------------------------------------------- Пункт A. --------------------------------------------------------')
price_list = [71.12, 71.81, 84, 73.39, 20.08, 87.17, 13, 56, 67.44, 60.50, 7.47, 79.55, 43, 29.49, 6.77,
              37.28, 97, 0.20, 25, 97.81]
print(price_list)
new_price_list = ''
for x in price_list:
    x = format(float(x), '.2f')
    r, k = str(x).split(".")
    new_price = ('{} руб. {} коп., '.format(r, k))
    new_price_list += new_price
print(new_price_list)
price_list_id = id(price_list)

# Пункт B)

print('--------------------------------------------- Пункт B. --------------------------------------------------------')
price_list.sort()
new_price_list_s = ''
for x in price_list:
    x = format(float(x), '.2f')
    r, k = str(x).split(".")
    new_price = ('{} руб. {} коп., '.format(r, k))
    new_price_list_s += new_price
print(price_list)
print(new_price_list_s)
if price_list_id == id(price_list):
    print('Объект списка после сортировки остался тот же!!!')
    print(price_list_id, id(price_list))
else:
    print('Объект списка после сортировки изменился!!!')

# Пункт C)

print('--------------------------------------------- Пункт C. --------------------------------------------------------')

price_list_reverse = [71.12, 71.81, 84, 73.39, 20.08, 87.17, 13, 56, 67.44, 60.50, 7.47, 79.55, 43, 29.49, 6.77,
                      37.28, 97, 0.20, 25, 97.81]
price_list_reverse.sort(reverse=True)
price_list_reverse_1 = ''
for x in price_list_reverse:
    x = format(float(x), '.2f')
    r, k = str(x).split(".")
    new_price = ('{} руб. {} коп., '.format(r, k))
    price_list_reverse_1 += new_price
print(price_list_reverse)
print(price_list_reverse_1)

# Пункт D)

print('--------------------------------------------- Пункт D. --------------------------------------------------------')
print(price_list_reverse[0:5])
print(price_list_reverse_1[0:83])
