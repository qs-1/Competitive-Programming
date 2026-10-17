import sys
import math
import random
MOD = 10**9 + 7
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter


cases = int(input())
inputs = []
maxi = -float("inf")
for _ in range(cases):
    a, b = list(map(int, input().split()))
    maxi = max(maxi, a, b)
    inputs.append((a,b))

# precalc factorials, modular inverses
fact = [0]*(maxi+1)
fact[0] = 1

curr = 1
for i in range(1,maxi+1):
    curr = curr*i % MOD
    fact[i] = curr

ans = []
for inp in inputs:
    a, b = inp
    num = fact[a]
    deno = (fact[b] * fact[a-b]) % MOD
    ans.append((num * pow(deno, MOD-2, MOD)) % MOD)

for _ in ans:
    print(_)