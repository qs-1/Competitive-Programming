def mini(n,s,x):
    k = s.count(x)
    if k == 0 or k == n:
        return 0
    
    y = 'a' if x=='b' else 'b'

    pre = [0]
    As_before = 0
    for i in range(n):
        pre.append(pre[-1] + (As_before if s[i] == y else 0))
        As_before += 1 if s[i] == x else 0

    suf = [0]
    As_after = 0
    for i in range(n-1,-1,-1):
        suf.append(suf[-1] + (As_after if s[i] == y else 0))
        As_after += 1 if s[i] == x else 0
    suf = suf[::-1]

    ans = float("inf")
    for i in range(n+1):
        ans = min(ans, pre[i] + suf[i])
    return ans

cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    print(min(mini(n,s,'a'),mini(n,s,'b')))