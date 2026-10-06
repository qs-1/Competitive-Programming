import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    x,y,z = list(map(int, input().split()))
    if (x|z)&(x|y)==x and (x|y)&(y|z)==y and (x|z)&(y|z)==z:
        print('YES');continue
    print("NO")