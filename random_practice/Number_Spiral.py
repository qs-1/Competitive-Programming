cases = int(input())
for i in range(cases):
    x,y= list(map(int, input().split()))
    level = max(x,y)
    sqr = level*level

    if level == 1: print(1);continue

    if level%2 == 0: # swapping so odd formulas work for even too
        x,y = y,x

    if x>=y: # horizontally increasing -->
        print(sqr - (2*(level)-1) + y)
    else: # vertically decreasing VVV
        print(sqr - x + 1)
