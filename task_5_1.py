def numbers(num=int(input('Ввелите число: \n'))):
    for a in (x for x in range(num+1) if x % 2 != 0):
        yield a


for b in numbers():
    print(b)
