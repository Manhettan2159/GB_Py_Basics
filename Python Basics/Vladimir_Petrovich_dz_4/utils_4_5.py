#Импорт функции
from task_2_3 import curency_rates
import sys

#Реализация запуска из командной строки с аргументом кода валюты.
print(curency_rates('usd'))
print(curency_rates('gbp'))
print(curency_rates('byn'))

#Реализация запуска из командной строки с аргументом кода валюты.
print(curency_rates(sys.argv[1]))





