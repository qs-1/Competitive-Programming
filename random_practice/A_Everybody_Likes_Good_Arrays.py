cases = int(input())
for _ in range(cases):
    n = int(input())
    lst = list(map(int, input().split()))
    # odd x odd = odd
    # all else even
    l=r=0
    ans = 0
    crrlong = 0
    while r<n:
        if lst[l]%2 == 0:
            r += 1
            currlong = 0
            while r<n and lst[r]%2==0:                
                currlong += 1
                r+=1
            ans += currlong
        else:
            r += 1
            currlong = 0
            while r<n and lst[r]%2==1:                
                currlong += 1
                r+=1
            ans += currlong
        l=r
        # l+=1
        # r+=1

    print(ans)            