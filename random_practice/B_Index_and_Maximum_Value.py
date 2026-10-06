cases = int(input())
for _ in range(cases):
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    p = 0
    maxx = max(arr)
    for __ in range(q):
        inp = list(input().split())
        if maxx >= int(inp[1]) and maxx <= int(inp[2]):
            maxx += -1 if inp[0]=='-' else 1
        print(maxx,end = ' ')
    print()