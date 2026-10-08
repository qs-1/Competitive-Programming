# brute force
def solve_brute_force(arr, ukey):
    return min(arr, key=lambda n: abs(n-ukey))

# div & conq
def solve_divide_and_conquer(arr, ukey):
    def helper(i,j):
        return min(arr[i:j+1], key=lambda n: abs(ukey - n))
    def dq(i=0,j=None):
        if j is None:
            j = len(arr)-1
        if j-i < 4:
            return helper(i,j)
        m1 = i + (j-i) // 4
        m2 = i + (2*m1)
        m3 = i + (3*m1)
        returns = [
            dq(i, m1),
            dq(m1 + 1, m2),
            dq(m2 + 1, m3),
            dq(m3 + 1, j)
        ]
        return min(returns, key=lambda n: abs(n - ukey))
    return dq()