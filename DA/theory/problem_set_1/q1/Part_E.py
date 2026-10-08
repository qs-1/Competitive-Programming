# brute force
def solve_brute_force(n, grid):
    vow = 'AEIOU'
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += 1 if grid[i][j] in vow else 0
    return cnt

# div & conq 2x2 base case
def solve_divide_and_conquer_2x2(n, grid):
    vow = 'AEIOU'
    def dq(ri=0, ci=0, rj=None, cj=None):
        if rj is None: rj = n-1
        if cj is None: cj = n-1
        if rj-ri == 1:
            cnt = 0
            for i in range(ri,rj+1):
                for j in range(ci,cj+1):
                    cnt += 1 if grid[i][j] in vow else 0
            return cnt
        mrow = (ri + rj) // 2
        mcol = (ci + cj) // 2
        tl = dq(ri, ci, mrow, mcol)
        tr = dq(ri, mcol+1, mrow, cj)
        bl = dq(mrow+1, ci, rj, mcol)
        br = dq(mrow+1, mcol+1, rj, cj)
        return tl + tr + bl + br
    return dq()

# div & conq 1x1 base case
def solve_divide_and_conquer_1x1(n, grid):
    vow = 'AEIOU'
    def dq(ri=0, ci=0, rj=None, cj=None):
        if rj is None: rj = n-1
        if cj is None: cj = n-1
        if rj-ri == 0:
            return 1 if grid[ri][ci] in vow else 0
        mrow = (ri + rj) // 2
        mcol = (ci + cj) // 2
        tl = dq(ri, ci, mrow, mcol)
        tr = dq(ri, mcol+1, mrow, cj)
        bl = dq(mrow+1, ci, rj, mcol)
        br = dq(mrow+1, mcol+1, rj, cj)
        return tl + tr + bl + br
    return dq()