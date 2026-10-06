import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n = int(input())
arr = list(map(int, input().split()))

def recur(a,b,i,sofar):
    if i==n:
        return abs(a-b)
    return min(recur(a+arr[i],b,i+1,sofar),        
    recur(a,b+arr[i],i+1,sofar))

print(recur(0,0,0,float('inf')))