# for _ in range(int(input())):
#     a,b = list(map(int, input().split()))
#     if (2*a - b)%3 == 0 and (2*b - a)%3 == 0 and 2*a >= b and 2*b >= a:
#         print('YES')
#     else:
#         print('NO')

for _ in range(int(input())):
    a,b = list(map(int, input().split()))
    if (a + b)%3 == 0  and  2*min(a,b) >= max(a,b):
        print('YES')
    else:
        print('NO')

