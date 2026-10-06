cases = int(input())
for _ in range(cases):
    n,m,knum = list(map(int, input().split()))
    x,y = list(map(int, input().split()))

    friends = []
    for n in range(knum):
        friends.append(list(map(int, input().split())))

    vika_parity = (x+y)%2

    for f in friends:
        f_parity = (f[0]+f[1])%2
        if vika_parity==f_parity:
            print('NO')
            break

    else:
        print('YES')