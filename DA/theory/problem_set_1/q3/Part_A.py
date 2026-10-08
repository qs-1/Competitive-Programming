# oneliner, nlogn
def solve_oneliner_nlogn(s, t):
    return sorted(s) == sorted(t)

# using hashmaps, linear
from collections import Counter
def solve_hashmap_linear(s, t):
    return Counter(s) == Counter(t)

# div & conq with hashmap, linear
def solve_divconq_hashmap_linear(s, t):
    if len(s)!=len(t):
        return False
    tc = Counter(t)
    def dq(i=0,j=None):
        if j is None:
            j = len(s)-1
        if i==j:
            if s[i] in tc and tc[s[i]]>0:
                tc[s[i]] -= 1
                return True
            else:
                return False
        m = (i+j) // 2
        return dq(i,m) and dq(m+1,j)
    return dq()

# bad div & conq, n^2 log n
def solve_bad_divconq_n2logn(s, t):
    if len(s)!=len(t):
        return False
    t = t.copy()
    t.sort()
    def binary_search(key, x=0, y=None):
        if y is None:
            y = len(t)-1
        if x>y:
            return None
        m = (x+y) // 2
        if t[m] == key:
            return m
        elif t[m]>key: return binary_search(key,x,m-1)
        else: return binary_search(key,m+1,y)
    def dq(i=0,j=None):
        if j is None:
            j = len(s)-1
        if i==j:
            idx = binary_search(s[i])
            if idx is not None:
                t[idx] = "#"
                t.sort()
                return True
            else:
                return False
        m = (i+j) // 2
        return dq(i,m) and dq(m+1,j)
    return dq()