n, wn = list(map(int, input().split()))
items = []  # List of tuples
for _ in range(n):
    x, y = list(map(int, input().split()))
    items.append((x, y))  # (weight, value)

dp = [[0]*(wn+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, wn+1):
        print(f"First {i} objects, Weight limit {j}")
        
        w,v = items[i-1]

        if w > j: #must skip
            dp[i][j] = dp[i-1][j]
            print(f"Exclusion object {i} gives value: {dp[i-1][j]}")
            print()
            continue

        #take best of take/skip
        skip = dp[i-1][j]
        take = v + dp[i-1][j-w]
        if skip>take:
            best = skip
            print(f"Exclusion object {i} gives value: {best}")
        else:
            best = take
            print(f"Inclusion of object {i} gives value: {best}")
        dp[i][j] = best

        print()
        
print(dp[-1][-1])