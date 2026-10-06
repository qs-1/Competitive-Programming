cases = int(input())
for _ in range(cases):
    m = int(input())
    arr = sorted(list(map(int, input().split())))
    nth = 0
    for i in range(m-1,0,-1):
        print(arr[nth],end = ' '); nth+=i 
    print(10**9)