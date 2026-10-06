cases = int(input())
for _ in range(cases):
    arr = list(map(int, input()))
    n = len(arr)
    if n<=2:print(0);continue

    suf = [0]
    for i in range(n-1,-1,-1):
        suf.append(suf[-1] + (1 if arr[i]==1 else 0))
    suf=suf[1:][::-1]

    pre = [0]
    for i in range(n):
        pre.append(pre[-1] + (1 if arr[i]==1 else 0))
    pre = pre[1:]

    c1 = n - arr.count(1)
    c2 = n - arr.count(0)
    ans = min(c1,c2)

    for k in range(0, n + 1):
        pre1s = pre[k-1] if k>0 else 0
        pre0s = k - pre1s
        
        suf1 = suf[k] if k<n else 0
        suf0 = (n-k) -suf1

        c3 = pre1s + suf0
        c4 = pre0s + suf1

        ans = min(ans, c3, c4)

    print(ans)
    