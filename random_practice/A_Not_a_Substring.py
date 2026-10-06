cases = int(input())
for _ in range(cases):
    s = input()
    if s == "()":
        print('NO')
    else:
        print('YES')
        if "((" in s or "))"in s:
            ans = "()"*len(s)
            print(ans)
        else:
            ans = "("*len(s)
            ans += ")"*len(s)
            print(ans)