# brute force
def solve_brute_force(arr):
    one_twt = len(arr)//20
    for i in range(len(arr)):
        if arr[i]&1 == 1: arr[i] *= 3
        if i >= len(arr) - one_twt and i&1!=1: arr[i] += 7  
    return arr[-1]

# div & conq
def solve_divconq(arr):
    length = len(arr)
    def dq(i=0,j=length-1):
        if i == j:
            if arr[i]&1==1: arr[i]*=3
            if i&1==0 and i>=length-(length//20): arr[i]+=7
            return

        m = (i+j)//2
        dq(i,m)
        dq(m+1,j)
    dq()
    return arr[-1]