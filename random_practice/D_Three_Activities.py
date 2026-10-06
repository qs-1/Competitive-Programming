cases = int(input())
for _ in range(cases):
    n = int(input())
    ski = list(map(int, input().split()))
    mov = list(map(int, input().split()))
    bord = list(map(int, input().split()))

    def top3ids(arr):
        a=b=c=-1
        for i in range(len(arr)):
            n = arr[i]
            if a==-1 or n>arr[a]:
                c = b
                b = a
                a = i
            elif b==-1 or n>arr[b]:
                c = b
                b = i
            elif c==-1 or n>arr[c]:
                c = i
        return (a, b, c)

    ski_top = top3ids(ski)
    mov_top = top3ids(mov)
    bord_top = top3ids(bord)

    maxx = 0
    for si in ski_top:
        for mi in mov_top:
            for bi in bord_top:
                if si != mi and mi != bi and si != bi:
                    maxx = max(maxx, ski[si]+mov[mi]+bord[bi])
    print(maxx)