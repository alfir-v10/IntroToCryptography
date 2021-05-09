import numpy as np
from scipy import stats
from collections import Counter
def run_serial(s_otr,posled):
    print('сериальный тест')
    s_otr, interval_in_posled = s_otr,posled
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