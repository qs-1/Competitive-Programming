cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if arr[0] != n:
        print("NO")
        continue
    
    rev = arr[::-1]
    ai = 0
    i = 0 
    j = n-1
    while ai < n:
        while i<j and rev[i] < ai+1:
            if rev[i] >= ai+1:
                break
            i+=1
        if not (rev[i] >= ai): break

        if j - i + 1 == arr[ai]:
            ai += 1
        else: break #false
    
    if ai == n: print('YES')
    else: print("NO")