def same(arr):
    n = arr[0]
    for num in arr[1:]:
        if num!=n:
            return False
    return True

cases = int(input())
for _ in range(cases):
    lst = list(map(int, input().split()))
    a,b,c = lst
    target = min(lst)


    m = 1
    while not same(lst) and m<4:
        l = max(lst)
        split = [target, l-target]
        lst.remove(l)
        lst.extend(split)
        m+=1
    
    if same(lst):
        print("YES")
    else:
        print("NO")