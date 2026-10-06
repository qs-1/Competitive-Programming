cases = int(input())
for _ in range(cases):
    n = int(input())
    
    x = 0
    i = 1
    while abs(x)<n:
        diff = 2*(i)-1
        if i%2==1:
            diff=-abs(diff)
        else:
            diff=abs(diff)
        x += diff
        i+=1

    if i%2==1:
        print("Sakurako")
    else:
        print("Kosuke")