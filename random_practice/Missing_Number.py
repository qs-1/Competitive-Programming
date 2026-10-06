n = int(input())
arr = set(map(int, input().split()))
for n in range(1, n+1):
    if n not in arr:
        print(n)