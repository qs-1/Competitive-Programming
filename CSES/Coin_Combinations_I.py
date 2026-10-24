import sys
import math
import random
MOD = 10**9 + 7
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

def main():
    n, target = map(int, input().split())
    coins = sorted(c for c in map(int, input().split()) if c <= target)
    if not coins:
        print(0)
        return

    dp = [0] * (target + 1)
    dp[0] = 1
    big = coins[-1]

    for curr in range(1, big):
        temp = 0
        for c in coins:
            if c > curr:
                break
            temp += dp[curr - c]
        dp[curr] = temp % MOD

    # skip c > curr comparison now that curr is atleast >= largest coin 
    for curr in range(big, target + 1):
        temp = 0
        for c in coins:
            temp += dp[curr - c]
        dp[curr] = temp % MOD

    print(dp[target])

main()




# import sys
# import math
# import heapq
# import bisect
# import random
# from functools import lru_cache
# from collections import defaultdict, Counter
 
# MOD = 10**9 + 7
# # @lru_cache(maxsize=None)
# input = sys.stdin.readline
# # sys.setrecursionlimit(200000)
# #hsh = random.randint(1, 1 << 32)
 
# def main():
#     n, target = list(map(int, input().split()))
#     coins = sorted([c for c in map(int, input().split()) if c <= target])
 
#     dp = [0] * (target + 1)
#     dp[0] = 1
 
#     for curr in range(1, target + 1):
#         temp = 0
#         for coin in coins:
#             if coin > curr:
#                 break
#             temp += dp[curr - coin]
#         while temp >= MOD:
#             temp -= MOD
#         dp[curr] = temp
 
#     print(dp[target])
 
# if __name__ == "__main__":
#     main()