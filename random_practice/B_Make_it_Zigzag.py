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
    if n==1:
        print(0)
        continue

    pmax = -float("inf")
    for i in range(n):
        pmax = max(pmax,arr[i])
        if (i+1)&1!=1:
            arr[i] = pmax

    ans=0
    for i in range(n):
        if (i+1)&1==0: continue

        if i>0 and i<n-2:
            ans += max(0, arr[i] - min(arr[i-1], arr[i+1]) + 1)
        elif i==0:
            ans += max(0, arr[i] - arr[i+1] + 1)
        else:
            ans += max(0, arr[i] - arr[i-1] + 1)

    print(ans)
        

