import sys
import math
import heapq
import bisect
import random
from functools import lru_cache
from collections import defaultdict, Counter

MOD = 10**9 + 7
# @lru_cache(maxsize=None)
input = sys.stdin.readline
# sys.setrecursionlimit(200000)
#hsh = random.randint(1, 1 << 32)

n, target = list(map(int, input().split()))
coins = sorted(c for c in map(int, input().split()) if c<=target)
    
dp = [0] * (target + 1)
dp[0] = 1

for coin in coins:
    for curr in range(coin, target + 1):
        dp[curr] = (dp[curr] + dp[curr - coin]) % MOD

print(dp[target])