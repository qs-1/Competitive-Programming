cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    s = input()

    if len(s) == 1:
        print("YES")
        continue

    hashi = {}
    for c in s:
        if c not in hashi:
            hashi[c] = 0
        hashi[c] += 1

    odds = 0
    for key, val in hashi.items():
        if val&1 != 0:
            odds += 1

    print('YES' if k>=(odds-1) else 'NO')

        