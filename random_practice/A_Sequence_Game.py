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
    x=int(input())
    if x in arr: print("YES");continue


    if x>max(arr) or x<min(arr):
        print('NO')

    else:
        print('YES')    