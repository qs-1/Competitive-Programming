import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n = int(input())
moves = []
def hano(curr, helper, target, n):
    if n==2:
        moves.append(f"{curr} {helper}")
        moves.append(f"{curr} {target}")
        moves.append(f"{helper} {target}")
        return 3

    elif n==1:
        moves.append(f"{curr} {target}")
        return 1

    return hano(curr,target,helper,n-1) + hano(curr,helper,target,1) + hano(helper,curr,target,n-1)

print(hano(1,2,3,n))
for move in moves:
    print(move)