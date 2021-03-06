"""
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None),
например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
"""







def pup_info(tutors,klasses: list):
    i = 0
    while i < len(tutors):
        try:
            pup_tuple =(tutors[i],klasses[i])
        except IndexError:
            pup_tuple =(tutors[i],None)
        i += 1
        yield pup_tuple

if __name__ == '__main__':

    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б',]

    pup_tuple = pup_info(tutors,klasses)

    print(next(pup_tuple))
    print(next(pup_tuple))
    print(next(pup_tuple))
    print(next(pup_tuple))
    print(next(pup_tuple))
    print(next(pup_tuple))
    print(next(pup_tuple))
    print(next(pup_tuple))








