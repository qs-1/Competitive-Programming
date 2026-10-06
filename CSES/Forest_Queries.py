import sys
import math
import heapq
import bisect
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter


n, queries = list(map(int, input().split()))
pregrid = [[0]*(n+1) for _ in range(n+1)]

for y in range(1,n+1):
    row = input().strip()
    for x in range(1, n+1):
        cell = 1 if row[x-1]=='*' else 0
        # curr = cell + top + left - diag since double counted
        pregrid[y][x] = cell + pregrid[y][x-1] + pregrid[y-1][x] - pregrid[y-1][x-1]
    
# for r in pregrid:
#     print(*r)



for k in range(queries):
    y1,x1,y2,x2 = list(map(int, input().split()))
    
    print(pregrid[y2][x2] - pregrid[y2][x1-1] - pregrid[y1-1][x2] + pregrid[y1-1][x1-1])