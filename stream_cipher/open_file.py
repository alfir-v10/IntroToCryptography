import numpy as np
def open_f(file_name):
    file = open(file_name,'r')
    f = file.read()
    s = f.split(',')
    s = s[:-1]
    print('Вы выбрали последовательность сгенерированная по методу М-последовательностей. Данный файл содержит последовательность длиной ' + str(len(s)))
    interval_in_posled = input('Введите интервал из последовательности, который хотите выбрать для тестирования(например, 0 10 значит от [0,10]): ')
    interval_in_posled = interval_in_posled.split(' ')
    interval_in_posled = [int(k) for k in interval_in_posled]
    s_otr = np.array(s[interval_in_posled[0]:interval_in_posled[1]], dtype=int)
    return s_otr, interval_in_posled