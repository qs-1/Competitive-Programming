cases = int(input())
for _ in range(cases):
    n = int(input())%4
    # print(n)
    if n in [1,2,3]:
        print('Alice')
    else:
        print('Bob')
