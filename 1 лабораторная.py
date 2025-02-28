# Четные четырехричные числа, не превышающие 204710, у которых вторая справа цифра равна 1. Выводит на экран цифры числа, исключая единицы. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
with open('chisla.txt') as fd: file = fd.read().split()
chars = {'4', '5', '6', '7', '8', '9'}
dictionary = {'1.0' : 'один', '1.5': 'одна целая пять десятых', '2.0': 'два', '2.5': 'две целых пять десятых'}
def num_to_word(averagenum): return dictionary[averagenum]
for element in file:
    if element.isdigit() and element.isalnum() and any(char in element for char in chars) == False:
        if len(element) >1 and int(element, 4) <= 2047 and int(element, 4) % 2 == 0 and element[-2] == '1':
            num = element.replace('1', '')
            checklist = list(num)
            checklist.sort()
            sr_num = str((int(checklist[0]) + int(checklist[-1])) / 2)
            print(element, '. Цифры числа без 1: ', num, '. Среднее число между минимальным и максимальным: ', sr_num, ' (', num_to_word(sr_num), ')', sep="")