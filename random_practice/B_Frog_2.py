n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

dp=[None for i in range(n)]
dp[0] = 0
dp[1] = abs(arr[0] - arr[1])

for i in range(2,n):
    dp[i] = abs(arr[i] - arr[i-1]) + dp[i-1]

    if k<=1: continue

    #min cost from i-k to i-1 for getting to i
    for j in range(max(0,i-k), i):
        dp[i] = min(dp[i],
                    abs(arr[i] - arr[j]) + dp[j])
        
print(dp[-1])