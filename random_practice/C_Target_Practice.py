cases = int(input())
for _ in range(cases):
    p = 0
    grid = []
    for d in range(10):
        grid.append(input())

    for i in range(10):
        for j in range(10):
            if grid[i][j] == "X":
                #weird, couldve done p += min(i, 9 - i, j, 9 - j) + 1
                normi = i if i<=4 else -(i-4)%5
                normj = j if j<=4 else -(j-4)%5
                # print(i,normi)
                if normj>=normi: 
                    p += normi+1
                else:
                    p += normj+1 
    print(p)