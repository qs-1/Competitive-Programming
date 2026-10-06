cases = int(input())
for _ in range(cases):
    n,k, r,c = list(map(int, input().split()))
    grid = [["."]*n for _ in range(n)]
    grid[r-1][c-1] = 'X'

    row = r-1
    col = (c-1)%k
    while row>0:
        col = (col+1) % k#up
        row-=1
    #or do start_col = (r - 1 + c - 1) % k
    for row in range(n):
        m=0
        while col + m*k < n:
            grid[row][col + m*k] = 'X'
            m+=1
        col = (col-1) % k

    for r in grid:
        for c in r:
            print(c if k!=1 else 'X',end = "")
        print()

