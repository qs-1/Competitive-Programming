import heapq

n, wn = list(map(int, input().split()))
pq = []

for k in range(n):
    w, v = list(map(int, input().split()))
    heapq.heappush(pq, (-v, w, k+1))

dp = [[0]*(wn+1) for i in range(n+1)]

for i in range(1, n+1):
    nv, w, _ = heapq.heappop(pq)
    v = -nv

    for j in range(1, wn+1):
        print(f"First {i} objects, Weight limit {j}")
        
        if w > j:
            dp[i][j] = dp[i-1][j]
            print(f"Exclusion of object {i} gives value: {dp[i-1][j]}")
            print()
            continue

        skip = dp[i-1][j]
        take = v + dp[i-1][j-w]
        
        if skip > take:
            best = skip
            print(f"Exclusion of object {i} gives value: {best}")
        else:
            best = take
            print(f"Inclusion of object {i} gives value: {best}")
        
        dp[i][j] = best
        print()

print(dp[n][wn])