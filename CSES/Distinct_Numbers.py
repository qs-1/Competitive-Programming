import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n=int(input())
print(len(set(map(int, input().split()))))

# # hash collision proof:
# arr.sort()
# ans = 1
# for i in range(1, n):
#     if arr[i] != arr[i - 1]:
#         ans += 1
# print(ans)
