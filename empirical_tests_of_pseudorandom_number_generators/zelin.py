import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from open_file import open_f
from collections import Counter
from scipy import stats
import scipy.integrate as integrate
def model_zelin():
    nums = input(
        'Выберите последовательность для моделирования, полученный:\n (1) по методу вычетов  \n (3) Выйти в меню моделирования норм распред вел \n (4) Выйти в основное меню Введите номер(число): ')
    if nums == '1':
        otr_s, s_np, s_np_norm, interval_in_posled = open_f(num=1)
        kam = np.sqrt(8/np.pi)
        otr_s_sign = s_np_norm[1000000:1500000]
        otr_s_tal =[]
        for k in range(len(otr_s)):
            if otr_s[k] < 1:
                if otr_s_sign[k] < 0.5:
                    otr_s_tal.append(-(np.round(((1/kam)*np.log((1+otr_s[k])/(1-otr_s[k]))), 2)))
                else:
                    otr_s_tal.append((np.round(((1 / kam) * np.log((1 + otr_s[k]) / (1 - otr_s[k]))), 2)))
        c = dict(Counter(otr_s_tal))
        #exp_func = np.round(np.array([((kam*np.exp(-kam*x))/pow((1+np.exp(-kam*x)), 2)) for x in np.arange(-10,10,0.1)]), 4)
        #exp_func_theor = np.round(np.array([((1/np.sqrt(2*np.pi))*np.exp(-x*x/2)) for x in np.arange(-x_max, x_max, x_delta)]),4)
        #fig, ax = plt.subplots()
        #ax.hist(otr_s_tal, len(c), density=True, color='g')
        #line1 = ax.plot(np.arange(-x_max, x_max, x_delta), exp_func, color='r', label = 'Аппроксим Зелинского')
        #line2 = ax.plot(np.arange(-x_max, x_max, x_delta), exp_func_theor, color='b',linestyle ='--', label = 'Стандартное нормальное распределение')
        #plt.legend()
        #plt.show()
        kam = np.sqrt(8 / np.pi)
        otr_s_sign = s_np_norm[150000:200000]
        otr_s_tal = []
        for k in range(len(otr_s)):
            if (otr_s[k] != 1) and (otr_s[k] != -1):
                if otr_s_sign[k] < 0.5:
                    otr_s_tal.append(-((1 / kam) * np.log((1 + otr_s[k]) / (1 - otr_s[k]))))
                else:
                    otr_s_tal.append(((1 / kam) * np.log((1 + otr_s[k]) / (1 - otr_s[k]))))
        int_count = 1000
        new_posled = otr_s_tal
        delta_interval = abs(min(new_posled) - max(new_posled)) / int_count
        otrezok = np.arange(min(new_posled), max(new_posled), delta_interval)
        otrezok = np.hstack((otrezok, otrezok[-1] + delta_interval))
        interval_slovar = {num: [np.round(otrezok[num], 2), np.round(otrezok[num + 1], 2)] for num in
                           range(len(otrezok) - 1)}
        print(len(interval_slovar))
        kolvo_in_interval = {}
        x = new_posled
        for n in interval_slovar:
            for k in x:
                if interval_slovar[n][0] <= k <= interval_slovar[n][1]:
                    x = np.delete(x, np.argwhere(x == k))
                    if n in kolvo_in_interval:
                        kolvo_in_interval[n] += 1
                    else:
                        kolvo_in_interval.update({n: 1})
        for k in range(int_count):
            if k not in kolvo_in_interval:
                kolvo_in_interval.update({k: 0})
        print(sum(kolvo_in_interval.values()))
        x = new_posled
        end_interval_slovar = {}
        for k in kolvo_in_interval:
            end_interval_slovar.update({tuple(interval_slovar[k]): kolvo_in_interval[k]})
        end_interval_spisok = []
        for k in end_interval_slovar:
            end_interval_spisok.append([k, end_interval_slovar[k]])
        nuts = []
        for k in end_interval_spisok: nuts.append(k[0][0])
        nuts = sorted(nuts)
        end_of_end_interval_spisok = []
        for k in nuts:
            for l in end_interval_spisok:
                if k == l[0][0]: end_of_end_interval_spisok.append(l)
        haski = []
        for k in end_interval_spisok: haski.append(k[1])
        print(sum(haski))
        empty_tuple = []
        ksi = otr_s_tal
        for k in end_of_end_interval_spisok[:]:
            try:
                empty_tuple.append(
                    pow(k[1] - len(ksi) * sum(
                        integrate.quad(lambda x: 1 / np.sqrt(2 * np.pi) * np.exp(-x * x / 2), k[0][0], k[0][1])),
                        2) / len(ksi) / sum(
                        integrate.quad(lambda x: 1 / np.sqrt(2 * np.pi) * np.exp(-x * x / 2), k[0][0], k[0][1])))
            except:
                pass
        from scipy import stats
        alpha = stats.chi2.ppf([0.1, 0.99], int(int_count) - 1)
        print('___________Частотный тест___________')
        print('Хи квадрат равен {}'.format(sum(tuple(empty_tuple))))
        print('Критерий хи-вадрат {} < {} < {}'.format(alpha[0], sum(tuple(empty_tuple)), alpha[1]))
        print('Тест пройден?', (alpha[0] < sum(tuple(empty_tuple)) < alpha[1]))

        print('Корреляционный тест')

        s_otr = otr_s_tal
        i = 0;
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

        print("Интервальный тест")
        s = new_posled
        alpha = float(input('Введите уровень значимости alpha: '))
        n = len(new_posled)
        s_exp = s[:]
        d_exp = abs(np.mean(s_exp))
        print(f'{d_exp} Экспериментальный доверительный интервал')
        d_krit = np.std(s) / np.sqrt(n * alpha)
        print(f'{d_krit} Критический доверительный интервал')
        print(
            'Для данного уровня значимости и подсчитанного теоретически числа испытаний проверим выполняется ли критерий(Чебышев):',
            d_exp < d_krit)

        sigma = 1
        if alpha == 0.1:
            d_krit_2 = sigma * 1.65 / pow(n, 1 / 2)
        elif alpha == 0.05:
            d_krit_2 = sigma * 1.96 / pow(n, 1 / 2)
        elif alpha == 0.01:
            d_krit_2 = sigma * 2.58 / pow(n, 1 / 2)
        print(f'{d_krit_2} Критический доверительный интервал')
        print(
            'Для данного уровня значимости и подсчитанного теоретически числа испытаний проверим выполняется ли критерий(Норм распред):',
            d_exp < d_krit_2)
    elif nums == '2':
        pass
    elif nums == '3':
        from menu import main_menu
        main_menu(x='4')
    elif nums == '4':
        from menu import main_menu
        main_menu()
    else:
        print("Введен некорректный запрос!")
        from menu import opros
        opros()
model_zelin()