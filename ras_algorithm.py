import sys

def primFerma(a,n):
    if a**(n-1)%n==1: return True
    else: return False

def gcd(a, b):
    if a == 0 or b == 0: return max(a, b)
    else:
        if a > b: return gcd(a - b, b)
        else: return gcd(a, b - a)
        
def bezout(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)
    
def qwest1(m, c):
    z1 = m; z2 = c
    while m != c:
        if m > c: m = m - c
        else: c = c - m
    if m == 1: return True
    else: return False
    
#ищу простые числа в диапазоне
array = list(range(50,100))
prost = []
for arr in array:
    if primFerma(2,arr): prost.append(arr)
    
#выбрали p,q
p = prost[0]
q = prost[1]

#выбираем длину ключа и число ферма
L = [128,256,512]
print('L',L)

F = [17, 257, 65537]

L2 = L[2]/2 #битовая длина p и q
print('L2', L2)
n = p*q