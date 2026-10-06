import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n = int(input())
    inters = []
    for i in range(n):
        inters.append(list(map(int, input().split())))

    mini = float("inf")

    def check(steps):
        l,r=0,0
        for a,b in inters:
            lnew = l - steps
            rnew = r + steps
            possl = max(lnew, a)
            possr = min(rnew, b)
            #no overlap
            if possl > possr:
                return False
            #upd
            l = possl; r = possr
        return True

    i = 0
    j = 10**9
    while i<=j:
        m = (i+j)//2
        
        valid = check(m)
        if valid: 
            mini = m
            j = m-1
        else:
            i = m+1

    print(mini)
    