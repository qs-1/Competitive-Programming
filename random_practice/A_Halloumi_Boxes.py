cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    

    if k==1 and arr != sorted(arr):
        print("NO")
    else:
        print("YES")
        