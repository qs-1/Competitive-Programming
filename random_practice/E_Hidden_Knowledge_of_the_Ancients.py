#finding exactly k distinct in subarray using inclusion exclusion principle 
from collections import defaultdict
for _ in range(int(input())):
    def atmk(k):
        f = defaultdict(int)
        ans = i = 0
        for j, x in enumerate(arr): 
            f[(x,)] += 1 #?? idk
            while len(f)>k:
                f[(arr[i],)] -= 1
                if not f[(arr[i],)]: del f[(arr[i],)]
                i += 1
            ans += max(0, min(j-i+1,r) - l + 1)
        return ans
    n,k,l,r = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(atmk(k) - atmk(k-1))

# finding using two pointers/sliding window
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# cases = int(input())
# for _ in range(cases):
#     n,k,l,r = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
    
#     vals=list(sorted(arr))
#     comp={v:i for i,v in enumerate(vals)}
#     arr = [comp[v] for v in arr]
    
#     ans = 0

#     f=[0]*n
#     uniq = 0
#     j=new_j=0
#     for i in range(n):
#         while uniq<k and j<n:
#             if f[arr[j]] == 0:
#                 uniq += 1
#             f[arr[j]] += 1 
#             j+=1
#         if uniq<k: break

#         while new_j<n and (f[arr[new_j]]>0 or new_j<j):
#             new_j += 1
#         start = max(i+l, j)
#         end = min(new_j, i+r)
#         ans += max(0,end-start+1)
#         f[arr[i]]-=1
#         if f[arr[i]]==0:
#             uniq-=1 
#     print(ans)