"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
#Реализация через yield
def odd_to_num_generator(num: int) ->int:
    for i in range(1,num,2):
        yield i

if __name__ == '__main__':
    num = odd_to_num_generator(20)
    print('Yield generator initialized!')
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))

#Реализация без yield, через генератор списков.
    print('List generator initialized!')
    odd_num_generator = [i for i in range(1,20,2)]
    print(*odd_num_generator,sep = '\n')


    #Реализация без yield через генератор.
    print('Non yield generator initialized!')
    odd_num_generator_2 = (i for i in range(1,20,2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))
    print(next(odd_num_generator_2))



