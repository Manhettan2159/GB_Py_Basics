"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def naive_realisation():
    total_time = ''
    # Ввод значения в секундах.(Предусмотрен ввод значения условии функции, но изначально я сделал такой вариант с ручным вводом.Пусть останется =)
    duration = int(input('Enter duration '))
    # Обьявление переменных
    sec = 0
    min = 0
    hrs = 0
    ds = 0

    # список для тестирования(В методичке было задание применить цикл для тестирования. Изначально сделал,пусть останется в комментарии.
    # check_list=[123123123,1232135436,346346,13,65646,2345,65446,67456]

    # цикл для тестирования
    # for duration in check_list:

    if duration < 60:
        total_time = ('Duration is', duration, 'sec')
    elif duration < 3600 and duration >= 60:
        min = duration // 60
        sec = duration % 60
        total_time = ('Duration is', min, 'min', sec, 'sec', )
    elif duration >= 3600 and duration < 86400:
        min = duration // 60
        sec = duration % 60
        if min < 60:
            total_time =('Duration is', min, 'min', sec, 'sec', )
        elif min > 60:
            hrs = min // 60
            min = min % 60
            total_time =('Duration is', hrs, 'hour(s)', min, 'min', sec, 'sec', )
    else:
        sec = duration % 60
        ds = duration // 86400
        min = (duration - ds * 86400) // 60
        if min >= 60:
            hrs = min // 60
            min = min % 60
        else:
            hrs = 0

        total_time = ('Duration is', ds, 'days ', hrs, 'hour(s)', min, 'min', sec, 'sec', )
    return total_time




def one_cycle_realisation():
    total_time = ''
    time_list = []
    sec = 0
    min = 0
    hrs = 0
    ds = 0
    i=0
    while i<5:
        duration = int(input('Enter duration '))
        if duration < 60:
            total_time = ('Duration is', duration, 'sec')
        elif duration < 3600 and duration >= 60:
            min = duration // 60
            sec = duration % 60
            total_time = ('Duration is', min, 'min', sec, 'sec',)
        elif duration >= 3600 and duration < 86400:
            min = duration // 60
            sec = duration % 60
            if min < 60:
                total_time = ('Duration is', min, 'min', sec, 'sec',)
            elif min > 60:
                hrs = min // 60
                min = min % 60
                total_time = ('Duration is', hrs, 'hour(s)', min, 'min', sec, 'sec',)
        else:
            sec = duration % 60
            ds = duration // 86400
            min = (duration - ds * 86400) // 60
            if min >= 60:
                hrs = min // 60
                min = min % 60
            else:
                hrs = 0

            total_time = ('Duration is', ds, 'days ', hrs, 'hour(s)', min, 'min', sec, 'sec',)
        i += 1
        time_list.append(total_time) #Вариант с возвращением списка из функции.
        #print(total_time) #Вариант с принтом после каждого цикла.
    return time_list




if __name__ == '__main__':
    #duration = 628 #Запрос организован внутри функции...
    print(naive_realisation())
    print(one_cycle_realisation())