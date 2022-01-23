from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokes_list = []


def get_jokes():
    global jokes_list
    for x in range(0, 5):
        word_1 = choice(nouns)
        nouns.remove(word_1)
        word_2 = choice(adverbs)
        adverbs.remove(word_2)
        word_3 = choice(adjectives)
        adjectives.remove(word_3)
        jokes = '{} {} {}'.format(word_1, word_2, word_3)
        jokes_list.append(jokes)
    return jokes_list


print(get_jokes())
