cases = int(input())
for _ in range(cases):
    n,x = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    lowest = -1
    currlow = -1
    for i in range(1,x+1):
        if i in arr:
            currlow = -1

        else:
            currlow-=1
        lowest = min(lowest,currlow)
        # print(i,lowest)

    for i in range(x-1,0,-1):
        if i in arr:
            currlow = -1

        else:
            currlow-=1
        # print(i,lowest,currlow)
        lowest = min(lowest,currlow)


    print(abs(lowest))