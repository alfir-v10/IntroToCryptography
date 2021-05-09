import numpy as np
import pandas as pd
import datetime
import time
from scipy import stats
import math
from open_file import open_f
def run_corr():
    print('Добро пожаловать в корреляционный тест')
    number = input('Выберите последовательность для тестирования, полученный:\n (1) по методу вычетов  \n (2) по методу М-последовательности \n (3) Выйти в меню тестов \n (4) Выйти в основное меню \n Введите номер(число): ')
    if number == '1':
        s_otr, s_np, s_np_norm, interval_in_posled = open_f(num=1)
        i = 0; accum = 0
        while i < (len(s_otr) - 1):
            accum += s_otr[i] * s_otr[i + 1]
            i += 1
        slag1 = len(s_otr) * accum
        accum = 0
        for k in s_otr: accum += k * k
        s1 = accum * len(s_otr)
        accum = 0
        for k in s_otr: accum += k
        s2 = accum ** 2
        R = (slag1 - s2) / (s1 - s2)
        xaq = len(s_otr)
        a_lev = -(1 / (xaq - 1)) - 2 / (xaq - 1) * np.sqrt(xaq * (xaq - 3) / (xaq + 1))
        a_prav = (1 / (xaq - 1)) + 2 / (xaq - 1) * np.sqrt(xaq * (xaq - 3) / (xaq + 1))
        print(f'Тест пройден?({a_lev}<{R}<{a_prav})', a_lev < R < a_prav)
    elif number == '2':
        s_otr, interval_in_posled = open_f(num=2)
        i = 0
        accum = 0
        while i < (len(s_otr) - 1):
            accum += s_otr[i] * s_otr[i + 1]
            i += 1
        slag1 = len(s_otr) * accum
        accum = 0
        for k in s_otr: accum += k * k
        s1 = accum * len(s_otr)
        accum = 0
        for k in s_otr: accum += k
        s2 = accum ** 2
        R = (slag1 - s2) / (s1 - s2)
        xaq = len(s_otr)
        a_lev = -(1 / (xaq - 1)) - 2 / (xaq - 1) * np.sqrt(xaq * (xaq - 3) / (xaq + 1))
        a_prav = (1 / (xaq - 1)) + 2 / (xaq - 1) * np.sqrt(xaq * (xaq - 3) / (xaq + 1))
        print(f'Тест пройден?({a_lev}<{R}<{a_prav})', a_lev < R < a_prav)
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