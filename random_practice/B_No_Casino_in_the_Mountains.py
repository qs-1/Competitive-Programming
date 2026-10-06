import math
cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    days = list(map(int, input().split()))

    presum = [0]
    for d in days:
        presum.append(presum[-1] + d)
    

    hike = 0
    rest = False
    i = 0
    while i<n-k+1:
        if rest == True:
            rest = False
            i+=1
        elif presum[k+i] - presum[i] == 0:
            hike+=1
            rest = True
            i = k+i
        else:
            i+=1

    print(hike)
