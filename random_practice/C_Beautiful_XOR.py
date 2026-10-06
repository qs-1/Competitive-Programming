import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1,1<<32)
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    a,b = map(int, input().split())
    if a==b:
        print(0);continue
    

    if a.bit_length()<b.bit_length():
        print(-1);continue
    
    if a^b<=a:
        print(1)
        print(a^b)
    else:
        print(2)
        # print(a,b)
        m = (1<<a.bit_length()) -1
        print(a^m, m^b)

    # else:
    #     print(-1)