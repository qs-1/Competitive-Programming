from math import ceil
cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    #longest untouched subsq 1->n
    cnt = 0
    prev=-1
    for num in arr:
        if num==1:
            prev=1
            cnt+=1
        elif num==prev+1:
            prev+=1
            cnt+=1

    print(ceil((n-cnt)/k))#repeatedly sort and move k block to end
