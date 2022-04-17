#Обьявление функции
def num_translate(input_num: str) -> str:
#Словарь внутри функции, что бы функция работала автономно.
    num_dict = {
        'one' : 'один',
        'two' : 'два',
        'three' : 'три',
        'four' : 'четыре',
        'five' : 'пять',
        'six' : 'шесть',
        'seven' : 'семь',
        'eight' : 'восемь',
        'nine' : 'девять',
        'ten' : 'десять',
                        }
    #Условия для входящей строки начинающейся с заглавной буквы и с прописной.
    if input_num.istitle() == True:
        return (num_dict.get(input_num.lower())).capitalize()
    else: return num_dict.get(input_num)

if __name__ == '__main__':
    print(num_translate('Nine'))

