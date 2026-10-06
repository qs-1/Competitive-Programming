for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    # all even piles end with bob, which makes alice get stuck
    print('YES' if any(arr.count(x)&1==1 for x in set(arr)) else 'NO')