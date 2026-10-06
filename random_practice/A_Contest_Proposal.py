cases = int(input())
for _ in range(cases):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    idx = 0
    cnt = 0
    ai = 0
    bi = 0
    while ai<n and bi<n:

        if b[bi] < a[ai]:
            # print(b[bi] , a[ai])
            cnt += 1
            bi+=1
        else:
            bi+=1
            ai+=1

    print(cnt)