cases = int(input())
for i in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    one = max(arr)
    two = (sum(arr) - one) / (n-1)
    print(one + two)