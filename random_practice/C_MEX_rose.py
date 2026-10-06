cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    cnts = [0]*(n+1)
    for num in arr:
        cnts[num] += 1
    miss = cnts[:k].count(0)
    print(max(miss, cnts[k]))