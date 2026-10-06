import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    m,a,b,c = list(map(int, input().split()))
    x = y = m
    x -= min(m,a)
    if x!=0: idc = min(x,c); x-=idc; c-=idc
    y -= min(m,b)
    if y!=0: y-=min(y,c)
    print((2*m)-(x+y))


