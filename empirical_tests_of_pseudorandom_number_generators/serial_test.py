import numpy as np
import pandas as pd
import datetime
import time
from scipy import stats
import math
from collections import Counter
from open_file import open_f
def run_serial():
    print('Добро пожаловать в сериальный тест')
    number = input('Выберите последовательность для тестирования, полученный:\n (1) по методу вычетов  \n (2) по методу М-последовательности \n (3) Выйти в меню тестов \n (4) Выйти в основное меню \n Введите номер(число): ')
    if number == '1':
        s_otr, s_np, s_np_norm, interval_in_posled = open_f(num=1)
        dlina_bloka = '2'
        N = len(s_otr) / int(dlina_bloka)
        s_otr = s_otr * 10
        s_otr = [int(k) for k in s_otr]
        s_interval = []
        i = 0
        while i < (len(s_otr) - int(dlina_bloka)):
            s_interval.append(s_otr[i:i + int(dlina_bloka)])
            i += int(dlina_bloka)
        s_interval_slice = []
        for k in s_interval:
            lp = ''
            for n in k: lp = lp + str(n)
            s_interval_slice.append(lp)
        s_interval_slice = [int(k) for k in s_interval_slice]
        spisok_chisel = np.arange(0, int(str(1) + str(0) * int(dlina_bloka)))
        count_s_interval_slice = Counter(s_interval_slice)
        chast_theor = len(s_otr) / (int(dlina_bloka)) / int(str(1) + str(0) * int(dlina_bloka))
        accum = []
        for k in spisok_chisel:
            if k in count_s_interval_slice: accum.append((count_s_interval_slice[k] - chast_theor) * (count_s_interval_slice[k] - chast_theor) / chast_theor)
            else: accum.append(chast_theor * chast_theor / chast_theor)
        alpha = stats.chi2.ppf([0.95], 99)
        print('Хи квадрат равен {}'.format(sum(tuple(accum))))
        print('Критерий хи-вадрат: хи(0.95) = {} , хи_тест = {}'.format(alpha[0], sum(tuple(accum))))
        print('Тест пройден?', (alpha[0] > sum(tuple(accum))))
    elif number == '2':
        s_otr, interval_in_posled = open_f(num=2)
        dlina_bloka = '2'
        s_interval = []
        i = 0
        while i < (len(s_otr) - int(dlina_bloka)):
            s_interval.append(s_otr[i:i + int(dlina_bloka)])
            i += int(dlina_bloka)
        s_interval_slice = []
        for k in s_interval:
            lp = ''
            for n in k:
                lp = lp + str(n)
            s_interval_slice.append(lp)
        s_interval_slice = [int(k) for k in s_interval_slice]
        spisok_chisel = np.array([0, 1, 10, 11])
        count_s_interval_slice = Counter(s_interval_slice)
        chast_theor = (len(s_otr)) / (int(dlina_bloka)) / 4
        accum = []
        for k in spisok_chisel:
            accum.append(pow((count_s_interval_slice[k] - chast_theor), 2) / chast_theor)
        alpha = stats.chi2.ppf([0.95], 4)
        print('Хи квадрат равен {}'.format(sum(tuple(accum))))
        print('Критерий хи-вадрат: хи(0.95) = {} , хи_тест = {}'.format(alpha[0], sum(tuple(accum))))
        print('Тест пройден?', (alpha[0] > sum(tuple(accum))))
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
run_serial()