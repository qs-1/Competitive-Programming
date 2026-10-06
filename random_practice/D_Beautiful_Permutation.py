import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

def gsum(pq,l,r):
    print(pq,l,r,flush=True)
    return int(input())

cases = int(input())
for _ in range(cases):
    n = int(input())
    
    i=1
    j = n
    end = 0

    while i<=j:
        m=(i+j)//2
        if gsum(2,m,n)-gsum(1,m,n) > 0:
            i=m+1
            end=m
        else:
            j=m-1

    added = gsum(2,1,n)-gsum(1,1,n)
    start = end - added+1

    print("!", start,end,flush=True)