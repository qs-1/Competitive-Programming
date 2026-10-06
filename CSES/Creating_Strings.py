import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter
s = [c for c in input().strip()]
n = len(s)

chars = {}
for c in s:
    if c not in chars:
        chars[c] = 0
    chars[c] += 1
# print(chars)


ans = [0]
def recur(i,temp):
    if i >= n:
        ans[0] += 1
        ans.append("".join(temp))
        return

    for c in sorted(chars):
        if chars[c]>0:
            # place it
            temp[i] = c
            chars[c] -= 1
            recur(i+1, temp) 
            chars[c] += 1 # undo usage 

recur(0, s)

for l in ans:
    print(l)