# Chebyshev adjacency: all 8 directions
from math import ceil

n = int(input())

maxx = maxy = -1
minx = miny = 10**9

for i in range(n):
    x,y = list(map(int, input().split()))
    maxx = max(x,maxx)
    maxy = max(y,maxy)
    
    minx = min(x,minx)
    miny = min(y,miny)

    min_row_t = ceil((maxx - minx)/2)
    min_col_t = ceil((maxy - miny)/2)

print(max(min_row_t, min_col_t))