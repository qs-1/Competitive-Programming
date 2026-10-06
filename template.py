import sys
import math
import heapq
import bisect
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    