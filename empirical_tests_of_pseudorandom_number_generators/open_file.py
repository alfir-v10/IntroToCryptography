import numpy as np
def open_f(num):
    if num == 1:
        file = open(r'cong.txt', 'r')
        f = file.read()
        s = f.split(',')
        s = s[:-1]
        interval_in_posled = input('Введите интервал из последовательности, который хотите выбрать для тестирования(например, 0 10 значит от [0,10]): ')
        interval_in_posled = interval_in_posled.split(' ')
        interval_in_posled = [int(k) for k in interval_in_posled]
        s_np = np.array(s, dtype=int)
        s_np_norm = s_np / max(s_np)
        s_otr = np.array(s_np_norm[interval_in_posled[0]:interval_in_posled[1]])
        return s_otr, s_np, s_np_norm, interval_in_posled
    elif num == 2:
        file = open(r'm_posled_method.txt','r')
        f = file.read()
        s = f.split(',')
        s = s[:-1]
        print('Вы выбрали последовательность сгенерированная по методу М-последовательностей. Данный файл содержит последовательность длиной ' + str(len(s)))
        interval_in_posled = input('Введите интервал из последовательности, который хотите выбрать для тестирования(например, 0 10 значит от [0,10]): ')
        interval_in_posled = interval_in_posled.split(' ')
        interval_in_posled = [int(k) for k in interval_in_posled]
        s_otr = np.array(s[interval_in_posled[0]:interval_in_posled[1]], dtype=int)
        return s_otr, interval_in_posled
    else: return "ERROR open_file"