import numpy as np
import pandas as pd
import datetime
import time
from scipy import stats
import math
def run_interval():
    print('Добро пожаловать в интервальный тест')
    number = input('Выберите последовательность для тестирования, полученный:\n (1) по методу вычетов  \n (2) по методу М-последовательности \n (3) Выйти в меню тестов \n (4) Выйти в основное меню \n Введите номер(число): ')
    if number == '1':
        file = open(r'cong.txt', 'r')
        f = file.read()
        s = f.split(',')
        s = s[:-1]
        print('Вы выбрали последовательность сгенерированная по методу вычетов. Данный файл содержит последовательность длиной ' + str(len(s)))
        s = np.array(s, dtype=int)
        s=s/max(s)
        #alpha = float(input('Введите уровень значимости alpha: '))
        #dov_int = float(input('Введите доверительный интервал d'))
        #n = np.var(s[:1000000]) / (pow(dov_int, 2) * alpha)
        #print(f"Число испытаний равно {n} в соответсвии с которым выборочное среднее попадает в доверительный интервал {dov_int} с зад ур знач {alpha}")
        alpha = float(input('Введите уровень значимости alpha: '))
        n = int(input('Введите число испытаний n(не более 1млн): '))
        if int(n) < len(s):
            s_exp = s[:int(n)]
            d_exp = abs(np.mean(s_exp) - 0.5)
            print(f'{d_exp} Экспериментальный доверительный интервал')
            d_krit = np.std(s) / np.sqrt(n * alpha)
            print(f'{d_krit} Критический доверительный интервал')
            print( 'Для данного уровня значимости и подсчитанного теоретически числа испытаний проверим выполняется ли критерий(Чебышев):', d_exp < d_krit)

            sigma = 1/12
            if alpha == 0.1:
                d_krit_2 = sigma*1.65/pow(n, 1/2)
            elif alpha == 0.05:
                d_krit_2 = sigma*1.96/pow(n, 1/2)
            elif alpha == 0.01:
                d_krit_2 = sigma*2.58/pow(n, 1/2)
            print(f'{d_krit_2} Критический доверительный интервал')
            print(
                'Для данного уровня значимости и подсчитанного теоретически числа испытаний проверим выполняется ли критерий(Норм распред):',
                d_exp < d_krit_2)

        else: print('Число таких испытаний превышает 5млн')
    elif number == '2':
        file = open(r'cong.txt', 'r')
        f = file.read()
        s = f.split(',')
        s = s[:-1]
        print('Вы выбрали последовательность сгенерированная по методу вычетов. Данный файл содержит последовательность длиной ' + str(len(s)))
        s = np.array(s, dtype=int)
        s=s/max(s)
        #alpha = float(input('Введите уровень значимости alpha: '))
        #dov_int = float(input('Введите доверительный интервал d'))
        #n = np.var(s[:1000000]) / (pow(dov_int, 2) * alpha)
        #print(f"Число испытаний равно {n} в соответсвии с которым выборочное среднее попадает в доверительный интервал {dov_int} с зад ур знач {alpha}")
        alpha = float(input('Введите уровень значимости alpha: '))
        n = int(input('Введите число испытаний n(не более 1млн): '))
        if int(n) < len(s):
            s_exp = s[:int(n)]
            d_exp = abs(np.mean(s_exp) - 0.5)
            print(f'{d_exp} Экспериментальный доверительный интервал')
            d_krit = np.std(s) / np.sqrt(n * alpha)
            print(f'{d_krit} Критический доверительный интервал')
            print( 'Для данного уровня значимости и подсчитанного теоретически числа испытаний проверим выполняется ли критерий(Чебышев):', d_exp < d_krit)

            sigma = 1/12
            if alpha == 0.1:
                d_krit_2 = sigma*1.65/pow(n, 1/2)
            elif alpha == 0.05:
                d_krit_2 = sigma*1.96/pow(n, 1/2)
            elif alpha == 0.01:
                d_krit_2 = sigma*2.58/pow(n, 1/2)
            print(f'{d_krit_2} Критический доверительный интервал')
            print(
                'Для данного уровня значимости и подсчитанного теоретически числа испытаний проверим выполняется ли критерий(Норм распред):',
                d_exp < d_krit_2)

        else: print('Число таких испытаний превышает 5млн')

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
run_interval()