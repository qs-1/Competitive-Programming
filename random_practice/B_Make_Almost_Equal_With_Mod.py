cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    e = len([x for x in arr if x&1!=1])
    o = n-e
    if e>0 and o>0:
        print(2)
    else:
        cand = 2
        while True:
            diff = set()
            for num in arr:
                diff.add(num%cand)
                if len(diff)>2:
                    break
            if len(diff) == 2: break
            cand *= 2
        print(cand)