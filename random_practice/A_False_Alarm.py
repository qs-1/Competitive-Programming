cases = int(input())
for _ in range(cases):
    n,t = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if arr.count(1)==1:
        print('YES' if t!=0 else 'NO');continue
    else:

        for i in range(n):
            if arr[i] == 1:
                break      
        for j in range(n-1,-1,-1):
            if arr[j] == 1:# bruh
                break 
        print('YES' if t>=j-i+1 else 'NO')
