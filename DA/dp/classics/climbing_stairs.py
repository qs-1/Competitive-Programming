"""(v) You are given n stairs. You can climb either 1, 2, or 3 steps at a time. 
Design a Dynamic Programming algorithm to find the total number of distinct ways to reach the top."""

def climb(n, dp):
    """
    Correctness:
    at each stair n, we can reach it from n-1, n-2, or n-3
    Total ways to reach n is given by ways to reach n-1 + ways to reach n-2 + ways to reach n-3
    Base cases are dp[0] = 1, dp[1] = 1, dp[2] = 2
    Memoization is used to avoid repeating work
    
    Optimality:
    Time Complexity is O(n) because of memoization, each value from 0 to n is computed once
    Space Complexity is O(n), the dp dictionary stores at most n+1 values and stack depth is O(n)
    """
    if n in dp:
        return dp[n]
    
    dp[n] = climb(n-1, dp) + climb(n-2, dp) + climb(n-3, dp)
    return dp[n]

n = int(input())

dp = {0: 1, 
      1: 1, 
      2: 2}

print(climb(n, dp))


# n = int(input())

# dp = [0]*(n+1)

# #starting from 0, taking 1,2 or 3 step
# dp[0] = 1
# dp[1] = 1
# dp[2] = 2 # 2 1steps or 1 2step

# for i in range(3,n+1):
#     dp[i] += dp[i-1] 
#     dp[i] += dp[i-2] 
#     dp[i] += dp[i-3] 

# print(dp[-1])