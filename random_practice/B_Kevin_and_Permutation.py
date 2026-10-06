cases = int(input())
for _ in range(cases):
    n, k = list(map(int, input().split()))
    arr = [None] * n
    arrset = set(x for x in range(1,n+1))
    num = 1
    for i in range(k-1,n,k):
        arr[i] = num
        arrset.remove(num)
        num+=1
    for i in range(n):
        if not arr[i]:
            arr[i] = arrset.pop()
    print(*arr)
