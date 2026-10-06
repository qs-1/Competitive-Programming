cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())

    prediff = [-float("inf")]*n
    for i in range(1,n):
        # if prev same, already found closest different for that
        # to its left, reuse that
        # if not then thats the closest
        prev = i-1
        if arr[prev] == arr[i]: 
            prediff[i] = prediff[prev]; continue
        prediff[i] = prev
    
    # print(*ndiff)
    for __ in range(q):
        s,r = list(map(int, input().split()))
        s-=1
        r-=1
        if prediff[r] >= s:
            print(prediff[r]+1, r+1); continue
        print(-1,-1)
    print()


# # TLEs but correct:
# # binary search on indices of all nums different 
# # from current to find one that fits in the range
# import bisect
# cases = int(input())
# for _ in range(cases):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     num_indices = {} # holds a number and a list of indices where it appears

#     for i in range(n):
#         if arr[i] not in num_indices:
#             num_indices[arr[i]] = []
#         num_indices[arr[i]].append(i)    

#     q = int(input())
#     for __ in range(q):
#         i,j = list(map(int, input().split()))
#         i-=1
#         j-=1
#         p1 = arr[i]
#         #p2 needs to be different from this and within i j range
#         #do binary seach on all possible numbers (except p1 itself)
#         f=False
#         for num in num_indices:
#             if num != p1: # different, valid for a pair
#                 #find if any index of it is within range
#                 indices = num_indices[num]
#                 match = bisect.bisect_left(indices, i)
#                 if match<len(indices) and indices[match]<=j:
#                     print(i+1, indices[match]+1); f=True; break
#         if not f: print(-1,-1)
#     print()