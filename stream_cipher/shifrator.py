from generator_m_posled_method import run_gen_two
from open_file import open_f
from corr_test import run_corr
from serial_test import run_serial
import numpy as np
#run_gen_two()

text = 'Поточный шифр – это шифр, в котором каждый символ открытого текста' \
       ' шифруется независимо от других символов с помощью потока ключей, ' \
       'который называется ключевой последовательностью ' \
       '(а также гамма-последовательностью, или просто гаммой). ' \
       'Ключевая последовательность произвольной длины получается из короткого ключа ' \
       'фиксированной длины с помощью некоторого алгоритма.'
text_bin = [bin(ord(ch))[2:].zfill(14) for ch in text]
#print(text_bin)
print(sum([len(k) for k in text_bin]))
text_bin_np = []
for k in text_bin:
    for t in k:
        text_bin_np.append(int(t))
text_bin_np = np.array(text_bin_np)
#print(text_bin_np)
run_corr(s_otr = text_bin_np, posled = [0, len(text_bin_np)])
run_serial(s_otr = text_bin_np, posled = [0, len(text_bin_np)])
s_otr, posled = open_f(file_name= 'gen_262143')
#print(s_otr)
run_corr(s_otr,posled)
run_serial(s_otr,posled)
#print(s_otr,  len(s_otr))

s_otr_14 = []
i = 0
while i < len(s_otr):
    s = s_otr[0 + i:i + 14]
    st=''
    for k in s:
        st += str(k)
    s_otr_14.append(st)
    i+=14

#print(len(s_otr_14))
text_bin_np = np.array([int(k,2) for k in np.array(text_bin)])
s_otr_14_np = np.array([int(k,2) for k in np.array(s_otr_14)])

xor = text_bin_np ^ s_otr_14_np
xor_bin = [bin(ch)[2:].zfill(14) for ch in xor]
#print(xor_bin)

xor_bin_np = np.array([int(k,2) for k in np.array(xor_bin)])
desh = xor_bin_np^s_otr_14_np
desh = [chr(ch) for ch in desh]
#print(desh)
shifr_text = ''
for k in xor_bin:
    shifr_text+=k
#print(shifr_text)
shifr_text = [int(k) for k in shifr_text]
run_corr(s_otr = shifr_text,posled = posled)
run_serial(s_otr = shifr_text,posled = posled)