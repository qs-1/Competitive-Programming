import sys
input = sys.stdin.readline

cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    s = input()
    if k==n: print("-"*n);continue
    l = lp = 0
    r = rp = n-1

    for c in s:
        if c=="0":
            l+=1
            lp+=1
        elif c=="1":
            r-=1
            rp-=1
        elif c=="2":
            lp+=1
            rp-=1

    arr = [""]*n
    for i in range(n):
        if i<l or i>r:
            arr[i] = '-'
        
        elif i<lp or i>rp:
            arr[i] = '?'

        else:
            arr[i] = "+"

    print("".join(arr))