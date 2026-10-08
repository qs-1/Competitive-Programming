# iterative
def solve_iterative(k, s):
    return ''.join(s[(i - k) % len(s)] for i in range(len(s)))

# div & conq
def solve_divconq(k, s):
    length = len(s)
    def dq(i=0, j=None):
        if j is None:
            j = length-1
        if i == j:
            return [s[(i - k) % length]]
        m = (i + j) // 2
        return dq(i, m) + dq(m+1, j)
    return "".join(dq())