incorrect_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
incorrect_list[1] = '"05"'
incorrect_list[-2] = '"+05"'
incorrect_list[3] = '"17"'
new_list = ' '.join(incorrect_list)
print(new_list)
