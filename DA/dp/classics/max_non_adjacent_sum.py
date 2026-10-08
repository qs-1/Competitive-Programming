"""(ii) Given an array of integers, design a Dynamic Programming algorithm that finds the maximum sum of
non-adjacent elements in the array."""

def non_adjmax(i, arr, dp):
    """
    Correctness:
    we use recurrence relation where at each index we have two choices
    Take arr[i] and add the max sum from i-2 (skippin adjacent)
    Skip arr[i] and take the max sum from i-1
    Base cases - index 0 returns arr[0], index 1 returns max(arr[0], arr[1])
    Memoization is used to avoid repeating work
    
    Optimality:
    Time Complexity is O(n) because of memoization, each index from 0 to n-1 is computed once
    Space Complexity is O(n), the dp dictionary stores at most n values and stack depth is O(n)
    """
    if i in dp:
        return dp[i]
    dp[i] = max(arr[i] + non_adjmax(i-2, arr, dp), non_adjmax(i-1, arr, dp))
    return dp[i]

n = int(input())
arr = list(map(int, input().split()))

dp = {0: arr[0], 
      1: max(arr[0], arr[1])}

print(non_adjmax(n-1, arr, dp))

# n = int(input())
# arr = list(map(int, input().split()))

# #1d dp
# dp = [0]*(n+1)
# dp[1] = max(0,arr[0]) #incase negatives allowed

# for i in range(2, n+1):
#     dp[i] = max(arr[i-1]+dp[i-2], dp[i-1])
# print(dp[-1])

# # 2d dp
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [[0]*(n+1) for i in range(2)]

# #0 chars, can make 0 sum, by either 'taking' N (if we can even call it that) or skipping it

# for i in range(1,n+1):
#     #0 will have skip case, 1 will have take1
    
#     #0 skip case: a bit difficult to see at first but since we are skipping 
#     #current character, it dosent matter whether we took previous one or not
#     #so best choice could be either, pick the bigger
#     dp[0][i] = max(dp[0][i-1], dp[1][i-1]) 
    
#     #take the current character, since we took, we must skip the prev, so
#     #only one choice left for the previous one, that is skipping it
#     dp[1][i] = arr[i-1] + dp[0][i-1]

# print(max(dp[0][-1],dp[1][-1]))