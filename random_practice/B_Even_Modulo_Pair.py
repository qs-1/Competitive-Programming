import sys

input = sys.stdin.readline

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    a,b=-1,-1
    o=[]
    e=[]
    for num in arr:
        if num&1: o.append(num);continue
        e.append(num)

    if len(e)>1:
        print(e[0],e[1]);continue
    
    lo = len(o)
    for i in range(lo):
        for j in range(i+1,lo): #oddodd
            if (o[j] // o[i])&1:
                a,b=o[i],o[j]
                break
        if a!=-1: break

    if a!=-1: print(a,b);continue

    for i in range(lo):
        for j in range(len(e)):
            if e[j]<o[i]:continue

            if (e[j]//o[i])%2==0:
                a,b=o[i],e[j]
                break

        if a!=-1: break

    if a!=-1:
        print(a,b)
    else:
        print(-1)        