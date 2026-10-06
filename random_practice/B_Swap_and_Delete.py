cases = int(input())
for _ in range(cases):
    arr = list(map(int, input()))
    ones = arr.count(1)
    zeros = arr.count(0)
    n = ones+zeros
    
    # for t, greedily make opposite prefix of s 
    # since deleting any element will only remove comparison
    # from the suffix part of s
    for i in range(n): 
        if arr[i]==0:
            if ones==0: print(n-i);break
            ones-=1
        elif arr[i]==1:
            if zeros==0: print(n-i);break
            zeros-=1
    else: print(0)