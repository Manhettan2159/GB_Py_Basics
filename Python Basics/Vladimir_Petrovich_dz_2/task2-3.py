"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
 (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
"""

random_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#Cчетчик
i = 0
#Цикл по начальной длинне списка.
while i < len(random_list):
    element = random_list[i]
    #Входное условие для единичных цифр
    if element.isdigit() == True and len(element) == 1 :
            #Кавычки
            random_list.insert(random_list.index(element),'"')
            random_list.insert(random_list.index(element)+1, '"')
            #Добавление 0.
            new_str = f'0{element[0]}'
            random_list[random_list.index(element)] = new_str
            #Cчетчик +3 т.к в список добавлено 2 новых строки
            i += 3

    #Входное условие для двойных чисел, добавление кавычек.
    elif element.isdigit() == True and len(element) > 1 :
        random_list.insert(random_list.index(element), '"')
        random_list.insert(random_list.index(element) + 1, '"')
        i += 3
    #Входное условие для одиночных чисел со знаком + или -.Добавляем кавычки и 0.
    elif element[0] == '+' or element[0] == '-' and len(element) < 3:
        if element[0] == '+':
            random_list.insert(random_list.index(element), '"')
            random_list.insert(random_list.index(element) + 1, '"')
            new_str = f'+0{element[1]}'
            random_list[random_list.index(element)] = new_str
            i +=3
        elif element[0] == '-':
            random_list.insert(random_list.index(element), '"')
            random_list.insert(random_list.index(element) + 1, '"')
            new_str = f'-0{element[1]}'
            random_list[random_list.index(element)] = new_str
            i += 3

    #Входное условие для десятичных чисел со знаком, добавляем кавычки
    elif element[0] == '+' or element[0] == '-' and len(element) > 2:
        random_list.insert(random_list.index(element), '"')
        random_list.insert(random_list.index(element) + 1, '"')
        i +=3

    else:
        #Ничего не добавлено, счетчик +1.
        i += 1

print(random_list)
#Сбор итоговой строки с заглавной буквой.
print(' '.join(random_list).capitalize())
'''
Сломал всю голову на этой задаче, раз 50 переписывал и стирал пока не разобрался со счетчиками =).
'''

