cases = int(input())
for _ in range(cases):
    r = int(input())
    arr = []
    for __ in range(r):
        arr.append(list(input()))
    t=0
    for i in range(r):
        a = arr[i].count('1') 
        if a==1: t=1; break
        b = arr[r-i-1].count('1')
        if b==1: t=1; break
    print('SQUARE' if t==0 else "TRIANGLE")