import requests
from bs4 import BeautifulSoup
import lxml
import sys


def collect_data():
    r = requests.get(url='https://minfin.com.ua/currency/nbu/')
    soup = BeautifulSoup(r.text, 'lxml')
    all_price = soup.find_all('p', class_="sc-1mi6rpw-9 kdhvRG")
    all_currencys = "'USD', 'EUR', 'PLN', 'RUB','UAH'"
    date_of_price = soup.find('span', class_="fn1qeo-0 iiIvzO").text
    print(f"Доступные валюты: {all_currencys}")

    user_input_1 = input("Введи валюту вашей старны.Напишите 'q' если хотите выйти:")
    user_input_2 = input(f"Введи валюту в которую вы хотите перевести '{user_input_1}'.Напишите 'q' если хотите выйти:")
    user_input_3 = input(f"Введи количество {user_input_1} которое вы хотите перевести в {user_input_2}:")

    if user_input_1 == 'UAH':
        if user_input_2 == 'USD':
            a = all_price[0].text.replace(',', "").strip()
            a = f"{a[:2]}.{a[2:]}"
            res = float(user_input_3) / float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()
        elif user_input_2 == 'EUR':
            a = all_price[1].text.replace(',', "").strip()
            a = f"{a[:2]}.{a[2:]}"
            res = float(user_input_3) / float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()
        elif user_input_2 == 'PLN':
            a = all_price[2].text.replace(',', "").strip()
            a = f"{a[0]}.{a[1:]}"
            res = float(user_input_3) / float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()
        elif user_input_2 == 'RUB':
            a = all_price[2].text.replace(',', "").strip()
            a = f"{a[0]}.{a[1:]}"
            res = float(user_input_3) / float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()
    if user_input_1 == 'USD':
        x = all_price[0].text.replace(',', "").strip()
        print(f"{date_of_price}: Доллар США -> {all_price[0].text} грн")
        x = f"{x[:2]}.{x[2:]}"
    elif user_input_1 == 'EUR':
        x = all_price[1].text.replace(',', "").strip()
        print(f"{date_of_price}: Евро -> {all_price[1].text} грн")
        x = f"{x[:2]}.{x[2:]}"
    elif user_input_1 == 'PLN':
        x = all_price[2].text.replace(',', "").strip()
        print(f"{date_of_price}: Польский злотый -> {all_price[2].text} грн")
        x = f"{x[0]}.{x[1:]}"
    elif user_input_1 == 'RUB':
        x = all_price[3].text.replace(',', "").strip()
        print(f"{date_of_price}: Российский рубль -> {all_price[3].text} грн")
        x = f"{x[0]}.{x[1:]}"
    elif user_input_1 == 'q':
        sys.exit()
    else:
        print("Возможно вы ввели что то не правильно,перепроверьте")
        sys.exit()

    if user_input_2 == 'UAH':
        if user_input_1 == 'USD':
            a = all_price[0].text.replace(',', "").strip()
            a = f"{a[:2]}.{a[2:]}"
            res = float(user_input_3) * float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()
        elif user_input_1 == 'EUR':
            a = all_price[1].text.replace(',', "").strip()
            a = f"{a[:2]}.{a[2:]}"
            res = float(user_input_3) * float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()
        elif user_input_1 == 'PLN':
            a = all_price[2].text.replace(',', "").strip()
            a = f"{a[0]}.{a[1:]}"
            res = float(user_input_3) * float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()
        elif user_input_1 == 'RUB':
            a = all_price[2].text.replace(',', "").strip()
            a = f"{a[0]}.{a[1:]}"
            res = float(user_input_3) * float(str(a))
            print(f'Результат {res} {user_input_2}')
            print(f"Округлённо {round(res, 2)} {user_input_2}")
            sys.exit()

    if user_input_2 == 'USD':
        y = all_price[0].text.replace(',', "").strip()
        print(f"{date_of_price}: Доллар США -> {all_price[0].text} грн")
        y = f"{y[:2]}.{y[2:]}"
    elif user_input_2 == 'EUR':
        y = all_price[1].text.replace(',', "").strip()
        print(f"{date_of_price}: Евро -> {all_price[1].text} грн")
        y = f"{y[:2]}.{y[2:]}"
    elif user_input_2 == 'PLN':
        y = all_price[2].text.replace(',', "").strip()
        print(f"{date_of_price}: Польский злотый -> {all_price[2].text} грн")
        y = f"{y[0]}.{y[1:]}"
    elif user_input_2 == 'RUB':
        y = all_price[3].text.replace(',', "").strip()
        print(f"{date_of_price}: Российский рубль -> {all_price[3].text} грн")
        y = f"{y[0]}.{y[1:]}"
    elif user_input_2 == 'q':
        sys.exit()
    else:
        print("Возможно вы ввели что то не правильно или такой валюты у нас нет списке,перепроверьте")
        sys.exit()

    ratio = float(str(x)) / float(str(y))
    result = float(user_input_3) * ratio
    print(f'Результат {result} {user_input_2}')
    print(f"И округлённо {round(result, 2)} {user_input_2}")


def main():
    collect_data()


if __name__ == '__main__':
    main()
