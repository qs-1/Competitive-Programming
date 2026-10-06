cases = int(input())
for _ in range(cases):
    rows,cols = list(map(int, input().split()))
    arr = []
    for i in range(rows):
        arr.append(input())

    tofind = ['v','i','k','a']
    finding = 0

    ans = "NO"
    for i in range(cols):    
        for j in range(rows):
            if arr[j][i] == tofind[finding]:
                # print(arr[j][i], tofind[finding])
                finding+=1
                if finding == 4: 
                    ans = "YES"
                    break
                break
        if ans=='YES': break
    print(ans)

    