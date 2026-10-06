cases = int(input())
for _ in range(cases):
    a,b,c = list(map(int, input().split()))
    
    ans = []
    if (b+c)%2==0:
        ans.append(1)
    else:
        ans.append(0)

    if (a+c)%2==0:
        ans.append(1)
    else:
        ans.append(0)

    if (a+b)%2==0:
        ans.append(1)
    else:
        ans.append(0)
    
    print(*ans)