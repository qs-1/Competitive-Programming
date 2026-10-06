cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    a=0
    for i in range(1,n-1):
        if arr[i-1] == 0 : continue
        step = arr[i-1]
        arr[i-1] = 0
        arr[i] -= step*2
        arr[i+1] -= step
        if arr[i] < 0 or arr[i+1]<0 : a = 1; break

    print('YES' if all(x==0 for x in arr) else 'NO')