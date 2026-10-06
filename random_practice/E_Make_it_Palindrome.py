import sys
import random
#hsh = random.randint(1,1<<32)
input = sys.stdin.readline
from collections import defaultdict, Counter

n = int(input())
arr = list(map(int, input().split()))
if n==1: print(0);exit(0)
hs = defaultdict(int)

between = cost = 0

if n&1==1:
    hs[arr[n//2]] += 1
    between += 1

#start from center, go to left (while adding each of its pairings ans)
for i in range(n//2 - 1, -1, -1): 
    #total in center - same as current in between gives the num of pairs
    #that are different and thus incur cost, this cost for a pair is given
    #by min(i, n-1-j)+1, since i<j always here, it becomes i+1
    
    #left with center cost
    different = between - hs[arr[i]] 
    cost += different * (i+1)

    #right with center cost
    different = between - hs[arr[n-1-i]] 
    cost += different * (i+1)

    #cost for leftmost and righmost pair itself
    cost += (i+1) if arr[i]!=arr[n-1-i] else 0 

    #add the two to the center block
    hs[arr[i]] += 1 
    hs[arr[n-1-i]] += 1 
    between += 2

print(cost)