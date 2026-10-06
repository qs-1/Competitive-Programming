import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    w = n
    l = 0
    #winners before final, losers nbefore final + final
    print((n-1)+(n-2)+1)

    #bruh.
    # mt = 0
    # while w>1 or l>1:
    #     mt += (w//2)
    #     mt += (l//2)
        
    #     t = 0
    #     if w&1==1: w-=1; t+=1
    #     lo = (w//2)
    #     w = lo + t

    #     #out
    #     t2 = 0
    #     if l&1==1: l-=1; t2+=1
    #     l = (l//2) + t2
        
    #     l += lo

    # print(mt+1)
    