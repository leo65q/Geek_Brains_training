from itertools import islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

claasroom = ((tutors[i], klasses[i]) for i in range(len(tutors)))

for c in claasroom:
    print(c)

print((None, klasses[-1]))
print(type(claasroom))
print(*islice(claasroom,9))
print(list(*islice(claasroom,9)))
