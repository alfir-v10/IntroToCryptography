import numpy as np
def run_corr(s_otr, posled):
    print('корреляционный тест')
    s_otr, interval_in_posled = s_otr, posled
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
    print(a_lev, a_prav)
    print(f'Тест пройден?({a_lev}<{R}<{a_prav})', a_lev < R < a_prav)
