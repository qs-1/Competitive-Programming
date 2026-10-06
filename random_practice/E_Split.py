import sys
input = sys.stdin.readline

cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    f = 0
    hashi = [0]*(n+1)
    for num in arr:
        hashi[num] += 1
    for i in range(n+1):
        if hashi[i]%k != 0: f=1;break
        hashi[i] //= k
    if f: print(0);continue

    curr = [0]*(n+1)
    ans = 0
    i = 0
    for j in range(n):
        curr[arr[j]] += 1
        while curr[arr[j]] > hashi[arr[j]]:
            curr[arr[i]] -= 1
            i+=1
        ans += j-i+1
    print(ans)