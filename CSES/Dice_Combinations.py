import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

MOD = 10**9 + 7
target = int(input())

# sys.setrecursionlimit(200000)
# from functools import lru_cache
# @lru_cache(maxsize=None)

# def recur(curr):
#     if curr == 0:
#         return 1

#     count = 0
#     for roll in range(1, min(curr, 6) + 1):
#         count = (count + recur(curr - roll)) % MOD

#     return count

# print(recur(target))


# target: ways
dp = {0:1}

for curr in range(1, target+1):
    dp[curr] = 0
    for roll in range(1, min(curr, 6) + 1):
        dp[curr] = (dp[curr] + dp[curr-roll]) % MOD

print(dp[target])