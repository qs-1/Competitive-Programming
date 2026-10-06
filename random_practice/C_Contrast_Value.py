cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))

    nodupe = []
    for x in arr:
        if not nodupe or nodupe[-1]!=x: nodupe.append(x)
    arr = nodupe
    n = len(nodupe)
    if n==1:print(1);continue

    i = 1
    ans = n
    while i<n:
        currlen = 1
        while i<n and arr[i-1] < arr[i]:
            i += 1
            currlen += 1
        if currlen>=3:
            ans-=currlen-2

        currlen = 1
        while i<n and arr[i-1] > arr[i]:
            i += 1
            currlen += 1
        if currlen>=3:
            ans-=currlen-2

    print(ans)