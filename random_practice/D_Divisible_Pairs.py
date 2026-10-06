cases = int(input())
for _ in range(cases):
    n,x,y = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    ans = 0
    seen = {}
    for n in arr:
        rem1 = n%x
        cond1 = (x - rem1) % x

        cond2 = n%y

        if (cond1, cond2) in seen:
            ans += seen[(cond1, cond2)]

        if (rem1, cond2) not in seen: #add remainders for this number to map incase its a match for another aj
            seen[(rem1, cond2)] = 1
        else: seen[(rem1, cond2)] += 1
    
    print(ans)