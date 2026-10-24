from math import inf
import sys
import math
import heapq
import bisect
import random
from functools import lru_cache
from collections import defaultdict, Counter

# MOD = 10**9 + 7
input = sys.stdin.readline
sys.setrecursionlimit(200000)
#hsh = random.randint(1, 1 << 32)

n, maxprice = list(map(int, input().split()))
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

# can buy each book atmost once
# cant exceed maxprice
# need to maximize pages

# @lru_cache(maxsize=None)
# def recur(i, currprice):
#     if i==n:
#         return 0

#     skip = recur(i+1, currprice)
#     take = 0
#     if currprice + prices[i] <= maxprice:
#         take = pages[i] + recur(i+1, currprice + prices[i])
    
#     return max(skip, take)

# print(recur(0, 0))


# # dp[first i books][max budget] = best pages
# dp = [[0] * (maxprice + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for budget in range(maxprice + 1):
#         skip = dp[i - 1][budget]

#         take = 0
#         if prices[i-1] <= budget:
#             take = pages[i-1] + dp[i - 1][budget - prices[i-1]]
        
#         dp[i][budget] = max(skip, take)

# print(dp[n][maxprice])


dp = [0] * (maxprice + 1)
for i in range(n):
    p = prices[i]
    g = pages[i]
    for budget in range(maxprice, p - 1, -1): # reverse order to not reuse book, values to left this way are still old and dont include current book
        dp[budget] = max(dp[budget], g + dp[budget - p])
print(dp[maxprice])