import numpy as np
import pandas as pd
import datetime
import time
from scipy import stats
import math
from collections import Counter
from open_file import open_f
def run_poker():
    print('Добро пожаловать в покер тест')
    number = input('Выберите последовательность для тестирования, полученный:\n (1) по методу вычетов  \n (2) по методу М-последовательности \n (3) Выйти в меню тестов \n (4) Выйти в основное меню \n Введите номер(число): ')
    if number == '1':
        s_otr, s_np, s_np_norm, interval_in_posled = open_f(num=1)
        dlina_bloka = 5
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
            for n in k:lp = lp + str(n)
            s_interval_slice.append(lp)
        class1 = []; class2 = []; class3 = []; class4 = []; class5 = []; class6 = []; class7 = []
        for k in s_interval_slice:
            if len(Counter(k).items()) == 5: class1.append(k)
            if len(Counter(k).items()) == 1: class7.append(k)
            if len(Counter(k).items()) == 4: class2.append(k)
            if len(Counter(k).items()) == 3:
                if list(Counter(k).most_common(2))[0][1] == list(Counter(k).most_common(2))[1][1] == 2: class3.append(k)
                else: class4.append(k)
            if len(Counter(k).items()) == 2:
                if list(Counter(k).most_common(2))[0][1] == 3: class5.append(k)
                else: class6.append(k)
        d = 10; pol = pow(d,4)
        d1 = (d-1); d2 = (d-2); d3 = (d-3); d4 = (d-4); d10 = (10*d1*d2)
        P1 = d1 * d2 * d3 * d4 / pol; P2 = d10 * d3 / pol; P3 = 15 * d1 * d2 / pol; P4 = d10 / pol
        P5 = 10 * d1 / pol; P6 = 5 * d1 / pol; P7 = 1 / pol
        int_len = int(interval_in_posled[1]) - int(interval_in_posled[0])
        PT1 = len(class1) / int_len
        PT2 = len(class2) / int_len
        PT3 = len(class3) / int_len
        PT4 = len(class4) / int_len
        PT5 = len(class5) / int_len
        PT6 = len(class6) / int_len
        PT7 = len(class7) / int_len
        khi = pow((PT1 - P1), 2) / P1 + pow((PT2 - P2), 2) / P2 + pow((PT3 - P3), 2) / P3 + pow((PT4 - P4), 2) / P4 + \
              pow((PT5 - P5), 2) / P5 + pow((PT6 - P6), 2) / P6 + pow((PT7 - P7), 2) / P7
        alpha = stats.chi2.ppf([0.95], 6)
        print('Хи квадрат равен {}'.format(khi))
        print('Критерий хи-вадрат: хи(0.95) = {} , хи_тест = {}'.format(alpha[0], khi))
        print('Тест пройден?', (alpha[0] > khi))

    elif number == '2':

        s_otr, interval_in_posled = open_f(num=2)
        dlina_bloka = 5
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
        class1 = []; class2 = []; class3 = []; class4 = []; class5 = []; class6 = []; class7 = []
        for k in s_interval_slice:
            if len(Counter(k).items()) == 5: class1.append(k)
            if len(Counter(k).items()) == 1: class7.append(k)
            if len(Counter(k).items()) == 4: class2.append(k)
            if len(Counter(k).items()) == 3:
                if list(Counter(k).most_common(2))[0][1] == list(Counter(k).most_common(2))[1][1] == 2: class3.append(k)
                else: class4.append(k)
            if len(Counter(k).items()) == 2:
                if list(Counter(k).most_common(2))[0][1] == 3: class5.append(k)
                else: class6.append(k)
        d = 10; pol = pow(d, 4)
        d1 = (d - 1); d2 = (d - 2); d3 = (d - 3); d4 = (d - 4); d10 = (10 * d1 * d2)
        P1 = d1 * d2 * d3 * d4 / pol; P2 = d10 * d3 / pol; P3 = 15 * d1 * d2 / pol; P4 = d10 / pol; P5 = 10 * d1 / pol; P6 = 5 * d1 / pol; P7 = 1 / pol
        int_len = int(interval_in_posled[1]) - int(interval_in_posled[0])
        PT1 = len(class1) / int_len
        PT2 = len(class2) / int_len
        PT3 = len(class3) / int_len
        PT4 = len(class4) / int_len
        PT5 = len(class5) / int_len
        PT6 = len(class6) / int_len
        PT7 = len(class7) / int_len
        khi = pow((PT1 - P1), 2) / P1 + pow((PT2 - P2), 2) / P2 + pow((PT3 - P3), 2) / P3 + pow((PT4 - P4), 2) / P4 + \
              pow((PT5 - P5), 2) / P5 + pow((PT6 - P6), 2) / P6 + pow((PT7 - P7), 2) / P7
        alpha = stats.chi2.ppf([0.95], 6)
        print('Хи квадрат равен {}'.format(khi))
        print('Критерий хи-вадрат: хи(0.95) = {} , хи_тест = {}'.format(alpha[0], khi))
        print('Тест пройден?', (alpha[0] > khi))

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
run_poker()
