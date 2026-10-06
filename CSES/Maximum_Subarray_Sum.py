import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n = int(input())
arr = list(map(int, input().split()))

maxi = -float("inf")
temp = 0
for i in range(n):
    temp += arr[i]
    maxi = max(temp, maxi)
    if temp<0:
        temp = 0

print(maxi)