s = input()
if len(s) == 1:
    print(1)
else:
    maxx = 1
    currmax = 1
    prev = s[0]
    for c in s[1:]:
        if c == prev:
            currmax += 1
        else:
            prev = c
            currmax = 1
        maxx = max(currmax,maxx)

    print(maxx)
         