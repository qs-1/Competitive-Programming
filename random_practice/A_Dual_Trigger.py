cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input().strip()

    ones = s.count('1')

    if ones % 2 == 1:
        print("NO")
        continue
    if ones == 0:
        print("YES")
        continue

    if ones == 2:
        if "11" in s:
            print("NO")
        else:
            print("YES")
        continue
    print("YES")