
cases = int(input())
for i in range(cases):
    n = int(input())
    lst = list(map(int, input().split()))

    maxx = -1
    for j in range(1,n):
        maxx = max(maxx, lst[j-1]*lst[j])

    print(maxx)