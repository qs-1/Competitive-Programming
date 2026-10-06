n,wn = list(map(int, input().split()))

w=[]; v=[]
for _ in range(n):
    x,y=list(map(int, input().split()))
    w.append(x); v.append(y)

#dp to store best value for each max weight from 0 to wn
dp = [[0]*(wn+1) for i in range(n+1)]
#base cases 0 as is, col 0 since picked none as max is 0 and row 0 since nothing of value to pick

for i in range(1, n+1):
    for j in range(1, wn+1):
        #take best of picking or skipping:
        #skip by taking prev value without this object
        #take by adding this new value, ALSO, SINCE THIS NEW OBJECT HAS SOME WEIGHT `X`,
        #WE CANT JUST ADD TO PREVIOUS SINCE THAT WOULD IGNORE THE WEIGHT FOR THIS NEW OBJECT,
        #INSTEAD PICK THE BEST VALUE AT THE DP WITHOUT THIS OBJECT (AND WITHOUT THIS NEW WEIGHT!)
        #think about it, if prev only had 1 space left and new object weighed 100, then we cant add it
        #we instead look at the best value we previously could achieve without this new weight, j-100
        #and add that with this new object, this way the weight adds up to max available each time,
        #maximizing achieveable value with this new object 
        
        if w[i-1] > j: #bigger than the bag, cant keep, so keep prev best 
            dp[i][j] = dp[i-1][j]; continue
        
        dp[i][j] = max(dp[i-1][j], v[i-1] + dp[i-1][j-w[i-1]])

print(dp[-1][-1])