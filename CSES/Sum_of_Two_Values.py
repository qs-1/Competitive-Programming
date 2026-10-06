import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))


# shouldve instead made the hashi while iterating, 
# everything done in one loop with duplicates handled


hashi = {}
for i in range(n):
    num = nums[i]
    if num not in hashi:
        hashi[num] = [0,[]]
    hashi[num][0] += 1
    hashi[num][1].append(i)

found = False
for i in range(n):
    other = m-nums[i]
    if other in hashi and ((other==nums[i] and hashi[other][0]>1) or (other!=nums[i] and hashi[other][0]>0)):
        print(i+1, hashi[other][1][-1]+1)
        found = True
        break

if not found:
    print("IMPOSSIBLE")
