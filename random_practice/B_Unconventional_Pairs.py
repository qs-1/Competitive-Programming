cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    ans = 0

    for i in range(1,n,2):
        ans = max(ans, arr[i]-arr[i-1])

    print(ans)