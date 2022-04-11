'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из 
  этого списка, сумма цифр которых делится нацело на 7. 
* Решить задачу под пунктом b, не создавая новый список.)
'''



def sum_list_1(user_list):
    sum_list=0
    sum=0
    """Вычисляет сумму чисел списка user_list, сумма цифр которых делится нацело на 7"""
    for num in user_list:
        temp_value=num
        while num != 0:
            sum = sum + num % 10
            num = num // 10
        if sum % 7 == 0:
            sum_list+=temp_value
        else:
            pass
        sum=0
    return sum_list  # Верните значение полученной суммы.


def sum_list_2(user_list) :
    sum=0
    sum_list=0
    for value in user_list:
        i=0
        new_value=value+17
        temp_value = value+17
        while new_value != 0:
            sum = sum + new_value % 10
            new_value = new_value // 10
        if sum % 7 == 0:
            sum_list+=temp_value
        else:
            pass
        i=i+1
        sum=0
    return sum_list

# Генерация списка кубов нечетных чисел при помощи цикла for
if __name__ == '__main__':
    test_list = []  # Обьявление списка
    for i in range(1, 1000):  # Генерация списка кубов нечетных чисел при помощи цикла for
        if i % 2 == 0:
            pass
        else:
            test_list.append(i ** 3)


    print(test_list)
    result_1 = sum_list_1(test_list)
    print(result_1)
    result_2 = sum_list_2(test_list)
    print(result_2)