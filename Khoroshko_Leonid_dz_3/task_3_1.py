def num_translate(number=input('Введите число от 0 до 10 на английском:\n ')):
    translate = ' '
    print(number_dict.get(number))
    return translate


number_dict = {"zero": "ноль",
               "one": "один",
               "two": "два",
               "three": "три",
               "four": "четыре",
               "five": "пять",
               "six": "шесть",
               "seven": "семь",
               "eight": "восемь",
               "nine": "девять",
               "ten": "десять"}

print(num_translate())
