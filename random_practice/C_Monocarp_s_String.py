import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input().strip()
    target = s.count('a') - s.count('b')
    if target==0: print(0);continue

    pp = {0:-1}
    currsum = 0
    mini = float("inf")
    for i in range(n):
        currsum += 1 if s[i]=='a' else -1
        
        need = currsum - target
        if need in pp: 
            j = pp[need]
            mini = min(mini, i-j)

        pp[currsum] = i

    print(mini if mini<n else -1)