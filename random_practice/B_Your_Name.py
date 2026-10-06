import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    s,t = input().split()
    
    hs = Counter(s)
    v = 1
    for c in t:
        if c not in hs:
            v = 0
            break
        elif hs[c] == 0:
            v = 0
            break
        else:
            hs[c] -= 1

    print('YES' if v==1 else "NO")