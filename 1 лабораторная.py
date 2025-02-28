# Четные четырехричные числа, не превышающие 204710, у которых вторая справа цифра равна 1. Выводит на экран цифры числа, исключая единицы. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
with open('chisla.txt') as fd:
    file = fd.read().split()
chars = {'4', '5', '6', '7', '8', '9'}
def num_to_word(sr_num):
    WORDS_ONES = ['ноль', 'один', 'два']
    return WORDS_ONES[sr_num]
for element in file:
    list = []
    if element.isdigit():
        if int(element, 4) <= 2047 and int(element, 4) % 2 == 0 and element[-2] == '1':
            num = element.replace('1', '')
            for i in num:
                list.append(i)
            list.sort()
            sr_num = (int(list[0]) + int(list[-1])) // 2
            print(element, '. Цифры числа без 1: ', num, '. Среднее число между минимальным и максимальным: ', sr_num, ' (', num_to_word(sr_num), ')', sep="")
        else: print(element, ' Элемент не соответствует условию')
    else: print(element, ' Элемент не соответствует условию')