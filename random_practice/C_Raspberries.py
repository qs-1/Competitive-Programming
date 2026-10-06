cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mindiff = float("inf")
    e = 0
    for i in range(n):
        modi = (arr[i]%k)
        if modi==0:
            mindiff = 0
            if k!=4: break

        mindiff = min(mindiff, abs(k - modi))
        
        if arr[i]&1 != 1: e+=1 

    if k!=4: print(mindiff);continue

    print(min( max(2-e,0), mindiff ))