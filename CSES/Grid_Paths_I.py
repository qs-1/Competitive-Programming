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

n = int(input())
grid = []
for i in range(n):
    grid.append([0 if x=='.' else 1 for x in input().strip()])

# for r in grid:
#     print(*r)

dp = [[0]*(n+1) for _ in range(n+1)]

# so starting cell gets 1
dp[0][1] = 1
# dp[0][1] = 0


for i in range(1, n+1):
    for j in range(1, n+1):
        if grid[i-1][j-1] == 1: # is blocked, no path ends here
            dp[i][j] = 0
            continue
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
        
print(dp[n][n])