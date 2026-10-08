"""(i) An algorithm that takes n number and finds its Tribonacci Value. The Tribonacci sequence is defined as
follows: 0, 1, 1, 2, 4, 7, 13, … where each number is the sum of the previous three numbers in the
sequence."""


def tribonacci(n, dp):
    """
    Correctness: 
    The function uses the tribonacci recurrence relation with base cases T(0) = 0, T(1) = 1, T(2) = 1 and recursive case T(n) = T(n-1) + T(n-2) + T(n-3)
    we use memo map dp to store found values to avoid repeated calculations
    
    Optimality: 
    Time Complexity is O(n) because of memoization, each value from 0 to n is found once. 
    Space Complexity is O(n), the dp dictionary stores n+1 values and stack depth due to recursion is also O(n).
    """
    if n in dp:
        return dp[n]
    dp[n] = tribonacci(n-1, dp) + tribonacci(n-2, dp) + tribonacci(n-3, dp)
    return dp[n]

n = int(input())

dp = {0: 0, 
     1: 1,
     2: 1}

print(tribonacci(n, dp))


# n = int(input())

# dp = [0]*(n+1)
# dp[1] = 1
# dp[2] = 1

# for i in range(2,n+1):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# print(dp[-1])
