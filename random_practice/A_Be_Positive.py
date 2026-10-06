cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))

    z = arr.count(0)    
    m = arr.count(-1)

    print(z + (2 if m&1==1 else 0))