cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()

    a= s.count('A')
    b= s.count('B')
    c= s.count('C')
    d= s.count('D')
    
    arr = [a,b,c,d]
    for i in range(len(arr)):
        if arr[i]>n:
            arr[i]=n

    print(sum(arr))