'''
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

def transform_string(value) -> str:
    if value >= 5 and value <= 20:
        message = str(f'{value} процентов')
    elif value%10==1:
        message = str(f'{value} процент')
    elif value%10>=2 and value%10<=4:
        message = str(f'{value} процента')
    else:
        message = str(f'{value} процентов')

    return message

if __name__ == '__main__':
    for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
        print(transform_string(n))
