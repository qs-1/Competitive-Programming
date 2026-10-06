from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr).values()
    print("Yes" if len(cnt)<=2 and abs(max(cnt) - min(cnt))<=1 else "No")