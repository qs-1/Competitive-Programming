import sys
import math
import bisect
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
    
if n<3:
    print("IMPOSSIBLE")
    exit(0)

arr = sorted([(arr[i], i) for i in range(n)])

found = False
for k in range(n):
    remtarget = target - arr[k][0]
    
    # now just 2 sum to get remtarget
    left = k+1 # skip dupes
    right = n-1

    while left < right:
        curr = arr[left][0] + arr[right][0]

        if curr == remtarget:
            found = True
            break
        elif curr < remtarget:
            left+=1
        else:
            right-=1

    if found:
        print(arr[k][1]+1, arr[left][1]+1, arr[right][1]+1)
        break

if not found:
    print("IMPOSSIBLE")
