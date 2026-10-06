cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    maxx = -1
    for c in s:
        maxx = max(maxx, ord(c))
    
    print(maxx-96)