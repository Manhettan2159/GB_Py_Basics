#Импорт модуля запросов
import requests



def curency_rates(val_code :str) -> str:
    #Проверка на верхний регистр
    if not val_code.isupper():
        val_code = val_code.upper()
    #Выполнение запроса к API
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    #Сохранение заголовка в переменную для вывода даты и времени.
    head = (response.headers)
    date = head['Date']
    cur_list = response.json()
    curency = ''
    #Проверка на случай неправильно указанного кода валюты.
    try:
        curency = cur_list['Valute'][f'{val_code}'].get('Value')
    except KeyError:
        print('Curency code is not valid')
        exit()
    #Строка вывода
    return f'{date}. Curency of {val_code} is {curency} RUB.'


if __name__ == '__main__':
    print(curency_rates('usd'))





