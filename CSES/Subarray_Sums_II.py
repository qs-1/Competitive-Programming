import sys
import math
import bisect
import random
input = sys.stdin.readline
hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

cnt = 0
seen = {0 ^ hsh: 1} 
curr = 0

for x in arr:
    curr += x
    
    past = curr - target
    
    cnt += seen.get(past ^ hsh, 0)
    
    seen[curr ^ hsh] = seen.get(curr ^ hsh, 0) + 1

print(cnt)
