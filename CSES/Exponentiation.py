import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

MOD = 10**9 + 7

cases = int(input())

# def power(a,b):
#     if b==0:
#         return 1
#     if b==1:
#         return a
#     temp = power(a, b//2)

#     temp = (temp * temp)%MOD 

#     if b%2==1:
#         temp = (temp*a)%MOD
    
#     return temp


def power(a,b):
    a%=MOD
    res = 1

    while b>0:
        if b&1: #odd
            res = (res*a)%MOD

        #square base 3^1 -> 3^2 -> 3^4 -> 3^8
        a = (a * a)%MOD

        b//=2

    return res



for _ in range(cases):
    a, b = list(map(int, input().split()))
    print(power(a,b))
