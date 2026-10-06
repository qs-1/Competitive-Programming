cases = int(input())
for _ in range(cases):
    n = int(input())
    arrset = set(list(map(int, input().split())))
    u = len(arrset)
    
    if n==1: print(1) #delete the only one
    elif u==2: print(n//2 + 1) #alternating pattern under given conditions, will always be even 1212, if odd 121 then first and last removed immediately
    else: print(n) #delete from either side one by one
