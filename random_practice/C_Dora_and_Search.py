import sys
input = sys.stdin.readline
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    mini = 1
    maxi = n
    i = f = 0
    j = n-1
    while j-i+1 > 2:
        if arr[j] == maxi: maxi-=1; j-=1
        elif arr[j] == mini: mini+=1; j-=1
        elif arr[i] == maxi: maxi-=1; i+=1
        elif arr[i] == mini: mini+=1; i+=1
        else: print(i+1, j+1); f=1; break
    if f == 0: print(-1)