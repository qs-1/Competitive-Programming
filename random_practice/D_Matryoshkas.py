import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list((map(int, input().split()))))
    hs = Counter(arr)

    ans = 0
    prec = -1
    prek = 0
    for k,c in hs.items():#
        if prec==-1:
            ans += c
        
        elif k!=prek+1:
            ans+=c

        elif c>prec:
            ans+=c-prec
        prek = k
        prec = c
        
    print(ans)