from math import lcm
cases = int(input())
for _ in range(cases):
    n,x,y = list(map(int, input().split()))

    xo = n//x - (n//lcm(x,y))
    yo = n//y - (n//lcm(x,y))
    
    big=((n*(n+1))//2) - (((n-xo)*(n-xo+1))//2)
    smol=(yo*(yo+1))//2
    
    print(big-smol)