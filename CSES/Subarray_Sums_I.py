import sys
import math
import bisect
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

sofar = 0
cnt = 0
i = 0
for j in range(n):
    sofar += arr[j]

    while i<j:
        if sofar>target:
            sofar -= arr[i]
            i+=1
        else: break

    if sofar == target:
        cnt += 1

print(cnt)