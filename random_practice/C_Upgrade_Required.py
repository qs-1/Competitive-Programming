n,q = list(map(int, input().split()))
arr = [0] + [1]*n
prev = 1
for i in range(q):
    curr, targ = list(map(int, input().split()))
    up = 0

    while prev<=curr:
        up += arr[prev]
        arr[targ] += arr[prev]
        prev += 1

    print(up)


# from collections import Counter

# n,q = list(map(int, input().split()))
# hs = Counter(range(1,n+1))

# prev = 0
# for i in range(q):
#     curr, targ = list(map(int, input().split()))
#     up = 0
#     for j in range(prev+1, curr+1):
#         if j in hs:
#             up+=hs.pop(j)
                
#     hs[targ] += up if up>0 else 0
#     print(up)
#     if curr>prev: prev = curr