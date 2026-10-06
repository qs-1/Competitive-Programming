import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    hs = Counter(arr)

    os=[]
    es = per = 0
    esmax = -float("inf")
    for k,v in hs.items():
        if v&1==1: os.append(k)
        
        if v//2 == 0:continue

        es+=(v//2)*2
        per += (v//2)*2*k
        esmax = max(esmax, k)

    a=b=c=-float("inf")
    if es>=3 and esmax<per - esmax:
        a = per


    oo = len(os)
    os.sort(reverse = True)
    if oo>=1:
        for odd in os:
            bper = per + odd
            bm = max(esmax, odd)
            if es+1>=3 and bm < bper - bm:
                a = bper
                break

    if oo>=2:
        for i in range(oo-1):
            diff = os[i]-os[i+1]
            cm = max(esmax,os[i],os[i+1])
            cper = per + os[i] + os[i+1]

            if es+2>=3 and diff < per and cm < cper - cm:
                c = per + os[i] + os[i+1]
                break
            
    ans = max(a,b,c)
    print(0 if ans == -float("inf") else ans)
