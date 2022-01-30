a = int(input('Ввелите число: \n'))
numbers = (x for x in range(a+1) if x % 2 != 0)
for i in numbers:
    print(i)

