# brute force
def solve_brute_force(arr):
    arr = arr.copy()
    prev = arr[0]
    for i in range(1,len(arr)):
        if arr[i]!=prev: prev = arr[i]; continue
        arr[i] = -1
    return arr

# div & conq with merging child ans, nlogn
def solve_divide_and_conquer_merge(arr):
    arr = arr.copy()
    def dq(i=0,j=None):
        if j is None:
            j = len(arr)-1
        if i == j:
            return (arr[i:j+1], {arr[i]})
        m = (i+j) // 2
        larr, lset = dq(i,m)
        rarr, rset = dq(m+1,j)
        for k in range(len(rarr)):
            if rarr[k] in lset:
                rarr[k] = -1
        return (larr+rarr, lset.union(rset))
    arr2, _ = dq()
    return arr2

# div & conq with shared unique nums set
def solve_divide_and_conquer_seen(arr):
    arr = arr.copy()
    seen = set()
    def dq(i=0,j=None):
        if j is None:
            j = len(arr)-1
        if i == j:
            if arr[i] in seen: arr[i] = -1
            else: seen.add(arr[i])
            return
        m = (i+j) // 2
        dq(i,m)
        dq(m+1,j)
    dq()
    return arr

# stack
def solve_stack(arr):
    arr = arr.copy()
    stack = arr[::]
    prev = stack.pop()
    i = len(arr)-2
    while i>-1:
        curr = stack.pop()
        if curr != prev: prev = curr; i-=1; continue
        arr[i] = -1
        prev = curr
        i-=1
    return arr