# Practice Task 1: Design reccursive algorithm to find factorial of a number n. Find its
# reccurance relation and solve via iteration/substitution method.

def solve(n):
    if n==1:
        return 1
    return n*solve(n-1)

    # dp = [1]*n
    # for i in range(1,n):
    #     dp[i]*=dp[i-1]*(i+1)
    # return dp[-1]
    
    # dp = [1]*(n+1)
    # for i in range(2,n+1):
    #     dp[i] *= dp[i-1]*i
    # return dp[n]

n = int(input())
print(solve(n))

# T(n) = n 