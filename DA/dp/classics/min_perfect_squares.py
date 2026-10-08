"""(iv) Write a Dynamic Programming based algorithm that takes a number n and finds the minimum
 number of perfect squares (1, 4, 9, 16, …) that sum up to n"""

def min_sqr(n, dp):
    """
    Correctness:
    used recurrence relation, for each number n, try all perfect squares k^2 <= n
    For each square k^2, find 1 + min_sqr(n - k^2)
    thwn take min across all choices
    Base case is dp[0] = 0 (no sqr to make 0)
    Memoization is used to avoid repeating work
    
    Optimality:
    Time Complexity is O(n * sqrt(n)) because for each value from 1 to n we try sqrt(n) perfect squares
    Space Complexity is O(n), the dp dictionary stores at most n+1 values and stack depth is O(n)
    """
    if n in dp:
        return dp[n]
    
    ans = float("inf")
    k = 1
    while k*k <= n:
        ans = min(ans, 1 + min_sqr(n - (k*k), dp))
        k += 1
    
    dp[n] = ans
    return dp[n]

n = int(input())

dp = {0: 0}

print(min_sqr(n, dp))


# n = int(input())

# #need to make exactly n
# #check from 0 to n if we can make exactly ith usin squares

# dp = [float("inf")]*(n+1)
# dp[0] = 0

# for i in range(1,n+1):
#     k = 1
#     while k*k <= i:
#         dp[i] = min(dp[i], 1 + dp[i - (k*k)]) # 1 for taking k, and min coins to make the rest
#         k+=1

# print(dp[-1])