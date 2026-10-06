cases = int(input())
for _ in range(cases):
    n = int(input())
    
    based = [] if n!= 0 else [0]
    while n>0:
        based.append(n%3)
        n = n//3
    x= 0
    cost = 0
    for num in based:
        if x==0:
            cost += (3**(x+1))*num
            x+=1
            continue
        cost += ((3**(x+1)) + (x*(3**(x-1))))*num
        x+=1
    print(cost)