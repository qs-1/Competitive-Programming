import sys
import random
import math
#hsh = random.randint(1,1<<32)
input = sys.stdin.readline
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    a = arr[0]
    b = a#?
    for num in arr:
        if num%b!=0:
            b=num;break 

    val = 1
    for num in arr:
        if not (num%a==0 or num%b==0):
            val = 0
            break

    print('Yes' if val else 'No')