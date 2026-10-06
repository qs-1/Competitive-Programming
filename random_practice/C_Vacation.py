#----------------recursive
import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# memo = [[None]*3 for _ in range(n+1)]
# def recur(i,j):
#     if j!=-1 and memo[i][j] != None:
#         return memo[i][j]

#     if i==n:
#         return 0
    
#     next_cost = -float("inf")
#     for k in range(3):
#         if k==j: continue
#         curr =  arr[i][k] + recur(i+1, k)
#         next_cost = max(next_cost, curr)

#     memo[i][j] = next_cost
#     return next_cost

# ans = recur(0,-1)
# print(ans)

#----------------iterative
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[-float("inf")]*3 for i in range(n)] #max for nth day
dp[0][0] = arr[0][0] 
dp[0][1] = arr[0][1] 
dp[0][2] = arr[0][2] 
for i in range(1,n):
    for j in range(3):
        dp[i][j] = arr[i][j] + max(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
print(max(dp[-1]))
