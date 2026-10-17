import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

MOD = 10**9 + 7

def modfacto(x):
    res = 1
    for i in range(2, x+1):
        res = (res * i)%MOD
    return res
    

def power(a,b):
    a%=MOD
    res = 1

    while b>0:
        if b&1: #odd
            res = (res*a)%MOD

        a = (a * a)%MOD

        b//=2

    return res


n, m = list(map(int, input().split()))

total = modfacto(n-1+m)%MOD

a = modfacto(n-1)%MOD
b = modfacto(m)%MOD

repeated = (a*b)%MOD
repeatedinv = power(repeated, MOD-2)

print((total*repeatedinv)%MOD)