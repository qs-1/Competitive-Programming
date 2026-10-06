import sys
import math
import bisect
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n, queries = list(map(int, input().split()))
arr = list(map(int, input().split()))

presum = [0] * (n + 1)
for i in range(n):
    presum[i+1] = presum[i] + arr[i]

for _ in range(queries):
    i, j = list(map(int, input().split()))
    print(presum[j] - presum[i-1])

    
    