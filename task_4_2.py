import requests


def currency_rates(currency_code=input("Введите название валюты: ")):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    if not (currency_code and url):
        return None

    currency_code = currency_code.upper()

    respond = requests.get(url)

    if respond.ok:

        cur = respond.text.split(currency_code)

        if len(cur) == 1:
            return None

        value = cur[1].split("</Value>")[0].split("<Value>")[1]

        value = float(value.replace(",", "."))

        return value

    else:
        return None


print(currency_rates())
