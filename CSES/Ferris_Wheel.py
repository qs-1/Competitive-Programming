import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n, maxw = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
gondolas = 0

i=0
j = n-1
while i<j:
    if arr[i] + arr[j] <= maxw:
        # print(arr[i],  arr[j])
        i+=1 # paired with lighter
        j-=1
    else:
        # print(arr[j])
        j-=1 # either case heavier placed 
    gondolas+=1

if i==j: gondolas+=1

print(gondolas)