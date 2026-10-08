# brute force
def solve_brute_force(arr):
    for i in range(0, len(arr), 2):
        t = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = t
    return arr

# div & conq
def solve_divconq(arr):
    def dq(i=0, j=None):
        if j is None:
            j = len(arr) - 1
        if j - i == 1:
            t = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = t
            return
        m = (i + j) // 2
        dq(i, m)
        dq(m + 1, j)
    dq()
    return arr