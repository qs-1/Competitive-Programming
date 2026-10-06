cases = int(input())
for _ in range(cases):
    n = int(input())
    if n&1==1:
        print(*[1 for i in range(n)])
        continue
    ans = [2, 3*2]
    for i in range(n-2): ans.append(2*2) 
    print(*ans)