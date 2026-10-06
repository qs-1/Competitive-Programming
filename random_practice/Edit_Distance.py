a=input()
b=input()

# #making a into b
# def edist_recur(a,b):
#     alen=len(a)
#     blen=len(b)
    
#     memo={}
#     def helper(i,j):
#         if (i,j) in memo:
#             return memo[(i,j)]
        
#         if j==blen:
#             #was a completed? all chars used? ie i=len(a)?
#             #if not delete them
#             return alen-i

#         elif i==alen:
#             #reached end of a, was b made? or some left to match?
#             #if left then insert those
#             return blen-j

#         maintain = float("inf")
#         if a[i]==b[j]: 
#             maintain = helper(i+1,j+1) 
#         insert =  1+helper(i,j+1) #a pointer same, but j matched go to next j
#         remove =  1+helper(i+1,j) #check next ith, j to be matched still
#         replace = 1+helper(i+1,j+1) #matched, next for both

#         best = min(maintain,
#                    insert,
#                    remove,
#                    replace)

#         memo[(i,j)] = best
#         return best

#     return helper(0,0)


def edist_iter(a,b):
    alen=len(a)
    blen=len(b)
    
    #2d dp array of n+1 * m+1
    #a cell will store the edit distance to make one into the other
    # +1 for the initial base cases 
    dp = [[0]*(blen+1) for _ in range(alen+1)]

    #if we have nothing in a and have to make b
    #cant do nothing but insert j times
    for j in range(blen+1):
        dp[0][j] = j
    
    #if we have nothing in b and have to make that with a
    #cant do nothing but delete everything in a
    for i in range(alen+1):
        dp[i][0] = i

    for i in range(1,alen+1):
        for j in range(1,blen+1):
            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1]
                continue
            dp[i][j] = 1 + min(dp[i][j-1],
                               dp[i-1][j-1],
                               dp[i-1][j])
    return dp[alen][blen]
print(edist_iter(a,b))