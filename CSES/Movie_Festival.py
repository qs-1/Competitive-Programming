import sys
import math
import random
input = sys.stdin.readline
#hsh = random.randint(1, 1 << 32)
from collections import defaultdict, Counter

n = int(input())
arr = []
    
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])

print(arr)

movies = 1

end = arr[0][1]
for i in range(1, n):
    if end <= arr[i][0]:
        end = arr[i][1]
        movies+=1


print(movies)