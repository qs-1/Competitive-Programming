cases = int(input())
for i in range(cases):
    n = int(input())
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == j+1 or lst[j]==1 or j>=lst[j]:
            print("YES")
            break
    else:
        print("NO")