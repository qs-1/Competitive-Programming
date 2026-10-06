import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n,q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    origqs = list(map(int, input().split()))
    qs = sorted(list(set(origqs)))

    presum = []
    prev = 0
    for num in arr:
        presum.append(num+prev)
        prev+=num

    ans = {}
    i = 0
    for q in qs:
        while i<n and q>=arr[i]:
            i+=1
        if i==0:
            ans[q] = 0
        else:
            ans[q] = presum[i-1]

    for q in origqs:
        print(ans[q], end = " ")
    print()