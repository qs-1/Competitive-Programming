import sys
input = sys.stdin.readline
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())

    l = n*n - k # cells - escape cells = stuck cells

    #if one stuck cell, not possible
    if l==1: print("NO");continue

    print('YES')
    for i in range(n):
        row = []
        for j in range(n):
            if l<=0: # placed all loops, now escape by just going down
                row.append('D')
            else:
                if i==0 and j==0:
                    row.append('R')
                elif i==0:
                    row.append('L')
                #now going up causes loop
                else:
                    row.append('U')
                l-=1
        print("".join(row))
