import sys
import functools
input = sys.stdin.readline
arr = list(map(int, input().split()))
n = len(arr)

# for saving where we split for range i j, used for placing brackets like ( A1 x ( A2 x A3 ) ) 
s = [[None]*n for _ in range(n)] 

# #recursive
# @functools.cache
# def mcm(i,j):
#     if i==j:
#         return 0
#     #try split at every i within arr
#     best = float("inf")
#     for sp in range(i, j):
#         currcost = mcm(i,sp) + mcm(sp+1, j) + (arr[i-1] * arr[sp] * arr[j]) # left half + right half costs + cost of multiplying these two
#         # best = min(best, currcost)
#         if currcost<best:
#             s[i][j] = sp
#             best = currcost
#     return best

#iterative
def mcm(i,j):
    # min cost of placing brackets in current range i j
    dp = [[float("inf")]*n for _ in range(n)]

    # since longer ranges require min cost of smaller ones,
    # find the smaller ranges costs first, ie diagonally
    # min costs for len 1, len 2 ...

    for i in range(n):
        dp[i][i] = 0

    for l in range(2,n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            for k in range(i,j):
                curr = dp[i][k] + dp[k+1][j] + (arr[i-1] * arr[k] * arr[j])
                if curr < dp[i][j]:
                    dp[i][j] = curr
                    s[i][j] = k

    return dp[1][-1]

def path(i,j):
    if i==j:
        print(f"A{i}", end='')
        return
    print('(',end='')
    split = s[i][j]
    path(i,split)
    print(' x ', end='')
    path(split+1,j)
    print(')',end='')


ans = mcm(1, n-1)
print(ans)
path(1,n-1)