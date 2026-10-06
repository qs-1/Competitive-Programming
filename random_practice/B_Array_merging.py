from collections import defaultdict
def run(n,lst):
    long = defaultdict(int)
    curr = 1
    for i in range(n-1):
        if lst[i] == lst[i+1]:
            curr += 1
        else:
            long[lst[i]] = max(long[lst[i]], curr)
            curr = 1
    #last conseq
    long[lst[-1]] = max(long[lst[-1]], curr)
    return long

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    if n == 1:
        print(2 if arr[0] == brr[0] else 1)
        continue

    longa = run(n, arr)
    longb = run(n, brr)
    u = set(arr+brr)
    ans = -float("inf")
    for num in u:
        a = longa[num] if num in longa else 0
        b = longb[num] if num in longb else 0
        ans = max(ans, longa.get(num,0) + longb.get(num,0))

    print(ans)