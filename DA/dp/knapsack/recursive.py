n, wn = list(map(int, input().split()))
items = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    items.append((x, y))


memo = {}
def knap(i,j):
    key = (i,j)

    if i==0 or j==0:
        memo[key]=0
        return 0
    
    if key in memo:
        return memo[key]

    best = -1
    if items[i-1][0] > j:
        best = knap(i-1,j)
        print(f"Exclusion of object {i} gives value: {memo[(i-1,j)]}")
    else:
        skip = knap(i-1,j)
        take = items[i-1][1] + knap(i-1,j-items[i-1][0])
        if skip>take:
            best = skip
            print(f"Exclusion of object {i} gives value: {memo[(i-1,j)]}")
        else:
            best = take
            print(f"Inclusion of object {i} gives value: {best}")

    memo[key] = best
    return best


ans = knap(n,wn)
print(ans)