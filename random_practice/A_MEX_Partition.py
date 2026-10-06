import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))

    hs = Counter(arr)
    
    mini = 0
    a = 0
    while True:
        if mini not in hs:
            print(mini)
            a = 1
            break
        mini+=1
    
    # if a==0:
    #     print()