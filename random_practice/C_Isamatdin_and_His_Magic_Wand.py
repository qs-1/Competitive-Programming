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

    # hs = defaultdict(int)
    o = 0
    e = 0
    for n in arr:
        if n&1:
            o += 1
        else:
            e += 1

    if o>0 and e>0:
        arr.sort()

    print(*arr)