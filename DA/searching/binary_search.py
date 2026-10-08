def solve():
    def valid(k):
        pass

    i = 0 
    j = 10**9

    ans = j

    while i <= j:
        m = (i + j) // 2

        if valid(m):
            ans = m
            j = m - 1
        else:
            i = m + 1
    
    print(ans)
