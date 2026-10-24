import math
import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter
 
n, target = list(map(int, input().split()))
coins = list(map(int, input().split()))
 
# from functools import lru_cache
# sys.setrecursionlimit(200000)
# @lru_cache(maxsize=None)
# def recur(curr):
#     if curr == 0:
#         return 0
    
#     ans = inf
#     for coin in coins:
#         if coin <= curr:
#             ans = min(ans, 1 + recur(curr - coin))
 
#     return ans 
 
# ans = recur(target)
# print(ans if ans != inf else -1)
 
inf = 10**9
dp = [inf] * (target + 1)
dp[0] = 0
 
for coin in coins:
    for curr in range(coin, target+1):
        if 1 + dp[curr - coin] < dp[curr]:
            dp[curr] = 1 + dp[curr - coin]
 
print(dp[target] if dp[target] != inf else -1)