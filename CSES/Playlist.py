import sys
import math
import bisect
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n = int(input())
arr = list(map(int, input().split()))    

i = 0
j = 1

maxi = 1
temp = {arr[i]}
cnt = 1
while j<n:
    # make window smaller from left if dupe
    while arr[j] in temp:
        temp.remove(arr[i])
        i += 1
        cnt -= 1

    # no dupe
    temp.add(arr[j])
    cnt += 1
    j+=1
    maxi = max(maxi, cnt)
    
print(maxi)