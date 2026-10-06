cases = int(input())
for i in range(cases):
    n = int(input())
    g = []
    
    for _ in range(n):
        g.append(list(map(int, input().split())))
    
    ans = [None]*((2*n)-1)

    for j in range(n):
        for k in range(n):
            ans[j+k] = g[j][k]

    for f in range(1,(2*n)+1):
        if f not in ans:
            miss = f
    
    print(miss,*ans)