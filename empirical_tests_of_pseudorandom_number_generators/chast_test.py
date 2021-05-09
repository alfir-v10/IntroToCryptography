import numpy as np
import pandas as pd
import datetime
import time
from scipy import stats
import math
def run_chast():
    print('Добро пожаловать в частотный тест')
    number = input('Выберите последовательность для тестирования, полученный:\n (1) по методу вычетов  \n (2) по методу М-последовательности \n (3) Выйти в меню тестов \n (4) Выйти в основное меню \nВведите номер(число): ')
    if number == '1':
        file = open(r'cong.txt', 'r')
        f = file.read()
        s = f.split(',')
        s = s[:-1]
        print('Вы выбрали последовательность сгенерированная по методу вычетов. Данный файл содержит последовательность длиной ' + str(len(s)))
        int_count = input('Введите количество интервалов на которое предстоит разбить отрезок [0,1]: ')
        interval_in_posled = input('Введите интервал из последовательности, который хотите выбрать для тестирования(например, 0 10 значит от [0,10]): ')
        """можно дописать проверку вводимых параметров в int_count вводиться должны одно число, в втором два числа"""
        interval_in_posled = interval_in_posled.split(' ')
        interval_in_posled = [int(k) for k in interval_in_posled]
        delta_interval = 1 / int(int_count)
        otrezok = np.arange(0, 1, delta_interval)
        otrezok = np.hstack((otrezok, otrezok[-1] + delta_interval))
        delta_interval_okrug = len(int_count)
        s_np = np.array(s, dtype=int)
        s_np_norm = s_np / max(s_np)
        interval_slovar = {}
        interval_slovar = {num: [otrezok[num], otrezok[num + 1]] for num in range(len(otrezok) - 1)}
        kolvo_in_interval = {}

        x = s_np_norm[interval_in_posled[0]:interval_in_posled[1]]
        start_time = datetime.datetime.now()
        for n in interval_slovar:
            for k in x:
                if interval_slovar[n][0] <= k <= interval_slovar[n][1]:
                    x = np.delete(x, np.argwhere(x == k))
                    if n in kolvo_in_interval: kolvo_in_interval[n] += 1
                    else: kolvo_in_interval.update({n: 1})
        print('Время выполнения: ', datetime.datetime.now() - start_time)

        x = s_np_norm[interval_in_posled[0]:interval_in_posled[1]]
        end_interval_slovar = {}
        for k in kolvo_in_interval: end_interval_slovar.update({tuple(interval_slovar[k]): kolvo_in_interval[k]})
        chast_theor = len(x) / int(int_count)
        end_interval_spisok = []
        print('Теоретическая частота : {}'.format(chast_theor))
        for k in end_interval_slovar: end_interval_spisok.append([k, end_interval_slovar[k]])
        nuts = []
        for k in end_interval_spisok: nuts.append(k[0][0])
        nuts = sorted(nuts)
        end_of_end_interval_spisok = []
        for k in nuts:
            for l in end_interval_spisok:
                if k == l[0][0]: end_of_end_interval_spisok.append(l)
        haski = []
        for k in end_interval_spisok: haski.append(k[1])
        print('Проверка на целостность используемой последовательности {}'.format(sum(haski)))
        empty_tuple = []
        for k in end_of_end_interval_spisok[1:]: empty_tuple.append(pow((k[1] - chast_theor), 2) / chast_theor)
        alpha = stats.chi2.ppf([0.01, 0.99], int(int_count) - 1)
        print('Хи квадрат равен {}'.format(sum(tuple(empty_tuple))))
        print('Критерий хи-вадрат {} < {} < {}'.format(alpha[0], sum(tuple(empty_tuple)), alpha[1]))
        print('Тест пройден?', (alpha[0] < sum(tuple(empty_tuple)) < alpha[1]))
    elif number == '2':
        file = open(r'm_posled_method.txt', 'r')
        f = file.read()
        s = f.split(',')
        s = s[:-1]
        print('Вы выбрали последовательность сгенерированная по методу М-последовательностей. Данный файл содержит последовательность длиной ' + str(len(s)))
        interval_in_posled = input('Введите интервал из последовательности, который хотите выбрать для тестирования(например, 0 10 значит от [0,10]): ')
        interval_in_posled = interval_in_posled.split(' ')
        interval_in_posled = [int(k) for k in interval_in_posled]
        sum_sum = 0
        for k in s[interval_in_posled[0]:interval_in_posled[1]]:
            if k == '0': sum_sum += 1
            else: sum_sum -= 1
        s_obs = abs(sum_sum) / np.sqrt(len(s[interval_in_posled[0]:interval_in_posled[1]]))
        print('Pvalue = {}'.format(math.erfc(s_obs)))
        print('Тест пройден?', (math.erfc(s_obs) > 0.01))
    elif number == '3':
        from menu import main_menu
        main_menu(x='2')
    elif number == '4':
        from menu import main_menu
        main_menu()
    else:
        print("Введен некорректный запрос!")
        from menu import opros
        opros()