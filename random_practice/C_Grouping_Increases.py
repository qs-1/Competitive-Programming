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
    if n==1: print(0);continue

    s1 = float("inf")
    s2 = float("inf")
    c = 0
    for n in arr:
        if s1>s2: s1,s2 = s2,s1

        if n <= s1:
            s1 = n

        elif n<=s2:
            s2 = n
        
        else: # fits in neither (n>both so place it in the smaller top)
            s1 = n
            c+=1
    print(c)