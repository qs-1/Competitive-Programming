"""(iii) Write a Dynamic Programming based algorithm that computes the nth Catalan number using the
recursive relation: Cn = Σ(Ci * Cn−1−i) for i = 0 to n−1, with base case C0 = 1"""

def cat(n, dp):
    """
    Correctness:
    used catalan recurrence relation Cn = Σ(Ci * Cn-1-i) for i = 0 to n-1
    Base case given C0 = 1
    For each n we sum products of all pairs Ci and Cn-1-i where i ranges from 0 to n-1
    Memoization is used to avoid repeating work
    
    Optimality:
    Time Complexity is O(n^2) because for each value from 0 to n we find sum of n terms
    Space Complexity is O(n), the dp saves at most n+1 values and stack depth is O(n)
    """
    if n in dp:
        return dp[n]
    
    result = 0
    for i in range(n):
        result += cat(i, dp) * cat(n - 1 - i, dp)
    
    dp[n] = result
    return dp[n]

n = int(input())

dp = {0: 1}

print(cat(n, dp))


# n = int(input())

# dp = [0]*(n+1)
# dp[0] = 1

# for i in range(1,n+1):
    
#     for j in range(i):
#         dp[i] += dp[j] * dp[i - 1 - j]

# print(dp[-1])