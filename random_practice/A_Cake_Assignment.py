import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    k,x = list(map(int, input().split()))
    choc=vani=2**k

    if x==choc:
        print(0)
        print("")
        continue

    c=0
    revans = []
    fina=x
    finb= 2**(k+1) - x #check excel sheet note
    while fina != 2**k:
        if finb>fina:
            finb-=fina
            fina*=2
            revans.append(1)
        else:
            fina-=finb
            finb*=2
            revans.append(2)
        c+=1
    print(c)
    print(*revans[::-1])