import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())

    UP = 1
    DOWN = 0
    dp = [ [ [0]*2 for __ in range(10) ] for _ in range(n)]

    # first can be anything from 10 digits
        #skip
    # second can be from any other 9 
    for d in range(10):
        dp[1][d][UP] = d
        dp[1][d][DOWN] = 9-d # nums bigger than current for it to break down


    for i in range(2,n): # for each position (from 3rd digit)
        for last in range(10): # for each possible previous ending digit
            for trend in range(2): # for each possible prev trend 
                
                # count of previous sequences
                cnt = dp[i-1][last][trend]

                # skip if prev sequences cant be extended with any of the 10 digits (0-9)
                for new_last in range(10):
                    if new_last == last: # adjcant cant be same
                        continue
                    
                    new_trend = UP if new_last>last else DOWN
                    if  new_trend==trend:
                        continue               

                    # valid now, DOWN UP or UP DOWN
                    dp[i][new_last][new_trend] += cnt

    # now sum the number of sequences of length n
    # each of these can have any ending digit
    # and any ending trend, so check and sum all
    ans = 0
    for last in range(10):
        ans += dp[n-1][last][UP]
        ans += dp[n-1][last][DOWN]
    print(ans%997)