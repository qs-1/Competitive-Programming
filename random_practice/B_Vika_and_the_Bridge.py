cases = int(input())
for _ in range(cases):
    n,c = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    col_inds = [[] for _ in range(c)] 
    for i in range(n):
        col_inds[arr[i]-1].append(i)

    best = float("inf")

    for indices in col_inds:

        first = second = 0
        prev = -1 # for starting to first occurance
        indices.append(n) # for last occurance to end difference
        
        for x in indices:
            diff = x - prev - 1
            if diff > first:
                second = first
                first = diff 
            elif diff > second:
                second = diff
            prev = x

        best = min(best, max(first//2, second))

    print(best)





# cases = int(input())
# for _ in range(cases):
#     n,k = list(map(int, input().split()))
#     arr = list(map(int, input().split()))

#     hsh = {}
#     for i in range(n):
#         if arr[i] not in hsh:
#             hsh[arr[i]] = []
#         hsh[arr[i]].append(i)

#     ans = float("inf")
#     for _, indices in hsh.items():
#         first = second = -1
        
#         length = len(indices)

#         for i in range(length-1):
#             j = indices[i+1] - indices[i] -1
#             if j > first:
#                 second = first
#                 first = j
#             elif j > second:
#                 second = j
    
#         if indices[0] > first:
#             second = first
#             first = indices[0]
#         elif indices[0]>second:
#             second = indices[0]
                
#         if n-1-indices[-1] > first:
#             second = first
#             first = n-1-indices[-1]
#         elif n-1-indices[-1] > second:
#             second = n-1-indices[-1]

#         ans = min(ans, max(first//2, second))

#     print(ans)