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
    ans = [0]*n
    
    prev = 1
    ans[0]=1
    for i in range(1,n):
        diff = arr[i]-arr[i-1]
        if diff==i+1:
            prev+=1
            ans[i]=prev
            continue

        if diff<i+1:#same
            ans[i] = ans[i-diff]


    print(*ans)