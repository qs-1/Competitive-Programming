import sys
import math
import heapq
import bisect
import random
from functools import lru_cache
from collections import defaultdict, Counter

# MOD = 10**9 + 7
# @lru_cache(maxsize=None)
input = sys.stdin.readline
# sys.setrecursionlimit(200000)
#hsh = random.randint(1, 1 << 32)

cases = int(input())
for _ in range(cases):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    