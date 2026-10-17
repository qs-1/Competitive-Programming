import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

def solve(x):
    ans = 1
    i = 2
    while i*i <= x:# perfect sq <=
        prime = 1
        while x%i == 0:
            x//=i
            prime += 1
        if prime>1: ans = ans * prime
        i+=1

    return ans * (2 if x>1 else 1) # leftover prime fact 

cases = int(input())
for _ in range(cases):
    n = int(input())
    print(solve(n))
