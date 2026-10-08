# brute force
def solve_brute_force(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("-" if (i+j)&1!=1 else "#")
        board.append(''.join(row))
    return board

# div & conq
def solve_divconq(n):
    board = [[None]*n for _ in range(n)]
    def dq(ri=0, rj=None, ci=0, cj=None):
        if rj is None: rj = n-1
        if cj is None: cj = n-1
        if ri==rj:
            board[ri][ci] = "-" if (ri+ci)&1!=1 else "#"
            return
        rm = (ri+rj) // 2
        cm = (ci+cj) // 2
        dq(ri,rm,ci,cm)#top left
        dq(ri,rm,cm+1,cj)#top right
        dq(rm+1,rj,ci,cm)#bottom left
        dq(rm+1,rj,cm+1,cj)#bottom right
    dq()
    return [''.join(row) for row in board]