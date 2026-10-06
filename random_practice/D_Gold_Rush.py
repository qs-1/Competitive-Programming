import math
import sys
import random
#hsh = random.randint(1,1<<32)
input = sys.stdin.readline
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n,m = list(map(int, input().split()))
    
    def dfs(n):
        if n==m:
            return True
        if n%3!=0:
            return False
        return dfs(n//3) or dfs(n-(n//3))
    
    print('YES' if dfs(n) else 'NO')