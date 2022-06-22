"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

import time
import random



def non_repeat_list(src_list: list):
    src_copy = src_list.copy()
    for n in src_copy:
        if src_copy.count(n) > 1:
            src.remove(n)


start_time = time.time()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
non_repeat_list(src)
print(src)
end = time.time()

print(end - start_time)

