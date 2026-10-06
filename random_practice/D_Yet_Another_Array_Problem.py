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
    
    primes=100
    p=[1]*(primes+1)
    p[0]=0
    p[1]=0

    for i in range(2, int(primes**0.5) + 1):
        if p[i]:
            for j in range(i*i, primes+1, i):
                p[j]=0 
    pr = []
    for i in range(primes + 1):
        if p[i]:
            pr.append(i)

    v = 0
    for pp in pr:
        for num in arr:
            if num%pp != 0:
                v=1
                break

        if v:
            print(pp)
            break
    if v==0:
        print(-1)

