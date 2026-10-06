import sys
import random
#hsh = random.randint(1,1<<32)
input = sys.stdin.readline
from collections import defaultdict, Counter

cases = int(input())
for _ in range(cases):
    n,k = list(map(int, input().split()))
    arr = list(input())

    ans =0
    cnt = Counter(arr)

    extra = 0
    for i in range(ord('a'),ord('z')):
        lo = chr(i)
        cap = chr(i-32)
        extra += abs(cnt[lo]-cnt[cap]) // 2

    pairs = 0
    for i in range(ord('a'),ord('z')):
        lo = chr(i)
        cap = chr(i-32)
        pairs += min(cnt[lo], cnt[cap]) if min(cnt[lo], cnt[cap])!=0 else 0
    print(min(extra,k)+pairs)