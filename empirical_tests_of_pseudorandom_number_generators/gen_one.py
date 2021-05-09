import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
def run_get_one():
    def cong_meth(a, x, c, y):
        x = (a * x + c) % y
        return x

    def theor(c, m, a):
        def qwest1(m, c):
            z1 = m; z2 = c
            while m != c:
                if m > c: m = m - c
                else: c = c - m
            if m == 1: return True
            else:
                print('Числа с и m не взаминопростые!')
                return False

        def prost(n):
            if n == 1: return False
            if n == 2: return True
            for x in range(2, n):
                if (n % x == 0): return False
                else: return False

        de = []
        for z in range(1, m + 1):
            if m % z == 0: de.append(z)

        def qwest2(de, a):
            for p in de:
                if prost(p):
                    if ((a - 1) % p) == 0: return True
                    else:
                        print('a-1 не кратно p для любого простого p, являющегося делителем m')
                        return False

        def qwest3(a, m):
            if (m % 4) == 0:
                if ((a - 1) % 4) == 0: return True
                else:
                    print('a-1 не кратно 4, если m кратно 4')
                    return False
            else: return False

        if ((qwest1(m, c) == True) and (qwest2(de, a) == True) and (qwest3(a, m) == True)): return True
        else: return False


    def hello():
        print('Добро пожаловать! Данный софт предоставляет вам генератор псевдослучайных чисел по <методу вычетов>.')
        print('Внимание! По умолчанию стоят следующие параметры a = 1025, c = 221249, m = 16**5, x = 1, k = 2000000.\n' +
              'Пропущенные параметры получат значение по умолчанию.\n' +
              'Введенные параметры должны иметь целочисленные значения. \n' +
              'Данные ограничения, обусловлены ленью писать лишний код на проверку содержимого, введенного с клавиатуры.'
              'При некорректном вводе будут использоваться значения по умолчанию')
        a = input("Введите параметр а(целое) ")
        c = input("Введите параметр с(целое) ")
        m = input("Введите параметр m(целое) ")
        x = input("Введите начальное значение x(целое) ")
        k = input("Введите кол-во генерируемых чисел(целое) ")
        if a == '': a = 'empty'
        if c == '': c = 'empty'
        if m == '': m = 'empty'
        if x == '': x = 'empty'
        if k == '': k = 'empty'
        return a, c, m, x, k

    a, c, m, x, k = hello()

    def proverka(a=1025, c=221249, m=16 ** 5, x=1, k=2000000):
        if (False == (a.isdigit())): a = 1025
        else: a = int(a)
        if (False == (c.isdigit())): c = 221249
        else: c = int(c)
        if (False == (m.isdigit())): m = 16 ** 5
        else: m = int(m)
        if (False == (x.isdigit())): x = 1
        else: x = int(x)
        if (False == (k.isdigit())): k = 2000000
        else: k = int(k)
        print('Вы ввели следующие параметры: ')
        print('\t' + 'a = ' + str(a) + ';\t' + 'c = ' + str(c) + ';\t')
        print('\t' + 'm = ' + str(m) + ';\t' + 'x = ' + str(x) + ';\t')
        print('\t' + 'Длина последовательности k = ' + str(k) + ';\t\n')
        print('c/m = ' + str(np.round((c / m), 3)) + '. Рекомендуется c/m = 0.211')
        print('а = ' + str(a) + ', sqrt(m) = ' + str(np.sqrt(m)) + '. Рекомендуется a = sqrt(m)')
        R1 = (1 / a) * (1 - 6 * c / m + 6 * c * c / m / m) + (a - 6) / m
        print('По теореме 2 коэффициент последовательной корреляция для \n последовательности с максимальным периодом R1 = '
              + str(R1) + '.')
        if theor(int(c), int(m), int(a)) == True: print('Данные параметры соответсвуют теореме 1')
        else: print('Исходя из теоремы 1, данные параметры не рекомендуются к использованию для генерации псевдослучайной последовательности.')

        def podverd(a=1025, c=221249, m=16 ** 5, x=1, k=2000000):
            file = input("Введите полный путь к файлу")
            viv = input('Вас устраивают данные параметры?(Y/N)')
            if viv == 'Y':
                print('Генерируем последовательность')
                print('Подождите... идет запись в файл')
                def gen1(a=a, c=c, m=m, x=x, k=k):
                    for i in np.arange(k):
                        print('Сгенерировано чисел: ', i)
                        x = cong_meth(a=a, x=x, c=c, y=m)
                        f = open(file, 'a')
                        f.write(str(x) + ',')
                        f.close
                start_time = datetime.datetime.now()
                gen1()
                print('Время выполнения программы: ', datetime.datetime.now() - start_time)
                print('Запись последовательности в файл прошло успешно.')
                print('{}'.format(file))
            elif viv == 'N':
                def vss():
                    vis = input('Хотите заного ввести параметры?(Y/N)')
                    if vis == 'Y':
                        a, c, m, x, k = hello()
                        proverka(a=a, c=c, m=m, x=x, k=k)
                    elif vis == 'N': print('Пока')
                    else:
                        print('Введена некорректная команда')
                        vss()
                vss()
            else:
                print('Введена некорректная команда')
                podverd()
        podverd(a=a, c=c, m=m, x=x, k=k)
    proverka(a, c, m, x, k)
