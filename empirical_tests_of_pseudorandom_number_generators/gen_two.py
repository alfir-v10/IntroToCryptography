import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
def run_gen_two():
    def hello():
        print('Добро пожаловать! Данный софт предоставляет вам генератор псевдослучайных чисел по методу основанный на свойствах М-последовательности.')
        print('Внимание! По умолчанию стоит примитивный неприводимый полином 21 степени с периодом 2,097,151.')
        print('Ниже представлены примитивные неприводимые полиномы:')
        print('Степень многочлена \t коэффициенты a0...an \t показатель (периода) T \n' +
              '       5 \t        100101               \t 31 \n' +
              '       7 \t        10000011               \t 127 \n' +
              '       9 \t        1000010001             \t 511 \n' +
              '       10 \t        100000010001        \t 1023 \n' +
              '       17 \t        100000000000001001     \t 131071 \n' +
              '       18 \t        1000000000010000001    \t 262143 \n' +
              '       21 \t        1000000000000000000101 \t 2097151 \n')
        f = input('Введите коэффициенты a0,..an, так чтобы полином содержал только три слагаемых(например, 1011): ')
        number = input('Введите длину генерируемой последовательности(целое число). По умолчанию 3млн.')
        return f, number


    def generator(f='1000000000000000000101', number="3000000"):
        T = 2 ** (len(f) - 1) - 1
        print('Коэффициенты генерируемого полином: ' + str(f))
        print('Теоретический период = ', T)
        input_pol = [int(k) for k in list(f)]  # перевели стринг в инт
        input_pol = np.array(input_pol)  # перевели интв в аррей
        input_pol_a = np.array(input_pol[1:])  # удалили первую единичку, так как она не используется в матрице
        # найдем позиции единичек, чтобы знать что с чем складывать по модулю
        s = []
        for i, k in enumerate(input_pol_a):
            if k == 1:
                s.append(i)
            else:
                pass
        # создаем начальное состояние с 1 единичкой

        # sw = []
        # sq =[]
        print('Введенные вами параметры следующие: \n' + "генерируемый полином: " + str(
            f) + "\n" + "Кол-во генерируемых чисел = " + str(number))
        file = input('Введите полный путь к файлу')
        naw = input('Начать генерацию чисел или выйти из программы?(1 or 0)')


        a = '0' * (len(f) - 1)
        b = '1' + a
        reg = list(b)
        reg = [int(k) for k in reg]


        # собственно сам генератор
        def m_posled(reg):
            M2 = reg[s[0]] ^ reg[s[1]]
            new_reg = np.hstack((M2, reg[:-1]))
            return new_reg, M2


        if naw == "1":
            print('Генерируем последовательность')
            print('Подождите... идет запись в файл')
            start_time = datetime.datetime.now()

            for k in np.arange(int(number)):
                # print('Сгенерировано чисел: ', k)
                reg, M2 = m_posled(reg)
                f = open(file, 'a')
                f.write(str(M2) + ',')
                f.close()
                # sw.append(M2)
                # sq.append(reg)

            print('Время выполнения программы: ', datetime.datetime.now() - start_time)
            print('Запись последовательности в файл прошла успешно.')
            print('Путь к файлу: {}'.format(file))
        elif naw == '0':
            pass
        """        
        i=1
        while i<len(sw):
            if list(sw[i:40+i]) == sw[0:40]:
                print("Подсчитанный программой период = ", i)
                #print(list(sw[i:40+i]),sw[0:40])
                break
            i+=1
            """

    f, number = hello()
    generator(f=f, number=number)
