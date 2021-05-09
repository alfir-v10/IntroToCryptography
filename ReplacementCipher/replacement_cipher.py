
file = '2_crypt.txt'
with open(file, 'r', encoding='utf-8') as f:
    words = f.read()
from collections import Counter
count = Counter(words)

freq = {}
for key, value in count.items():
    freq.update({round(value/ sum(count.values()),4): key})
file_freq = 'file_freq.txt'
with open(file_freq, 'w', encoding='utf-8') as f:
    for key in sorted(freq.keys(), reverse=True):
        f.write(str(key)+ ': '+str(freq[key])+'\n')
file_final = '2_crypt_final.txt'

words=words.replace('в', 'о')
words=words.replace('ъ', 'е')
words=words.replace('у', 'и')
words=words.replace('а', 'в')
words=words.replace('ч', 'с')
words=words.replace('д', 'г')
words=words.replace('э', 'р')
words=words.replace('я', 'ш')
words=words.replace('щ', 'я')
words=words.replace('м', 'н')
words=words.replace('у', 'и')
words=words.replace('ю', 'д')
words=words.replace('и', 'а')
words=words.replace('ж', 'п')
words=words.replace('т', 'л')
words=words.replace('т', 'л')

bigrams = Counter([words[i:i+2] for i in range(len(words)) if ' ' not in words[i:i+2]])
print(bigrams)

words=words.replace('ми', 'ни')
words=words.replace('мм', 'нн')
words=words.replace('ме', 'не')
words=words.replace('эя', 'рш')
words=words.replace('ут', 'ал')
trigrams = Counter([words[i:i+3] for i in range(len(words)) if ' ' not in words[i:i+2]])
print(trigrams)
words=words.replace('одо', 'ого')
words=words.replace('шиш', 'или')
with open(file_final, 'w', encoding='utf-8') as f:
    f.writelines(words)

word_list = Counter([k for k in words.split(' ')])
from pprint import pprint
print(word_list)