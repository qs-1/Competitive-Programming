import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = input().strip()
    if arr.count("1") == 0:
        print(0)
        continue

    prev=None
    ans = 0
    for i in range(n):
        if arr[i]=="1":
            if prev==None:
                ans+=1
            elif prev<=i-k:
                ans+=1
            prev = i
    print(ans)