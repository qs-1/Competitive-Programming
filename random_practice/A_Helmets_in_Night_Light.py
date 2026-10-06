cases = int(input())
for _ in range(cases):
    n,init = list(map(int, input().split()))
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    cp = sorted(list(zip(c,p)), key = lambda x: (x[0],-x[1]))

    #first then smallest 
    ans = init
    n-=1
    
    for cc,pp in cp:
        if cc>init: #directly
            ans += init * n
            break
        diff = max(n - pp, n)
        told = min(pp, n)
        n -= told
        ans += cc * told
        if n==0: break
    print(ans)