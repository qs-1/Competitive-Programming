cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    at = arr[k-1]
    arr.sort()
    timebuffer = at #stays same, height increase = time taken

    f = 1
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > timebuffer:
            f = 0
            break
    if f:
        print("yes")
        continue
    print('no')


