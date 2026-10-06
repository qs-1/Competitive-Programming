cases = int(input())
for _ in range(cases):
    n, k = list(map(int, input().split()))
    if k==n:
        for i in range(n):
            print(1,end=' ')
    elif k==1:
        for i in range(1,n+1):
            print(i,end=' ')
    else:
        print(-1)
    print()