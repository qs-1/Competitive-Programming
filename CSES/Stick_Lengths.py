import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n = int(input())
arr = sorted(list(map(int, input().split())))

ans = 0
if n%2 == 0:
    target = int((arr[n//2 - 1] + arr[n//2]) / 2)
else:
    target = arr[n//2]

for i in range(n):
    ans += abs(target - arr[i])

print(ans)