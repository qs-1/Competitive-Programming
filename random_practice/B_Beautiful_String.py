import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    s=input().strip()

    z=s.count('0')        
    w=s.count('1')

    if z==n or w==n:
        print(0)        
        print("")  
        continue

    f = s[0]
    ans = []
    for i in range(1,n):
        if s[i]!=f:
            ans.append(i+1)#fuck
    print(len(ans))
    print(*ans)