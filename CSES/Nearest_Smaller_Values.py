import sys
import math
import heapq
import bisect
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter


n = int(input())
arr = list(map(int, input().split()))
 
stack = []
for i in range(n):

    while stack and arr[i] <= stack[-1][0]: # remove all bigger on left than curr
        stack.pop()
    
    if not stack: # no other smaller
        print(0,end=' ')
    else: # theres a smaller
        print(stack[-1][1]+1,end=' ')

    stack.append((arr[i],i))
    

    

    
