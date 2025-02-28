# Четные четырехричные числа, не превышающие 204710, у которых вторая справа цифра равна 1. Выводит на экран цифры числа, исключая единицы. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
import re
with open('chisla.txt') as fd: file = fd.read()
dictionary = {'1.0' : 'один', '1.5':'одна целая пять десятых', '2.0': 'два', '2.5':'две целых пять десятых'}
def num_to_word(avg): return dictionary[avg]
match_list = re.findall(r'\b[0123]{,4}1[02]\b|\b1[02]\b', file)
for element in match_list:
    num = element.replace('1', '')
    checklist = list(num)
    checklist.sort()
    avg = str((int(checklist[0]) + int(checklist[-1])) / 2)
    print(element, '. Цифры числа без 1: ',num, '. Среднее число между минимальным и максимальным: ', avg, ' (', num_to_word(avg), ')', sep="")