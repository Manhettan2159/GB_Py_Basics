"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
"""
#Обьявление функции с аргументом count(кол-во шуток) и repeat(Y,y - повторы слов разрешены, N,n- запрещены)
def getjokes(count: int, repeat: str):
    import random
    #Списки внутри функции
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    #Обьявление счетчика и выходного списка.
    i = 0
    jokes_list = []
    #Условие для шуток с повторами.
    if repeat == 'Y' or repeat == 'y':
        while i < count:
            jokes_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            i += 1
        return jokes_list
    #Условие для шуток без повторов.
    elif repeat == 'N' or repeat == 'n':
        while i < count:
            jokes_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            del_list = jokes_list[i].split()
            nouns.remove(del_list[0])
            adverbs.remove(del_list[1])
            adjectives.remove(del_list[2])
            i += 1
        return jokes_list


if __name__ == '__main__':
    print(getjokes(5,'N'))