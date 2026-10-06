import math

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    if n ==1:
        print(1)
        continue


    gg = arr[0]
    for n in arr:
        gg = math.gcd(n,gg)

    print(arr[-1]//gg)