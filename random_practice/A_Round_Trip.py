import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    r,x,d,n = list(map(int, input().split()))
    rounds = input().strip()

    cnt=0
    curr = r
    v=0
    for c in rounds:
        if c=='1':
            cnt+=1
            if v==0:
                curr=max(0,curr-d)
                if curr<x: v=1
        else:
            if curr<x: v=1

            if v==1:
                cnt+=1
        
    print(cnt)

