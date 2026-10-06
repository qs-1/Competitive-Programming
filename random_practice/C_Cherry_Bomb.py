cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    fixed = False
    needsum = -1
    impossible = False
    for i in range(n):
        if needsum != -1 and b[i]!=-1 and a[i] + b[i] != needsum:
            impossible = True
            break

        if b[i]!=-1 and needsum==-1:
            fixed = True
            needsum = a[i] + b[i]

    if impossible:
        print(0);continue


    if fixed: # sum is fixed, can only be what they made like 1 and 2 = 3 then other -1s must also make 3 with ai
        currmin = float('inf')
        currmax = -1
        for i in range(n):
            if a[i] < currmin and b[i] == -1:
                currmin = a[i]
            if a[i] > currmax and b[i] == -1:
                currmax = a[i]

        if currmax>needsum:
            print(0);continue        
        need = needsum-currmin
        
        if need>k: 
            print(0)
        else: 
            can = True
            for i in range(n):
                if b[i] != -1 and a[i] + b[i] != needsum:
                    can = False
            print(1 if can else 0)

    else:
        smol,big = min(a),max(a)
        print(k - (big-smol) + 1)

