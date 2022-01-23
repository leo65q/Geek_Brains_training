name_dict = {}


def thesaurus(*args):
    for name in args:

        if name_dict.get(name[0]):
            name_dict[name[0]].append(name)
        else:
            name_dict[name[0]] = [name]

    return name_dict


print(thesaurus('Александр', 'Леонид', 'Кирилл', 'Елизавета', 'Степан', 'Владимир', 'Иван', 'Тимур', 'София', 'Сергей',
                'Даниил', 'Валерия', 'Никита', 'Екатерина'))
