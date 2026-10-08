# brute force, linear
def solve_brute_force(s):
    cnt = 0
    for c in s:
        if c == 'T':
            cnt += 1
    return cnt

# div & conq, linear
def solve_divconq(s):
    def dq(i=0, j=None):
        if j is None:
            j = len(s) - 1
        if i == j:
            return 1 if s[i] == 'T' else 0
        if s[i] == 'T':
            return j - i + 1
        m = (i + j) // 2
        return dq(i, m) + dq(m + 1, j)
    return dq()

# binary search recursive, logarithmic
def solve_bs_recursive(s):
    def bs(i=0, j=None):
        if j is None:
            j = len(s) - 1
        if i > j:
            return 0  # not found
        m = (i + j) // 2
        if s[m] == "T" and (m == 0 or s[m - 1] != 'T'): # found leftmost T (either entire TTTs, or some different before it)
            return len(s) - m
        elif s[m] == 'T':
            return bs(i, m - 1)
        else:
            return bs(m + 1, j)
    return bs()

# binary search iterative, logarithmic
def solve_bs_iterative(s):
    cnt = 0
    i = 0
    j = len(s) - 1
    while i <= j:
        m = (i + j) // 2
        if s[m] == "T" and (m == 0 or s[m - 1] != 'T'):
            cnt = len(s) - m
            break
        elif s[m] == 'T':# found T but its not the start of the TTT... run, check left half to find it
            j = m - 1
        else:
            i = m + 1
    return cnt