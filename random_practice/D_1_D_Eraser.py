import sys
import random
#hsh = random.randint(1,1<<32)
input = sys.stdin.readline
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(input())

    i = 0
    op=0
    while i<n:
        if arr[i] == "B":
            i+=k
            op+=1
        else:
            i+=1    

    print(op)