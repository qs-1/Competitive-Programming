import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    arr = list(map(int, input().split()))
    print("yes" if len(set(arr))==1 else "no")    