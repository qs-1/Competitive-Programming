cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))

    f = p =  0
    psum = [0]
    for i in range(n):
        arr[i]*= -1 if i&1==1 else 1
        p += arr[i]
        psum.append(p)

    psum.sort()
    for j in range(n):
        if psum[j]==psum[j+1]:
            f = 1; break
    print('YES' if f==1 else 'NO')
