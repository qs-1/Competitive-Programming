# brute force
def solve_brute_force(arr):
    a = b = c = -float("inf")
    for n in arr:
        if n > a:
            c = b
            b = a
            a = n
        elif n > b:
            c = b
            b = n
        elif n > c:
            c = n
    return c

# div & conq
def solve_divconq(arr):
    def merge(larr, rarr):
        temp = []
        i = j = 0
        left_len = len(larr)
        right_len = len(rarr)
        while i < left_len and j < right_len:
            if larr[i] < rarr[j]: temp.append(larr[i]); i += 1
            else: temp.append(rarr[j]); j += 1
        while i < left_len: temp.append(larr[i]); i += 1
        while j < right_len: temp.append(rarr[j]); j += 1
        return temp[-3:]
    def dq(i=0, j=None):
        if j is None:
            j = len(arr)-1
        if i == j:
            return [-float("inf"), -float("inf"), arr[i]]
        m = (i + j) // 2
        larr = dq(i, m)
        rarr = dq(m+1, j)
        return merge(larr, rarr)
    return dq()[0]