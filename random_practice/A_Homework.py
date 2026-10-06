cases = int(input())
for _ in range(cases):
    alen = int(input())
    a = input()
    blen = int(input())
    b = input()
    c = input()
    
    ans = a
    for i in range(blen):
        if c[i] == "V":
            ans = b[i] + ans
        else:
            ans = ans + b[i]
    print(ans)
