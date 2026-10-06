import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n, m, maxdiff = list(map(int, input().split()))
desired = sorted(list(map(int, input().split())))
sizes = sorted(list(map(int, input().split())))
# print(desired)
# print(sizes)

ans = 0
j = 0
for guy in desired:
    
    while j<m:
        diff = sizes[j]-guy
        
        if abs(diff)<=maxdiff:
            ans+=1
            j+=1 # use room
            break # go to next guy
        elif sizes[j]-guy>maxdiff: # too big, will only increase, keep room, ie keep j same
            break
        else: # room too small, ie diff too small so check bigger rooms
            j+=1
print(ans)